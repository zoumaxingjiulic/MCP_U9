# 官方文档全量结构索引

来源：https://openapi.yyu9c.com/file/U9COPENAPI.json

这是公开文档的逐项提取，不代表所有接口均已在公司环境验证，也不代表公开版本与本机补丁一致。原文缺少的必填、状态含义、精度、权限和分页信息不做补写。

操作总数：618。

## POST /webapi/AIRouting/CreateOrUpdate

```json
{
  "tags": [
    "AIRouting"
  ],
  "operationId": "AIRouting_CreateOrUpdate",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.AIRouting.AIRoutingDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.CBO.AIRouting.OptRtnData]]"
      }
    }
  }
}
```
## POST /webapi/AlterDoc/Delete

```json
{
  "tags": [
    "AlterDoc"
  ],
  "summary": "删除资产变更",
  "operationId": "AlterDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "资产变更删除集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AlterDoc/Create

```json
{
  "tags": [
    "AlterDoc"
  ],
  "summary": "创建资产变更",
  "operationId": "AlterDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "创建资产变更集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.FA.AssetChange.InsertAlterDocDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AlterDoc/Approve

```json
{
  "tags": [
    "AlterDoc"
  ],
  "summary": "审核资产变更单",
  "operationId": "AlterDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "审核资产变更集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AlterDoc/Submit

```json
{
  "tags": [
    "AlterDoc"
  ],
  "summary": "提交资产变更单",
  "operationId": "AlterDoc_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "提交资产变更集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AlterDoc/Unapprove

```json
{
  "tags": [
    "AlterDoc"
  ],
  "summary": "弃审资产变更单",
  "operationId": "AlterDoc_Unapprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "弃审资产变更集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/APBill/Create

```json
{
  "tags": [
    "APBill"
  ],
  "summary": "新增应付单",
  "operationId": "APBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "aPBillHeadRDatas",
      "in": "body",
      "description": "应付单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/U9RestSV.Model.AP.APBillHeadRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/APBill/Delete

```json
{
  "tags": [
    "APBill"
  ],
  "summary": "删除应付单",
  "operationId": "APBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDocRDatas",
      "in": "body",
      "description": "应付单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/APBill/CreateBySrc

```json
{
  "tags": [
    "APBill"
  ],
  "summary": "应付外部立账（有来源）",
  "operationId": "APBill_CreateBySrc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "apAccrueAPIDTORDatas",
      "in": "body",
      "description": "应收外部立账集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.AP.APAccrueAPIDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/APBill/Submit

```json
{
  "tags": [
    "APBill"
  ],
  "summary": "提交应付单",
  "operationId": "APBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/APBill/Approve

```json
{
  "tags": [
    "APBill"
  ],
  "summary": "审核应付单",
  "operationId": "APBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/APBill/UnApprove

```json
{
  "tags": [
    "APBill"
  ],
  "summary": "弃审应付单",
  "operationId": "APBill_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ARBill/Create

```json
{
  "tags": [
    "ARBill"
  ],
  "summary": "新增应收单",
  "operationId": "ARBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "aRBillHeadRDatas",
      "in": "body",
      "description": "应收单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/U9RestSV.Model.AR.ARBillHeadRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ARBill/Delete

```json
{
  "tags": [
    "ARBill"
  ],
  "summary": "删除应收单",
  "operationId": "ARBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDocRDatas",
      "in": "body",
      "description": "应收单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ARBill/CreateBySrc

```json
{
  "tags": [
    "ARBill"
  ],
  "summary": "应收外部立账（有来源）",
  "operationId": "ARBill_CreateBySrc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "arAccrueAPIDTORDatas",
      "in": "body",
      "description": "应收外部立账集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.AR.ARAccrueAPIDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ARBill/Submit

```json
{
  "tags": [
    "ARBill"
  ],
  "summary": "提交应收单",
  "operationId": "ARBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ARBill/Approve

```json
{
  "tags": [
    "ARBill"
  ],
  "summary": "审核应收单",
  "operationId": "ARBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ARBill/UnApprove

```json
{
  "tags": [
    "ARBill"
  ],
  "summary": "弃审应收单",
  "operationId": "ARBill_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AssetCard/Delete

```json
{
  "tags": [
    "AssetCard"
  ],
  "summary": "删除资产卡片",
  "operationId": "AssetCard_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "资产卡片主键集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AssetCard/Create

```json
{
  "tags": [
    "AssetCard"
  ],
  "summary": "创建资产卡片",
  "operationId": "AssetCard_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "资产卡片主键集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.FA.AssetCard.InsertAssetCardDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AssetCard/CreateSrcDoc

```json
{
  "tags": [
    "AssetCard"
  ],
  "summary": "创建资产卡片(有来源单据的)",
  "operationId": "AssetCard_CreateSrcDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "资产卡片主键集合",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.FA.AssetCard.InsertAssetCardSrcDocDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AssetCard/Submit

```json
{
  "tags": [
    "AssetCard"
  ],
  "summary": "提交资产卡片",
  "operationId": "AssetCard_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "提交资产卡片集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/AssetCard/Approve

```json
{
  "tags": [
    "AssetCard"
  ],
  "summary": "审核资产卡片",
  "operationId": "AssetCard_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "审核资产卡片集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Attachment/QueryAttachmentPage1

```json
{
  "tags": [
    "Attachment"
  ],
  "summary": "查询U9附件信息",
  "operationId": "Attachment_QueryAttachmentPage1",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Business.CBO.Pub.U9CToBIPAttachQueryParam"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Business.CBO.Pub.U9ToBIPAttachmentReturnDTO]"
      }
    }
  }
}
```

## POST /webapi/Attachment/QueryAttachmentPage

```json
{
  "tags": [
    "Attachment"
  ],
  "summary": "查询U9附件信息2",
  "operationId": "Attachment_QueryAttachmentPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Business.CBO.Pub.U9CToBIPAttachQueryParam"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/System.Web.Http.Results.JsonResult[UFIDA.U9.ISV.PUB.RestSV.Common.ApiResultForDocAttachment[UFIDA.U9.ISV.PUB.RestSV.Business.CBO.Pub.U9ToBIPAttachmentReturnDTO]]"
      }
    }
  }
}
```

## POST /webapi/Attachment/BIPToU9AttachmentCallBack

```json
{
  "tags": [
    "Attachment"
  ],
  "summary": "BIP附件回调",
  "operationId": "Attachment_BIPToU9AttachmentCallBack",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/System.Web.Http.Results.JsonResult[UFIDA.U9.ISV.PUB.RestSV.Common.ApiResultForDocAttachment[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPToU9AttachmentCallBackResp]]"
      }
    }
  }
}
```

## POST /webapi/Attachment/U9ToBIPAttachmentCallBack

```json
{
  "tags": [
    "Attachment"
  ],
  "summary": "",
  "operationId": "Attachment_U9ToBIPAttachmentCallBack",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.U9ToBIPAttachmentCallBackReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/System.Web.Http.Results.JsonResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.U9ToBIPAttachmentCallBackResp]"
      }
    }
  }
}
```

## POST /webapi/AttachmentFile/AttachmentFileUpload

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "附件上传openAPI接口",
  "operationId": "AttachmentFile_AttachmentFileUpload",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "上传内容列表",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.AttachmentFile.AttachmentFileUploadDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]]"
      }
    }
  }
}
```

## GET /webapi/AttachmentFile/Download

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "通过返回地址下载附件，地址可通过上传，下载附件接口获取",
  "operationId": "AttachmentFile_Download",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "code",
      "in": "query",
      "description": "有效编码",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/AttachmentFile/AttachmentFileDownload

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "附件下载openAPI接口",
  "operationId": "AttachmentFile_AttachmentFileDownload",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "handler",
      "in": "query",
      "description": "handler",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]"
      }
    }
  }
}
```

## GET /webapi/AttachmentFile/AttachmentFileDownloadByDocID

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "根据单据ID下载附件",
  "operationId": "AttachmentFile_AttachmentFileDownloadByDocID",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "docid",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]]"
      }
    }
  }
}
```

## POST /webapi/AttachmentFile/AttachmentFileDownloadByDocID

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "根据单据ID下载附件",
  "operationId": "AttachmentFile_AttachmentFileDownloadByDocID",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "docid",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]]"
      }
    }
  }
}
```

## GET /webapi/AttachmentFile/AttachmentFileDeleteByDocID

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "根据单据ID删除附件",
  "operationId": "AttachmentFile_AttachmentFileDeleteByDocID",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "docid",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]]"
      }
    }
  }
}
```

## POST /webapi/AttachmentFile/AttachmentFileDeleteByDocID

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "根据单据ID删除附件",
  "operationId": "AttachmentFile_AttachmentFileDeleteByDocID",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "docid",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]]"
      }
    }
  }
}
```

## GET /webapi/AttachmentFile/AttachmentFileDelete

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "附件删除接口",
  "operationId": "AttachmentFile_AttachmentFileDelete",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "handler",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]"
      }
    }
  }
}
```

## POST /webapi/AttachmentFile/AttachmentFileDelete

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "附件删除接口",
  "operationId": "AttachmentFile_AttachmentFileDelete",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "handler",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.AttachmentFile.FileResult]"
      }
    }
  }
}
```

## POST /webapi/AttachmentFile/UploadToBip

```json
{
  "tags": [
    "AttachmentFile"
  ],
  "summary": "附件同步至BIP",
  "operationId": "AttachmentFile_UploadToBip",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.AttachmentFile.UploadToBipReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.AttachmentFile.UploadToBipResp]"
      }
    }
  }
}
```

## POST /webapi/Bank/Create

```json
{
  "tags": [
    "Bank"
  ],
  "summary": "创建银行网点",
  "operationId": "Bank_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.BankDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Bank/Modify

```json
{
  "tags": [
    "Bank"
  ],
  "summary": "修改银行网点",
  "operationId": "Bank_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.BankDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Bank/Delete

```json
{
  "tags": [
    "Bank"
  ],
  "summary": "删除银行网点",
  "operationId": "Bank_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DeleteBankDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Bank/QueryPage

```json
{
  "tags": [
    "Bank"
  ],
  "summary": "查询银行网点",
  "operationId": "Bank_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonApiQueryParamDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/BankAccount/QueryPage

```json
{
  "tags": [
    "BankAccount"
  ],
  "summary": "查询银行网点",
  "operationId": "BankAccount_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonApiQueryParamDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/BankCategory/QueryPage

```json
{
  "tags": [
    "BankCategory"
  ],
  "summary": "查询银行分类",
  "operationId": "BankCategory_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonApiQueryParamDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/BarCode/Salt

```json
{
  "tags": [
    "BarCode"
  ],
  "summary": "获取登录加密的盐值",
  "operationId": "BarCode_Salt",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltResp]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BarCode/SaltV2

```json
{
  "tags": [
    "BarCode"
  ],
  "operationId": "BarCode_SaltV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltResp]"
      }
    }
  }
}
```

## POST /webapi/BarCode/Login

```json
{
  "tags": [
    "BarCode"
  ],
  "summary": "登录验证",
  "operationId": "BarCode_Login",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.ApiLoginReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.BarCode.ApiLoginResp]"
      }
    }
  }
}
```

## POST /webapi/BarCode/BCToken

```json
{
  "tags": [
    "BarCode"
  ],
  "summary": "条码自动获取token",
  "operationId": "BarCode_BCToken",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetTokenReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.BarCode.GetTokenResp]"
      }
    }
  }
}
```

## GET /webapi/BarCode/Ping

```json
{
  "tags": [
    "BarCode"
  ],
  "summary": "",
  "operationId": "BarCode_Ping",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.PingReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.PingResp"
      }
    }
  }
}
```

## POST /webapi/BarCode/Ents

```json
{
  "tags": [
    "BarCode"
  ],
  "summary": "获取企业列表",
  "operationId": "BarCode_Ents",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BarCode/Orgs

```json
{
  "tags": [
    "BarCode"
  ],
  "summary": "获取组织列表",
  "operationId": "BarCode_Orgs",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BarCode/EntsV2

```json
{
  "tags": [
    "BarCode"
  ],
  "operationId": "BarCode_EntsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  }
}
```

## POST /webapi/BarCode/OrgsV2

```json
{
  "tags": [
    "BarCode"
  ],
  "operationId": "BarCode_OrgsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  }
}
```

## POST /webapi/BarCode/LanguagesV2

```json
{
  "tags": [
    "BarCode"
  ],
  "summary": "获取指定企业下启用的语种信息",
  "operationId": "BarCode_LanguagesV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLanguageListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetLanguageListResp]]"
      }
    }
  }
}
```

## POST /webapi/BarcodeCreate/Create

```json
{
  "tags": [
    "BarcodeCreate"
  ],
  "summary": "创建条码接口",
  "operationId": "BarcodeCreate_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "barcodeDataList",
      "in": "body",
      "description": "条码信息",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.Barcode.BarcodeData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/BarcodeCreate/GetBarCodeByEntityInfo

```json
{
  "tags": [
    "BarcodeCreate"
  ],
  "summary": "依据创建实体获取物料条码",
  "operationId": "BarcodeCreate_GetBarCodeByEntityInfo",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "entityList",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.Barcode.GetDocGeneratedBarCodeData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Collections.Generic.List[System.Collections.Hashtable]]]"
      }
    }
  }
}
```

## POST /webapi/BarcodeCreate/GetDocGenerateQty

```json
{
  "tags": [
    "BarcodeCreate"
  ],
  "summary": "获取当前实体行已经生成条码的相关信息",
  "operationId": "BarcodeCreate_GetDocGenerateQty",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getBarCodeGenerateInfoDataList",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.Barcode.GetDocGenerateInfoData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Collections.Generic.List[UFIDA.U9.ISV.BC.RestSV.Model.Barcode.GetDocGenerateInfoReturnData]]]"
      }
    }
  }
}
```

## POST /webapi/BarcodeCreate/CreateBarCodeByAssignQty

```json
{
  "tags": [
    "BarcodeCreate"
  ],
  "summary": "指定数量创建条码",
  "operationId": "BarcodeCreate_CreateBarCodeByAssignQty",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "AssignQtyCreateBarCodeDataList",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.Barcode.AssignQtyCreateBarCodeData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Collections.Generic.List[System.String]]]"
      }
    }
  }
}
```

## POST /webapi/BarCodeOperatorDoc/Create

```json
{
  "tags": [
    "BarCodeOperatorDoc"
  ],
  "summary": "条码生单审核接口",
  "operationId": "BarCodeOperatorDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "integratedMiddleDTODatas",
      "in": "body",
      "description": "集成通用DTO",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.OperateDoc.BaseCommon.IntegratedMiddleDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/BaseBarCodeAnaylse/Create

```json
{
  "tags": [
    "BaseBarCodeAnaylse"
  ],
  "summary": "条码解析接口",
  "operationId": "BaseBarCodeAnaylse_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "baseBarCodeAnaylseData",
      "in": "body",
      "description": "待解析条码集合",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.BarCodeAnalys.BaseCommon.BaseBarCodeAnaylseData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/BaseInfo/Ents

```json
{
  "tags": [
    "BaseInfo"
  ],
  "summary": "获取企业列表",
  "operationId": "BaseInfo_Ents",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BaseInfo/Orgs

```json
{
  "tags": [
    "BaseInfo"
  ],
  "summary": "获取组织列表",
  "operationId": "BaseInfo_Orgs",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BaseInfo/EntsV2

```json
{
  "tags": [
    "BaseInfo"
  ],
  "operationId": "BaseInfo_EntsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  }
}
```

## POST /webapi/BaseInfo/OrgsV2

```json
{
  "tags": [
    "BaseInfo"
  ],
  "operationId": "BaseInfo_OrgsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  }
}
```

## POST /webapi/BaseInfo/LanguagesV2

```json
{
  "tags": [
    "BaseInfo"
  ],
  "summary": "获取指定企业下启用的语种信息",
  "operationId": "BaseInfo_LanguagesV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLanguageListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetLanguageListResp]]"
      }
    }
  }
}
```

## POST /webapi/BIP/OrgSave

```json
{
  "tags": [
    "BIP"
  ],
  "summary": "组织保存BIP",
  "operationId": "BIP_OrgSave",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.BIP.YYCOrgDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/BIP/DeptSave

```json
{
  "tags": [
    "BIP"
  ],
  "summary": "部门保存BIP",
  "operationId": "BIP_DeptSave",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.BIP.YYCDeptDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/BIP/CurrencySave

```json
{
  "tags": [
    "BIP"
  ],
  "summary": "币种保存BIP",
  "operationId": "BIP_CurrencySave",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.BIP.YYCCurrencyDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/BIP/CountrySave

```json
{
  "tags": [
    "BIP"
  ],
  "summary": "国家保存BIP",
  "operationId": "BIP_CountrySave",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.BIP.YYCCountryDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/BIP/BankCategorySave

```json
{
  "tags": [
    "BIP"
  ],
  "summary": "银行类别保存BIP",
  "operationId": "BIP_BankCategorySave",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.BIP.YYCBankCategoryDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/BIP/BankSave

```json
{
  "tags": [
    "BIP"
  ],
  "summary": "银行保存BIP",
  "operationId": "BIP_BankSave",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.BIP.YYCBankDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/BIService/TokenLogin

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "Token登录验证",
  "operationId": "BIService_TokenLogin",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BIService.LoginWithTokenReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.BIService.LoginWithTokenResp]"
      }
    }
  }
}
```

## GET /webapi/BIService/GetBusinessData

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "数据服务调用业务存储过程取数据的接口",
  "operationId": "BIService_GetBusinessData",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/System.Web.Http.Results.JsonResult[UFSoft.UBF.MVC.Model.DAS.GetBusinessDataResp]"
      }
    }
  }
}
```

## POST /webapi/BIService/GetLightAnalysisSqlByField

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "获取轻分析SQL",
  "operationId": "BIService_GetLightAnalysisSqlByField",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.DAS.LightAnalysisSqlReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[UFSoft.UBF.MVC.Model.DAS.LightAnalysisSqlResp]"
      }
    }
  }
}
```

## POST /webapi/BIService/Salt

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "获取登录加密的盐值",
  "operationId": "BIService_Salt",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltResp]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BIService/SaltV2

```json
{
  "tags": [
    "BIService"
  ],
  "operationId": "BIService_SaltV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[UFSoft.UBF.MVC.Model.BarCode.GetLoginSaltResp]"
      }
    }
  }
}
```

## POST /webapi/BIService/Login

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "登录验证",
  "operationId": "BIService_Login",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.ApiLoginReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.BarCode.ApiLoginResp]"
      }
    }
  }
}
```

