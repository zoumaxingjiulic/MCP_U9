"""A minimal official MCP SDK client, independent of any LLM or chat page."""

import argparse
import asyncio
import json
import sys
from pathlib import Path

from mcp import Client
from mcp.client.stdio import StdioServerParameters


async def query(args):
    server = StdioServerParameters(
        command=sys.executable, args=["-m", "u9_mcp.server", "--env-file", str(args.env_file.resolve())]
    )
    async with Client(server, read_timeout_seconds=60) as client:
        result = await client.call_tool(
            "u9_get_item",
            {
                "organization_code": args.organization_code,
                "item_code": args.item_code,
            },
        )
        print(json.dumps(result.structured_content, ensure_ascii=False, indent=2))
        return 1 if result.is_error else 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", required=True, type=Path)
    parser.add_argument("--organization-code", required=True)
    parser.add_argument("--item-code", required=True)
    raise SystemExit(asyncio.run(query(parser.parse_args())))


if __name__ == "__main__":
    main()
