# 接口适配记录

记录日期：2026-09-10。按照“文档 → 最小脚本 → 工具契约 → 分层实现 → MCP 与 ERP 核对”顺序完成。

## 来源

- [官方文档页面](https://openapi.yyu9c.com/doc.html#/home)
- [页面实际配置](https://openapi.yyu9c.com/v3/api-docs/swagger-config)，仅列出 U9C OPENAPI 一个分组文件。
- [完整 OpenAPI JSON](https://openapi.yyu9c.com/file/U9COPENAPI.json)
- [接入说明 PDF](https://openapi.yyu9c.com/file/document.pdf)，共 17 页；全文提取并查看认证/返回码关键页面。
- 原始 JSON SHA-256：`06b7c838070f4c14c9f76333457470b7ceb01c74033538f706da8728b2f92be9`。

官方 JS 通用分支中的 swagger-resources/static services 路径在此站点为 404；最终资源地址依据浏览器实际加载记录确认，未据此猜测公司 ERP 接口路径。没有尝试绕过本机 Swagger 的访问限制。

## 认证

| 属性 | 确认内容 |
| --- | --- |
| 方法/路径 | `GET {U9_BASE_URL}/webapi/OAuth2/AuthLogin` |
| 参数 | `clientid`、`clientsecret`、`entCode`、`orgCode`、`userCode` |
| 参数来源 | 授权用户确认；账号密码用于 ERP 页面登录，应用密钥用于 API 认证，二者不混用 |
| 可选参数 | loginType/loginDate/language 未传；不在本地编造新默认值 |
| 成功条件 | ResCode 为整数 0，Success 为 true，Data 为非空 Token 字符串 |
| Token 使用 | HTTP 请求头 `token`，不是推断出来的 Bearer 认证 |
| 存储 | 内存；不持久化 Token，不返回给 MCP 调用方 |
| 有效期 | 文档说明配置上限 240 分钟，当前具体配置未读取；不猜测 TTL |
| 恢复 | 只在文档过期码 402/504 时重新认证一次；同一进程串行，避免并发重复认证 |

文档指出重新获取 Token 或重启 IIS 会使已有 Token 失效。多个进程/其他系统共享同一个应用身份时可能互相影响；本阶段是单本地进程，未验证跨进程 Token 协调。

## 单料品查询

`POST {U9_BASE_URL}/webapi/ItemMaster/Query`，`Content-Type: application/json`。

下例完全虚构：

```json
[{"ItemMaster":{"Code":"SYN-ITEM"}}]
```

请求 Model：`UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.QueryItemDTOData`；ItemMaster 引用 `UFIDA.U9.ISV.PUB.RestSV.CommonArchiveDataDTOData`。没有分页或组织输入属性；组织由认证上下文绑定。OtherID 是三方关联标识，本阶段不需要，不作为幂等键使用。

响应 Model：`ApiResult[List[UFIDA.U9.ISV.Item.ItemMasterDTOData]]`。本机实际 Data 为 JSON 数组；虽然 PDF 描述过序列化 Data，一旦此环境改为字符串/其他结构，当前适配器报格式变化，不自行猜测解析策略。

| 上游字段 | 工具字段 | 规则 |
| --- | --- | --- |
| m_iD | id | 正整数 int64 → 十进制字符串 |
| m_code | code | 与请求准确料号一致，否则格式错误 |
| m_name | name | 必须为字符串，不把缺失转换为无结果 |
| m_sPECS | specifications | 字符串或显式 null；缺失为结构变化 |
| m_org | organization | 必须存在；编码与配置和输入一致 |
| m_inventoryUOM | inventory_unit | 库存主单位，保持 ID/编码/名称 |
| m_purchaseUOM | purchase_unit | 采购单位，保持 ID/编码/名称 |
| m_salesUOM | sales_unit | 销售单位，保持 ID/编码/名称 |
| 引用对象 m_iD/m_code/m_name | id/code/name | 同样严格校验；不透传 `$id`、sysState 等内部信息 |

单位显式 null 可以返回 null，单位对象或属性缺失则报格式变化。JSON `$ref` 形式的对象替代不在当前实测结构中，遇到时失败并要求维护适配器；不擅自把未知引用当空值。

成功样本返回一条，ERP 页面按同一准确料号/组织核对名称、规格和三个单位名称一致；不存在料号实测返回 ResCode=0、Data=[]。不存在的料号不映射成权限错误。

## 错误边界

接入 PDF 第 2–3 页给出 ResCode：0 成功；401 未授权；402 Token 过期；403 请求过期；404 路由错误；405 授权码过期；406 用户不存在；407 ClientID 未启用；408 组织不存在；500 内部错误；501 验签失败；502 参数错误；503 登录失败；504 Token 失效；601 客户端 IP 未授权。

以上是 ERP 响应体业务代码，与 HTTP 状态码分开处理。本阶段按认证、组织/IP、过期恢复及其他上游错误分类；ResMsg/Exception 不进入工具结果。文档定义并不意味着每种错误已经在真实环境触发；异常覆盖采用模拟测试，避免修改授权或破坏环境来造错。

原始成功响应、页面核对期望只存 `.local/erp-evidence/`。记录中不包含密码、应用密钥、Token、Cookie 或真实料品编号。
