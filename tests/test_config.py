from pathlib import Path

import pytest
from pydantic import ValidationError

from u9_mcp.config import load_http_settings


def write_env(tmp_path: Path, **values: str) -> Path:
    path = tmp_path / "test.env"
    path.write_text("\n".join(f"{key}={value}" for key, value in values.items()), encoding="utf-8")
    return path


def test_http_settings_are_explicit_and_trim_csv(tmp_path, monkeypatch):
    for key in [
        "MCP_ACCESS_TOKEN",
        "MCP_ALLOWED_HOSTS",
        "MCP_ALLOWED_ORIGINS",
        "MCP_MAX_REQUEST_BODY_SIZE",
        "MCP_MAX_SESSIONS",
        "MCP_SESSION_IDLE_TIMEOUT",
    ]:
        monkeypatch.delenv(key, raising=False)
    settings = load_http_settings(
        write_env(
            tmp_path,
            MCP_ACCESS_TOKEN="t" * 48,
            MCP_ALLOWED_HOSTS="localhost:*, 10.0.0.8:*",
            MCP_ALLOWED_ORIGINS="https://mcp.example.test",
            MCP_MAX_REQUEST_BODY_SIZE="2048",
            MCP_MAX_SESSIONS="8",
            MCP_SESSION_IDLE_TIMEOUT="45",
        )
    )
    assert settings.allowed_hosts == ["localhost:*", "10.0.0.8:*"]
    assert settings.allowed_origins == ["https://mcp.example.test"]
    assert settings.max_request_body_size == 2048
    assert settings.max_sessions == 8
    assert settings.session_idle_timeout == 45


@pytest.mark.parametrize(
    ("token", "hosts"),
    [("short", "localhost:*"), ("t" * 48, ""), ("t" * 48, "https://example.test")],
)
def test_http_settings_reject_weak_token_or_invalid_hosts(tmp_path, monkeypatch, token, hosts):
    monkeypatch.delenv("MCP_ACCESS_TOKEN", raising=False)
    monkeypatch.delenv("MCP_ALLOWED_HOSTS", raising=False)
    with pytest.raises(ValidationError):
        load_http_settings(write_env(tmp_path, MCP_ACCESS_TOKEN=token, MCP_ALLOWED_HOSTS=hosts))
