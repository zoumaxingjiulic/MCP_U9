from typing import Literal

ErrorCode = Literal[
    "INVALID_ARGUMENT",
    "PERMISSION_DENIED",
    "AUTH_FAILED",
    "AMBIGUOUS_ENTITY",
    "UPSTREAM_TIMEOUT",
    "UPSTREAM_UNAVAILABLE",
    "UPSTREAM_FORMAT_CHANGED",
    "UPSTREAM_ERROR",
    "INTERNAL_ERROR",
]


class BusinessError(Exception):
    def __init__(self, code: ErrorCode, message: str, *, retryable: bool = False):
        self.code = code
        self.message = message
        self.retryable = retryable
        super().__init__(message)


def format_error() -> BusinessError:
    return BusinessError("UPSTREAM_FORMAT_CHANGED", "ERP 响应结构不符合已验证契约，请联系维护人员。")
