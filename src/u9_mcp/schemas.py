from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from .errors import ErrorCode


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, hide_input_in_errors=True)


class ItemQuery(StrictModel):
    organization_code: str = Field(min_length=1, max_length=100, description="服务配置中已授权的组织编码")
    item_code: str = Field(min_length=1, max_length=100, description="准确料号，保留前导零，不支持模糊匹配")

    @field_validator("organization_code", "item_code")
    @classmethod
    def exact_code(cls, value: str) -> str:
        if value != value.strip() or any(ord(c) < 32 for c in value) or any(c in value for c in "*%?"):
            raise ValueError("必须提供准确编码，不支持通配符或首尾空白")
        return value


class Archive(StrictModel):
    id: str = Field(pattern=r"^[1-9][0-9]*$")
    code: str = Field(min_length=1)
    name: str


class Item(StrictModel):
    id: str = Field(pattern=r"^[1-9][0-9]*$")
    code: str = Field(min_length=1)
    name: str
    specifications: str | None
    organization: Archive
    inventory_unit: Archive | None
    purchase_unit: Archive | None
    sales_unit: Archive | None


class QueryResult(StrictModel):
    enterprise_code: str
    query: ItemQuery
    total: Literal[0, 1]
    returned: Literal[0, 1]
    has_more: Literal[False] = False
    items: list[Item] = Field(max_length=1)


class ErrorInfo(StrictModel):
    code: ErrorCode
    message: str
    retryable: bool


class ToolResult(StrictModel):
    trace_id: str
    success: bool
    data: QueryResult | None = None
    error: ErrorInfo | None = None

    @model_validator(mode="after")
    def consistent_result(self):
        if self.success != (self.data is not None and self.error is None):
            raise ValueError("结果状态不一致")
        if not self.success and (self.error is None or self.data is not None):
            raise ValueError("错误结果状态不一致")
        return self
