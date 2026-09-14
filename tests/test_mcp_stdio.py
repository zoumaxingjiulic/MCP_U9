"""A real official SDK client and stdio subprocess against a local mock ERP."""

import json
import sys
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlsplit

import pytest
from conftest import synthetic_item
from jsonschema import validate
from mcp import Client
from mcp.client.stdio import StdioServerParameters
from mcp.shared.exceptions import MCPError


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
            code = body[0]["ItemMaster"]["Code"]
            calls.append(code)
            if code == "ERROR":
                self.send_json({"ResCode": 601, "Success": False, "ResMsg": "synthetic-secret"})
            elif code == "MALFORMED":
                self.send_json({"ResCode": 0, "Success": True, "Data": {}})
            else:
                self.send_json(
                    {"ResCode": 0, "Success": True, "Data": [] if code == "EMPTY" else [synthetic_item()]}
                )

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_port, calls
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


async def test_real_sdk_stdio_initialization_discovery_calls_and_errors():
    with mock_erp() as (port, calls):
        params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "u9_mcp.server"],
            cwd=str(Path(__file__).resolve().parents[1]),
            env={
                "U9_BASE_URL": f"http://127.0.0.1:{port}/U9C",
                "U9_ALLOW_HTTP": "true",
                "U9_CLIENT_ID": "TEST-APP",
                "U9_CLIENT_SECRET": "synthetic-secret",
                "U9_ENT_CODE": "TEST-ENT",
                "U9_ORG_CODE": "TEST-ORG",
                "U9_USER_CODE": "TEST-USER",
            },
        )
        async with Client(params, read_timeout_seconds=10) as client:
            tools = (await client.list_tools()).tools
            assert len(tools) == 1 and tools[0].name == "u9_get_item"
            tool = tools[0]
            assert tool.input_schema["additionalProperties"] is False
            assert set(tool.input_schema["required"]) == {"organization_code", "item_code"}
            assert tool.annotations.read_only_hint is True
            for code, error in [
                ("SYN-ITEM", None),
                ("EMPTY", None),
                ("ERROR", "PERMISSION_DENIED"),
                ("MALFORMED", "UPSTREAM_FORMAT_CHANGED"),
            ]:
                result = await client.call_tool(
                    tool.name, {"organization_code": "TEST-ORG", "item_code": code}
                )
                payload = result.structured_content
                validate(payload, tool.output_schema)
                assert json.loads(result.content[0].text) == payload
                assert result.is_error == (error is not None)
                if error:
                    assert payload["error"]["code"] == error
                else:
                    assert payload["data"]["total"] == (0 if code == "EMPTY" else 1)
                assert "synthetic-secret" not in result.content[0].text
            count = len(calls)
            for arguments, error in [
                ({"item_code": "SYN-ITEM"}, "INVALID_ARGUMENT"),
                ({"organization_code": "OTHER", "item_code": "SYN-ITEM"}, "PERMISSION_DENIED"),
                (
                    {"organization_code": "TEST-ORG", "item_code": "SYN-ITEM", "url": "bad"},
                    "INVALID_ARGUMENT",
                ),
            ]:
                result = await client.call_tool(tool.name, arguments)
                assert result.is_error and result.structured_content["error"]["code"] == error
            assert len(calls) == count
            with pytest.raises(MCPError) as unknown:
                await client.call_tool("unknown", {})
            assert unknown.value.code == -32602
            assert calls.count("auth") == 1
