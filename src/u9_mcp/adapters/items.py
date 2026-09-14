from pydantic import ValidationError

from ..errors import BusinessError, format_error
from ..schemas import Archive, Item


def identifier(value) -> str:
    if type(value) is not int or value <= 0:
        raise format_error()
    return str(value)


def archive(value) -> Archive | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise format_error()
    try:
        return Archive(id=identifier(value["m_iD"]), code=value["m_code"], name=value["m_name"])
    except (KeyError, ValidationError):
        raise format_error() from None


def adapt_item(value: dict, *, organization_code: str, item_code: str) -> Item:
    try:
        org = archive(value["m_org"])
        if org is None:
            raise format_error()
        if org.code != organization_code:
            raise BusinessError("PERMISSION_DENIED", "ERP 返回的组织不在本次授权范围内。")
        if value["m_code"] != item_code:
            raise format_error()
        return Item(
            id=identifier(value["m_iD"]),
            code=value["m_code"],
            name=value["m_name"],
            specifications=value["m_sPECS"],
            organization=org,
            inventory_unit=archive(value["m_inventoryUOM"]),
            purchase_unit=archive(value["m_purchaseUOM"]),
            sales_unit=archive(value["m_salesUOM"]),
        )
    except (KeyError, ValidationError):
        raise format_error() from None
