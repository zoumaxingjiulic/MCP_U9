from starlette.testclient import TestClient

from u9_mcp.config import LocalChatSettings
from u9_mcp.local_chat import create_local_chat_app


class FakeLocalChatService:
    async def status(self):
        return {"model": "synthetic-model", "tools": ["u9_get_item"]}

    async def answer(self, message):
        return {
            "answer": f"received: {message}",
            "model": "synthetic-model",
            "trace": [{"tool": "u9_get_item", "is_error": False, "result": {"data": {}}}],
        }


def local_chat_settings():
    return LocalChatSettings(
        dashscope_api_key="synthetic-dashscope-key-" + "x" * 32,
        dashscope_model="synthetic-model",
        mcp_url="http://127.0.0.1:18001/mcp",
        mcp_access_token="synthetic-mcp-token-" + "x" * 32,
    )


def test_local_chat_serves_page_and_calls_service():
    client = TestClient(create_local_chat_app(local_chat_settings(), FakeLocalChatService()))
    assert client.get("/").status_code == 200
    assert client.get("/healthz").json() == {"status": "ok"}
    assert client.get("/api/status").json() == {
        "model": "synthetic-model",
        "tools": ["u9_get_item"],
    }
    result = client.post("/api/chat", json={"message": "查询物料"})
    assert result.status_code == 200
    assert result.json()["trace"][0]["tool"] == "u9_get_item"


def test_local_chat_rejects_invalid_chat_request():
    client = TestClient(create_local_chat_app(local_chat_settings(), FakeLocalChatService()))
    assert client.post("/api/chat", json={"message": ""}).status_code == 400
    assert client.post("/api/chat", json={"message": "x", "extra": 1}).status_code == 400
