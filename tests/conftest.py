"""All test identities and objects are fabricated, never copied from ERP."""

from copy import deepcopy

import pytest

from u9_mcp.config import Settings


@pytest.fixture
def settings():
    return Settings(
        base_url="https://erp.example.invalid/U9C",
        client_id="TEST-APP",
        client_secret="synthetic-secret",
        enterprise_code="TEST-ENT",
        organization_code="TEST-ORG",
        user_code="TEST-USER",
    )


def synthetic_item():
    archive = {"m_iD": 9007199254740993, "m_code": "TEST-ORG", "m_name": "虚构测试组织"}
    unit = {"m_iD": 9007199254740997, "m_code": "SYN-UOM", "m_name": "测试单位"}
    return {
        "m_iD": 9007199254740995,
        "m_code": "SYN-ITEM",
        "m_name": "虚构测试料品",
        "m_sPECS": "测试规格",
        "m_org": archive,
        "m_inventoryUOM": unit,
        "m_purchaseUOM": deepcopy(unit),
        "m_salesUOM": deepcopy(unit),
        "m_standardCost": "not exposed",
        "Description": "untrusted text must not be exposed",
    }


@pytest.fixture
def row():
    return synthetic_item()
