"""Export the exact tool definition returned by MCP tools/list without ERP access."""

import json
from pathlib import Path

from u9_mcp.tools.items import definition


def main():
    target = Path(__file__).resolve().parents[1] / "docs/schemas/u9_get_item.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(
            definition().model_dump(mode="json", by_alias=True, exclude_none=True),
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print("Exported docs/schemas/u9_get_item.json")


if __name__ == "__main__":
    main()
