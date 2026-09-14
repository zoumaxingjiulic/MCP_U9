import os
from pathlib import Path
from urllib.parse import urlsplit

from dotenv import dotenv_values
from pydantic import BaseModel, ConfigDict, Field, SecretStr, field_validator, model_validator


class Settings(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, hide_input_in_errors=True)
    base_url: str
    client_id: str
    client_secret: SecretStr
    enterprise_code: str
    organization_code: str
    user_code: str
    allow_http: bool = False

    @field_validator("base_url", "client_id", "enterprise_code", "organization_code", "user_code")
    @classmethod
    def not_blank(cls, value: str) -> str:
        if not value or value != value.strip() or any(ord(c) < 32 for c in value):
            raise ValueError("配置不能为空或包含首尾空白/控制字符")
        return value

    @model_validator(mode="after")
    def valid_destination(self):
        url = urlsplit(self.base_url)
        if url.scheme not in {"http", "https"} or not url.hostname or url.username or url.password:
            raise ValueError("ERP 地址必须是无内嵌凭据的 HTTP(S) 地址")
        if url.query or url.fragment or (url.scheme == "http" and not self.allow_http):
            raise ValueError("ERP 地址含查询参数/片段，或尚未显式配置 HTTP 环境")
        if not self.client_secret.get_secret_value().strip():
            raise ValueError("缺少应用密钥")
        return self


def load_settings(env_file: Path | None = None) -> Settings:
    source = dict(dotenv_values(env_file)) if env_file is not None else {}
    source.update(os.environ)
    keys = {
        "base_url": "U9_BASE_URL",
        "client_id": "U9_CLIENT_ID",
        "client_secret": "U9_CLIENT_SECRET",
        "enterprise_code": "U9_ENT_CODE",
        "organization_code": "U9_ORG_CODE",
        "user_code": "U9_USER_CODE",
    }
    values = {name: source.get(key, "") for name, key in keys.items()}
    values["allow_http"] = source.get("U9_ALLOW_HTTP", "false")
    return Settings.model_validate(values)


class HttpSettings(BaseModel):
    """Security and resource limits for the remote MCP transport."""

    model_config = ConfigDict(extra="forbid", frozen=True, hide_input_in_errors=True)
    access_token: SecretStr
    allowed_hosts: list[str]
    allowed_origins: list[str] = Field(default_factory=list)
    max_request_body_size: int = 1_048_576
    max_sessions: int = 64
    session_idle_timeout: float = 300

    @field_validator("access_token")
    @classmethod
    def strong_access_token(cls, value: SecretStr) -> SecretStr:
        token = value.get_secret_value()
        if not 32 <= len(token) <= 512 or token != token.strip() or any(ord(c) < 33 for c in token):
            raise ValueError("MCP 访问令牌必须是 32–512 个无空白可打印字符")
        return value

    @field_validator("allowed_hosts")
    @classmethod
    def hosts_required(cls, values: list[str]) -> list[str]:
        if not values or any(not value or "/" in value or "://" in value for value in values):
            raise ValueError("必须配置合法的 MCP Host 白名单")
        return values


def _csv(source: dict, key: str, default: str = "") -> list[str]:
    raw = source.get(key, default)
    return [value.strip() for value in (raw or "").split(",") if value.strip()]


def load_http_settings(env_file: Path | None = None) -> HttpSettings:
    source = dict(dotenv_values(env_file)) if env_file is not None else {}
    source.update(os.environ)
    return HttpSettings.model_validate(
        {
            "access_token": source.get("MCP_ACCESS_TOKEN", ""),
            "allowed_hosts": _csv(source, "MCP_ALLOWED_HOSTS", "localhost:*,127.0.0.1:*"),
            "allowed_origins": _csv(source, "MCP_ALLOWED_ORIGINS"),
            "max_request_body_size": source.get("MCP_MAX_REQUEST_BODY_SIZE", "1048576"),
            "max_sessions": source.get("MCP_MAX_SESSIONS", "64"),
            "session_idle_timeout": source.get("MCP_SESSION_IDLE_TIMEOUT", "300"),
        }
    )
