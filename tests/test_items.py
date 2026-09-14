import asyncio
import json
from copy import deepcopy
from decimal import Decimal

import httpx
import pytest
from jsonschema import validate
from pydantic import ValidationError

from u9_mcp.clients.u9 import AUTH_PATH, ITEM_PATH, U9Client
from u9_mcp.config import Settings
from u9_mcp.schemas import ItemQuery
from u9_mcp.services.items import ItemService
from u9_mcp.tools.items import definition, execute

QUERY = {"organization_code": "TEST-ORG", "item_code": "SYN-ITEM"}


async def run(settings, handler, query=None):
    client = U9Client(settings, transport=httpx.MockTransport(handler))
    try:
        result = await execute(ItemService(client), QUERY if query is None else query)
        validate(result.structured_content, definition().output_schema)
        assert json.loads(result.content[0].text) == result.structured_content
        return result
    finally:
        await client.close()


def handler_for(data, *, code=0):
    def handler(request):
        if request.url.path.endswith(AUTH_PATH):
            return httpx.Response(200, json={"ResCode": 0, "Success": True, "Data": "synthetic-token"})
        return httpx.Response(
            200,
            json={
                "ResCode": code,
                "Success": code == 0,
                "Data": data,
                "ResMsg": "secret/internal stack",
                "Exception": "synthetic-secret",
            },
        )

    return handler


async def test_success_exact_request_precision_and_minimal_output(settings, row):
    calls = []
    inner = handler_for([row])

    def handler(request):
        calls.append(request)
        return inner(request)

    result = await run(settings, handler)
    assert not result.is_error
    payload = result.structured_content["data"]
    assert payload["total"] == payload["returned"] == 1
    assert payload["has_more"] is False
    item = payload["items"][0]
    assert item["id"] == "9007199254740995"
    assert item["inventory_unit"]["id"] == "9007199254740997"
    assert set(item) == {
        "id",
        "code",
        "name",
        "specifications",
        "organization",
        "inventory_unit",
        "purchase_unit",
        "sales_unit",
    }
    auth, request = calls
    assert dict(auth.url.params) == {
        "clientid": "TEST-APP",
        "clientsecret": "synthetic-secret",
        "entCode": "TEST-ENT",
        "orgCode": "TEST-ORG",
        "userCode": "TEST-USER",
    }
    assert request.method == "POST" and request.url.path == "/U9C" + ITEM_PATH
    assert request.headers["token"] == "synthetic-token"
    assert json.loads(request.content) == [{"ItemMaster": {"Code": "SYN-ITEM"}}]


async def test_empty(settings):
    result = await run(settings, handler_for([]))
    assert not result.is_error
    assert result.structured_content["data"]["total"] == 0
    assert result.structured_content["data"]["items"] == []


async def test_default_organization_uses_configured_scope(settings, row):
    result = await run(settings, handler_for([row]), {"item_code": "SYN-ITEM"})
    assert not result.is_error
    assert result.structured_content["data"]["query"] == QUERY
    row["m_org"]["m_code"] = "OTHER"
    result = await run(settings, handler_for([row]), {"item_code": "SYN-ITEM"})
    assert result.structured_content["error"]["code"] == "PERMISSION_DENIED"


@pytest.mark.parametrize(
    "query",
    [
        {},
        {**QUERY, "item_code": 1},
        {**QUERY, "extra": True},
        {**QUERY, "item_code": " "},
        {**QUERY, "item_code": " SYN-ITEM"},
        {**QUERY, "item_code": "%"},
        {**QUERY, "item_code": "x" * 101},
        {**QUERY, "organization_code": None},
    ],
)
async def test_invalid_input_does_not_call_erp(settings, query):
    def handler(request):
        pytest.fail("invalid query must not reach ERP")

    result = await run(settings, handler, query)
    assert result.is_error and result.structured_content["error"]["code"] == "INVALID_ARGUMENT"


async def test_local_organization_permission_before_network(settings):
    def handler(request):
        pytest.fail("unauthorized organization reached ERP")

    result = await run(settings, handler, {**QUERY, "organization_code": "OTHER"})
    assert result.structured_content["error"]["code"] == "PERMISSION_DENIED"


async def test_response_organization_mismatch(settings, row):
    row["m_org"]["m_code"] = "OTHER"
    result = await run(settings, handler_for([row]))
    assert result.structured_content["error"]["code"] == "PERMISSION_DENIED"


async def test_multiple_results_never_truncated(settings, row):
    result = await run(settings, handler_for([row, deepcopy(row)]))
    assert result.structured_content["error"]["code"] == "AMBIGUOUS_ENTITY"
    assert result.structured_content["data"] is None


@pytest.mark.parametrize(
    "mutation", ["missing", "wrong_code", "bad_id", "missing_unit", "bad_name", "json_ref"]
)
async def test_response_changes_fail_closed(settings, row, mutation):
    if mutation == "missing":
        del row["m_org"]
    elif mutation == "wrong_code":
        row["m_code"] = "different"
    elif mutation == "bad_id":
        row["m_iD"] = 12.5
    elif mutation == "missing_unit":
        del row["m_inventoryUOM"]
    elif mutation == "bad_name":
        row["m_name"] = 123
    else:
        row["m_inventoryUOM"] = {"$ref": "unverified"}
    result = await run(settings, handler_for([row]))
    assert result.structured_content["error"]["code"] == "UPSTREAM_FORMAT_CHANGED"


@pytest.mark.parametrize("bad_data", [None, {}, "[]", [None]])
async def test_bad_envelope_is_not_empty(settings, bad_data):
    result = await run(settings, handler_for(bad_data))
    assert result.structured_content["error"]["code"] == "UPSTREAM_FORMAT_CHANGED"


