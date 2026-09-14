import logging
import time
from uuid import uuid4

from mcp import types
from pydantic import ValidationError

from ..errors import BusinessError
from ..schemas import ErrorInfo, ItemQuery, ToolResult
from ..services.items import ItemService

NAME = "u9_get_item"
LOG = logging.getLogger("u9_mcp.audit")


def definition() -> types.Tool:
    return types.Tool(
        name=NAME,
        title="查询单个料品",
        description=(
            "在服务绑定的企业及授权组织中，按准确料号查询一个料品档案。"
            "只需提供 item_code，保留料号前导零。组织由服务端配置自动确定，不要向用户索要组织编码。"
            "返回品名、规格、组织以及库存/采购/销售单位；无匹配返回空列表。"
            "不支持模糊查询、跨组织查询、库存数量或金额统计，也不修改料品。"
        ),
        input_schema=ItemQuery.model_json_schema(),
        output_schema=ToolResult.model_json_schema(),
        annotations=types.ToolAnnotations(read_only_hint=True, open_world_hint=False),
    )


async def execute(service: ItemService, arguments: dict) -> types.CallToolResult:
    trace_id = str(uuid4())
    started = time.monotonic()
    try:
        query = ItemQuery.model_validate(arguments)
        output = ToolResult(trace_id=trace_id, success=True, data=await service.get_item(query))
    except ValidationError:
        output = ToolResult(
            trace_id=trace_id,
            success=False,
            error=ErrorInfo(
                code="INVALID_ARGUMENT",
                message="请提供准确的 item_code 字符串；组织编码可省略，不接受额外字段、通配符或首尾空白。",
                retryable=False,
            ),
        )
    except BusinessError as exc:
        output = ToolResult(
            trace_id=trace_id,
            success=False,
            error=ErrorInfo(code=exc.code, message=exc.message, retryable=exc.retryable),
        )
    except Exception:  # noqa: BLE001 - Last protocol boundary must never expose ERP exceptions or secrets.
        output = ToolResult(
            trace_id=trace_id,
            success=False,
            error=ErrorInfo(
                code="INTERNAL_ERROR",
                message="内部处理失败，请提供追踪 ID 联系维护人员。",
                retryable=False,
            ),
        )
    payload = output.model_dump(mode="json")
    LOG.info(
        "tool=%s trace_id=%s duration_ms=%d status=%s",
        NAME,
        trace_id,
        (time.monotonic() - started) * 1000,
        "OK" if output.success else output.error.code,
    )
    return types.CallToolResult(
        content=[types.TextContent(type="text", text=output.model_dump_json())],
        structured_content=payload,
        is_error=not output.success,
    )
