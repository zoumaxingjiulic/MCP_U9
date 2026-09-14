import argparse
import asyncio
import logging
import sys
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from mcp import types
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.server.transport_security import TransportSecuritySettings
from mcp.shared.exceptions import MCPError
from pydantic import ValidationError
from starlette.routing import Route

from .clients.u9 import U9Client
from .config import HttpSettings, Settings, load_http_settings, load_settings
from .http import BearerTokenMiddleware, health
from .services.items import ItemService
from .tools import items


def create_server(settings: Settings, *, transport=None) -> Server:
    @asynccontextmanager
    async def lifespan(server):
        client = U9Client(settings, transport=transport)
        try:
            yield ItemService(client)
        finally:
            await client.close()

    async def list_tools(context, params):
        return types.ListToolsResult(tools=[items.definition()])

    async def call_tool(context, params):
        if params.name != items.NAME:
            raise MCPError(code=-32602, message="Unknown tool")
        return await items.execute(context.lifespan_context, params.arguments or {})

    return Server(
        "u9-cloud-mcp", version="0.3.0", lifespan=lifespan, on_list_tools=list_tools, on_call_tool=call_tool
    )


async def serve_stdio(settings: Settings):
    server = create_server(settings)
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def create_http_app(settings: Settings, http_settings: HttpSettings):
    server = create_server(settings)
    app = server.streamable_http_app(
        streamable_http_path="/mcp",
        json_response=True,
        stateless_http=False,
        max_request_body_size=http_settings.max_request_body_size,
        session_idle_timeout=http_settings.session_idle_timeout,
        max_sessions=http_settings.max_sessions,
        transport_security=TransportSecuritySettings(
            enable_dns_rebinding_protection=True,
            allowed_hosts=http_settings.allowed_hosts,
            allowed_origins=http_settings.allowed_origins,
        ),
        custom_starlette_routes=[Route("/healthz", health, methods=["GET"])],
    )
    return BearerTokenMiddleware(app, http_settings)


def main():
    parser = argparse.ArgumentParser(description="U9 Cloud read-only MCP server")
    parser.add_argument(
        "--env-file", type=Path, help="Explicit private environment file; otherwise use environment only"
    )
    parser.add_argument("--transport", choices=["stdio", "streamable-http"], default="stdio")
    parser.add_argument("--host", default="127.0.0.1", help="HTTP bind address")
    parser.add_argument("--port", type=int, default=8000, help="HTTP bind port")
    args = parser.parse_args()
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
    logging.getLogger("u9_mcp.audit").setLevel(logging.INFO)
    # Never log HTTP URLs: the vendor authentication endpoint uses query-string credentials.
    logging.getLogger("httpx").setLevel(logging.CRITICAL)
    logging.getLogger("httpcore").setLevel(logging.CRITICAL)
    try:
        settings = load_settings(args.env_file)
        http_settings = load_http_settings(args.env_file) if args.transport == "streamable-http" else None
    except (ValidationError, OSError, ValueError):
        print("CONFIG_ERROR: 请检查私有配置文件及必填 U9 环境变量。", file=sys.stderr)
        raise SystemExit(2) from None
    try:
        if args.transport == "stdio":
            asyncio.run(serve_stdio(settings))
        else:
            assert http_settings is not None
            uvicorn.run(
                create_http_app(settings, http_settings),
                host=args.host,
                port=args.port,
                access_log=False,
                proxy_headers=False,
                server_header=False,
            )
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