@pytest.mark.parametrize(
    "code,expected",
    [
        (401, "AUTH_FAILED"),
        (407, "AUTH_FAILED"),
        (408, "PERMISSION_DENIED"),
        (601, "PERMISSION_DENIED"),
        (500, "UPSTREAM_ERROR"),
        (404, "UPSTREAM_ERROR"),
        (403, "UPSTREAM_ERROR"),
        (502, "UPSTREAM_ERROR"),
    ],
)
async def test_vendor_errors_are_sanitized(settings, code, expected):
    result = await run(settings, handler_for([], code=code))
    assert result.is_error and result.structured_content["error"]["code"] == expected
    assert "synthetic-secret" not in result.content[0].text
    assert "internal stack" not in result.content[0].text


async def test_auth_failure_stops_business_call(settings):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, json={"ResCode": 407, "Success": False, "Data": None})

    result = await run(settings, handler)
    assert len(calls) == 1
    assert result.structured_content["error"]["code"] == "AUTH_FAILED"


@pytest.mark.parametrize("expires_again", [False, True])
@pytest.mark.parametrize("expiry_code", [402, 504])
async def test_token_expiry_retries_at_most_once(settings, row, expires_again, expiry_code):
    counts = {"auth": 0, "query": 0}

    def handler(request):
        if request.url.path.endswith(AUTH_PATH):
            counts["auth"] += 1
            return httpx.Response(200, json={"ResCode": 0, "Success": True, "Data": "synthetic-token"})
        counts["query"] += 1
        code = expiry_code if counts["query"] == 1 or expires_again else 0
        return httpx.Response(200, json={"ResCode": code, "Success": code == 0, "Data": [row]})

    result = await run(settings, handler)
    assert counts == {"auth": 2, "query": 2}
    assert result.is_error is expires_again


@pytest.mark.parametrize(
    "status,expected",
    [
        (302, "UPSTREAM_ERROR"),
        (404, "UPSTREAM_ERROR"),
        (401, "PERMISSION_DENIED"),
        (403, "PERMISSION_DENIED"),
        (429, "UPSTREAM_UNAVAILABLE"),
        (500, "UPSTREAM_UNAVAILABLE"),
    ],
)
async def test_http_failures_and_no_redirect(settings, status, expected):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(status, headers={"Location": "https://other.example.invalid"})

    result = await run(settings, handler)
    assert len(calls) == 1
    assert result.structured_content["error"]["code"] == expected


@pytest.mark.parametrize(
    "kind,expected",
    [
        ("timeout", "UPSTREAM_TIMEOUT"),
        ("network", "UPSTREAM_UNAVAILABLE"),
        ("html", "UPSTREAM_FORMAT_CHANGED"),
        ("oversize", "UPSTREAM_FORMAT_CHANGED"),
        ("false_success", "UPSTREAM_FORMAT_CHANGED"),
        ("bool_code", "UPSTREAM_FORMAT_CHANGED"),
        ("nan", "UPSTREAM_FORMAT_CHANGED"),
    ],
)
async def test_abnormal_transport(settings, kind, expected):
    def handler(request):
        if kind == "timeout":
            raise httpx.ReadTimeout("synthetic-secret", request=request)
        if kind == "network":
            raise httpx.ConnectError("synthetic-secret", request=request)
        if kind == "html":
            return httpx.Response(200, text="<html>synthetic-secret</html>")
        if kind == "oversize":
            return httpx.Response(200, content=b"x" * 2_000_001)
        if kind == "false_success":
            return httpx.Response(200, json={"ResCode": 0, "Success": False, "Data": []})
        if kind == "bool_code":
            return httpx.Response(200, json={"ResCode": False, "Success": True, "Data": []})
        return httpx.Response(200, content=b'{"ResCode":0,"Success":true,"Data":NaN}')

    result = await run(settings, handler)
    assert result.structured_content["error"]["code"] == expected
    assert "synthetic-secret" not in result.content[0].text


async def test_decimal_parsing(settings):
    client = U9Client(
        settings,
        transport=httpx.MockTransport(
            lambda r: httpx.Response(
                200, content=b'{"ResCode":0,"Success":true,"Data":123456789012345.123456789}'
            )
        ),
    )
    try:
        result = await client._request(AUTH_PATH)
        assert result["Data"] == Decimal("123456789012345.123456789")
    finally:
        await client.close()


async def test_token_cache_and_cancellation_release_lock(settings, row):
    entered = asyncio.Event()
    hold = asyncio.Event()
    counts = {"auth": 0, "query": 0}

    async def handler(request):
        if request.url.path.endswith(AUTH_PATH):
            counts["auth"] += 1
            return httpx.Response(200, json={"ResCode": 0, "Success": True, "Data": "synthetic-token"})
        counts["query"] += 1
        if counts["query"] == 1:
            entered.set()
            await hold.wait()
        return httpx.Response(200, json={"ResCode": 0, "Success": True, "Data": [row]})

    client = U9Client(settings, transport=httpx.MockTransport(handler))
    try:
        task = asyncio.create_task(client.query_item("SYN-ITEM"))
        await asyncio.wait_for(entered.wait(), 2)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        result = await asyncio.wait_for(client.query_item("SYN-ITEM"), 2)
        assert result[0]["m_code"] == "SYN-ITEM"
        assert counts == {"auth": 1, "query": 2}
    finally:
        await client.close()


def test_configuration_requires_explicit_http_and_hides_secret(settings):
    with pytest.raises(ValidationError):
        Settings(**{**settings.model_dump(), "base_url": "http://erp.example.invalid/U9C"})
    assert "synthetic-secret" not in repr(settings)
    assert ItemQuery(**QUERY).item_code == "SYN-ITEM"
