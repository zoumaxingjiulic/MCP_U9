# 官方文档审阅与缺口

已获取官方页面配置所列的整个 OpenAPI 文件，对全部接口、Model、属性及 `$ref` 做遍历、提取与引用完整性检查，形成可搜索原文索引。接入说明 PDF 共 17 页，已全文提取阅读；涉及认证、返回码和有效期的图示已渲染核实。

| 盘点项 | 结果 |
| --- | ---: |
| 路径 | 615 |
| HTTP 操作 | 618 |
| Model | 839 |
| Model 属性 | 12,455 |
| `$ref` | 3,594 |
| 无法解析的引用 | 0 |
| 外部引用 | 0 |
| 缺少 summary 的操作 | 35 |
| 使用旧式 body 参数的操作 | 588 |
| 使用旧式 response schema 的操作 | 618 |
| 未声明 required 的 Model | 731 |
| 没有 description 的属性 | 4,713 |
| 标记 deprecated 的操作 | 10 |

完整参数、响应、类型、format、required、enum 和描述保存在 [全部接口](reference/all-operations.md) 与 [全部 Model](reference/all-models.md)，统计及 SHA-256 在 [audit.json](reference/audit.json)。这是全量结构审阅；其他业务工具的字段语义和企业口径需在各自实现阶段继续核实，不能将结构检查称为全业务验收。

## 影响实现的发现

1. 文件标记 OpenAPI 3.0.1，却使用 `parameters.in=body`、响应体 `schema`、参数顶层 type，以及 `conn`/`proo` 等旧式或非标准字段。因此不把它直接交给自动生成器后认定得到可靠客户端。
2. `info.version=v1` 是接口文档版本，不是公司安装的 U9 版本。servers 写 `http://localhost:8080` 也不是公司 ERP 地址；真实根地址来自授权配置和 PDF 拼接规则。
3. 没有全局 security/securitySchemes 声明；多数业务操作通过显式 `token` header 参数说明认证。缺少 security 声明不等于允许匿名调用。
4. HTTP 方法不能当作业务只读标记：附件删除提供 GET/POST，而物料查询使用 POST。每个工具需按业务动作确认，不能“一切 GET 都只读”。
5. 路径名与摘要存在不一致，例如 `Resource/Delete` 摘要为“资源BOM”、`ItemRequest/Delete` 摘要为“弃审料品需求清单”、RMA/RMR 的部分文字与导航标题不一致。不据此自行修正接口名、审批语义或反向动作。
6. `cc/Create`、`GetCommonReference/Create` 等 Create 路径的说明为获取参照；`CalcQCResult`、打印、附件下载等看似查询的能力可能计算或生成临时文件。它们没有纳入第一阶段工具。
7. 存在 CommonEntity/Query、QueryCommon/QueryInfoBySql 和通用服务执行入口；它们不能直接包装为允许模型传 SQL/实体/任意方法的万能工具。
8. 有明确标注 BIP/YYC/智能工厂专用的接口；发现接口不代表企业授权或许可适用。条码、BIService、BaseInfo、DAS 的认证/组织接口也不能替代已经确认的 OAuth2 流程。
9. 大量响应字段缺少含义说明。`sysState` 枚举数字是对象内部状态，不可直接解释为单据“已审核/未审核”。物料 m_state、库存可用量、采购/销售金额等需各自业务核对。
10. 金额/数量经常声明为 number/double，不能据此假设两位小数或统一单位。本阶段只返回档案与单位，不输出成本字段；JSON 小数用 Decimal，ID 用字符串。
11. 同一业务有 Query、QueryPage、Get...ByPage 等不同查询 DTO 和响应包装；没有统一分页协议可供猜测。本阶段 QueryItemDTOData 只有 ItemMaster/OtherID，采用精确单对象上限。
12. PDF 指出批量调用 ResCode=0 不代表每条业务成功，需检查 Data 中逐条成功标志。此结论主要影响未来写工具；当前读取的物料实体数组经过严格对象校验。
13. PDF 给出有授权/无授权的客开示例和动态 SQL 示例。它们是厂商材料，不构成本项目执行客开、修改权限、写 SQL 或部署的授权；本项目没有采用这些方案。
14. 本机 Swagger 的 IP/正式环境限制在 PDF 中有明确说明，没有尝试绕过。完整补丁清单仍需实施顾问或版本维护资料补充。

## 首阶段选择

ItemMaster/Query 有明确文档、可定位 DTO、只读业务语义和可核对 ERP 页面，最小调用已成功，因此只实现 `u9_get_item`。其他库存、单据、财务、制造、审批、附件、人事和集成能力仅完成文档盘点，没有暴露为 MCP 工具，也没有在企业环境批量调用。
