"""One bounded read-only probe using documented U9 endpoints. No credential output."""

import json
import os
from decimal import Decimal
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]


def config():
    values = {}
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key] = value
    return {key: os.environ.get(key, value) for key, value in values.items()}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--item-code")
    args = parser.parse_args()
    cfg = config()
    opener = build_opener(ProxyHandler({}), NoRedirect())

    def request(path, *, params=None, body=None, token=None):
        url = cfg["U9_BASE_URL"].rstrip("/") + path
        if params:
            url += "?" + urlencode(params)
        headers = {"Accept": "application/json"}
        if token:
            headers["token"] = token
        if body is not None:
            headers["Content-Type"] = "application/json"
        req = Request(url, data=None if body is None else json.dumps(body).encode(), headers=headers)
        try:
            with opener.open(req, timeout=20) as response:
                raw = response.read(2_000_001)
                if len(raw) > 2_000_000:
                    raise ValueError("response too large")
                result = json.loads(raw, parse_float=Decimal)
        except HTTPError as exc:
            print(json.dumps({"stage": path, "http_status": exc.code}))
            raise SystemExit(1) from None
        except (URLError, ValueError):
            print(json.dumps({"stage": path, "error": "NETWORK_OR_FORMAT_ERROR"}))
            raise SystemExit(1) from None
        print(
            json.dumps(
                {
                    "stage": path,
                    "ResCode": result.get("ResCode"),
                    "Success": result.get("Success"),
                    "data_type": type(result.get("Data")).__name__,
                }
            )
        )
        return result

    login = request(
        "/webapi/OAuth2/AuthLogin",
        params={
            "clientid": cfg["U9_CLIENT_ID"],
            "clientsecret": cfg["U9_CLIENT_SECRET"],
            "entCode": cfg["U9_ENT_CODE"],
            "orgCode": cfg["U9_ORG_CODE"],
            "userCode": cfg["U9_USER_CODE"],
        },
    )
    if login.get("ResCode") != 0 or not isinstance(login.get("Data"), str) or not login["Data"]:
        raise SystemExit(1)
    if not args.item_code:
        return
    result = request(
        "/webapi/ItemMaster/Query", token=login["Data"], body=[{"ItemMaster": {"Code": args.item_code}}]
    )
    if result.get("ResCode") != 0:
        raise SystemExit(1)
    # Raw evidence stays local and ignored; never print complete ERP objects.
    private = ROOT / ".local" / "erp-evidence"
    private.mkdir(parents=True, exist_ok=True)
    (private / "item-query.json").write_text(
        json.dumps(result, ensure_ascii=False, default=str, indent=2), encoding="utf-8"
    )
    data = result.get("Data")
    if isinstance(data, str):
        data = json.loads(data, parse_float=Decimal)
    print(
        json.dumps(
            {
                "data_type": type(data).__name__,
                "count": len(data) if isinstance(data, list) else None,
                "first_record_fields": sorted(data[0])
                if isinstance(data, list) and data and isinstance(data[0], dict)
                else [],
            }
        )
    )


if __name__ == "__main__":
    main()