## POST /webapi/BIService/BCToken

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "条码自动获取token",
  "operationId": "BIService_BCToken",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetTokenReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.BarCode.GetTokenResp]"
      }
    }
  }
}
```

## GET /webapi/BIService/Ping

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "",
  "operationId": "BIService_Ping",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.PingReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.PingResp"
      }
    }
  }
}
```

## POST /webapi/BIService/Ents

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "获取企业列表",
  "operationId": "BIService_Ents",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BIService/Orgs

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "获取组织列表",
  "operationId": "BIService_Orgs",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/BIService/EntsV2

```json
{
  "tags": [
    "BIService"
  ],
  "operationId": "BIService_EntsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  }
}
```

## POST /webapi/BIService/OrgsV2

```json
{
  "tags": [
    "BIService"
  ],
  "operationId": "BIService_OrgsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  }
}
```

## POST /webapi/BIService/LanguagesV2

```json
{
  "tags": [
    "BIService"
  ],
  "summary": "获取指定企业下启用的语种信息",
  "operationId": "BIService_LanguagesV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLanguageListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetLanguageListResp]]"
      }
    }
  }
}
```

## POST /webapi/BOM/Create

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "创建BOM",
  "operationId": "BOM_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "bomDatas",
      "in": "body",
      "description": "BOM集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.BOMMasterDTO4RS"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/BOM/Modify

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "修改BOM",
  "operationId": "BOM_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "bomDatas",
      "in": "body",
      "description": "BOM集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.BOMMasterDTO4RS"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/BOM/Delete

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "删除BOM",
  "operationId": "BOM_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "bomDatas",
      "in": "body",
      "description": "BOM集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DeleteBOMDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/BOM/Query

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "查询BOM",
  "operationId": "BOM_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "bomDatas",
      "in": "body",
      "description": "BOM集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DeleteBOMDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MFG.BOM.BOMMasterDTO4CreateSvData]]"
      }
    }
  }
}
```

## POST /webapi/BOM/BatchSubmit

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "批量提交BOM",
  "operationId": "BOM_BatchSubmit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "bomDatas",
      "in": "body",
      "description": "BOM集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.BatchOperateDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/BOM/BatchApprove

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "批量审核BOM",
  "operationId": "BOM_BatchApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "bomDatas",
      "in": "body",
      "description": "BOM集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.BatchOperateDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/BOM/BatchUnApprove

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "批量弃审BOM",
  "operationId": "BOM_BatchUnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "bomDatas",
      "in": "body",
      "description": "BOM集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.BatchOperateDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/BOM/BIPQueryPage

```json
{
  "tags": [
    "BOM"
  ],
  "summary": "bip查找BOM",
  "operationId": "BOM_BIPQueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonApiQueryParamDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/cc/Create

```json
{
  "tags": [
    "cc"
  ],
  "summary": "获取单据类型参照信息",
  "operationId": "cc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getDocTypeReference",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.CommonReference.GetDocTypeReferenceData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/CheckDiffBill/Create

```json
{
  "tags": [
    "CheckDiffBill"
  ],
  "summary": "创建盘点差异单",
  "operationId": "CheckDiffBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "checkDiffBillRData",
      "in": "body",
      "description": "盘点差异单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.CheckDiffBillRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CheckDiffBill/Submit

```json
{
  "tags": [
    "CheckDiffBill"
  ],
  "summary": "提交盘点差异单",
  "operationId": "CheckDiffBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "盘点差异单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CheckDiffBill/Approve

```json
{
  "tags": [
    "CheckDiffBill"
  ],
  "summary": "审核盘点差异单",
  "operationId": "CheckDiffBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "盘点差异单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CheckDiffBill/UnApprove

```json
{
  "tags": [
    "CheckDiffBill"
  ],
  "summary": "弃审盘点差异单",
  "operationId": "CheckDiffBill_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "盘点差异单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CheckDiffBill/Delete

```json
{
  "tags": [
    "CheckDiffBill"
  ],
  "summary": "删除盘点差异单",
  "operationId": "CheckDiffBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "盘点差异单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CMRcvPayBill/Create

```json
{
  "tags": [
    "CMRcvPayBill"
  ],
  "summary": "增加现金银行收付款单",
  "operationId": "CMRcvPayBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "cmRcvPayBillDatas",
      "in": "body",
      "description": "现金银行收付款集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.CM.CMRcvPayBillDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CMRcvPayBill/Delete

```json
{
  "tags": [
    "CMRcvPayBill"
  ],
  "summary": "删除现金银行收付款单",
  "operationId": "CMRcvPayBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "现金银行收付款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.CM.RcvPayBillQueryConditionDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CMRcvPayBill/Submit

```json
{
  "tags": [
    "CMRcvPayBill"
  ],
  "summary": "提交现金银行收付款单",
  "operationId": "CMRcvPayBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SubmitDatas",
      "in": "body",
      "description": "现金银行收付款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.CM.RcvPayBillQueryConditionDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CMRcvPayBill/Approve

```json
{
  "tags": [
    "CMRcvPayBill"
  ],
  "summary": "审核现金银行收付款单",
  "operationId": "CMRcvPayBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SubmitDatas",
      "in": "body",
      "description": "现金银行收付款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.CM.RcvPayBillQueryConditionDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CMRcvPayBill/CancelApprove

```json
{
  "tags": [
    "CMRcvPayBill"
  ],
  "summary": "弃审现金银行收付款单",
  "operationId": "CMRcvPayBill_CancelApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SubmitDatas",
      "in": "body",
      "description": "现金银行收付款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.CM.RcvPayBillQueryConditionDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CommonEntity/Query

```json
{
  "tags": [
    "CommonEntity"
  ],
  "summary": "公共查询接口",
  "operationId": "CommonEntity_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "parms",
      "in": "body",
      "description": "参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiComParms"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Object]"
      }
    }
  }
}
```

## POST /webapi/CommonEntity/QueryNew

```json
{
  "tags": [
    "CommonEntity"
  ],
  "operationId": "CommonEntity_QueryNew",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "parms",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiComParms"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Object]"
      }
    }
  }
}
```

## POST /webapi/CommonEntity/GetFormUrl

```json
{
  "tags": [
    "CommonEntity"
  ],
  "operationId": "CommonEntity_GetFormUrl",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "parms",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiUrlParms"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Object]"
      }
    }
  }
}
```

## POST /webapi/CompleteApplyDoc/Create

```json
{
  "tags": [
    "CompleteApplyDoc"
  ],
  "summary": "新增完工申报单",
  "operationId": "CompleteApplyDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "completeApplyDocDatas",
      "in": "body",
      "description": "完工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.NewComplete.CompleteDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteApplyDoc/Modify

```json
{
  "tags": [
    "CompleteApplyDoc"
  ],
  "summary": "修改完工申报单",
  "operationId": "CompleteApplyDoc_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "completeApplyDocDatas",
      "in": "body",
      "description": "完工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.NewComplete.CompleteApplyDocDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteApplyDoc/Delete

```json
{
  "tags": [
    "CompleteApplyDoc"
  ],
  "summary": "删除完工申报单",
  "operationId": "CompleteApplyDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "completeApplyDocDatas",
      "in": "body",
      "description": "完工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteApplyDoc/Query

```json
{
  "tags": [
    "CompleteApplyDoc"
  ],
  "summary": "查询完工申报单",
  "operationId": "CompleteApplyDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "completeApplyDocDatas",
      "in": "body",
      "description": "完工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MO.CompleteApplyDocDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteApplyDoc/Approve

```json
{
  "tags": [
    "CompleteApplyDoc"
  ],
  "summary": "审核完工申报单",
  "operationId": "CompleteApplyDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "completeApplyDocDatas",
      "in": "body",
      "description": "完工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteApplyDoc/UnApprove

```json
{
  "tags": [
    "CompleteApplyDoc"
  ],
  "summary": "弃审完工申报单",
  "operationId": "CompleteApplyDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "completeApplyDocDatas",
      "in": "body",
      "description": "弃审申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteDoc/Create

```json
{
  "tags": [
    "CompleteDoc"
  ],
  "summary": "新增完工报告",
  "operationId": "CompleteDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "CompRptDatas",
      "in": "body",
      "description": "完工报告集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.CompRptDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteDoc/Query

```json
{
  "tags": [
    "CompleteDoc"
  ],
  "summary": "查询完工报告单",
  "operationId": "CompleteDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "CompRptDatas",
      "in": "body",
      "description": "完工报告单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.CompleteRpt.CompRptKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MO.CompRptDataDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteDoc/Delete

```json
{
  "tags": [
    "CompleteDoc"
  ],
  "summary": "删除完工报告单",
  "operationId": "CompleteDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "CompRptDatas",
      "in": "body",
      "description": "完工报告单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.ResUsageRptKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteDoc/Approve

```json
{
  "tags": [
    "CompleteDoc"
  ],
  "summary": "审核完工报告单",
  "operationId": "CompleteDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "CompRptDatas",
      "in": "body",
      "description": "完工报告单集合",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.ApproveCompleteRData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CompleteDoc/Rcv

```json
{
  "tags": [
    "CompleteDoc"
  ],
  "summary": "完工报告单入库动作",
  "operationId": "CompleteDoc_Rcv",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "RcvCompleteRptDTORDatas",
      "in": "body",
      "description": "完工报告入库信息集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.CompleteRpt.RcvCompleteRptDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ConfirmReqFund/Approve

```json
{
  "tags": [
    "ConfirmReqFund"
  ],
  "summary": "审核请款单确认",
  "operationId": "ConfirmReqFund_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ConfirmReqFund/UnApprove

```json
{
  "tags": [
    "ConfirmReqFund"
  ],
  "summary": "弃审请款单确认",
  "operationId": "ConfirmReqFund_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Contact/Create

```json
{
  "tags": [
    "Contact"
  ],
  "summary": "创建联系对象",
  "operationId": "Contact_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "contactDatas",
      "in": "body",
      "description": "联系对象集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Contact.ContactDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Contact/Modify

```json
{
  "tags": [
    "Contact"
  ],
  "summary": "修改联系对象",
  "operationId": "Contact_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "contactDatas",
      "in": "body",
      "description": "联系对象集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Contact.ContactDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Contact/Delete

```json
{
  "tags": [
    "Contact"
  ],
  "summary": "删除联系对象",
  "operationId": "Contact_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "contactDatas",
      "in": "body",
      "description": "联系对象集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Contact.ContactDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ControlObjSend/ControlObjSend

```json
{
  "tags": [
    "ControlObjSend"
  ],
  "summary": "档案下发",
  "operationId": "ControlObjSend_ControlObjSend",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "cosDatas",
      "in": "body",
      "description": "档案集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ControlObjSendDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Country/QueryPage

```json
{
  "tags": [
    "Country"
  ],
  "summary": "查询国家",
  "operationId": "Country_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonApiQueryParamDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/Customer/Create

```json
{
  "tags": [
    "Customer"
  ],
  "summary": "创建客户",
  "operationId": "Customer_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "customerDatas",
      "in": "body",
      "description": "客户集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Customer.CustomerDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Customer/Modify

```json
{
  "tags": [
    "Customer"
  ],
  "summary": "修改客户",
  "operationId": "Customer_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "customerDatas",
      "in": "body",
      "description": "客户集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Customer.CustomerDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Customer/Delete

```json
{
  "tags": [
    "Customer"
  ],
  "summary": "删除客户",
  "operationId": "Customer_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "customerDatas",
      "in": "body",
      "description": "客户集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Customer.QueryCustomerDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Customer/Query

```json
{
  "tags": [
    "Customer"
  ],
  "summary": "查询客户",
  "operationId": "Customer_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "customerDatas",
      "in": "body",
      "description": "客户集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Customer.QueryCustomerDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Customer.CustomerDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Customer/Submit

```json
{
  "tags": [
    "Customer"
  ],
  "summary": "提交客户",
  "operationId": "Customer_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "customerDatas",
      "in": "body",
      "description": "客户集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Customer.QueryCustomerDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/CustomerItem/Create

```json
{
  "tags": [
    "CustomerItem"
  ],
  "summary": "创建料品客户交叉档案",
  "operationId": "CustomerItem_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "customerDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.CustomerItemData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/CustomerRelation/Create

```json
{
  "tags": [
    "CustomerRelation"
  ],
  "summary": "创建客户关系",
  "operationId": "CustomerRelation_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "customerRelationDTOs",
      "in": "body",
      "description": "客户关系集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.CustomerRelation.CustomerRelationDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/DAS/AddOrUpdateMenu

```json
{
  "tags": [
    "DAS"
  ],
  "summary": "实现数据服务发布菜单 \r\n新增或者更新，根据id判断",
  "operationId": "DAS_AddOrUpdateMenu",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.DAS.AddOrUpdateMenuReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.DAS.AddOrUpdateMenuResp]"
      }
    }
  }
}
```

## POST /webapi/DAS/DeleteMenu

```json
{
  "tags": [
    "DAS"
  ],
  "summary": "实现菜单删除接口",
  "operationId": "DAS_DeleteMenu",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.DAS.DeleteMenuReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFSoft.UBF.MVC.Model.DAS.DeleteMenuResp]"
      }
    }
  }
}
```

## POST /webapi/DAS/MenuList

```json
{
  "tags": [
    "DAS"
  ],
  "summary": "查询菜单列表",
  "operationId": "DAS_MenuList",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.DAS.MenuListReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.DAS.MenuListResp]]"
      }
    }
  }
}
```

## POST /webapi/DAS/Ents

```json
{
  "tags": [
    "DAS"
  ],
  "summary": "获取企业列表",
  "operationId": "DAS_Ents",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/DAS/Orgs

```json
{
  "tags": [
    "DAS"
  ],
  "summary": "获取组织列表",
  "operationId": "DAS_Orgs",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  },
  "deprecated": true
}
```

## POST /webapi/DAS/EntsV2

```json
{
  "tags": [
    "DAS"
  ],
  "operationId": "DAS_EntsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetEnterpriseListResp]]"
      }
    }
  }
}
```

## POST /webapi/DAS/OrgsV2

```json
{
  "tags": [
    "DAS"
  ],
  "operationId": "DAS_OrgsV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetOrgListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetOrgListResp]]"
      }
    }
  }
}
```

## POST /webapi/DAS/LanguagesV2

```json
{
  "tags": [
    "DAS"
  ],
  "summary": "获取指定企业下启用的语种信息",
  "operationId": "DAS_LanguagesV2",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.BarCode.GetLanguageListReq"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiEncryptResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.BarCode.GetLanguageListResp]]"
      }
    }
  }
}
```

## POST /webapi/DataGetSystem/Get

```json
{
  "tags": [
    "DataGetSystem"
  ],
  "operationId": "DataGetSystem_Get",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/DefineValue/QueryPage

```json
{
  "tags": [
    "DefineValue"
  ],
  "summary": "查询值集值",
  "operationId": "DefineValue_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DefineValue.QueryPageDefineValueDTOData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/DefineValue/CreateDefineValue

```json
{
  "tags": [
    "DefineValue"
  ],
  "summary": "新增值集值(不需要传入值集值ID)",
  "operationId": "DefineValue_CreateDefineValue",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DefineValue.CreateOrModifyDefineValueDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/DefineValue/BatchCreateDefineValue

```json
{
  "tags": [
    "DefineValue"
  ],
  "summary": "新增值集值(不需要传入值集值ID)。支持返回批量创建值集值的ID",
  "operationId": "DefineValue_BatchCreateDefineValue",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DefineValue.CreateOrModifyDefineValueDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/DefineValue/ModifyDefineValue

```json
{
  "tags": [
    "DefineValue"
  ],
  "summary": "修改值集值(必须传入值集值ID)",
  "operationId": "DefineValue_ModifyDefineValue",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DefineValue.CreateOrModifyDefineValueDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/DefineValue/BatchModifyDefineValue

```json
{
  "tags": [
    "DefineValue"
  ],
  "summary": "修改值集值(必须传入值集值ID)",
  "operationId": "DefineValue_BatchModifyDefineValue",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DefineValue.CreateOrModifyDefineValueDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Department/Create

```json
{
  "tags": [
    "Department"
  ],
  "summary": "增加部门",
  "operationId": "Department_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "deptDatas",
      "in": "body",
      "description": "部门集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.CopyOfDepartmentDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Department/Delete

```json
{
  "tags": [
    "Department"
  ],
  "summary": "删除部门",
  "operationId": "Department_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "deptDatas",
      "in": "body",
      "description": "部门集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DelDepartmentDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Department/Modify

```json
{
  "tags": [
    "Department"
  ],
  "summary": "修改部门",
  "operationId": "Department_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "deptDatas",
      "in": "body",
      "description": "部门集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.CopyOfDepartmentDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Department/Query

```json
{
  "tags": [
    "Department"
  ],
  "summary": "查询部门",
  "operationId": "Department_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "deptDatas",
      "in": "body",
      "description": "部门集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.QueryDepartmentDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.DeptOperatorSV.CopyOfDepartmentDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DimissionDoc/Create

```json
{
  "tags": [
    "DimissionDoc"
  ],
  "summary": "创建离职单",
  "operationId": "DimissionDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateDimissionDocReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateDimissionDocResp]"
      }
    }
  }
}
```

## POST /webapi/DimissionDoc/Submit

```json
{
  "tags": [
    "DimissionDoc"
  ],
  "summary": "提交离职单",
  "operationId": "DimissionDoc_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.SubmitDimissionDocResp]]"
      }
    }
  }
}
```

## POST /webapi/DimissionDoc/Approve

```json
{
  "tags": [
    "DimissionDoc"
  ],
  "summary": "审核离职单",
  "operationId": "DimissionDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveDimissionDocResp]]"
      }
    }
  }
}
```

## POST /webapi/DimissionDoc/Delete

```json
{
  "tags": [
    "DimissionDoc"
  ],
  "summary": "删除离职单",
  "operationId": "DimissionDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.DeleteDimissionDocResp]]"
      }
    }
  }
}
```

## POST /webapi/DispatchCompleteOrderDoc/Delete

```json
{
  "tags": [
    "DispatchCompleteOrderDoc"
  ],
  "summary": "删除派工申报单",
  "operationId": "DispatchCompleteOrderDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "派工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.DispatchCompleteOrderDoc.DispatchCompleteOrderDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchCompleteOrderDoc/Approve

```json
{
  "tags": [
    "DispatchCompleteOrderDoc"
  ],
  "summary": "审核派工申报单",
  "operationId": "DispatchCompleteOrderDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "派工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.DispatchCompleteOrderDoc.DispatchCompleteOrderDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchCompleteOrderDoc/UnApprove

```json
{
  "tags": [
    "DispatchCompleteOrderDoc"
  ],
  "summary": "弃审派工申报单",
  "operationId": "DispatchCompleteOrderDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "派工申报单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.DispatchCompleteOrderDoc.DispatchCompleteOrderDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchCompleteOrderDoc/Create

```json
{
  "tags": [
    "DispatchCompleteOrderDoc"
  ],
  "summary": "创建派工申报单",
  "operationId": "DispatchCompleteOrderDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.DispatchCompleteOrderDoc.AddDispatchCompleteOrderDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/Create

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "summary": "新增派工单",
  "operationId": "DispatchOrderDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "description": "派工单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/Query

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "summary": "查询派工单",
  "operationId": "DispatchOrderDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "description": "派工单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGConditionRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MO.PGDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/Delete

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "summary": "删除派工单",
  "operationId": "DispatchOrderDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "description": "派工单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGConditionRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/Approve

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "summary": "审核派工单",
  "operationId": "DispatchOrderDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "description": "派工单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGConditionRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/UnApprove

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "summary": "弃审派工单",
  "operationId": "DispatchOrderDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "description": "派工单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGConditionRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/Open

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "operationId": "DispatchOrderDoc_Open",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGOperateRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/Close

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "operationId": "DispatchOrderDoc_Close",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGOperateRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DispatchOrderDoc/Back

```json
{
  "tags": [
    "DispatchOrderDoc"
  ],
  "operationId": "DispatchOrderDoc_Back",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DispatchDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGOperateRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/DoPrint/SetPrintDatas

```json
{
  "tags": [
    "DoPrint"
  ],
  "summary": "打印接口",
  "operationId": "DoPrint_SetPrintDatas",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "doPrintDatas",
      "in": "body",
      "description": "打印参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.DoPrintDatas"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/ECNDoc/Create

```json
{
  "tags": [
    "ECNDoc"
  ],
  "summary": "新增工程变更单",
  "operationId": "ECNDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ecnDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.ECN.ECNDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ECNDoc/Modify

```json
{
  "tags": [
    "ECNDoc"
  ],
  "summary": "修改工程变更单",
  "operationId": "ECNDoc_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ecnDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.ECN.ECNDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ECNDoc/Delete

```json
{
  "tags": [
    "ECNDoc"
  ],
  "summary": "删除 工程变更单",
  "operationId": "ECNDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ecnDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.ECN.DeleteECNDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ECNDoc/Submit

```json
{
  "tags": [
    "ECNDoc"
  ],
  "summary": "提交/收回 工程变更单",
  "operationId": "ECNDoc_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ecnDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.ECN.ApproveECNDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ECNDoc/Approve

```json
{
  "tags": [
    "ECNDoc"
  ],
  "summary": "审核/弃审 工程变更单",
  "operationId": "ECNDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ecnDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.ECN.ApproveECNDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ECNDoc/PublishECNDoc

```json
{
  "tags": [
    "ECNDoc"
  ],
  "summary": "发布工程变更单",
  "operationId": "ECNDoc_PublishECNDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ecnDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.ECN.PublishECNDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ECNDoc/PublishCancel

```json
{
  "tags": [
    "ECNDoc"
  ],
  "summary": "取消发布工程变更单",
  "operationId": "ECNDoc_PublishCancel",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ecnDocDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.ECN.PublishECNDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/EmploymentDoc/Submit

```json
{
  "tags": [
    "EmploymentDoc"
  ],
  "summary": "提交入职单",
  "operationId": "EmploymentDoc_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveEmploymentDocResp]]"
      }
    }
  }
}
```

## POST /webapi/EmploymentDoc/Approve

```json
{
  "tags": [
    "EmploymentDoc"
  ],
  "summary": "审核入职单",
  "operationId": "EmploymentDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveEmploymentDocResp]]"
      }
    }
  }
}
```

## POST /webapi/EmploymentDoc/UnApprove

```json
{
  "tags": [
    "EmploymentDoc"
  ],
  "summary": "弃审入职单",
  "operationId": "EmploymentDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveEmploymentDocResp]]"
      }
    }
  }
}
```

## POST /webapi/ERBill/DeleteER

```json
{
  "tags": [
    "ERBill"
  ],
  "summary": "删除借款还款报销单",
  "operationId": "ERBill_DeleteER",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.ER.ImportERBillQueryConditionDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ExtEnumValue/QueryPage

```json
{
  "tags": [
    "ExtEnumValue"
  ],
  "summary": "查询枚举值",
  "operationId": "ExtEnumValue_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ExtEnumValue.QueryPageExtEnumValueDTOData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## GET /webapi/GeneratePrintFile/DownloadPrintPDF

```json
{
  "tags": [
    "GeneratePrintFile"
  ],
  "summary": "下载模板生成的pdf文件",
  "operationId": "GeneratePrintFile_DownloadPrintPDF",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req.printTemplateID",
      "in": "query",
      "required": true,
      "type": "string"
    },
    {
      "name": "req.docNo",
      "in": "query",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.docID",
      "in": "query",
      "required": false,
      "type": "integer",
      "format": "int64"
    },
    {
      "name": "req.printData",
      "in": "query",
      "required": false,
      "type": "object"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/GetAppDynamicConfig/Create

```json
{
  "tags": [
    "GetAppDynamicConfig"
  ],
  "summary": "获取应用动态设计配置接口",
  "operationId": "GetAppDynamicConfig_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getAppDynamicConfigData",
      "in": "body",
      "description": "获取配置信息",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.GetAppDynamicConfig.GetAppDynamicConfigData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/GetCommonReference/Create

```json
{
  "tags": [
    "GetCommonReference"
  ],
  "summary": "获取公共参照信息",
  "operationId": "GetCommonReference_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getBaseReference",
      "in": "body",
      "description": "获取信息",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.CommonReference.GetCommonReferenceData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/GetDocReference/Create

```json
{
  "tags": [
    "GetDocReference"
  ],
  "summary": "获取单据参照信息",
  "operationId": "GetDocReference_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getDocReference",
      "in": "body",
      "description": "获取信息",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.GetDocReference.GetDocReferenceData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/GetParamSetting/GetParam

```json
{
  "tags": [
    "GetParamSetting"
  ],
  "summary": "获取条码平台参数",
  "operationId": "GetParamSetting_GetParam",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramDatas",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.Common.ParamDatas"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/GetPrinters/GetOnlineServices

```json
{
  "tags": [
    "GetPrinters"
  ],
  "summary": "获取打印模板列表接口",
  "operationId": "GetPrinters_GetOnlineServices",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getOnlineServicesData",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.GetOnlineServicesData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.ResponseInfo]"
      }
    }
  }
}
```
## POST /webapi/GetUsedLabel/GetLabel

```json
{
  "tags": [
    "GetUsedLabel"
  ],
  "summary": "获取打印模板接口",
  "operationId": "GetUsedLabel_GetLabel",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getUsedLabelData",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.GetUsedLabelData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/GetUserLabelsList/GetLabels

```json
{
  "tags": [
    "GetUserLabelsList"
  ],
  "summary": "获取打印模板列表接口",
  "operationId": "GetUserLabelsList_GetLabels",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getUserLabelsData",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.GetUserLabelsData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.ResponseInfo]"
      }
    }
  }
}
```
## POST /webapi/GetValueSetDef/Create

```json
{
  "tags": [
    "GetValueSetDef"
  ],
  "summary": "获取值集值",
  "operationId": "GetValueSetDef_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "getValueSetDefDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.CommonReference.GetValueSetDefDatas"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/Idoc/GetDocListTask

```json
{
  "tags": [
    "Idoc"
  ],
  "operationId": "Idoc_GetDocListTask",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/Idoc/GetBookListTask

```json
{
  "tags": [
    "Idoc"
  ],
  "operationId": "Idoc_GetBookListTask",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/Idoc/IdocVerify

```json
{
  "tags": [
    "Idoc"
  ],
  "operationId": "Idoc_IdocVerify",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/Idoc/UploadFile

```json
{
  "tags": [
    "Idoc"
  ],
  "operationId": "Idoc_UploadFile",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/Idoc/GetSrcDoc

```json
{
  "tags": [
    "Idoc"
  ],
  "operationId": "Idoc_GetSrcDoc",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/Idoc/CheckU9DataSource

```json
{
  "tags": [
    "Idoc"
  ],
  "operationId": "Idoc_CheckU9DataSource",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "type": "object"
      }
    }
  }
}
```

## POST /webapi/InnerBalance/Submit

```json
{
  "tags": [
    "InnerBalance"
  ],
  "summary": "提交内部结算清单",
  "operationId": "InnerBalance_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InnerBalance/Approve

```json
{
  "tags": [
    "InnerBalance"
  ],
  "summary": "审核内部结算清单",
  "operationId": "InnerBalance_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InnerBalance/UnApprove

```json
{
  "tags": [
    "InnerBalance"
  ],
  "summary": "弃审内部结算清单",
  "operationId": "InnerBalance_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InsideTransferDoc/Create

```json
{
  "tags": [
    "InsideTransferDoc"
  ],
  "summary": "创建内部调动单",
  "operationId": "InsideTransferDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateInsideTransferDocReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateInsideTransferDocResp]"
      }
    }
  }
}
```

## POST /webapi/InsideTransferDoc/Submit

```json
{
  "tags": [
    "InsideTransferDoc"
  ],
  "summary": "提交内部调动单",
  "operationId": "InsideTransferDoc_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveInsideTransDocResp]]"
      }
    }
  }
}
```

## POST /webapi/InsideTransferDoc/Approve

```json
{
  "tags": [
    "InsideTransferDoc"
  ],
  "summary": "审核内部调动单",
  "operationId": "InsideTransferDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveInsideTransDocResp]]"
      }
    }
  }
}
```

## POST /webapi/InsideTransferDoc/Delete

```json
{
  "tags": [
    "InsideTransferDoc"
  ],
  "summary": "删除内部调动单",
  "operationId": "InsideTransferDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveInsideTransDocResp]]"
      }
    }
  }
}
```

## POST /webapi/InstructionRobot/Excute

```json
{
  "tags": [
    "InstructionRobot"
  ],
  "operationId": "InstructionRobot_Excute",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.FR.ExcuteInstructionRobotDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/InterOrgTransferDoc/Create

```json
{
  "tags": [
    "InterOrgTransferDoc"
  ],
  "summary": "创建跨组织调动单",
  "operationId": "InterOrgTransferDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateInterOrgTransferDocReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateInterOrgTransferDocResp]"
      }
    }
  }
}
```

## POST /webapi/InterOrgTransferDoc/Submit

```json
{
  "tags": [
    "InterOrgTransferDoc"
  ],
  "summary": "提交跨组织调动单",
  "operationId": "InterOrgTransferDoc_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveInterOrgTransferDocResp]]"
      }
    }
  }
}
```

## POST /webapi/InterOrgTransferDoc/Approve

```json
{
  "tags": [
    "InterOrgTransferDoc"
  ],
  "summary": "审核跨组织调动单",
  "operationId": "InterOrgTransferDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveInterOrgTransferDocResp]]"
      }
    }
  }
}
```

## POST /webapi/InterOrgTransferDoc/Delete

```json
{
  "tags": [
    "InterOrgTransferDoc"
  ],
  "summary": "删除跨组织调动单",
  "operationId": "InterOrgTransferDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveInterOrgTransferDocResp]]"
      }
    }
  }
}
```

## POST /webapi/InventorySheet/Create

```json
{
  "tags": [
    "InventorySheet"
  ],
  "summary": "创建日常盘点单",
  "operationId": "InventorySheet_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "日常盘点单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.InventorySheetRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InventorySheet/Submit

```json
{
  "tags": [
    "InventorySheet"
  ],
  "summary": "提交日常盘点单",
  "operationId": "InventorySheet_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InventorySheet/Checking

```json
{
  "tags": [
    "InventorySheet"
  ],
  "summary": "盘点日常盘点单",
  "operationId": "InventorySheet_Checking",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InventorySheet/Approve

```json
{
  "tags": [
    "InventorySheet"
  ],
  "summary": "审核日常盘点单",
  "operationId": "InventorySheet_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InventorySheet/UnApprove

```json
{
  "tags": [
    "InventorySheet"
  ],
  "summary": "弃审日常盘点单",
  "operationId": "InventorySheet_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/InventorySheet/Delete

```json
{
  "tags": [
    "InventorySheet"
  ],
  "summary": "删除日常盘点单",
  "operationId": "InventorySheet_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Invtrans/QueryQohAndAvailable

```json
{
  "tags": [
    "Invtrans"
  ],
  "summary": "查询可用量/库存量",
  "operationId": "Invtrans_QueryQohAndAvailable",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.InvTrans.INVBinLotShipmentDistributeDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.InvTrans.WhQoh.INVBinLotShipmentDistributeDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Invtrans/EasyQueryQoh

```json
{
  "tags": [
    "Invtrans"
  ],
  "summary": "查询库存可用量（YYC集成用）",
  "operationId": "Invtrans_EasyQueryQoh",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.InvTrans.EasyQueryQohDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.INV.RestSV.Common.CommonDTO.ResultForYYCData"
      }
    }
  }
}
```

## POST /webapi/IssueApplyDoc/Approve

```json
{
  "tags": [
    "IssueApplyDoc"
  ],
  "summary": "审核领料申请单",
  "operationId": "IssueApplyDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.NewIssue.ApproveApplyDocDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueApplyDoc/Create

```json
{
  "tags": [
    "IssueApplyDoc"
  ],
  "summary": "创建领料申请单",
  "operationId": "IssueApplyDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.NewIssue.IssueApplyDocDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/Create

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "新增生产领料单",
  "operationId": "IssueDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.IssueDoc.IssueDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/Modify

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "修改生产领料单",
  "operationId": "IssueDoc_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.IssueDoc.IssueModifyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/Delete

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "删除生产领料单",
  "operationId": "IssueDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.PGConditionRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/Query

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "查询生产领料单",
  "operationId": "IssueDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.IssueDoc.IssueKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MO.IssueDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/Approve

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "审核生产领料单",
  "operationId": "IssueDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.IssueDoc.ApproveIssueDoc4ExternalDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/Confirm

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "生产领料单发料确认",
  "operationId": "IssueDoc_Confirm",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.IssueDoc.ApproveIssueDoc4ExternalDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/CreateRecedeIssueDoc

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "新增生产退料单",
  "operationId": "IssueDoc_CreateRecedeIssueDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产退料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.IssueDoc.RecedeItemAndSnDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/IssueDoc/CreateRecedeIssueDocNew

```json
{
  "tags": [
    "IssueDoc"
  ],
  "summary": "新增生产退料单,\r\n有单行",
  "operationId": "IssueDoc_CreateRecedeIssueDocNew",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "生产退料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.IssueDoc.RecedeItemAndSnHeadDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemCategory/Create

```json
{
  "tags": [
    "ItemCategory"
  ],
  "summary": "创建料品分类",
  "operationId": "ItemCategory_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品分类集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemCategoryDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemCategory/Modify

```json
{
  "tags": [
    "ItemCategory"
  ],
  "summary": "料品分类修改",
  "operationId": "ItemCategory_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemCategoryDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemConvertRatioInClass/Create

```json
{
  "tags": [
    "ItemConvertRatioInClass"
  ],
  "summary": "创建料品计量单位组内转换率",
  "operationId": "ItemConvertRatioInClass_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemConvertRatioInClassDtoRDatas",
      "in": "body",
      "description": "料品计量单位组内转换率集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemConvertRatioInClass.ItemConvertRatioInClassDtoRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemConvertRatioInClass/Modify

```json
{
  "tags": [
    "ItemConvertRatioInClass"
  ],
  "summary": "修改料品计量单位组内转换率",
  "operationId": "ItemConvertRatioInClass_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemConvertRatioInClassDtoRDatas",
      "in": "body",
      "description": "料品计量单位组内转换率集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemConvertRatioInClass.ItemConvertRatioInClassDtoRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemConvertRatioInClass/Delete

```json
{
  "tags": [
    "ItemConvertRatioInClass"
  ],
  "summary": "删除料品计量单位组内转换率",
  "operationId": "ItemConvertRatioInClass_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemConvertRatioInClassDtoRDatas",
      "in": "body",
      "description": "料品计量单位组内转换率集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemConvertRatioInClass.ItemConvertRatioInClassDtoRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemConvertRatioOverClass/Create

```json
{
  "tags": [
    "ItemConvertRatioOverClass"
  ],
  "summary": "创建料品计量单位组间转换率",
  "operationId": "ItemConvertRatioOverClass_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemConvertRatioOverClasses",
      "in": "body",
      "description": "料品计量单位组间转换率集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemConvertRatioOverClass.ItemConvertRatioOverClassDtoRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemConvertRatioOverClass/Modify

```json
{
  "tags": [
    "ItemConvertRatioOverClass"
  ],
  "summary": "修改料品计量单位组间转换率",
  "operationId": "ItemConvertRatioOverClass_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemConvertRatioOverClasses",
      "in": "body",
      "description": "料品计量单位组间转换率集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemConvertRatioOverClass.ItemConvertRatioOverClassDtoRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemConvertRatioOverClass/Delete

```json
{
  "tags": [
    "ItemConvertRatioOverClass"
  ],
  "summary": "删除料品计量单位组间转换率",
  "operationId": "ItemConvertRatioOverClass_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemConvertRatioOverClasses",
      "in": "body",
      "description": "料品计量单位组间转换率集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemConvertRatioOverClass.ItemConvertRatioOverClassDtoRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMaster/Create

```json
{
  "tags": [
    "ItemMaster"
  ],
  "summary": "按DTO创建料品",
  "operationId": "ItemMaster_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemMasterDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMaster/CreateByAutoCode

```json
{
  "tags": [
    "ItemMaster"
  ],
  "summary": "创建单个料品",
  "operationId": "ItemMaster_CreateByAutoCode",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemMasterDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMaster/CreateByAttributes

```json
{
  "tags": [
    "ItemMaster"
  ],
  "summary": "按实体属性创建料品",
  "operationId": "ItemMaster_CreateByAttributes",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemMasterModifyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMaster/Delete

```json
{
  "tags": [
    "ItemMaster"
  ],
  "summary": "删除料品",
  "operationId": "ItemMaster_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.DeleteItemMasterDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMaster/Modify

```json
{
  "tags": [
    "ItemMaster"
  ],
  "summary": "修改料品",
  "operationId": "ItemMaster_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemMasterModifyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMaster/Query

```json
{
  "tags": [
    "ItemMaster"
  ],
  "summary": "查询料品",
  "operationId": "ItemMaster_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.QueryItemDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.Item.ItemMasterDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMasterFree/Create

```json
{
  "tags": [
    "ItemMasterFree"
  ],
  "summary": "按DTO创建 料品自由项",
  "operationId": "ItemMasterFree_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDataFrees",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemMasterFreeDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemMasterVersion/Create

```json
{
  "tags": [
    "ItemMasterVersion"
  ],
  "summary": "按DTO创建料品版本",
  "operationId": "ItemMasterVersion_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品版本集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ItemMaster.ItemMasterVersionDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ItemRequest/Create

```json
{
  "tags": [
    "ItemRequest"
  ],
  "summary": "创建料品需求",
  "operationId": "ItemRequest_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "itemDatas",
      "in": "body",
      "description": "料品集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.ItemRequest.ItemRequestDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemRequest/Submit

```json
{
  "tags": [
    "ItemRequest"
  ],
  "summary": "提交料品需求清单",
  "operationId": "ItemRequest_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.ItemRequest.ItemRequestApproveDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemRequest/Approve

```json
{
  "tags": [
    "ItemRequest"
  ],
  "summary": "审核料品需求清单",
  "operationId": "ItemRequest_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.ItemRequest.ItemRequestApproveDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemRequest/UnApprove

```json
{
  "tags": [
    "ItemRequest"
  ],
  "summary": "弃审料品需求清单",
  "operationId": "ItemRequest_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.ItemRequest.ItemRequestApproveDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ItemRequest/Delete

```json
{
  "tags": [
    "ItemRequest"
  ],
  "summary": "弃审料品需求清单",
  "operationId": "ItemRequest_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.ItemRequest.ItemRequestApproveDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Job/CreateJobType

```json
{
  "tags": [
    "Job"
  ],
  "summary": "创建职务分类",
  "operationId": "Job_CreateJobType",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateJobTypeReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateJobTypeResp]"
      }
    }
  }
}
```

## POST /webapi/Job/SaveJobTypeForBIP

```json
{
  "tags": [
    "Job"
  ],
  "summary": "人力云保存职务分类",
  "operationId": "Job_SaveJobTypeForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.YYCDTO[UFIDA.U9.HI.HIBP.Api.Dto.CreateJobTypeReq]"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.CBO.PubSV.ControllerSV.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/Job/CreateJob

```json
{
  "tags": [
    "Job"
  ],
  "summary": "创建职务",
  "operationId": "Job_CreateJob",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateJobReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateJobResp]"
      }
    }
  }
}
```

## POST /webapi/Job/SaveJobForBIP

```json
{
  "tags": [
    "Job"
  ],
  "summary": "人力云保存职务",
  "operationId": "Job_SaveJobForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.YYCDTO[UFIDA.U9.HI.HIBP.Api.Dto.CreateJobReq]"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.CBO.PubSV.ControllerSV.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/LanguageConfig/Create

```json
{
  "tags": [
    "LanguageConfig"
  ],
  "summary": "获取多语配置接口",
  "operationId": "LanguageConfig_Create",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/LanguageGetConfig/Get

```json
{
  "tags": [
    "LanguageGetConfig"
  ],
  "summary": "获取多语配置接口",
  "operationId": "LanguageGetConfig_Get",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "language",
      "in": "body",
      "description": "语言编码",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/LendBackTrans/Create

```json
{
  "tags": [
    "LendBackTrans"
  ],
  "summary": "新增还入单服务",
  "operationId": "LendBackTrans_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "还入单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.INV.RestSV.Model.INV.LendBackTransRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendBackTrans/Submit

```json
{
  "tags": [
    "LendBackTrans"
  ],
  "summary": "提交还入单服务",
  "operationId": "LendBackTrans_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "还入单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendBackTrans/Approve

```json
{
  "tags": [
    "LendBackTrans"
  ],
  "summary": "审核还入单服务",
  "operationId": "LendBackTrans_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "还入单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendBackTrans/UnApprove

```json
{
  "tags": [
    "LendBackTrans"
  ],
  "summary": "弃审还入单服务",
  "operationId": "LendBackTrans_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "还入单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendBackTrans/Delete

```json
{
  "tags": [
    "LendBackTrans"
  ],
  "summary": "删除还入单服务",
  "operationId": "LendBackTrans_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "还入单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendTrans/Create

```json
{
  "tags": [
    "LendTrans"
  ],
  "summary": "新增借出单服务",
  "operationId": "LendTrans_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "借出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.INV.RestSV.Model.INV.LendTransRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendTrans/Submit

```json
{
  "tags": [
    "LendTrans"
  ],
  "summary": "提交借出单服务",
  "operationId": "LendTrans_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "借出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendTrans/Approve

```json
{
  "tags": [
    "LendTrans"
  ],
  "summary": "审核借出单服务",
  "operationId": "LendTrans_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "借出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendTrans/UnApprove

```json
{
  "tags": [
    "LendTrans"
  ],
  "summary": "弃审借出单服务",
  "operationId": "LendTrans_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "借出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LendTrans/Delete

```json
{
  "tags": [
    "LendTrans"
  ],
  "summary": "删除借出单服务",
  "operationId": "LendTrans_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "借出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LicenseInfo/GetLicenseInfoToBI

```json
{
  "tags": [
    "LicenseInfo"
  ],
  "summary": "获取数据服务许可数量接口",
  "operationId": "LicenseInfo_GetLicenseInfoToBI",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "传入参数信息",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Model.License.LicenseInfoDTORData"
      }
    },
    {
      "name": "auth",
      "in": "query",
      "description": "授权参数",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFSoft.UBF.MVC.Model.License.LicenseInfoResult]]"
      }
    }
  }
}
```

## POST /webapi/LoadBill/Create

```json
{
  "tags": [
    "LoadBill"
  ],
  "summary": "创建借款单",
  "operationId": "LoadBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.ER.LoanBillDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoadBill/Submit

```json
{
  "tags": [
    "LoadBill"
  ],
  "summary": "提交借款单",
  "operationId": "LoadBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoadBill/Approve

```json
{
  "tags": [
    "LoadBill"
  ],
  "summary": "审核借款单",
  "operationId": "LoadBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoadBill/UnApprove

```json
{
  "tags": [
    "LoadBill"
  ],
  "summary": "弃审借款单",
  "operationId": "LoadBill_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoadBill/Delete

```json
{
  "tags": [
    "LoadBill"
  ],
  "summary": "删除借款单",
  "operationId": "LoadBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "借款单删除集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoanPaying/Create

```json
{
  "tags": [
    "LoanPaying"
  ],
  "summary": "创建还款单",
  "operationId": "LoanPaying_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.ER.LoanPayingDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoanPaying/Delete

```json
{
  "tags": [
    "LoanPaying"
  ],
  "summary": "删除还款单",
  "operationId": "LoanPaying_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "还款单删除集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoanPaying/Submit

```json
{
  "tags": [
    "LoanPaying"
  ],
  "summary": "提交还款单",
  "operationId": "LoanPaying_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "还款单提交集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoanPaying/Approve

```json
{
  "tags": [
    "LoanPaying"
  ],
  "summary": "审核还款单",
  "operationId": "LoanPaying_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "还款单审核集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/LoanPaying/UnApprove

```json
{
  "tags": [
    "LoanPaying"
  ],
  "summary": "弃审还款单",
  "operationId": "LoanPaying_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "还款单弃审集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Location/Create

```json
{
  "tags": [
    "Location"
  ],
  "summary": "创建地址",
  "operationId": "Location_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.LocationDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Location/Modify

```json
{
  "tags": [
    "Location"
  ],
  "summary": "修改地址",
  "operationId": "Location_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.LocationDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Location/Delete

```json
{
  "tags": [
    "Location"
  ],
  "summary": "删除地址",
  "operationId": "Location_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.DeleteLocationDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Location/QueryPage

```json
{
  "tags": [
    "Location"
  ],
  "summary": "查询地址",
  "operationId": "Location_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.QueryLocationDTOData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/LotMaster/Create

```json
{
  "tags": [
    "LotMaster"
  ],
  "summary": "创建批号",
  "operationId": "LotMaster_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ltoDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.LotMaster.CreateLotMasterRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/LotMaster/Delete

```json
{
  "tags": [
    "LotMaster"
  ],
  "summary": "删除批号",
  "operationId": "LotMaster_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ltoDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.LotMaster.DeleteLotMasterRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MaterialDeliveryDoc/Create

```json
{
  "tags": [
    "MaterialDeliveryDoc"
  ],
  "summary": "新增材料出库单",
  "operationId": "MaterialDeliveryDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "materialDeliveryDocDatas",
      "in": "body",
      "description": "材料出库单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.NewIssue.MaterialDeliveryDocDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MaterialDeliveryDoc/Approve

```json
{
  "tags": [
    "MaterialDeliveryDoc"
  ],
  "summary": "审核和弃审材料出库单",
  "operationId": "MaterialDeliveryDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "newIssueDocKeyDTODatas",
      "in": "body",
      "description": "审核材料出库单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.NewIssue.NewIssueDocKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MaterialDeliveryDoc/Delete

```json
{
  "tags": [
    "MaterialDeliveryDoc"
  ],
  "summary": "删除材料出库单",
  "operationId": "MaterialDeliveryDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "newIssueDocKeyDTODatas",
      "in": "body",
      "description": "生产领料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.NewIssue.NewIssueDocKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MESAPIMOWorkHour/Create

```json
{
  "tags": [
    "MESAPIMOWorkHour"
  ],
  "summary": "新增工时数据（新）",
  "operationId": "MESAPIMOWorkHour_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "workHourDatas",
      "in": "body",
      "description": "工时集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MOWorkHour.MESMOWorkHourDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MESAPIMOWorkHour/Delete

```json
{
  "tags": [
    "MESAPIMOWorkHour"
  ],
  "summary": "删除工时数据",
  "operationId": "MESAPIMOWorkHour_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "otherIds",
      "in": "body",
      "description": "工时集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MESAPIWorkingHoursDataDI/Create

```json
{
  "tags": [
    "MESAPIWorkingHoursDataDI"
  ],
  "summary": "新增工时数据接口数据(新)",
  "operationId": "MESAPIWorkingHoursDataDI_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "workingHoursDatas",
      "in": "body",
      "description": "工时数据集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MDCI.MESWorkingHoursDataDIData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MESAPIWorkingHoursDataDI/Delete

```json
{
  "tags": [
    "MESAPIWorkingHoursDataDI"
  ],
  "summary": "删除工时数据",
  "operationId": "MESAPIWorkingHoursDataDI_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "otherIds",
      "in": "body",
      "description": "工时集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscRcvTrans/Create

```json
{
  "tags": [
    "MiscRcvTrans"
  ],
  "summary": "新增杂收单服务",
  "operationId": "MiscRcvTrans_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂收单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.MiscRcvRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscRcvTrans/Submit

```json
{
  "tags": [
    "MiscRcvTrans"
  ],
  "summary": "提交杂收单服务",
  "operationId": "MiscRcvTrans_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂收单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscRcvTrans/Approve

```json
{
  "tags": [
    "MiscRcvTrans"
  ],
  "summary": "审核杂收单服务",
  "operationId": "MiscRcvTrans_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂收单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscRcvTrans/UnApprove

```json
{
  "tags": [
    "MiscRcvTrans"
  ],
  "summary": "弃审杂收单服务",
  "operationId": "MiscRcvTrans_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂收单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscRcvTrans/Delete

```json
{
  "tags": [
    "MiscRcvTrans"
  ],
  "summary": "删除杂收单服务",
  "operationId": "MiscRcvTrans_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂收单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscShip/Create

```json
{
  "tags": [
    "MiscShip"
  ],
  "summary": "新增杂发单服务",
  "operationId": "MiscShip_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂发单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.MiscShipRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscShip/Submit

```json
{
  "tags": [
    "MiscShip"
  ],
  "summary": "提交杂发单服务",
  "operationId": "MiscShip_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂发单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscShip/Approve

```json
{
  "tags": [
    "MiscShip"
  ],
  "summary": "审核杂发单服务",
  "operationId": "MiscShip_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂发单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscShip/UnApprove

```json
{
  "tags": [
    "MiscShip"
  ],
  "summary": "弃审杂发单服务",
  "operationId": "MiscShip_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂发单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MiscShip/Delete

```json
{
  "tags": [
    "MiscShip"
  ],
  "summary": "删除杂发单服务",
  "operationId": "MiscShip_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "杂发单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MobileApproval/SubmitApproval

```json
{
  "tags": [
    "MobileApproval"
  ],
  "summary": "移动审批openAPI接口",
  "operationId": "MobileApproval_SubmitApproval",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "审批单据列表",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Platform.MobileApprovalDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/Create

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "新增生产订单",
  "operationId": "MODoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "生产订单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MODTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/Query

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "查询生产订单",
  "operationId": "MODoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "生产订单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MOKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MO.MODTOData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/ApproveMo

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "审核或弃审MO",
  "operationId": "MODoc_ApproveMo",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "审核/弃审生产订单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MOParamDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/CancelMo

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "作废生产订单",
  "operationId": "MODoc_CancelMo",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "作废生产订单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MOParamDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/CompleteMo

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "打开或关闭MO",
  "operationId": "MODoc_CompleteMo",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "打开或关闭生产订单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MOParamDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/DeleteMO

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "删除生产订单",
  "operationId": "MODoc_DeleteMO",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "删除生产订单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MOParamDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/StartMo

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "开工或反开MO",
  "operationId": "MODoc_StartMo",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "开工或反开工生产订单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MOParamDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MODoc/ApproveMOModify

```json
{
  "tags": [
    "MODoc"
  ],
  "summary": "审核生产订单变更单",
  "operationId": "MODoc_ApproveMOModify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "moDocDatas",
      "in": "body",
      "description": "审核生产订单变更单",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MODoc.MOModifyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/MOWorkHour/Create

```json
{
  "tags": [
    "MOWorkHour"
  ],
  "summary": "新增工时数据",
  "operationId": "MOWorkHour_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "workHourDatas",
      "in": "body",
      "description": "工时集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MOWorkHour.MOWorkHourDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/MOWorkHour/Delete

```json
{
  "tags": [
    "MOWorkHour"
  ],
  "summary": "删除工时数据",
  "operationId": "MOWorkHour_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "workHourDatas",
      "in": "body",
      "description": "工时集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.MOWorkHour.MOWorkHourDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## GET /webapi/OAuth2/GetSalt

```json
{
  "tags": [
    "OAuth2"
  ],
  "summary": "根据userCode获取盐值",
  "operationId": "OAuth2_GetSalt",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "userCode",
      "in": "query",
      "description": "用户名",
      "required": true,
      "type": "string"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## GET /webapi/OAuth2/GetAuthorizeCode

```json
{
  "tags": [
    "OAuth2"
  ],
  "summary": "获取授权码",
  "operationId": "OAuth2_GetAuthorizeCode",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "clientid",
      "in": "query",
      "description": "clientid",
      "required": true,
      "type": "string"
    },
    {
      "name": "clientsecret",
      "in": "query",
      "description": "clientsecret",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## GET /webapi/OAuth2/Login

```json
{
  "tags": [
    "OAuth2"
  ],
  "summary": "登录获取token",
  "operationId": "OAuth2_Login",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "entCode",
      "in": "query",
      "description": "企业编码",
      "required": true,
      "type": "string"
    },
    {
      "name": "userCode",
      "in": "query",
      "description": "用户名(域登录传递域账号，不带域名)",
      "required": true,
      "type": "string"
    },
    {
      "name": "orgCode",
      "in": "query",
      "description": "组织编码",
      "required": true,
      "type": "string"
    },
    {
      "name": "code",
      "in": "query",
      "description": "授权码",
      "required": true,
      "type": "string"
    },
    {
      "name": "loginType",
      "in": "query",
      "description": "登录方式，默认为1，1-普通登录、2-域登录",
      "required": false,
      "type": "integer",
      "format": "int32"
    },
    {
      "name": "loginDate",
      "in": "query",
      "description": "登录日期，上下文日期，表单处理取此日期，不传默认当前日期",
      "required": false,
      "type": "string",
      "format": "date-time"
    },
    {
      "name": "language",
      "in": "query",
      "description": "语种，默认中文（zh-CN）",
      "required": false,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## GET /webapi/OAuth2/AuthLogin

```json
{
  "tags": [
    "OAuth2"
  ],
  "summary": "登录获取token",
  "operationId": "OAuth2_AuthLogin",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "clientid",
      "in": "query",
      "description": "clientid",
      "required": true,
      "type": "string"
    },
    {
      "name": "clientsecret",
      "in": "query",
      "description": "clientsecret",
      "required": true,
      "type": "string"
    },
    {
      "name": "entCode",
      "in": "query",
      "description": "企业编码",
      "required": true,
      "type": "string"
    },
    {
      "name": "userCode",
      "in": "query",
      "description": "用户名(域登录传递域账号，不带域名)",
      "required": true,
      "type": "string"
    },
    {
      "name": "orgCode",
      "in": "query",
      "description": "组织编码",
      "required": true,
      "type": "string"
    },
    {
      "name": "loginType",
      "in": "query",
      "description": "登录方式，默认为1，1-普通登录、2-域登录",
      "required": false,
      "type": "integer",
      "format": "int32"
    },
    {
      "name": "loginDate",
      "in": "query",
      "description": "登录日期，上下文日期，表单处理取此日期，不传默认当前日期",
      "required": false,
      "type": "string",
      "format": "date-time"
    },
    {
      "name": "language",
      "in": "query",
      "description": "语种，默认中文（zh-CN）",
      "required": false,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## GET /webapi/OAuth2/RefreshToken

```json
{
  "tags": [
    "OAuth2"
  ],
  "summary": "刷新token",
  "operationId": "OAuth2_RefreshToken",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "query",
      "description": "token值",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## GET /webapi/OAuth2/DestroyToken

```json
{
  "tags": [
    "OAuth2"
  ],
  "summary": "销毁token",
  "operationId": "OAuth2_DestroyToken",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## GET /webapi/OAuth2/SSOLogin

```json
{
  "tags": [
    "OAuth2"
  ],
  "summary": "单点登录获取授权码",
  "operationId": "OAuth2_SSOLogin",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "clientid",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "clientsecret",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "entCode",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "userCode",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "orgCode",
      "in": "query",
      "description": "",
      "required": true,
      "type": "string"
    },
    {
      "name": "loginType",
      "in": "query",
      "description": "",
      "required": true,
      "type": "integer",
      "format": "int32"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## POST /webapi/OpBusiness/CreateOpTransferBusiness

```json
{
  "tags": [
    "OpBusiness"
  ],
  "summary": "创建工序转移数据-智能工厂专用",
  "operationId": "OpBusiness_CreateOpTransferBusiness",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dtoList",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.RcvRpt.FetchOperationQtyDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpBusiness/DeleteOpTransferBusiness

```json
{
  "tags": [
    "OpBusiness"
  ],
  "operationId": "OpBusiness_DeleteOpTransferBusiness",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dtoList",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.RcvRpt.DeleteOperationQtyDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpBusiness/CreateOpRcvBusinessTemp

```json
{
  "tags": [
    "OpBusiness"
  ],
  "summary": "新增委外收货数据",
  "operationId": "OpBusiness_CreateOpRcvBusinessTemp",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dtoList",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.RcvRpt.FetchOperationQtyDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpBusiness/CreateOpRcvBusiness

```json
{
  "tags": [
    "OpBusiness"
  ],
  "summary": "创建工序委外业务数据",
  "operationId": "OpBusiness_CreateOpRcvBusiness",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dtoList",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.RcvRpt.FetchOpRcvBusinessDataDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpenAPIServiceHub/Execute

```json
{
  "tags": [
    "OpenAPIServiceHub"
  ],
  "operationId": "OpenAPIServiceHub_Execute",
  "conn": [
    "application/json",
    "text/json",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "jObject",
      "in": "body",
      "required": true,
      "schema": {
        "type": "object"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Object]"
      }
    }
  }
}
```

## GET /webapi/OpenAPIServiceHub/Describe

```json
{
  "tags": [
    "OpenAPIServiceHub"
  ],
  "operationId": "OpenAPIServiceHub_Describe",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Object]"
      }
    }
  }
}
```

## GET /webapi/OpenAPIServiceHub/DescribeService

```json
{
  "tags": [
    "OpenAPIServiceHub"
  ],
  "operationId": "OpenAPIServiceHub_DescribeService",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "service",
      "in": "query",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Object]"
      }
    }
  }
}
```

## POST /webapi/Operator/Create

```json
{
  "tags": [
    "Operator"
  ],
  "summary": "创建业务员服务",
  "operationId": "Operator_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "业务员集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Operator.AddOperatorDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Operator/Delete

```json
{
  "tags": [
    "Operator"
  ],
  "summary": "删除业务员服务",
  "operationId": "Operator_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Operator.DeleteOperatorDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Operator/Modify

```json
{
  "tags": [
    "Operator"
  ],
  "summary": "修改业务员服务",
  "operationId": "Operator_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "业务员集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Operator.AddOperatorDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/OpTransferDoc/Create

```json
{
  "tags": [
    "OpTransferDoc"
  ],
  "summary": "新增工序转移单",
  "operationId": "OpTransferDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "opTransferDocDatas",
      "in": "body",
      "description": "工序转移单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.OpTransferDoc.OpTransDocDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpTransferDoc/Modify

```json
{
  "tags": [
    "OpTransferDoc"
  ],
  "summary": "修改工序转移单",
  "operationId": "OpTransferDoc_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "opTransferDocDatas",
      "in": "body",
      "description": "工序转移单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.OpTransferDoc.RTGModifyDTOData1"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpTransferDoc/Delete

```json
{
  "tags": [
    "OpTransferDoc"
  ],
  "summary": "删除工序转移单",
  "operationId": "OpTransferDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "opTransferDocDatas",
      "in": "body",
      "description": "工序转移单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.OpTransferDoc.OpTransDocKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpTransferDoc/Query

```json
{
  "tags": [
    "OpTransferDoc"
  ],
  "summary": "查询工序转移单",
  "operationId": "OpTransferDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "opTransferDocDatas",
      "in": "body",
      "description": "工序转移单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.OpTransferDoc.OpTransDocKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MO.OpTransDocDataDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpTransferDoc/Approve

```json
{
  "tags": [
    "OpTransferDoc"
  ],
  "summary": "审核工序转移单",
  "operationId": "OpTransferDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "opTransferDocDatas",
      "in": "body",
      "description": "工序转移单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.OpTransferDoc.OpTransDocKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/OpTransferDoc/UnApprove

```json
{
  "tags": [
    "OpTransferDoc"
  ],
  "summary": "弃审工序转移单",
  "operationId": "OpTransferDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "opTransferDocDatas",
      "in": "body",
      "description": "工序转移单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.SFC.OpTransferDoc.OpTransDocKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PayBill/Create

```json
{
  "tags": [
    "PayBill"
  ],
  "summary": "新增付款单",
  "operationId": "PayBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "payBillHeadRDatas",
      "in": "body",
      "description": "付款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/U9RestSV.Model.AP.PayBillHeadRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayBill/Delete

```json
{
  "tags": [
    "PayBill"
  ],
  "summary": "删除付款单",
  "operationId": "PayBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDocRDatas",
      "in": "body",
      "description": "付款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayBill/Submit

```json
{
  "tags": [
    "PayBill"
  ],
  "summary": "提交付款单",
  "operationId": "PayBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayBill/Approve

```json
{
  "tags": [
    "PayBill"
  ],
  "summary": "审核付款单",
  "operationId": "PayBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayBill/UnApprove

```json
{
  "tags": [
    "PayBill"
  ],
  "summary": "弃审付款单",
  "operationId": "PayBill_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayReqFund/Create

```json
{
  "tags": [
    "PayReqFund"
  ],
  "summary": "请款单外部立账API",
  "operationId": "PayReqFund_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "payReqFundDTOs",
      "in": "body",
      "description": "请款单外部立账集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.AP.PayReqFundHeadDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayReqFund/CreateStandard

```json
{
  "tags": [
    "PayReqFund"
  ],
  "operationId": "PayReqFund_CreateStandard",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "payReqFundDTOs",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.AP.StandardPayReqFundHeadDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayReqFund/Delete

```json
{
  "tags": [
    "PayReqFund"
  ],
  "summary": "删除请款单",
  "operationId": "PayReqFund_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "请款单删除集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayReqFund/Approve

```json
{
  "tags": [
    "PayReqFund"
  ],
  "summary": "审核请款单",
  "operationId": "PayReqFund_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayReqFund/Submit

```json
{
  "tags": [
    "PayReqFund"
  ],
  "summary": "提交请款单",
  "operationId": "PayReqFund_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PayReqFund/UnApprove

```json
{
  "tags": [
    "PayReqFund"
  ],
  "summary": "弃审请款单",
  "operationId": "PayReqFund_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PC/Create

```json
{
  "tags": [
    "PC"
  ],
  "summary": "创建采购合同服务",
  "operationId": "PC_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PCRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PC/Approved

```json
{
  "tags": [
    "PC"
  ],
  "summary": "审核采购合同服务",
  "operationId": "PC_Approved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PCDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PC/UnApproved

```json
{
  "tags": [
    "PC"
  ],
  "summary": "弃审采购合同服务",
  "operationId": "PC_UnApproved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PCDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PC/Submit

```json
{
  "tags": [
    "PC"
  ],
  "summary": "提交采购合同服务",
  "operationId": "PC_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PCDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PC/Delete

```json
{
  "tags": [
    "PC"
  ],
  "summary": "删除采购合同服务",
  "operationId": "PC_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PC/CreateBIP

```json
{
  "tags": [
    "PC"
  ],
  "summary": "创建BIP采购合同服务",
  "operationId": "PC_CreateBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "param",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.PCData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.ResultForYYCData"
      }
    }
  }
}
```

## POST /webapi/PC/DeleteBIP

```json
{
  "tags": [
    "PC"
  ],
  "summary": "删除BIP采购合同服务",
  "operationId": "PC_DeleteBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.PCData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.ResultDeleteForYYCData"
      }
    }
  }
}
```

## POST /webapi/PeriodCloseRobot/Excute

```json
{
  "tags": [
    "PeriodCloseRobot"
  ],
  "operationId": "PeriodCloseRobot_Excute",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.FR.ExcutePRRobotDTORData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/CreateEmployCategory

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "创建员工类别",
  "operationId": "PersonInfoDoc_CreateEmployCategory",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateEmployCategoryReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateEmployCategoryResp]"
      }
    }
  }
}
```

## GET /webapi/PersonInfoDoc/GetPersonInfoDoc/{ID}

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "获取人员信息",
  "operationId": "PersonInfoDoc_GetPersonInfoDoc",
  "conn": [],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req.iD",
      "in": "query",
      "description": "人员信息ID",
      "required": false,
      "type": "integer",
      "format": "int64"
    },
    {
      "name": "req.personID",
      "in": "query",
      "description": "证件号码",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.personName",
      "in": "query",
      "description": "人员姓名",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.workingOrg",
      "in": "query",
      "description": "工作人事组织",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.employeeCode",
      "in": "query",
      "description": "员工编码",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.businessOrg",
      "in": "query",
      "description": "现任业务组织",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.deptCode",
      "in": "query",
      "description": "现任部门编码",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.jobCode",
      "in": "query",
      "description": "现任职务编码",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.positionCode",
      "in": "query",
      "description": "现任岗位编码",
      "required": false,
      "type": "string"
    },
    {
      "name": "req.entranceType",
      "in": "query",
      "description": "入职类型Enum",
      "required": false,
      "type": "integer",
      "format": "int32"
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.PersonInfoDocResp]]"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/CreatePersonInfoDoc

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "创建员工信息（人员基本信息）",
  "operationId": "PersonInfoDoc_CreatePersonInfoDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreatePersonInfoDocReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreatePersonInfoDocResq]"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/CreatePersonInfo

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "创建人员信息（未启用HR模块）",
  "operationId": "PersonInfoDoc_CreatePersonInfo",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreatePersonInfoReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreatePersonInfoDocResq]"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/UpdatePersonInfoDoc

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "修改人员信息（未启用HR模块）",
  "operationId": "PersonInfoDoc_UpdatePersonInfoDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.UpdatePersonInfoDocReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreatePersonInfoDocResq]"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/CreateEmployeeBankAccount

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "创建员工账号",
  "operationId": "PersonInfoDoc_CreateEmployeeBankAccount",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateEmployeeBankAccountReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateEmployeeBankAccountResp]"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/SaveEmployCategoryForBIP

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "人力云保存员工类别",
  "operationId": "PersonInfoDoc_SaveEmployCategoryForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.YYCDTO[UFIDA.U9.HI.HIBP.Api.Dto.CreateEmployCategoryReq]"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.CBO.PubSV.ControllerSV.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/SavePersonInfoDocForBIP

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "人力云保存人员信息（未启用HR模块）",
  "operationId": "PersonInfoDoc_SavePersonInfoDocForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.YYCDTO[UFIDA.U9.HI.HIBP.Api.Dto.CreatePersonInfoReq]"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.CBO.PubSV.ControllerSV.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/PersonInfoDoc/SaveEmployeeBankAccountForBIP

```json
{
  "tags": [
    "PersonInfoDoc"
  ],
  "summary": "人力云保存员工账号",
  "operationId": "PersonInfoDoc_SaveEmployeeBankAccountForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.YYCDTO[UFIDA.U9.HI.HIBP.Api.Dto.CreateEmployeeBankAccountReq]"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.CBO.PubSV.ControllerSV.BIPCommonOrderResultDTO[System.Collections.Generic.List[UFIDA.U9.CBO.Pub.Controller.CommonArchiveDataDTO]]"
      }
    }
  }
}
```

## POST /webapi/PlanOrder/Create

```json
{
  "tags": [
    "PlanOrder"
  ],
  "summary": "创建计划订单",
  "operationId": "PlanOrder_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "paramsIn",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MRP.AddPlanOrderRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/Create

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "新增委外发料单",
  "operationId": "PMIssueDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外发料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PMIssue.PMIssueDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/Modify

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "修改委外发料单",
  "operationId": "PMIssueDoc_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外发料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PMIssue.PMIssueModifyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/Delete

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "删除委外发料单",
  "operationId": "PMIssueDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外发料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PMIssue.PMIssueKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/Query

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "查询委外发料单",
  "operationId": "PMIssueDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外发料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PMIssue.PMIssueKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PMIssue.PMIssueDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/Approve

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "审核委外发料单",
  "operationId": "PMIssueDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外发料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PMIssue.PMIssueDoc4ExternalDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/Confirm

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "委外发料单发料确认",
  "operationId": "PMIssueDoc_Confirm",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外发料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PMIssue.PMIssueDoc4ExternalDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/CreateRecedeIssueDoc

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "新增委外退料单",
  "operationId": "PMIssueDoc_CreateRecedeIssueDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外退料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PMIssue.PMRecedeItemAndSnDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PMIssueDoc/CreateRecedeIssueDocNew

```json
{
  "tags": [
    "PMIssueDoc"
  ],
  "summary": "新增委外退料单,\r\n有单行",
  "operationId": "PMIssueDoc_CreateRecedeIssueDocNew",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "issueDocDatas",
      "in": "body",
      "description": "委外退料单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.PMIssue.PMRecedeItemAndSnHeadDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/POModify/Approve

```json
{
  "tags": [
    "POModify"
  ],
  "summary": "审核采购订单变更单",
  "operationId": "POModify_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "poModifyDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/POModify/Submit

```json
{
  "tags": [
    "POModify"
  ],
  "summary": "提交采购订单变更单",
  "operationId": "POModify_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "poModifyDTOs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Position/CreatePositionType

```json
{
  "tags": [
    "Position"
  ],
  "summary": "创建岗位分类",
  "operationId": "Position_CreatePositionType",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreatePositionTypeReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreatePositionTypeResp]"
      }
    }
  }
}
```

## POST /webapi/Position/SavePositionTypeForBIP

```json
{
  "tags": [
    "Position"
  ],
  "summary": "人力云保存岗位分类",
  "operationId": "Position_SavePositionTypeForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.YYCDTO[UFIDA.U9.HI.HIBP.Api.Dto.CreatePositionTypeReq]"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.CBO.PubSV.ControllerSV.BIPCommonOrderResultDTO[System.Collections.Generic.List[UFIDA.U9.CBO.Pub.Controller.CommonArchiveDataDTO]]"
      }
    }
  }
}
```

## POST /webapi/Position/CreatePosition

```json
{
  "tags": [
    "Position"
  ],
  "summary": "创建岗位",
  "operationId": "Position_CreatePosition",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreatePositionReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreatePositionResp]"
      }
    }
  }
}
```

## POST /webapi/Position/SavePositionForBIP

```json
{
  "tags": [
    "Position"
  ],
  "summary": "人力云保存岗位",
  "operationId": "Position_SavePositionForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "yyc",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.YYCDTO[UFIDA.U9.HI.HIBP.Api.Dto.CreatePositionReq]"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.CBO.PubSV.ControllerSV.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/POToAsn/CreateAsnBySrcPO

```json
{
  "tags": [
    "POToAsn"
  ],
  "summary": "新增ASN单-来源采购",
  "operationId": "POToAsn_CreateAsnBySrcPO",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createAsnByPODTOs",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.CreateAsnByPODTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/POToAsn/Delete

```json
{
  "tags": [
    "POToAsn"
  ],
  "summary": "删除ASN单服务",
  "operationId": "POToAsn_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/POToAsn/Approved

```json
{
  "tags": [
    "POToAsn"
  ],
  "summary": "审核ASN服务",
  "operationId": "POToAsn_Approved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.AsnDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/POToAsn/UnApproved

```json
{
  "tags": [
    "POToAsn"
  ],
  "summary": "弃审ASN服务",
  "operationId": "POToAsn_UnApproved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.AsnDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/POToAsn/Submit

```json
{
  "tags": [
    "POToAsn"
  ],
  "summary": "提交ASN服务",
  "operationId": "POToAsn_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.AsnDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/POToAsn/Open

```json
{
  "tags": [
    "POToAsn"
  ],
  "summary": "打开ASN服务",
  "operationId": "POToAsn_Open",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.AsnDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/POToAsn/Close

```json
{
  "tags": [
    "POToAsn"
  ],
  "summary": "关闭ASN服务",
  "operationId": "POToAsn_Close",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.AsnDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/Create

```json
{
  "tags": [
    "PR"
  ],
  "summary": "创建请购单服务",
  "operationId": "PR_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/Approved

```json
{
  "tags": [
    "PR"
  ],
  "summary": "审核请购单服务",
  "operationId": "PR_Approved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/UnApproved

```json
{
  "tags": [
    "PR"
  ],
  "summary": "弃审请购单服务",
  "operationId": "PR_UnApproved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/Submit

```json
{
  "tags": [
    "PR"
  ],
  "summary": "提交请购单服务",
  "operationId": "PR_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/Delete

```json
{
  "tags": [
    "PR"
  ],
  "summary": "删除请购单服务",
  "operationId": "PR_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/Open

```json
{
  "tags": [
    "PR"
  ],
  "summary": "打开请购单",
  "operationId": "PR_Open",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/Close

```json
{
  "tags": [
    "PR"
  ],
  "summary": "关闭请购单",
  "operationId": "PR_Close",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/OpenLine

```json
{
  "tags": [
    "PR"
  ],
  "summary": "行打开请购单",
  "operationId": "PR_OpenLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PR/CloseLine

```json
{
  "tags": [
    "PR"
  ],
  "summary": "行关闭请购单",
  "operationId": "PR_CloseLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PRDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PrintToService/Print

```json
{
  "tags": [
    "PrintToService"
  ],
  "summary": "打印接口",
  "operationId": "PrintToService_Print",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ydbPrintData",
      "in": "body",
      "description": "打印参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.YDBPrintData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.ResponseInfo"
      }
    }
  }
}
```

## POST /webapi/ProbationDoc/Submit

```json
{
  "tags": [
    "ProbationDoc"
  ],
  "summary": "提交转正申请单",
  "operationId": "ProbationDoc_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveProbationDocResp]]"
      }
    }
  }
}
```

## POST /webapi/ProbationDoc/Approve

```json
{
  "tags": [
    "ProbationDoc"
  ],
  "summary": "审核转正申请单",
  "operationId": "ProbationDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveProbationDocResp]]"
      }
    }
  }
}
```

## POST /webapi/ProbationDoc/UnApprove

```json
{
  "tags": [
    "ProbationDoc"
  ],
  "summary": "弃审转正申请单",
  "operationId": "ProbationDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.DocOperateCommonReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.HI.HIBP.Api.Dto.ApproveProbationDocResp]]"
      }
    }
  }
}
```

## POST /webapi/Project/Create

```json
{
  "tags": [
    "Project"
  ],
  "summary": "创建项目",
  "operationId": "Project_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "projDatas",
      "in": "body",
      "description": "项目集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ProjectDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Project/Modify

```json
{
  "tags": [
    "Project"
  ],
  "summary": "修改项目",
  "operationId": "Project_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "projDatas",
      "in": "body",
      "description": "项目集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ProjectDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Project/Delete

```json
{
  "tags": [
    "Project"
  ],
  "summary": "删除项目",
  "operationId": "Project_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "projDatas",
      "in": "body",
      "description": "项目集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.QueryProjectDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Project/Query

```json
{
  "tags": [
    "Project"
  ],
  "summary": "查询项目",
  "operationId": "Project_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "projDatas",
      "in": "body",
      "description": "项目集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.QueryProjectDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ProjectDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Project/QueryPage

```json
{
  "tags": [
    "Project"
  ],
  "summary": "查询项目",
  "operationId": "Project_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.QueryPageProjectDTOData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/Project/Approve

```json
{
  "tags": [
    "Project"
  ],
  "summary": "审核项目",
  "operationId": "Project_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "审核参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.QueryProjectDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ProjMaster/Create

```json
{
  "tags": [
    "ProjMaster"
  ],
  "summary": "创建项目主档",
  "operationId": "ProjMaster_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "projMaster",
      "in": "body",
      "description": "项目主档参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.PMM.ProjMasterDtoData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]"
      }
    }
  }
}
```

## POST /webapi/ProjMaster/Approve

```json
{
  "tags": [
    "ProjMaster"
  ],
  "summary": "提交审核弃审项目主档",
  "operationId": "ProjMaster_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "approveprojMaster",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.PMM.ApproveProjMasterDto"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]"
      }
    }
  }
}
```

## POST /webapi/ProjMaster/Delete

```json
{
  "tags": [
    "ProjMaster"
  ],
  "summary": "删除项目主档",
  "operationId": "ProjMaster_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "projMaster",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.PMM.ProjMasterParamDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Create

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "新增无来源采购订单",
  "operationId": "PurchaseOrder_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PO.PurchaseOrderDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/CreatePurchaseOrderBySrc

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "新增有来源采购订单",
  "operationId": "PurchaseOrder_CreatePurchaseOrderBySrc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PO.CreatePOBySrcDocDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PO.ResultPODTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Delete

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "删除采购订单",
  "operationId": "PurchaseOrder_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "采购订单结合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Approve

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "审核采购订单",
  "operationId": "PurchaseOrder_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Submit

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "提交采购订单",
  "operationId": "PurchaseOrder_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/UnApprove

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "弃审采购订单",
  "operationId": "PurchaseOrder_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Cancel

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "终止采购订单",
  "operationId": "PurchaseOrder_Cancel",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Hold

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "解除挂起采购订单 by guojjjuan 20240731",
  "operationId": "PurchaseOrder_Hold",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Release

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "挂起采购订单",
  "operationId": "PurchaseOrder_Release",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Open

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "打开采购订单",
  "operationId": "PurchaseOrder_Open",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/Close

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "关闭采购订单",
  "operationId": "PurchaseOrder_Close",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "purchaseOrderDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/OpenLine

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "行打开采购订单",
  "operationId": "PurchaseOrder_OpenLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "POLineKeyDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PO.POLineKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/CloseLine

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "行关闭采购订单",
  "operationId": "PurchaseOrder_CloseLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "POLineKeyDTOs",
      "in": "body",
      "description": "采购订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PO.POLineKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurchaseOrder/POCreateSO

```json
{
  "tags": [
    "PurchaseOrder"
  ],
  "summary": "采购订单协同创建销售订单",
  "operationId": "PurchaseOrder_POCreateSO",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "poCreateSODTOs",
      "in": "body",
      "description": "采购订单协同创建销售订单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PO.POCreateSODTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurDiscountPolicy/Create

```json
{
  "tags": [
    "PurDiscountPolicy"
  ],
  "summary": "创建厂商折扣",
  "operationId": "PurDiscountPolicy_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "PSPDTORDATAs",
      "in": "body",
      "description": "厂商折扣集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PPR.PurDiscountPolicy.PDPRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PurDiscountPolicy/Delete

```json
{
  "tags": [
    "PurDiscountPolicy"
  ],
  "summary": "删除厂商折扣",
  "operationId": "PurDiscountPolicy_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "PSPDTORDATAs",
      "in": "body",
      "description": "厂商折扣集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PurDiscountPolicy/Submit

```json
{
  "tags": [
    "PurDiscountPolicy"
  ],
  "summary": "提交厂商折扣",
  "operationId": "PurDiscountPolicy_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "PSPDTORDATAs",
      "in": "body",
      "description": "厂商折扣集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PurDiscountPolicy/Approve

```json
{
  "tags": [
    "PurDiscountPolicy"
  ],
  "summary": "审核厂商折扣",
  "operationId": "PurDiscountPolicy_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "PSPDTORDATAs",
      "in": "body",
      "description": "厂商折扣集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PurDiscountPolicy/UnApprove

```json
{
  "tags": [
    "PurDiscountPolicy"
  ],
  "summary": "弃审厂商折扣",
  "operationId": "PurDiscountPolicy_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "PSPDTORDATAs",
      "in": "body",
      "description": "厂商折扣集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PurDiscountPolicy/CancelPur

```json
{
  "tags": [
    "PurDiscountPolicy"
  ],
  "summary": "终止厂商折扣",
  "operationId": "PurDiscountPolicy_CancelPur",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "PSPDTORDATAs",
      "in": "body",
      "description": "终止厂商折扣",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PPR.PurDiscountPolicy.CancelPPRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceAdjustment/Create

```json
{
  "tags": [
    "PurPriceAdjustment"
  ],
  "summary": "创建厂商价格调整服务",
  "operationId": "PurPriceAdjustment_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PurPriceAdjustmentDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceAdjustment/Approved

```json
{
  "tags": [
    "PurPriceAdjustment"
  ],
  "summary": "审核厂商价格调整服务",
  "operationId": "PurPriceAdjustment_Approved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceAdjustment/Cancel

```json
{
  "tags": [
    "PurPriceAdjustment"
  ],
  "summary": "终止厂商价格调整服务",
  "operationId": "PurPriceAdjustment_Cancel",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceAdjustment/Delete

```json
{
  "tags": [
    "PurPriceAdjustment"
  ],
  "summary": "删除厂商价格调整服务",
  "operationId": "PurPriceAdjustment_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceAdjustment/Submit

```json
{
  "tags": [
    "PurPriceAdjustment"
  ],
  "summary": "提交厂商价格调整服务",
  "operationId": "PurPriceAdjustment_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "inputDatas",
      "in": "body",
      "description": "入口参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceList/Create

```json
{
  "tags": [
    "PurPriceList"
  ],
  "summary": "新增厂商价表",
  "operationId": "PurPriceList_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optList",
      "in": "body",
      "description": "厂商价表集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PurPriceListDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceList/Submit

```json
{
  "tags": [
    "PurPriceList"
  ],
  "summary": "提交厂商价表",
  "operationId": "PurPriceList_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optList",
      "in": "body",
      "description": "数据集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceList/Approved

```json
{
  "tags": [
    "PurPriceList"
  ],
  "summary": "审核厂商价表",
  "operationId": "PurPriceList_Approved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optList",
      "in": "body",
      "description": "数据集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceList/UnApproved

```json
{
  "tags": [
    "PurPriceList"
  ],
  "summary": "弃审厂商价表",
  "operationId": "PurPriceList_UnApproved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optList",
      "in": "body",
      "description": "数据集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceList/Delete

```json
{
  "tags": [
    "PurPriceList"
  ],
  "summary": "删除厂商价表",
  "operationId": "PurPriceList_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optList",
      "in": "body",
      "description": "数据集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/PurPriceList/BipCancel

```json
{
  "tags": [
    "PurPriceList"
  ],
  "summary": "终止厂商价表 (该方法仅供BIP内部使用)",
  "operationId": "PurPriceList_BipCancel",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.U9OrderCommonDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.BIPCommonReturnDTO"
      }
    }
  }
}
```

## POST /webapi/QCDoc/QualityCheck

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "质检",
  "operationId": "QCDoc_QualityCheck",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDoc/CalcQCResult

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "计算质检结果",
  "operationId": "QCDoc_CalcQCResult",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDoc/Complete

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "质检完成",
  "operationId": "QCDoc_Complete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDoc/Approve

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "审核",
  "operationId": "QCDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDoc/UnApprove

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "弃审",
  "operationId": "QCDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDoc/Rtn

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "退回",
  "operationId": "QCDoc_Rtn",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptDocRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDoc/PullCreate

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "拉式生单",
  "operationId": "QCDoc_PullCreate",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.PullQCDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.PullQCDocRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDoc/CreateOtherQC

```json
{
  "tags": [
    "QCDoc"
  ],
  "summary": "创建其他质检单",
  "operationId": "QCDoc_CreateOtherQC",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.QCDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/QCDocLine/QualityCheck

```json
{
  "tags": [
    "QCDocLine"
  ],
  "summary": "质检",
  "operationId": "QCDocLine_QualityCheck",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDocLine/CalcQCResult

```json
{
  "tags": [
    "QCDocLine"
  ],
  "summary": "计算质检结果",
  "operationId": "QCDocLine_CalcQCResult",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDocLine/Complete

```json
{
  "tags": [
    "QCDocLine"
  ],
  "summary": "质检完成",
  "operationId": "QCDocLine_Complete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDocLine/Approve

```json
{
  "tags": [
    "QCDocLine"
  ],
  "summary": "审核",
  "operationId": "QCDocLine_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDocLine/UnApprove

```json
{
  "tags": [
    "QCDocLine"
  ],
  "summary": "弃审",
  "operationId": "QCDocLine_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QCDocLine/Rtn

```json
{
  "tags": [
    "QCDocLine"
  ],
  "summary": "退回",
  "operationId": "QCDocLine_Rtn",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.QC.RestSV.Model.QC.OptLineRtnData]]"
      }
    }
  }
}
```

## POST /webapi/QueryCommon/QueryInfoBySql

```json
{
  "tags": [
    "QueryCommon"
  ],
  "summary": "根据SQL查询档案信息",
  "operationId": "QueryCommon_QueryInfoBySql",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "queryCommonDTO",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.QueryCommonDTOData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Data.DataTable]"
      }
    }
  }
}
```

## GET /webapi/QueryCommon/GetTimeStamp

```json
{
  "tags": [
    "QueryCommon"
  ],
  "summary": "获取时间戳",
  "operationId": "QueryCommon_GetTimeStamp",
  "conn": [],
  "proo": [
    "application/json",
    "text/json"
  ],
  "parameters": [
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[Newtonsoft.Json.Linq.JObject]"
      }
    }
  }
}
```

## POST /webapi/Quot/Create

```json
{
  "tags": [
    "Quot"
  ],
  "summary": "新增报价单",
  "operationId": "Quot_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "QuotDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.Quot.QuotDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RcvRptDoc/Create

```json
{
  "tags": [
    "RcvRptDoc"
  ],
  "summary": "新增成品入库单",
  "operationId": "RcvRptDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvRptDocDatas",
      "in": "body",
      "description": "成品入库单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.NewComplete.CompleteDocInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/RcvRptDoc/Modify

```json
{
  "tags": [
    "RcvRptDoc"
  ],
  "summary": "修改成品入库单",
  "operationId": "RcvRptDoc_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvRptDocDatas",
      "in": "body",
      "description": "成品入库单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MFG.MO.NewComplete.RcvRptDocDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/RcvRptDoc/Delete

```json
{
  "tags": [
    "RcvRptDoc"
  ],
  "summary": "删除成品入库单",
  "operationId": "RcvRptDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvRptDocDatas",
      "in": "body",
      "description": "成品入库单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/RcvRptDoc/Query

```json
{
  "tags": [
    "RcvRptDoc"
  ],
  "summary": "查询成品入库单",
  "operationId": "RcvRptDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvRptDocDatas",
      "in": "body",
      "description": "成品入库单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MO.RcvRptDocDTOData]]"
      }
    }
  }
}
```

## POST /webapi/RcvRptDoc/Approve

```json
{
  "tags": [
    "RcvRptDoc"
  ],
  "summary": "审核成品入库单",
  "operationId": "RcvRptDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvRptDocDatas",
      "in": "body",
      "description": "成品入库单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/RcvRptDoc/UnApprove

```json
{
  "tags": [
    "RcvRptDoc"
  ],
  "summary": "弃审成品入库单",
  "operationId": "RcvRptDoc_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvRptDocDatas",
      "in": "body",
      "description": "成品入库单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.WOKeyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/RecBill/Create

```json
{
  "tags": [
    "RecBill"
  ],
  "summary": "新增收款单",
  "operationId": "RecBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "recBillHeadRDatas",
      "in": "body",
      "description": "收款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/U9RestSV.Model.AR.RecBillHeadRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RecBill/Delete

```json
{
  "tags": [
    "RecBill"
  ],
  "summary": "删除收款单",
  "operationId": "RecBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDocRDatas",
      "in": "body",
      "description": "收款单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RecBill/Submit

```json
{
  "tags": [
    "RecBill"
  ],
  "summary": "提交收款单",
  "operationId": "RecBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RecBill/Approve

```json
{
  "tags": [
    "RecBill"
  ],
  "summary": "审核收款单",
  "operationId": "RecBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RecBill/UnApprove

```json
{
  "tags": [
    "RecBill"
  ],
  "summary": "弃审收款单",
  "operationId": "RecBill_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/CreateRcvBySrc

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "新增退货单有来源",
  "operationId": "Receivement_CreateRcvBySrc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createRtnRcvBySrcDTOs",
      "in": "body",
      "description": "根据来源创建退货DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.CreateRtnRcvBySrcDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/CreateSaleRcvBySrc

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "新增销退收货单有来源",
  "operationId": "Receivement_CreateSaleRcvBySrc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createSaleRtnRcvBySrcDTOs",
      "in": "body",
      "description": "根据来源创建销退收货DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.PM.CreateSaleRtnRcvBySrcDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/Delete

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "删除收货单",
  "operationId": "Receivement_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvDatas",
      "in": "body",
      "description": "收货单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.ReceivementDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/Submit

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "提交收货单",
  "operationId": "Receivement_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvDatas",
      "in": "body",
      "description": "收货单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.ReceivementDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/Approve

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "审核收货单",
  "operationId": "Receivement_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvDatas",
      "in": "body",
      "description": "收货单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.ReceivementDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/UnApprove

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "弃审收货单",
  "operationId": "Receivement_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvDatas",
      "in": "body",
      "description": "收货单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.ReceivementDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/SubmitLine

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "行提交收货单",
  "operationId": "Receivement_SubmitLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvLineDatas",
      "in": "body",
      "description": "收货单行集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.RcvLineDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/ApproveLine

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "行审核收货单",
  "operationId": "Receivement_ApproveLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvLineDatas",
      "in": "body",
      "description": "收货单行集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.RcvLineDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/UnApproveLine

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "行弃审收货单",
  "operationId": "Receivement_UnApproveLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvLineDatas",
      "in": "body",
      "description": "收货单行集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.RcvLineDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/HoldLine

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "挂起收货单",
  "operationId": "Receivement_HoldLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvLineDatas",
      "in": "body",
      "description": "收货单行集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.RcvLineDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/ReleaseLine

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "解除收货单",
  "operationId": "Receivement_ReleaseLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvLineDatas",
      "in": "body",
      "description": "收货单行集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.RcvLineDTOData_Act"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/CreateRcvBySrcPO

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "新增收货单-来源采购",
  "operationId": "Receivement_CreateRcvBySrcPO",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createRcvBySrcPODTOs",
      "in": "body",
      "description": "根据来源采购创建收货DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.PM.CreateRcvBySrcPODTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[ResultRcvDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/CreateReceivement

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "新增收货单",
  "operationId": "Receivement_CreateReceivement",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvDTO",
      "in": "body",
      "description": "创建收货DTO",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.PM.ReceivementDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/CreateRcvBySrcASN

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "新增收货单-来源ASN",
  "operationId": "Receivement_CreateRcvBySrcASN",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createRcvByASNDTOs",
      "in": "body",
      "description": "根据来源ASN创建收货DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.CreateRcvByASNDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/GetRcvByPage

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "BIP通过查询方案查询收货单，同步他们的对账信息。",
  "operationId": "Receivement_GetRcvByPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "param",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.PageQueryRcvDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PM.RestSV.Model.SCM.PM.BIPResultDTOData]"
      }
    }
  }
}
```

## POST /webapi/Receivement/EyeballingRcv

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "标准收货的\"点收单(行)功能",
  "operationId": "Receivement_EyeballingRcv",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "eyeBallingRcvDataDTOs",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.EyeBallingRcvDataDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/SplitRcvLine

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "拆分收货单行",
  "operationId": "Receivement_SplitRcvLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "splitRcvLineDTOs",
      "in": "body",
      "description": "拆分收货行DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.PM.SplitRcvLineDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[ResultRcvDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Receivement/RcvDispense

```json
{
  "tags": [
    "Receivement"
  ],
  "summary": "收货单固定资产分发接口",
  "operationId": "Receivement_RcvDispense",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rcvLineDispenseParams",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.PM.RcvLineDispenseParamsDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.PM.Rcv.RcvlineDispenseResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ReimBill/Create

```json
{
  "tags": [
    "ReimBill"
  ],
  "summary": "创建报销单",
  "operationId": "ReimBill_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Model.ER.ReimburseBillHeadDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ReimBill/Approve

```json
{
  "tags": [
    "ReimBill"
  ],
  "summary": "审核报销单",
  "operationId": "ReimBill_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ReimBill/Submit

```json
{
  "tags": [
    "ReimBill"
  ],
  "summary": "提交报销单",
  "operationId": "ReimBill_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ReimBill/UnApprove

```json
{
  "tags": [
    "ReimBill"
  ],
  "summary": "弃审报销单",
  "operationId": "ReimBill_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ReimBill/Delete

```json
{
  "tags": [
    "ReimBill"
  ],
  "summary": "删除报销单",
  "operationId": "ReimBill_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "DelDatas",
      "in": "body",
      "description": "还款单删除集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Report/GetReportPdfFile

```json
{
  "tags": [
    "Report"
  ],
  "summary": "",
  "operationId": "Report_GetReportPdfFile",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.GetReportPdfFileReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResultList[UFSoft.UBF.MVC.GetReportPdfFileResp]"
      }
    }
  }
}
```

## POST /webapi/Resource/Create

```json
{
  "tags": [
    "Resource"
  ],
  "summary": "创建资源",
  "operationId": "Resource_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "resDatas",
      "in": "body",
      "description": "资源集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Resource.ResourceDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Resource/Modify

```json
{
  "tags": [
    "Resource"
  ],
  "summary": "修改资源",
  "operationId": "Resource_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "resDatas",
      "in": "body",
      "description": "资源集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Resource.ResourceModifyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Resource/Delete

```json
{
  "tags": [
    "Resource"
  ],
  "summary": "资源BOM",
  "operationId": "Resource_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "resDatas",
      "in": "body",
      "description": "资源集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Resource.QueryOrDeleteResourceDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Resource/Query

```json
{
  "tags": [
    "Resource"
  ],
  "summary": "查询资源",
  "operationId": "Resource_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "resDatas",
      "in": "body",
      "description": "资源集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Resource.QueryOrDeleteResourceDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Resource.ResourceDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ResUsageRptDoc/Create

```json
{
  "tags": [
    "ResUsageRptDoc"
  ],
  "summary": "新增创建资源报告单",
  "operationId": "ResUsageRptDoc_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ResUsageRptDocDatas",
      "in": "body",
      "description": "资源报告单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.ISVResUsageRptDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ResUsageRptDoc/Delete

```json
{
  "tags": [
    "ResUsageRptDoc"
  ],
  "summary": "删除资源报告单",
  "operationId": "ResUsageRptDoc_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ResUsageRptDocDatas",
      "in": "body",
      "description": "资源报告单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.ResUsageRptKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ResUsageRptDoc/Approve

```json
{
  "tags": [
    "ResUsageRptDoc"
  ],
  "summary": "审核资源报告单",
  "operationId": "ResUsageRptDoc_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ResUsageRptDocDatas",
      "in": "body",
      "description": "资源报告单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MO.ResUsageRptKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/RMA/Create

```json
{
  "tags": [
    "RMA"
  ],
  "summary": "创建退回处理单",
  "operationId": "RMA_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rmaDTOList",
      "in": "body",
      "description": "供应商集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.RMA.RMAOpenAPIData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMA/Submit

```json
{
  "tags": [
    "RMA"
  ],
  "summary": "提交退回处理单",
  "operationId": "RMA_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "退回处理单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMA/Approve

```json
{
  "tags": [
    "RMA"
  ],
  "summary": "审核退回处理单",
  "operationId": "RMA_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "退回处理单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMA/UnApprove

```json
{
  "tags": [
    "RMA"
  ],
  "summary": "弃审退回处理单",
  "operationId": "RMA_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "退回处理单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMA/Delete

```json
{
  "tags": [
    "RMA"
  ],
  "summary": "删除退回处理单",
  "operationId": "RMA_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rmaDTOList",
      "in": "body",
      "description": "退回处理单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMA/CreateRMABySrcDoc

```json
{
  "tags": [
    "RMA"
  ],
  "summary": "创建有来源的退回处理单",
  "operationId": "RMA_CreateRMABySrcDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rmaSrcDocInfo",
      "in": "body",
      "description": "来源单据信息",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.RMA.RmaSrcDocInfo"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMR/Create

```json
{
  "tags": [
    "RMR"
  ],
  "summary": "创建退回申请单",
  "operationId": "RMR_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rmrheadDTOList",
      "in": "body",
      "description": "退回申请单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.RMR.RMRHeadDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMR/Detele

```json
{
  "tags": [
    "RMR"
  ],
  "summary": "删除退回申请单",
  "operationId": "RMR_Detele",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMR/Accept

```json
{
  "tags": [
    "RMR"
  ],
  "summary": "受理退回申请单",
  "operationId": "RMR_Accept",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMR/Submit

```json
{
  "tags": [
    "RMR"
  ],
  "summary": "提交退回申请单",
  "operationId": "RMR_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMR/Approve

```json
{
  "tags": [
    "RMR"
  ],
  "summary": "审核退回申请单",
  "operationId": "RMR_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMR/UnApprove

```json
{
  "tags": [
    "RMR"
  ],
  "summary": "弃审退回申请单",
  "operationId": "RMR_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/RMR/CreateRMRBySrcDoc

```json
{
  "tags": [
    "RMR"
  ],
  "summary": "创建有来源的退回申请单",
  "operationId": "RMR_CreateRMRBySrcDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rmrSrcDocInfo",
      "in": "body",
      "description": "来源单据信息",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.RMR.RmrSrcDocInfo"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Routing/Create

```json
{
  "tags": [
    "Routing"
  ],
  "summary": "创建工艺路线",
  "operationId": "Routing_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "工艺路线集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.RTG.RTGCreateInParaDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Routing/Modify

```json
{
  "tags": [
    "Routing"
  ],
  "summary": "修改工艺路线",
  "operationId": "Routing_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "工艺路线集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.RTG.RTGModifyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Routing/Delete

```json
{
  "tags": [
    "Routing"
  ],
  "summary": "删除工艺路线",
  "operationId": "Routing_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "工艺路线集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.RTG.RemoveRTGSrvData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Routing/Query

```json
{
  "tags": [
    "Routing"
  ],
  "summary": "查询工艺路线",
  "operationId": "Routing_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "工艺路线集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.RTG.RTGKeyDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.MFG.BOM.RTGDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SaleContract/Create

```json
{
  "tags": [
    "SaleContract"
  ],
  "summary": "新增销售合同",
  "operationId": "SaleContract_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createSaleContractRData",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.SO.CreateSaleContractRData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SaleContract/Submit

```json
{
  "tags": [
    "SaleContract"
  ],
  "summary": "提交销售合同",
  "operationId": "SaleContract_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SaleContract/Approve

```json
{
  "tags": [
    "SaleContract"
  ],
  "summary": "审批销售合同",
  "operationId": "SaleContract_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SaleContract/UnApproved

```json
{
  "tags": [
    "SaleContract"
  ],
  "summary": "弃审销售合同",
  "operationId": "SaleContract_UnApproved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SaleContract/Delete

```json
{
  "tags": [
    "SaleContract"
  ],
  "summary": "删除销售合同",
  "operationId": "SaleContract_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceAdjustment/Create

```json
{
  "tags": [
    "SalePriceAdjustment"
  ],
  "summary": "创建销售调价单",
  "operationId": "SalePriceAdjustment_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPADTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SPR.SalePriceAdjustment.SPARData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceAdjustment/Delete

```json
{
  "tags": [
    "SalePriceAdjustment"
  ],
  "summary": "删除销售调价单",
  "operationId": "SalePriceAdjustment_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPADTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceAdjustment/Submit

```json
{
  "tags": [
    "SalePriceAdjustment"
  ],
  "summary": "提交销售调价单",
  "operationId": "SalePriceAdjustment_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPADTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceAdjustment/Approve

```json
{
  "tags": [
    "SalePriceAdjustment"
  ],
  "summary": "审核销售调价单",
  "operationId": "SalePriceAdjustment_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPADTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceList/Create

```json
{
  "tags": [
    "SalePriceList"
  ],
  "summary": "创建销售价表",
  "operationId": "SalePriceList_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPRDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SPR.SalePriceListDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceList/Delete

```json
{
  "tags": [
    "SalePriceList"
  ],
  "summary": "删除销售价表",
  "operationId": "SalePriceList_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPRDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceList/Approve

```json
{
  "tags": [
    "SalePriceList"
  ],
  "summary": "审核销售价表",
  "operationId": "SalePriceList_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SalePriceList/UnApprove

```json
{
  "tags": [
    "SalePriceList"
  ],
  "summary": "弃审销售价表",
  "operationId": "SalePriceList_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Seiban/Create

```json
{
  "tags": [
    "Seiban"
  ],
  "summary": "创建番号",
  "operationId": "Seiban_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.SeibanDataDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SeibanMaster/Create

```json
{
  "tags": [
    "SeibanMaster"
  ],
  "summary": "创建番号",
  "operationId": "SeibanMaster_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Operator.AddSeibanMasterDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SetPrintDatasServices/SetPrintDatas

```json
{
  "tags": [
    "SetPrintDatasServices"
  ],
  "summary": "组织打印数据接口",
  "operationId": "SetPrintDatasServices_SetPrintDatas",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "setPrintDatas",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.ResultPrintData"
      }
    }
  }
}
```

## POST /webapi/Ship/Create

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "创建出货单",
  "operationId": "Ship_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.Ship.ShipRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Ship/CreateBySrcDoc

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "创建出货单按来源单据",
  "operationId": "Ship_CreateBySrcDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.Ship.ShipSrcDocInfo"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Ship/Delete

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "删除出货单",
  "operationId": "Ship_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Ship/Approve

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "审核出货单",
  "operationId": "Ship_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Ship/Submit

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "提交出货单",
  "operationId": "Ship_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Ship/SubmitAndApprove

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "提交并审核出货单",
  "operationId": "Ship_SubmitAndApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Ship/UnApproved

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "弃审出货单",
  "operationId": "Ship_UnApproved",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/Ship/Query

```json
{
  "tags": [
    "Ship"
  ],
  "summary": "查询出货单",
  "operationId": "Ship_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SHIPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.Ship.ShipQueryCondRData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.Ship.ShipRData]]"
      }
    }
  }
}
```

## POST /webapi/ShipPlan/Create

```json
{
  "tags": [
    "ShipPlan"
  ],
  "summary": "创建出货计划",
  "operationId": "ShipPlan_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.ShipPlan.ShipPlanRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ShipPlan/CreateBySrcDoc

```json
{
  "tags": [
    "ShipPlan"
  ],
  "summary": "创建出货计划按来源单据",
  "operationId": "ShipPlan_CreateBySrcDoc",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SPDTORDATAs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.ShipPlan.SPSrcDocInfo"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/ShipPlan/Submit

```json
{
  "tags": [
    "ShipPlan"
  ],
  "summary": "提交出货计划",
  "operationId": "ShipPlan_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ShipPlan/Approve

```json
{
  "tags": [
    "ShipPlan"
  ],
  "summary": "审核出货计划",
  "operationId": "ShipPlan_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ShipPlan/UnApprove

```json
{
  "tags": [
    "ShipPlan"
  ],
  "summary": "弃审出货计划",
  "operationId": "ShipPlan_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ShipPlan/Delete

```json
{
  "tags": [
    "ShipPlan"
  ],
  "summary": "删除出货计划",
  "operationId": "ShipPlan_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SignInData/Create

```json
{
  "tags": [
    "SignInData"
  ],
  "summary": "创建签到数据",
  "operationId": "SignInData_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "req",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.HI.HIBP.Api.Dto.CreateSignInDataReq"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.HI.HIBP.Api.Dto.CreateSignInDataResp]"
      }
    }
  }
}
```

## POST /webapi/SO/Create

```json
{
  "tags": [
    "SO"
  ],
  "summary": "创建SO",
  "operationId": "SO_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "soDTOList",
      "in": "body",
      "description": "soDTOList",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.SO.SODTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/Modify

```json
{
  "tags": [
    "SO"
  ],
  "summary": "修改SO",
  "operationId": "SO_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "soDTOList",
      "in": "body",
      "description": "soDTOList",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.SO.SODTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/Delete

```json
{
  "tags": [
    "SO"
  ],
  "summary": "删除SO",
  "operationId": "SO_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/Submit

```json
{
  "tags": [
    "SO"
  ],
  "summary": "提交SO",
  "operationId": "SO_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/Approve

```json
{
  "tags": [
    "SO"
  ],
  "summary": "审核SO",
  "operationId": "SO_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/UnApprove

```json
{
  "tags": [
    "SO"
  ],
  "summary": "弃审SO",
  "operationId": "SO_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/Open

```json
{
  "tags": [
    "SO"
  ],
  "summary": "整单打开SO",
  "operationId": "SO_Open",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/Close

```json
{
  "tags": [
    "SO"
  ],
  "summary": "整单关闭SO",
  "operationId": "SO_Close",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/OpenLine

```json
{
  "tags": [
    "SO"
  ],
  "summary": "SO行打开",
  "operationId": "SO_OpenLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SOLineKeyDTOList",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.SO.SOLineKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/CloseLine

```json
{
  "tags": [
    "SO"
  ],
  "summary": "SO行关闭",
  "operationId": "SO_CloseLine",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "SOLineKeyDTOList",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SCM.SM.SO.SOLineKeyDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/ReleaseSO

```json
{
  "tags": [
    "SO"
  ],
  "summary": "下达SO",
  "operationId": "SO_ReleaseSO",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/CancelReleaseSO

```json
{
  "tags": [
    "SO"
  ],
  "summary": "取消下达SO",
  "operationId": "SO_CancelReleaseSO",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SO/SCMDocCreditCheck4BIP

```json
{
  "tags": [
    "SO"
  ],
  "summary": "供应链业务单据信用检查-BIP专属服务",
  "operationId": "SO_SCMDocCreditCheck4BIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "creditCheckInfos",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SO.CreditCheckHeadDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.BIPCommonOrderResultDTOData[System.Collections.Generic.List[UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.SCMDocCreditCheck4BIPData]]"
      }
    }
  }
}
```

## POST /webapi/SO/GetCreditObjectInfoByCustomer

```json
{
  "tags": [
    "SO"
  ],
  "summary": "查询客户信用余额服务",
  "operationId": "SO_GetCreditObjectInfoByCustomer",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "creditCustomers",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SO.CreditCheckHeadDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.BIPCommonOrderResultDTOData[System.Collections.Generic.List[UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.GetCreditBlanceByCustomerBIPData]]"
      }
    }
  }
}
```

## POST /webapi/SO/SOCanModifyDTOForBIP

```json
{
  "tags": [
    "SO"
  ],
  "summary": "查询销售订单是否可变更",
  "operationId": "SO_SOCanModifyDTOForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "querydto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.YYCSOCanModifyDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.BIPCommonResultDTOData[UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.SOCanModifyRtnDTO]"
      }
    }
  }
}
```

## POST /webapi/SO/ModifySOForBIP

```json
{
  "tags": [
    "SO"
  ],
  "summary": "销售订单变更",
  "operationId": "SO_ModifySOForBIP",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "updatedto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.YYCSOModifyDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.SM.RestSV.Model.SM.SO.BIPCommonOrderResultDTOData[UFIDA.U9.CBO.Pub.Controller.CommonArchiveDataDTO]"
      }
    }
  }
}
```

## POST /webapi/SOModify/Submit

```json
{
  "tags": [
    "SOModify"
  ],
  "summary": "提交销售变更",
  "operationId": "SOModify_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "optDatas",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SOModify/Approve

```json
{
  "tags": [
    "SOModify"
  ],
  "summary": "审核销售变更",
  "operationId": "SOModify_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "optDatas",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/SOModify/UnApprove

```json
{
  "tags": [
    "SOModify"
  ],
  "summary": "弃审销售变更",
  "operationId": "SOModify_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "optDatas",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/StdWorkingHours/Create

```json
{
  "tags": [
    "StdWorkingHours"
  ],
  "summary": "创建定额工时(成本管理-成本会计-分配设定 -定额工时)",
  "operationId": "StdWorkingHours_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "stdWorkingHoursDatas",
      "in": "body",
      "description": "定额工时",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CA.StdWorkingHoursDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Supplier/NewCreate

```json
{
  "tags": [
    "Supplier"
  ],
  "summary": "New新增供应商",
  "operationId": "Supplier_NewCreate",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplierDTOs",
      "in": "body",
      "description": "供应商集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Supplier.NewSupplierDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Supplier/Create

```json
{
  "tags": [
    "Supplier"
  ],
  "summary": "新增供应商",
  "operationId": "Supplier_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplierDTOs",
      "in": "body",
      "description": "供应商集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.Supplier.SupplierDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Supplier/QrySupplier

```json
{
  "tags": [
    "Supplier"
  ],
  "summary": "查询供应商",
  "operationId": "Supplier_QrySupplier",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplierDatas",
      "in": "body",
      "description": "查询供应商集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.Supplier.QuerySupplierDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Supplier/DelSup

```json
{
  "tags": [
    "Supplier"
  ],
  "summary": "删除供应商",
  "operationId": "Supplier_DelSup",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplierDatas",
      "in": "body",
      "description": "删除供应商集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Supplier.DelSupplierDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Supplier/CreateByScheme

```json
{
  "tags": [
    "Supplier"
  ],
  "summary": "创建供应商(集成方案)",
  "operationId": "Supplier_CreateByScheme",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplierDTOs",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Supplier.SupplierDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.BIPCommonArchivesResultDTOData"
      }
    }
  }
}
```

## POST /webapi/Supplier/QueryPage

```json
{
  "tags": [
    "Supplier"
  ],
  "summary": "查询分页(集成方案)",
  "operationId": "Supplier_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonApiQueryParamDTO"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/Supplier/Modify

```json
{
  "tags": [
    "Supplier"
  ],
  "summary": "修改供应商",
  "operationId": "Supplier_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplierDTOs",
      "in": "body",
      "description": "供应商集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.Supplier.NewSupplierDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SupplierItem/Create

```json
{
  "tags": [
    "SupplierItem"
  ],
  "summary": "创建供应商料品交叉",
  "operationId": "SupplierItem_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplierItemDTODatas",
      "in": "body",
      "description": "供应商料品交叉DTO集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO_SCM.SupplierItemDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SupplySource/SubmitSupplySource

```json
{
  "tags": [
    "SupplySource"
  ],
  "summary": "提交货源表",
  "operationId": "SupplySource_SubmitSupplySource",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplySourceDatas",
      "in": "body",
      "description": "提交货源表ID集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.SupplySource.SubmitApproveSupplySourceDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SupplySource/ApproveSupplySource

```json
{
  "tags": [
    "SupplySource"
  ],
  "summary": "审核货源表",
  "operationId": "SupplySource_ApproveSupplySource",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplySourceDatas",
      "in": "body",
      "description": "审核货源表ID集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.SupplySource.SubmitApproveSupplySourceDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/SupplySource/CreateSupplySource

```json
{
  "tags": [
    "SupplySource"
  ],
  "summary": "创建货源表",
  "operationId": "SupplySource_CreateSupplySource",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "supplySourceDatas",
      "in": "body",
      "description": "创建货源表参数集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.SupplySource.CreateSupplySourceDTO"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TemporaryStorage/TemporaryStorageSave

```json
{
  "tags": [
    "TemporaryStorage"
  ],
  "summary": "暂存save",
  "operationId": "TemporaryStorage_TemporaryStorageSave",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "TemporaryStorageData",
      "in": "body",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.TemporaryStorage.TemporaryStorageData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/TemporaryStorage/TemporaryStorageDelete

```json
{
  "tags": [
    "TemporaryStorage"
  ],
  "summary": "暂存delete",
  "operationId": "TemporaryStorage_TemporaryStorageDelete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "TemporaryStorageData",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.TemporaryStorage.TemporaryStorageData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/TemporaryStorage/TemporaryStorageQuery

```json
{
  "tags": [
    "TemporaryStorage"
  ],
  "summary": "暂存query",
  "operationId": "TemporaryStorage_TemporaryStorageQuery",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "TemporaryStorageData",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.TemporaryStorage.TemporaryStorageData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[UFIDA.U9.ISV.BC.RestSV.Model.TemporaryStorage.TemporaryStorageReturnData]]"
      }
    }
  }
}
```

## POST /webapi/TransferApply/Create

```json
{
  "tags": [
    "TransferApply"
  ],
  "summary": "新增调拨申请单服务",
  "operationId": "TransferApply_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调拨申请单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.TransferApplyRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferApply/Submit

```json
{
  "tags": [
    "TransferApply"
  ],
  "summary": "提交调拨申请单服务",
  "operationId": "TransferApply_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调拨申请单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferApply/Approve

```json
{
  "tags": [
    "TransferApply"
  ],
  "summary": "审核调拨申请单服务",
  "operationId": "TransferApply_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调拨申请单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferApply/UnApprove

```json
{
  "tags": [
    "TransferApply"
  ],
  "summary": "弃审调拨申请单服务",
  "operationId": "TransferApply_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调拨申请单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferApply/Delete

```json
{
  "tags": [
    "TransferApply"
  ],
  "summary": "删除调拨申请单服务",
  "operationId": "TransferApply_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调拨申请单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferForm/Create

```json
{
  "tags": [
    "TransferForm"
  ],
  "summary": "新增形态转换单服务",
  "operationId": "TransferForm_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "形态转换单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.TransferFormRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferForm/Submit

```json
{
  "tags": [
    "TransferForm"
  ],
  "summary": "提交形态转换单服务",
  "operationId": "TransferForm_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "形态转换单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferForm/Approve

```json
{
  "tags": [
    "TransferForm"
  ],
  "summary": "审核形态转换单服务",
  "operationId": "TransferForm_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "形态转换单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferForm/UnApprove

```json
{
  "tags": [
    "TransferForm"
  ],
  "summary": "弃审形态转换单服务",
  "operationId": "TransferForm_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "形态转换单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferForm/Delete

```json
{
  "tags": [
    "TransferForm"
  ],
  "summary": "删除形态转换单服务",
  "operationId": "TransferForm_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "形态转换单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferIn/CreateTransferInBySrcTransferOut

```json
{
  "tags": [
    "TransferIn"
  ],
  "summary": "新增有来源创建调入单",
  "operationId": "TransferIn_CreateTransferInBySrcTransferOut",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createTransOutBySrcTransferInDTOs",
      "in": "body",
      "description": "根据来源创建调入单DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.INV.RestSV.Model.INV.CreateTransInBySrcTransOut"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferIn/Create

```json
{
  "tags": [
    "TransferIn"
  ],
  "summary": "创建调入单",
  "operationId": "TransferIn_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "transferInData",
      "in": "body",
      "description": "调入单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.TransferInRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferIn/Submit

```json
{
  "tags": [
    "TransferIn"
  ],
  "summary": "提交调入单",
  "operationId": "TransferIn_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferIn/Approve

```json
{
  "tags": [
    "TransferIn"
  ],
  "summary": "审核调入单",
  "operationId": "TransferIn_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferIn/UnApprove

```json
{
  "tags": [
    "TransferIn"
  ],
  "summary": "弃审调入单",
  "operationId": "TransferIn_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferIn/Delete

```json
{
  "tags": [
    "TransferIn"
  ],
  "summary": "删除调入单",
  "operationId": "TransferIn_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDatas",
      "in": "body",
      "description": "内部结算清单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferOut/CreateTransOutBySrcTransferApply

```json
{
  "tags": [
    "TransferOut"
  ],
  "summary": "新增有来源创建调出单",
  "operationId": "TransferOut_CreateTransOutBySrcTransferApply",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "createTransOutBySrcTransferApplyDTOs",
      "in": "body",
      "description": "根据来源创建销退收货DTOs",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.INV.RestSV.Model.INV.CreateTransOutBySrcTransApply"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferOut/Create

```json
{
  "tags": [
    "TransferOut"
  ],
  "summary": "创建调出单服务",
  "operationId": "TransferOut_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.RestSV.Model.SCM.INV.TransferOutRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferOut/Submit

```json
{
  "tags": [
    "TransferOut"
  ],
  "summary": "提交调出单服务",
  "operationId": "TransferOut_Submit",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferOut/Approve

```json
{
  "tags": [
    "TransferOut"
  ],
  "summary": "审核调出单服务",
  "operationId": "TransferOut_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferOut/UnApprove

```json
{
  "tags": [
    "TransferOut"
  ],
  "summary": "弃审调出单服务",
  "operationId": "TransferOut_UnApprove",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransferOut/Delete

```json
{
  "tags": [
    "TransferOut"
  ],
  "summary": "删除调出单服务",
  "operationId": "TransferOut_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "调出单头集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/TransOutDoc/Query

```json
{
  "tags": [
    "TransOutDoc"
  ],
  "summary": "查询调出单服务",
  "operationId": "TransOutDoc_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "rtgDatas",
      "in": "body",
      "description": "查询调出单参数集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/UbfCache/Clear

```json
{
  "tags": [
    "UbfCache"
  ],
  "summary": "clear specified cache",
  "operationId": "UbfCache_Clear",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "model",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Runtime.Caching.ClearCacheModel"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## POST /webapi/UbfCache/ClearAll

```json
{
  "tags": [
    "UbfCache"
  ],
  "summary": "clear all cache\r\nonly manager's cache",
  "operationId": "UbfCache_ClearAll",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "model",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Runtime.Caching.ClearAllCacheModel"
      }
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.String]"
      }
    }
  }
}
```

## POST /webapi/UOM/Create

```json
{
  "tags": [
    "UOM"
  ],
  "summary": "创建计量单位",
  "operationId": "UOM_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "uomDatas",
      "in": "body",
      "description": "计量单位集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.UOM.UOMDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/UOM/Modify

```json
{
  "tags": [
    "UOM"
  ],
  "summary": "修改计量单位",
  "operationId": "UOM_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "uomDatas",
      "in": "body",
      "description": "计量单位集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.UOM.UOMDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/UOM/Delete

```json
{
  "tags": [
    "UOM"
  ],
  "summary": "删除计量单位",
  "operationId": "UOM_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "uomDatas",
      "in": "body",
      "description": "计量单位集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.UOM.DeleteUOMDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/UOM/Query

```json
{
  "tags": [
    "UOM"
  ],
  "summary": "查询计量单位",
  "operationId": "UOM_Query",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "uomDatas",
      "in": "body",
      "description": "计量单位集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.UOM.QueryUOMDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.CBO.UOM.UOMDTORData]]"
      }
    }
  }
}
```

## POST /webapi/UploadFile/UploadFileDatas

```json
{
  "tags": [
    "UploadFile"
  ],
  "summary": "上传文件接口",
  "operationId": "UploadFile_UploadFileDatas",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "UploadFiles",
      "in": "body",
      "description": "上传文件参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.Upload.AttachmentFile"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/UploadFile/UploadRemoveFileDatas

```json
{
  "tags": [
    "UploadFile"
  ],
  "summary": "上传文件删除接口",
  "operationId": "UploadFile_UploadRemoveFileDatas",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "handlers",
      "in": "body",
      "description": "上传文件删除参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/UploadFile/UploadDocFile

```json
{
  "tags": [
    "UploadFile"
  ],
  "summary": "上传文件单据接口",
  "operationId": "UploadFile_UploadDocFile",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "uploadFile",
      "in": "body",
      "description": "上传文件单据参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.Upload.UploadFile"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.Common.CommonReturnData[System.Object]]"
      }
    }
  }
}
```

## POST /webapi/UserInfo/Create

```json
{
  "tags": [
    "UserInfo"
  ],
  "summary": "创建用户",
  "operationId": "UserInfo_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.UserInfoDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/UserInfo/Modify

```json
{
  "tags": [
    "UserInfo"
  ],
  "summary": "修改用户",
  "operationId": "UserInfo_Modify",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.UserInfoDTORData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/UserInfo/Delete

```json
{
  "tags": [
    "UserInfo"
  ],
  "summary": "删除用户",
  "operationId": "UserInfo_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.DeleteUserInfoDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ValueSetDef/QueryPage

```json
{
  "tags": [
    "ValueSetDef"
  ],
  "summary": "查询值集",
  "operationId": "ValueSetDef_QueryPage",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ValueSetDef.QueryPageValueSetDefDTOData"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.CommonResultDTORData]"
      }
    }
  }
}
```

## POST /webapi/ValueSetDef/Create

```json
{
  "tags": [
    "ValueSetDef"
  ],
  "summary": "新增值集",
  "operationId": "ValueSetDef_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "dto",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.CBO.ValueSetDef.CreateValueSetDefDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/ValueSetDef/Delete

```json
{
  "tags": [
    "ValueSetDef"
  ],
  "summary": "删除值集",
  "operationId": "ValueSetDef_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "data",
      "in": "body",
      "description": "删除参数(支持ID,CODE)",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.CommonArchiveDataDTOData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Verification/Create

```json
{
  "tags": [
    "Verification"
  ],
  "summary": "创建核销单",
  "operationId": "Verification_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "verificationDocDatas",
      "in": "body",
      "description": "核销单集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PM.RestSV.Model.SCM.VerificationDocData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Voucher/Create

```json
{
  "tags": [
    "Voucher"
  ],
  "summary": "创建凭证",
  "operationId": "Voucher_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.U9RestSV.Model.GL.VoucherRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.FI.RestSV.Business.GL.ResultDTOVData]]"
      }
    }
  }
}
```

## POST /webapi/Voucher/Delete

```json
{
  "tags": [
    "Voucher"
  ],
  "summary": "删除凭证",
  "operationId": "Voucher_Delete",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDocRDatas",
      "in": "body",
      "description": "凭证集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Voucher/Approve

```json
{
  "tags": [
    "Voucher"
  ],
  "operationId": "Voucher_Approve",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDocRDatas",
      "in": "body",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.PUB.RestSV.Model.Pub.OptDocRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/Voucher/DeleteVoucherForYYC

```json
{
  "tags": [
    "Voucher"
  ],
  "summary": "删除凭证For费控",
  "operationId": "Voucher_DeleteVoucherForYYC",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "ysid",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.U9RestSV.Model.GL.YYCDelP"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.FI.RestSV.Common.Util.ResultDeleteForYYCData"
      }
    }
  }
}
```

## POST /webapi/Voucher/QueryVoucherMapForYYC

```json
{
  "tags": [
    "Voucher"
  ],
  "summary": "U9费控凭证线索查询",
  "operationId": "Voucher_QueryVoucherMapForYYC",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "optDocRDatas",
      "in": "body",
      "description": "查询参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.U9RestSV.Model.GL.YYCQueryParam"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.U9RestSV.Model.GL.YYCQueryReturnDTO"
      }
    }
  }
}
```

## POST /webapi/WorkCenterOperationRpt/Create

```json
{
  "tags": [
    "WorkCenterOperationRpt"
  ],
  "summary": "创建工作中心工序报告",
  "operationId": "WorkCenterOperationRpt_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "datas",
      "in": "body",
      "description": "",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.SFC.WorkCenterOperationRpt.WorkCenterOperationRptRData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTORData]]"
      }
    }
  }
}
```

## POST /webapi/WorkingHoursDataDI/Create

```json
{
  "tags": [
    "WorkingHoursDataDI"
  ],
  "summary": "新增工时数据接口数据",
  "operationId": "WorkingHoursDataDI_Create",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "workingHoursDatas",
      "in": "body",
      "description": "工时数据集合",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/UFIDA.U9.ISV.MFG.RestSV.Model.MDCI.WorkingHoursDataDIData"
        }
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[System.Collections.Generic.List[UFIDA.U9.ISV.PUB.RestSV.Model.Pub.ResultDTOData]]"
      }
    }
  }
}
```

## POST /webapi/YDBPreview/YDBPreviewDatas

```json
{
  "tags": [
    "YDBPreview"
  ],
  "summary": "预览接口",
  "operationId": "YDBPreview_YDBPreviewDatas",
  "conn": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml",
    "application/x-www-form-urlencoded"
  ],
  "proo": [
    "application/json",
    "text/json",
    "application/xml",
    "text/xml"
  ],
  "parameters": [
    {
      "name": "previewParam",
      "in": "body",
      "description": "预览参数",
      "required": true,
      "schema": {
        "$ref": "#/components/schemas/UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.YDBPreviewParam"
      }
    },
    {
      "name": "token",
      "in": "header",
      "description": "安全",
      "required": true,
      "type": "string"
    }
  ],
  "responses": {
    "200": {
      "description": "OK",
      "schema": {
        "$ref": "#/components/schemas/UFSoft.UBF.MVC.Common.ApiResult[UFIDA.U9.ISV.BC.RestSV.Model.PrintCommon.ResponseInfo]"
      }
    }
  }
}
```
<!-- End of generated operation index. -->
