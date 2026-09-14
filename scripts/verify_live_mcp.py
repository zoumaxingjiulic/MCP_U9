"""Explicit opt-in: real SDK stdio client -> server -> authorized ERP.

The expected JSON stays outside version control; stdout contains checks only.
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

from jsonschema import validate
from mcp import Client
from mcp.client.stdio import StdioServerParameters


async def verify(args):
    expected = json.loads(args.expected.read_text(encoding="utf-8"))
    params = StdioServerParameters(
        command=sys.executable, args=["-m", "u9_mcp.server", "--env-file", str(args.env_file.resolve())]
    )
    async with Client(params, read_timeout_seconds=60) as client:
        listed = await client.list_tools()
        assert len(listed.tools) == 1 and listed.tools[0].name == "u9_get_item"
        tool = listed.tools[0]
        assert tool.input_schema["required"] == ["item_code"]
        result = await client.call_tool("u9_get_item", {"item_code": expected["query"]["item_code"]})
        assert not result.is_error, "ERP tool failed; see sanitized result/log"
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
                    "mcp_stdio": "passed",
                    "tool_discovery": "passed",
                    "schema": "passed",
                    "erp_comparison_fields": list(expected["item"]),
                    "result": "passed",
                },
                ensure_ascii=False,
            )
        )
        if args.empty_code:
            empty_query = {**expected["query"], "item_code": args.empty_code}
            empty = await client.call_tool("u9_get_item", empty_query)
            validate(empty.structured_content, tool.output_schema)
            # Missing objects are not assumed to be successful empty responses.
            if not empty.is_error:
                assert empty.structured_content["data"]["items"] == []
                print('{"empty_result":"passed"}')
            else:
                print(
                    json.dumps({"empty_result": "upstream_error", "error": empty.structured_content["error"]})
                )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", type=Path, required=True)
    parser.add_argument("--expected", type=Path, required=True)
    parser.add_argument("--empty-code")
    args = parser.parse_args()
    asyncio.run(verify(args))


if __name__ == "__main__":
    main()
