"""Call a deployed Streamable HTTP server through the official MCP SDK."""

import argparse
import asyncio
import json
import os

import httpx2
from mcp import Client
from mcp.client.streamable_http import streamable_http_client


async def run(url: str, token: str, organization_code: str | None, item_code: str) -> None:
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx2.AsyncClient(headers=headers, trust_env=False) as http_client:
        transport = streamable_http_client(url, http_client=http_client)
        async with Client(transport, read_timeout_seconds=15) as client:
            result = await client.call_tool(
                "u9_get_item",
                {
                    **({"organization_code": organization_code} if organization_code else {}),
                    "item_code": item_code,
                },
            )
            print(json.dumps(result.structured_content, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8000/mcp")
    parser.add_argument("--token", default=os.getenv("MCP_ACCESS_TOKEN"))
    parser.add_argument("--organization-code", help="可省略，默认使用服务端授权组织")
    parser.add_argument("--item-code", required=True)
    args = parser.parse_args()
    if not args.token:
        parser.error("请通过 --token 或 MCP_ACCESS_TOKEN 提供访问令牌")
    asyncio.run(run(args.url, args.token, args.organization_code, args.item_code))


if __name__ == "__main__":
    main()
