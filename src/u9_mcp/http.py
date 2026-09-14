import secrets

from starlette.datastructures import Headers
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp, Receive, Scope, Send

from .config import HttpSettings


async def health(request) -> JSONResponse:
    """Liveness only: never contacts ERP or returns configuration."""
    return JSONResponse({"status": "ok"})


class BearerTokenMiddleware:
    """Protect every endpoint except liveness with a deployment access token."""

    def __init__(self, app: ASGIApp, settings: HttpSettings):
        self.app = app
        self._expected = settings.access_token.get_secret_value()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or scope.get("path") == "/healthz":
            await self.app(scope, receive, send)
            return
        authorization = Headers(scope=scope).get("authorization", "")
        prefix = "Bearer "
        candidate = authorization[len(prefix) :] if authorization.startswith(prefix) else ""
        if len(candidate) > 512 or not secrets.compare_digest(candidate, self._expected):
            response = Response(
                "Unauthorized",
                status_code=401,
                headers={"WWW-Authenticate": 'Bearer realm="u9-cloud-mcp"'},
            )
            await response(scope, receive, send)
            return
        await self.app(scope, receive, send)
