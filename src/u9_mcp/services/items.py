import asyncio

from ..adapters.items import adapt_item
from ..clients.u9 import U9Client
from ..errors import BusinessError
from ..schemas import ItemQuery, QueryResult


class ItemService:
    def __init__(self, client: U9Client):
        self.client = client

    async def get_item(self, query: ItemQuery) -> QueryResult:
        settings = self.client.settings
        if query.organization_code != settings.organization_code:
            raise BusinessError("PERMISSION_DENIED", "只能查询服务配置中已授权的组织。")
        try:
            async with asyncio.timeout(50):
                rows = await self.client.query_item(query.item_code)
        except TimeoutError:
            raise BusinessError(
                "UPSTREAM_TIMEOUT", "查询等待或执行超时，请稍后重试。", retryable=True
            ) from None
        if len(rows) > 1:
            raise BusinessError("AMBIGUOUS_ENTITY", "准确料号返回多个对象，请核实 ERP 组织与档案唯一性。")
        items = [
            adapt_item(row, organization_code=query.organization_code, item_code=query.item_code)
            for row in rows
        ]
        return QueryResult(
            enterprise_code=settings.enterprise_code,
            query=query,
            total=len(items),
            returned=len(items),
            items=items,
        )
