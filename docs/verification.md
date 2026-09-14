# 第一阶段验证记录

业务验收日期：2026-09-10；Streamable HTTP 与容器配置验证日期：2026-09-14。

| 检查 | 状态与证据 |
| --- | --- |
| 参考总结 | 已完整阅读用户提供的 OA 总结，未复用其认证或假设接口 |
| 系统版本 | ERP 登录页与“关于”页确认 U9Cloud 标准版；完整版本号/补丁清单尚未获取 |
| 文档覆盖 | 618 个操作、839 个 Model、12,455 属性全量提取，3,594 引用全部可解析 |
| 身份及组织 | 用户确认参数含义，登录页核实企业/组织，API 返回组织再次核对 |
| 最小认证 | 官方 AuthLogin 在授权环境 ResCode=0、Success=true，Token 未打印 |
| 最小查询 | 准确料号 Query 返回一条；完成后才设计工具契约并实现 |
| 模拟接口/规则 | 58 项 pytest 通过，使用纯虚构数据，包含下述真实 stdio/HTTP MCP 集成测试 |
| 真实 MCP 协议 | 官方 SDK Client 启动独立服务子进程；stdio 完成初始化、发现、调用、未知工具和错误，Streamable HTTP 完成 Bearer 认证、Host 防护、发现和调用 |
| Schema | 成功/空结果/错误均校验 outputSchema，structuredContent 与文本 JSON 一致 |
| ERP 联调 | 官方 MCP Client 分别经 stdio 和本机 Streamable HTTP 服务连接真实 ERP，查询均通过 |
| 页面核对 | 同组织同料号，编码、品名、规格、组织编码/名称、库存/采购/销售单位名称共 8 项一致 |
| 无结果 | 真实 ERP 不存在料号返回成功空数组，工具 total=returned=0、has_more=false |
| 数据处理 | int64 ID 字符串化，Decimal 解析；不输出金额、数量、状态或备注 |
| 凭据分离 | 应用凭据仅私有 `.env`；登录密码没有写入项目文件；Token 只在内存 |
| 写入和部署 | 无写工具、无数据库/权限修改；已提供非 root、只读文件系统的 Docker/Compose 部署配置 |

自动化覆盖正常、无匹配、必填/类型/额外字段/通配符/范围错误、请求组织越权、返回组织不符、多个匹配、缺失字段、错误 ID、未知引用、错误包装、认证失败、业务错误、HTTP 错误、重定向拒绝、超时、网络异常、2 MB 响应上限、NaN 拒绝、Token 缓存和最多一次过期恢复、取消后锁释放、大整数精度与字段白名单。测试样本均为虚构。

真实联调使用 `scripts/verify_live_mcp.py`，期望值来自 ERP 料品页面。真实样本和原始响应位于忽略目录 `.local/erp-evidence/`，不进入提交。页面仅通过查找读取，不保存、审核、删除或新增料品。

## 尚未完成的扩展验收

- 完整 U9 版本号、补丁清单以及该版本官方支持矩阵仍待补充。已实测功能可用于当前授权环境，不能宣称全部版本兼容。
- 没有实施所有接口的真实业务验证或所有字段的业务口径确认；第一阶段只验证一个工具。
- 没有接入具体大模型或聊天宿主，未运行独立模型选工具评测；官方 MCP 客户端调用已通过。这不会在业务服务内增加模型依赖。
- 仅一个成功料品样本和一个无结果样本完成真实核对，其他异常使用模拟验证；未通过修改 ERP 权限、账号状态或制造生产故障来造错。
- 当前身份共享一个 ERP 应用及账号，不支持多人权限隔离、跨组织、OAuth 或 ERP Token 跨进程协调。Compose 是单实例部署配置，不含集群编排与自动发布流水线。

## 复现

```powershell
uv sync --locked
uv run pytest -q
uv run ruff check src tests scripts examples
uv run ruff format --check src tests scripts examples
docker compose config
uv run python scripts/verify_live_mcp.py --env-file .env --expected .local/erp-evidence/expected.json
MCP_ACCESS_TOKEN=... uv run python scripts/verify_live_mcp_http.py --url https://mcp.example.com/mcp --expected .local/erp-evidence/expected.json
```

新增工具需重新做最小调用、契约、模拟接口、真实 MCP 和 ERP 页面核对，不能用此次测试替代。
