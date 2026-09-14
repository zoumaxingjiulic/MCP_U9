# U9 Cloud ERP MCP

第一阶段提供一个可独立运行的只读业务工具：`u9_get_item`，按组织和准确料号查询料品名称、规格与计量单位。使用官方 Python MCP SDK `mcp==2.2.0`，同时支持本地 stdio 和服务器 Streamable HTTP；业务服务不依赖大模型或聊天页面。

已通过模拟接口测试、官方 SDK 客户端的真实 stdio/Streamable HTTP 协议测试，以及授权 ERP 环境的页面字段核对。详细边界和未完成事项见 [验收记录](docs/verification.md)。

## 本地使用

Python 3.12+ 与 uv；本次验证使用 Python 3.14.3。依赖已锁定在 `uv.lock`。

```powershell
uv sync --locked
```

当前电脑的授权配置已写入私有 `.env`，并被 Git 忽略。新环境参照 `.env.example` 填写；不要覆盖现有私有配置。`U9_BASE_URL` 为已确认的 U9 应用根地址，不含 `/webapi`。进程环境变量优先于文件，未传 `--env-file` 时只读取环境变量。

运行服务：

```powershell
uv run u9-mcp --env-file .env
```

服务启动后等待 MCP 客户端发送协议消息；终端没有聊天界面或欢迎文本是正常现象。stdout 只传协议，审计日志写入 stderr。

支持 stdio 的 MCP 宿主可参考 [mcp.example.json](mcp.example.json) 中的启动命令。文件不含凭据；其他客户端按其配置格式填入同一 command/args，项目移动后需修改绝对路径。该示例不会自动修改任何宿主配置。

也可用项目提供的官方 SDK 客户端查询（下列编码是虚构示例，需替换为已授权组织及真实料号）：

```powershell
uv run python examples/query_item.py --env-file .env --organization-code TEST-ORG --item-code SYN-ITEM
```

## Docker 部署

服务器需安装 Docker Engine 与 Compose 插件。复制示例配置并在服务器本地填写，`.env` 已被 Git 和 Docker 构建上下文忽略：

```bash
cp .env.example .env
python3 -c "import secrets; print(secrets.token_urlsafe(48))"
```

将生成值写入 `MCP_ACCESS_TOKEN`。`MCP_ALLOWED_HOSTS` 必须列出客户端实际访问的域名或 IP（含端口或使用 `:*`），例如 `mcp.example.com,192.168.1.30:*`。若 U9 仍为已授权的内网 HTTP 地址，显式设置 `U9_ALLOW_HTTP=true`。

默认端口只发布到服务器的 `127.0.0.1`，适合由 Nginx/Caddy/API 网关终止 HTTPS：

```bash
docker compose up -d --build
docker compose ps
curl http://127.0.0.1:8000/healthz
```

MCP 地址为 `https://mcp.example.com/mcp`，客户端每个请求需带 `Authorization: Bearer <MCP_ACCESS_TOKEN>`。直接在受信内网开放时，在 `.env` 设置 `MCP_BIND_IP=0.0.0.0`；不要把明文 HTTP 端口直接暴露到公网。浏览器客户端还需将精确 Origin 加入 `MCP_ALLOWED_ORIGINS`，原生 MCP 客户端通常留空。

更新代码后重新构建并检查日志：

```bash
git pull --ff-only
docker compose up -d --build
docker compose logs --tail=100 u9-mcp
```

用官方 SDK 客户端验证部署实例（示例编码需替换）：

```bash
export MCP_ACCESS_TOKEN='服务器中的同一令牌'
uv run python examples/query_item_http.py \
  --url https://mcp.example.com/mcp \
  --organization-code TEST-ORG \
  --item-code SYN-ITEM
```

授权环境的正式字段核对使用忽略目录中的人工期望值：

```bash
export MCP_ACCESS_TOKEN='服务器中的同一令牌'
uv run python scripts/verify_live_mcp_http.py \
  --url https://mcp.example.com/mcp \
  --expected .local/erp-evidence/expected.json
```

`/healthz` 仅表示 MCP 进程存活，不读取配置或探测 ERP。业务可用性应以授权料号的 MCP 查询及 ERP 页面字段核对为准。当前静态 Bearer 令牌适用于单一受信调用方；多人独立身份、OAuth 和按用户映射 ERP 权限属于后续阶段。

工具输入：

```json
{"organization_code":"TEST-ORG","item_code":"SYN-ITEM"}
```

完整输入和输出定义见 [JSON Schema](docs/schemas/u9_get_item.json) 与 [工具契约](docs/tool-contract.md)。没有物料匹配时返回空列表；无权限、超时和接口格式变化均返回错误，不伪装为空结果。

## 代码结构

```text
src/u9_mcp/
  config.py        私有配置与校验
  clients/         HTTP、应用认证、内存 Token、超时和限额
  adapters/        上游结构校验、ID 精度与白名单字段映射
  services/        组织授权、准确匹配和单对象完整性
  schemas.py       严格输入、输出模型
  errors.py        安全业务错误
  tools/           MCP 工具定义与结构化结果
  server.py        官方 SDK 生命周期、stdio 与 Streamable HTTP 入口
  http.py          HTTP Bearer 认证和存活检查
tests/             纯虚构数据，模拟 ERP 与真实 stdio/HTTP MCP 子进程
scripts/           文档盘点、最小探测、Schema 导出和真实验收
examples/          独立 MCP 查询客户端
```

## 验证

自动化测试不读取 `.env`，不连接真实 ERP：

```powershell
uv run pytest -q
uv run ruff check src tests scripts examples
uv run ruff format --check src tests scripts examples
docker compose config
```

授权真实联调单独执行，`expected.json` 的期望值必须从 ERP 页面取得，不能从同一次 API 返回值自动生成。核对结果只打印通过状态和字段名：

```powershell
uv run python scripts/verify_live_mcp.py --env-file .env --expected .local/erp-evidence/expected.json
uv run python scripts/verify_live_mcp_http.py --url https://mcp.example.com/mcp --expected .local/erp-evidence/expected.json
```

该私有核对文件仅存在于当前工作目录，不提交。工具只返回必要业务字段，所有金额、数量及状态映射均不在本阶段范围。一个进程固定绑定一个 ERP 用户/应用/企业/组织；这不等于多人身份隔离。

## 文档

- [需求与边界](docs/requirements.md)
- [接口适配与实际字段映射](docs/api-mapping.md)
- [全部接口和 Model 索引](docs/reference/README.md)：618 个操作、839 个 Model、12,455 个属性，保留原文参数、类型、枚举、约束、响应与引用。
- [官方文档审阅发现](docs/document-review.md)
- [工具契约](docs/tool-contract.md) / [验收记录与限制](docs/verification.md)

文档来自官方页面实际加载的公开资源。需要刷新时先下载，再盘点；新版盘点结果不代表已完成新版 ERP 联调：

```powershell
uv run python scripts/fetch_vendor_docs.py
uv run python scripts/audit_vendor_docs.py
uv run python scripts/export_tool_schema.py
```

本项目实现仅接受已明确的查询接口，不提供任意 URL、SQL、脚本或写操作工具。所有写入能力均需后续独立设计与验收。
