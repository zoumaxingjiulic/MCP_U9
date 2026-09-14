"""Explicit opt-in: deployed Streamable HTTP MCP -> authorized ERP.

The expected JSON stays outside version control; stdout contains checks only.
"""

import argparse
import asyncio
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

import httpx2
from jsonschema import validate
from mcp import Client
from mcp.client.streamable_http import streamable_http_client


async def verify(args) -> None:
    if urlsplit(args.url).scheme != "https" and not args.allow_http:
        raise SystemExit("拒绝明文远程连接；仅本机/受信内网测试可显式使用 --allow-http")
    token = os.getenv("MCP_ACCESS_TOKEN", "")
    if not token:
        raise SystemExit("缺少 MCP_ACCESS_TOKEN")
    expected = json.loads(args.expected.read_text(encoding="utf-8-sig"))
    async with httpx2.AsyncClient(
        headers={"Authorization": f"Bearer {token}"}, trust_env=False
    ) as http_client:
        transport = streamable_http_client(args.url, http_client=http_client)
        async with Client(transport, read_timeout_seconds=60) as client:
            listed = await client.list_tools()
            assert len(listed.tools) == 1 and listed.tools[0].name == "u9_get_item"
            tool = listed.tools[0]
            assert tool.input_schema["required"] == ["item_code"]
            result = await client.call_tool("u9_get_item", {"item_code": expected["query"]["item_code"]})
            assert not result.is_error, "ERP tool failed; see sanitized server log"
            payload = result.structured_content
            validate(payload, tool.output_schema)
            assert json.loads(result.content[0].text) == payload
            data = payload["data"]
            assert data["query"]["organization_code"] == expected["query"]["organization_code"]
            assert data["total"] == 1 and data["returned"] == 1 and not data["has_more"]
            item = data["items"][0]
            for field, value in expected["item"].items():
                actual = item
                for key in field.split("."):
                    actual = actual[key]
                assert actual == value, f"ERP comparison failed: {field}"
            print(
                json.dumps(
                    {
                        "mcp_streamable_http": "passed",
                        "tool_discovery": "passed",
                        "schema": "passed",
                        "erp_comparison_fields": list(expected["item"]),
                        "result": "passed",
                    },
                    ensure_ascii=False,
                )
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--expected", type=Path, required=True)
    parser.add_argument("--allow-http", action="store_true")
    args = parser.parse_args()
    asyncio.run(verify(args))


if __name__ == "__main__":
    main()
