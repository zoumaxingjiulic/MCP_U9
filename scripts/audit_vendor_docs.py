"""Inventory every operation, model field and reference; does not contact ERP."""

import hashlib
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".local/vendor-docs/U9COPENAPI.json"
OUT = ROOT / "docs/reference"
METHODS = {"get", "post", "put", "delete", "patch", "head", "options", "trace"}


def walk(value, location=""):
    yield location, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, f"{location}/{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{location}/{index}")


def main():
    raw = SOURCE.read_bytes()
    doc = json.loads(raw.decode("utf-8-sig"))
    models = doc["components"]["schemas"]
    ops = [
        (path, method, value)
        for path, entry in doc["paths"].items()
        for method, value in entry.items()
        if method in METHODS
    ]
    refs, broken, external = [], [], []
    for location, value in walk(doc):
        if isinstance(value, dict) and "$ref" in value:
            ref = value["$ref"]
            refs.append({"location": location, "ref": ref})
            if not ref.startswith("#/"):
                external.append(ref)
                continue
            target = doc
            try:
                for part in ref[2:].split("/"):
                    target = target[part.replace("~1", "/").replace("~0", "~")]
            except (KeyError, TypeError):
                broken.append({"location": location, "ref": ref})
    counts = Counter(tag for _, _, op in ops for tag in op.get("tags", ["UNTAGGED"]))
    audit = {
        "source_url": "https://openapi.yyu9c.com/file/U9COPENAPI.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "inspected_at": datetime.now(UTC).isoformat(),
        "declared_openapi": doc.get("openapi"),
        "info": doc.get("info"),
        "servers": doc.get("servers"),
        "paths": len(doc["paths"]),
        "operations": len(ops),
        "models": len(models),
        "model_properties": sum(len(m.get("properties", {})) for m in models.values()),
        "references": len(refs),
        "broken_references": broken,
        "external_references": external,
        "groups": dict(sorted(counts.items())),
        "operations_without_summary": sum(not op.get("summary") for _, _, op in ops),
        "operations_without_security_declaration": sum("security" not in op for _, _, op in ops),
        "legacy_body_parameters": sum(
            p.get("in") == "body" for _, _, op in ops for p in op.get("parameters", [])
        ),
        "legacy_response_schemas": sum(
            "schema" in r for _, _, op in ops for r in op.get("responses", {}).values()
        ),
        "deprecated_operations": [f"{m.upper()} {p}" for p, m, o in ops if o.get("deprecated")],
        "models_without_required": sum(not m.get("required") for m in models.values()),
        "properties_without_description": sum(
            not p.get("description") for m in models.values() for p in m.get("properties", {}).values()
        ),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")
    preamble = (
        "# 官方文档全量结构索引\n\n"
        "来源：https://openapi.yyu9c.com/file/U9COPENAPI.json\n\n"
        "这是公开文档的逐项提取，不代表所有接口均已在公司环境验证，也不代表公开版本与本机补丁一致。"
        "原文缺少的必填、状态含义、精度、权限和分页信息不做补写。\n\n"
    )
    operations = [preamble, f"操作总数：{len(ops)}。\n\n"]
    for path, method, op in ops:
        operations += [
            f"## {method.upper()} {path}\n\n",
            "```json\n" + json.dumps(op, ensure_ascii=False, indent=2) + "\n```\n\n",
        ]
    (OUT / "all-operations.md").write_text("".join(operations), encoding="utf-8")
    definitions = [preamble, f"Model 总数：{len(models)}。\n\n"]
    for name, schema in models.items():
        definitions += [
            f"## {name}\n\n",
            "```json\n" + json.dumps(schema, ensure_ascii=False, indent=2) + "\n```\n\n",
        ]
    (OUT / "all-models.md").write_text("".join(definitions), encoding="utf-8")
    index = [preamble, "| 业务分组 | 操作数 |\n| --- | ---: |\n"]
    index.extend(f"| {name} | {count} |\n" for name, count in sorted(counts.items()))
    index += [
        "\n完整参数、响应及 Model 字段见 [所有接口](all-operations.md) 和 [所有 Model](all-models.md)。\n",
        "\n自动遍历所有节点与引用完成；语义联调范围仍仅限首个只读场景。\n",
    ]
    (OUT / "README.md").write_text("".join(index), encoding="utf-8")
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
