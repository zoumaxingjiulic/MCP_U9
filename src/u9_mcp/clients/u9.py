import asyncio
import json
from decimal import Decimal
from typing import Any

import httpx

from ..config import Settings
from ..errors import BusinessError, format_error

AUTH_PATH = "/webapi/OAuth2/AuthLogin"
ITEM_PATH = "/webapi/ItemMaster/Query"
MAX_BYTES = 2_000_000


class U9Client:
    """Single identity, serialized reads, memory-only token, one expiry recovery."""

    def __init__(self, settings: Settings, *, transport: httpx.AsyncBaseTransport | None = None):
        self.settings = settings
        self._token: str | None = None
        self._lock = asyncio.Lock()
        self._http = httpx.AsyncClient(
            timeout=httpx.Timeout(20),
            follow_redirects=False,
            trust_env=False,
            limits=httpx.Limits(max_connections=1, max_keepalive_connections=1),
            transport=transport,
        )

    async def close(self):
        self._token = None
        await self._http.aclose()

    async def _request(self, path: str, *, params=None, body=None, token=None) -> dict[str, Any]:
        if path not in {AUTH_PATH, ITEM_PATH}:
            raise BusinessError("PERMISSION_DENIED", "请求超出本阶段授权接口范围。")
        headers = {"Accept": "application/json"}
        if token:
            headers["token"] = token
        try:
            async with self._http.stream(
                "GET" if path == AUTH_PATH else "POST",
                self.settings.base_url.rstrip("/") + path,
                params=params,
                json=body,
                headers=headers,
            ) as response:
                if response.status_code in {401, 403}:
                    raise BusinessError("PERMISSION_DENIED", "ERP 拒绝当前身份的接口访问。")
                if response.status_code == 429 or response.status_code >= 500:
                    raise BusinessError(
                        "UPSTREAM_UNAVAILABLE", "ERP 暂时不可用，请稍后重试。", retryable=True
                    )
                if response.status_code != 200:
                    raise BusinessError("UPSTREAM_ERROR", "ERP 返回未预期的 HTTP 状态，请联系维护人员。")
                raw = bytearray()
                async for chunk in response.aiter_bytes():
                    raw.extend(chunk)
                    if len(raw) > MAX_BYTES:
                        raise format_error()
        except httpx.TimeoutException:
            raise BusinessError(
                "UPSTREAM_TIMEOUT", "ERP 请求超时，可稍后重试该只读查询。", retryable=True
            ) from None
        except httpx.HTTPError:
            raise BusinessError(
                "UPSTREAM_UNAVAILABLE", "无法连接 ERP，请检查网络。", retryable=True
            ) from None
        try:
            result = json.loads(raw, parse_float=Decimal, parse_constant=self._reject_constant)
        except (ValueError, TypeError, RecursionError):
            raise format_error() from None
        if not isinstance(result, dict) or type(result.get("ResCode")) is not int:
            raise format_error()
        if result["ResCode"] == 0 and result.get("Success") is not True:
            raise format_error()
        return result

    @staticmethod
    def _reject_constant(value):
        raise ValueError("Invalid JSON constant")

    @staticmethod
    def _check_status(result: dict):
        code = result["ResCode"]
        if code == 0:
            return
        if code in {401, 405, 406, 407, 501, 503, 402, 504}:
            raise BusinessError("AUTH_FAILED", "ERP 身份认证失败或令牌无效，请检查应用和账号配置。")
        if code in {408, 601}:
            raise BusinessError("PERMISSION_DENIED", "ERP 拒绝组织或客户端访问，请检查授权范围。")
        raise BusinessError("UPSTREAM_ERROR", "ERP 未能完成请求，请用追踪 ID 联系维护人员。")

    async def _login(self):
        cfg = self.settings
        result = await self._request(
            AUTH_PATH,
            params={
                "clientid": cfg.client_id,
                "clientsecret": cfg.client_secret.get_secret_value(),
                "entCode": cfg.enterprise_code,
                "orgCode": cfg.organization_code,
                "userCode": cfg.user_code,
            },
        )
        self._check_status(result)
        token = result.get("Data")
        if not isinstance(token, str) or not token.strip() or any(ord(c) < 32 for c in token):
            raise format_error()
        self._token = token

    async def query_item(self, item_code: str) -> list[dict]:
        async with self._lock:
            if self._token is None:
                await self._login()
            result = await self._request(
                ITEM_PATH, body=[{"ItemMaster": {"Code": item_code}}], token=self._token
            )
            if result["ResCode"] in {402, 504}:
                self._token = None
                await self._login()
                result = await self._request(
                    ITEM_PATH, body=[{"ItemMaster": {"Code": item_code}}], token=self._token
                )
                if result["ResCode"] in {402, 504}:
                    self._token = None
            self._check_status(result)
            data = result.get("Data")
            # Actual installation returns an array; fail closed on undocumented alternatives.
            if not isinstance(data, list) or any(not isinstance(item, dict) for item in data):
                raise format_error()
            return data
