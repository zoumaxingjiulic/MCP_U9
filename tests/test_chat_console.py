from starlette.testclient import TestClient

from u9_mcp.chat_console import create_console_app
from u9_mcp.config import ChatSettings


class FakeConsoleService:
    async def status(self):
        return {"model": "synthetic-model", "tools": ["u9_get_item"]}

    async def answer(self, message):
        return {
            "answer": f"received: {message}",
            "model": "synthetic-model",
            "trace": [{"tool": "u9_get_item", "is_error": False, "result": {"data": {}}}],
        }


def chat_settings():
    return ChatSettings(
        dashscope_api_key="synthetic-dashscope-key-" + "x" * 32,
        dashscope_model="synthetic-model",
        mcp_access_token="synthetic-mcp-token-" + "x" * 32,
        chat_access_token="synthetic-chat-token-" + "x" * 32,
    )


def test_console_serves_page_and_protects_apis():
    client = TestClient(create_console_app(chat_settings(), FakeConsoleService()))
    assert client.get("/").status_code == 200
    assert client.get("/healthz").json() == {"status": "ok"}
    assert client.get("/api/status").status_code == 401
    headers = {"X-Chat-Access-Token": "synthetic-chat-token-" + "x" * 32}
    assert client.get("/api/status", headers=headers).json() == {
        "model": "synthetic-model",
        "tools": ["u9_get_item"],
    }
    result = client.post("/api/chat", headers=headers, json={"message": "查询物料"})
    assert result.status_code == 200
    assert result.json()["trace"][0]["tool"] == "u9_get_item"


def test_console_rejects_invalid_chat_request():
    client = TestClient(create_console_app(chat_settings(), FakeConsoleService()))
    headers = {"X-Chat-Access-Token": "synthetic-chat-token-" + "x" * 32}
    assert client.post("/api/chat", headers=headers, json={"message": ""}).status_code == 400
    assert client.post("/api/chat", headers=headers, json={"message": "x", "extra": 1}).status_code == 400
