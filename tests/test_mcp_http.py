"""Official SDK client against a real Streamable HTTP process and mock ERP."""

import asyncio
import json
import os
import socket
import sys
import time
import urllib.error
import urllib.request
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlsplit

import httpx2
from conftest import synthetic_item
from mcp import Client
from mcp.client.streamable_http import streamable_http_client


@contextmanager
def mock_erp():
    calls = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def send_json(self, data):
            raw = json.dumps(data).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self):
            calls.append("auth")
            assert urlsplit(self.path).path == "/U9C/webapi/OAuth2/AuthLogin"
            self.send_json({"ResCode": 0, "Success": True, "Data": "synthetic-token"})

        def do_POST(self):
            assert self.path == "/U9C/webapi/ItemMaster/Query"
            assert self.headers["token"] == "synthetic-token"
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            calls.append(body[0]["ItemMaster"]["Code"])
            self.send_json({"ResCode": 0, "Success": True, "Data": [synthetic_item()]})

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_port, calls
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def request_status(url: str, *, token: str | None = None, host: str | None = None) -> int:
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if host:
        headers["Host"] = host
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=2) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


async def test_streamable_http_auth_discovery_and_tool_call():
    token = "synthetic-mcp-token-" + "t" * 32
    with mock_erp() as (erp_port, calls):
        port = free_port()
        env = {
            **os.environ,
            "U9_BASE_URL": f"http://127.0.0.1:{erp_port}/U9C",
            "U9_ALLOW_HTTP": "true",
            "U9_CLIENT_ID": "TEST-APP",
            "U9_CLIENT_SECRET": "synthetic-secret",
            "U9_ENT_CODE": "TEST-ENT",
            "U9_ORG_CODE": "TEST-ORG",
            "U9_USER_CODE": "TEST-USER",
            "MCP_ACCESS_TOKEN": token,
            "MCP_ALLOWED_HOSTS": "127.0.0.1:*",
            "MCP_MAX_REQUEST_BODY_SIZE": "1024",
            "MCP_MAX_SESSIONS": "4",
            "MCP_SESSION_IDLE_TIMEOUT": "30",
        }
        process = await asyncio.create_subprocess_exec(
            sys.executable,
            "-m",
            "u9_mcp.server",
            "--transport",
            "streamable-http",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
            cwd=Path(__file__).resolve().parents[1],
            env=env,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        base_url = f"http://127.0.0.1:{port}"
        try:
            deadline = time.monotonic() + 10
            while time.monotonic() < deadline:
                try:
                    if await asyncio.to_thread(request_status, base_url + "/healthz") == 200:
                        break
                except OSError:
                    await asyncio.sleep(0.05)
            else:
                raise AssertionError("HTTP MCP server did not become ready")

            assert await asyncio.to_thread(request_status, base_url + "/mcp") == 401
            assert (
                await asyncio.to_thread(request_status, base_url + "/mcp", token="wrong-" + "x" * 32) == 401
            )
            assert (
                await asyncio.to_thread(request_status, base_url + "/mcp", token=token, host="evil.example")
                == 421
            )

            async with httpx2.AsyncClient(
                headers={"Authorization": f"Bearer {token}"}, trust_env=False
            ) as http_client:
                transport = streamable_http_client(base_url + "/mcp", http_client=http_client)
                async with Client(transport, read_timeout_seconds=10) as client:
                    tools = (await client.list_tools()).tools
                    assert [tool.name for tool in tools] == ["u9_get_item"]
                    result = await client.call_tool(
                        "u9_get_item",
                        {"organization_code": "TEST-ORG", "item_code": "SYN-ITEM"},
                    )
                    assert not result.is_error
                    assert result.structured_content["data"]["items"][0]["code"] == "SYN-ITEM"
            assert calls == ["auth", "SYN-ITEM"]
        finally:
            process.terminate()
            await asyncio.wait_for(process.wait(), timeout=5)
