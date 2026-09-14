# 首个只读工具契约

状态：最小真实 ERP 调用已通过，以下为本阶段实现边界；最终三类测试见验收记录。

- 工具：`u9_get_item`，中文名“查询单个料品”。
- 输入：只需必填 `item_code` 非空字符串，保留前导零；组织自动使用服务端 `U9_ORG_CODE`。兼容旧客户端可选 `organization_code`，若提供必须等于授权组织，不能切换组织；拒绝未知字段、通配符、显式 null 和首尾空白。长度上限 100 是本服务限制，不宣称为 U9 上限。
- 用途：在服务配置的企业和唯一授权组织中，按准确料号获取料品档案。没有模糊搜索、跨组织、库存数量或金额统计。
- 身份：stdio 或 HTTP 服务进程固定绑定一个 ERP 应用/用户/企业/组织；调用者共享该身份，不提供多人身份隔离。HTTP 入口要求独立 Bearer 令牌。每次调用使用服务端组织，校验可选的输入组织，并再次核对 ERP 返回组织和料号。输出 query 保留实际查询组织以便核对。
- 已验证接口：`GET {U9_BASE_URL}/webapi/OAuth2/AuthLogin`；`POST {U9_BASE_URL}/webapi/ItemMaster/Query`，请求头 `token`，请求体 `[{"ItemMaster":{"Code":"准确料号"}}]`。
- 输出：追踪 ID、成功标志、数据或安全错误。成功数据包含实际查询范围、`total`、`returned`、`has_more=false`、最多一条 `items`；料品包含字符串 ID、编码、品名、规格、组织、库存/采购/销售单位的 ID、编码和名称。仅白名单字段。
- 分页：上游该查询 DTO 没有分页参数，本阶段精确查询最多一个对象。返回多条时报告歧义，不截断、不编造总数或分页。无匹配返回空列表；真实空结果行为另行验证。
- 精度与单位：所有 int64 ID 转为十进制字符串，避免 JavaScript 精度损失；本阶段不输出金额/数量、不做单位换算、币种汇总和状态编码解释。HTTP JSON 小数使用 Decimal 解析，为未来能力保留原始精度。
- 错误：`INVALID_ARGUMENT`、`PERMISSION_DENIED`、`AUTH_FAILED`、`AMBIGUOUS_ENTITY`、`UPSTREAM_TIMEOUT`、`UPSTREAM_UNAVAILABLE`、`UPSTREAM_FORMAT_CHANGED`、`UPSTREAM_ERROR`、`INTERNAL_ERROR`。业务失败标记 MCP `isError=true`；错误不返回上游 ResMsg、Exception、URL、Token 或业务原文。
- 网络：单进程最多一个在途业务调用；单 HTTP 调用 20 秒，整个业务调用（含等待）50 秒；响应体最多 2 MB。Token 仅存内存，只有已记录的过期码 402/504 触发最多一次重新认证/重试；不自动重试业务超时或普通错误。取消会停止等待/网络请求；不能保证远端已启动的查询停止。
- 权限提示：`readOnlyHint=true`、`openWorldHint=false`；提示不是权限机制。没有写入工具。
- 日志：stderr 仅记录工具、追踪 ID、耗时和安全错误码；stdout 专用于 MCP。
- Schema：从 Pydantic 模型生成，工具列表中提供 inputSchema/outputSchema；协议由官方 `mcp==2.2.0` SDK 处理。
- 测试：模拟 ERP HTTP 覆盖成功/空结果/参数/认证/权限/超时/结构变化/上限/Token 过期；官方 MCP 客户端通过真实 stdio 和 Streamable HTTP 子进程测试初始化、发现、调用、认证及错误；授权 ERP 样本与页面核对，真实数据保存在忽略目录。

完整版本/补丁号尚未从页面获得，“关于”页仅显示 U9Cloud 标准版；当前契约仅对已实测接口成立，不承诺其他补丁或其他工具。
