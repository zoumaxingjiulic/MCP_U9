"""Small, human-operated web console for testing the U9 read-only MCP service."""

import argparse
import json
import logging
import secrets
import sys
from typing import Any, Protocol

import httpx
import httpx2
import uvicorn
from mcp import Client
from mcp.client.streamable_http import streamable_http_client
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route
from starlette.types import ASGIApp, Receive, Scope, Send

from .config import ChatSettings, load_chat_settings

SYSTEM_PROMPT = """你是 U9 ERP 的只读查询助手。仅在需要 ERP 数据时调用提供的工具；
不要编造料品、组织、状态或接口结果。若工具返回错误或空结果，直接说明。不要尝试写入、
执行脚本、访问 URL 或使用未提供的工具。回答使用中文，并简洁说明是否调用了工具。"""


class ChatRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    message: str = Field(min_length=1, max_length=2_000)


class ConsoleService(Protocol):
    async def status(self) -> dict[str, Any]: ...

    async def answer(self, message: str) -> dict[str, Any]: ...


class U9ChatService:
    def __init__(self, settings: ChatSettings):
        self.settings = settings

    async def _model(self, messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> dict[str, Any]:
        headers = {"Authorization": f"Bearer {self.settings.dashscope_api_key.get_secret_value()}"}
        payload = {"model": self.settings.dashscope_model, "messages": messages, "tools": tools}
        async with httpx.AsyncClient(timeout=60, trust_env=False) as client:
            response = await client.post(
                f"{self.settings.dashscope_base_url}/chat/completions", headers=headers, json=payload
            )
        if response.is_error:
            raise RuntimeError(f"模型服务返回 HTTP {response.status_code}")
        try:
            body = response.json()
            return body["choices"][0]["message"]
        except (KeyError, TypeError, ValueError) as error:
            raise RuntimeError("模型服务返回了无法识别的响应") from error

    async def _with_mcp(self):
        headers = {"Authorization": f"Bearer {self.settings.mcp_access_token.get_secret_value()}"}
        http_client = httpx2.AsyncClient(headers=headers, timeout=30, trust_env=False)
        transport = streamable_http_client(self.settings.mcp_url, http_client=http_client)
        return http_client, Client(transport, read_timeout_seconds=60)

    async def status(self) -> dict[str, Any]:
        http_client, client = await self._with_mcp()
        try:
            async with http_client, client:
                tools = (await client.list_tools()).tools
                return {"model": self.settings.dashscope_model, "tools": [tool.name for tool in tools]}
        except Exception as error:
            raise RuntimeError("无法连接 MCP 服务") from error

    async def answer(self, question: str) -> dict[str, Any]:
        http_client, client = await self._with_mcp()
        messages: list[dict[str, Any]] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]
        trace: list[dict[str, Any]] = []
        try:
            async with http_client, client:
                mcp_tools = (await client.list_tools()).tools
                tools = [
                    {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description or "",
                            "parameters": tool.input_schema,
                        },
                    }
                    for tool in mcp_tools
                ]
                allowed_names = {tool.name for tool in mcp_tools}
                for _ in range(4):
                    message = await self._model(messages, tools)
                    calls = message.get("tool_calls") or []
                    messages.append(
                        {
                            "role": "assistant",
                            "content": message.get("content") or "",
                            **({"tool_calls": calls} if calls else {}),
                        }
                    )
                    if not calls:
                        return {
                            "answer": message.get("content") or "模型没有返回文本。",
                            "model": self.settings.dashscope_model,
                            "trace": trace,
                        }
                    for call in calls:
                        function = call.get("function") or {}
                        name = function.get("name")
                        call_id = call.get("id") or name or "unknown"
                        try:
                            arguments = json.loads(function.get("arguments") or "{}")
                            if name not in allowed_names or not isinstance(arguments, dict):
                                raise ValueError("模型请求了无效工具或参数")
                            result = await client.call_tool(name, arguments)
                            payload = result.structured_content
                            trace.append({"tool": name, "is_error": result.is_error, "result": payload})
                        except (ValueError, json.JSONDecodeError) as error:
                            payload = {"error": {"code": "INVALID_MODEL_TOOL_CALL", "message": str(error)}}
                            trace.append({"tool": name or "unknown", "is_error": True, "result": payload})
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": call_id,
                                "content": json.dumps(payload, ensure_ascii=False),
                            }
                        )
        except RuntimeError:
            raise
        except Exception as error:
            raise RuntimeError("MCP 工具调用失败") from error
        return {"answer": "模型连续请求工具，已达到本次最多 4 轮的限制。", "trace": trace}


class ConsoleAuthMiddleware:
    def __init__(self, app: ASGIApp, settings: ChatSettings):
        self.app = app
        self.expected = settings.chat_access_token.get_secret_value()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or not scope.get("path", "").startswith("/api/"):
            await self.app(scope, receive, send)
            return
        candidate = Request(scope, receive=receive).headers.get("x-chat-access-token", "")
        if len(candidate) > 512 or not secrets.compare_digest(candidate, self.expected):
            await JSONResponse({"error": "未授权"}, status_code=401)(scope, receive, send)
            return
        await self.app(scope, receive, send)


async def index(request: Request) -> HTMLResponse:
    return HTMLResponse(PAGE, headers={"Cache-Control": "no-store"})


def create_console_app(settings: ChatSettings, service: ConsoleService | None = None) -> Starlette:
    service = service or U9ChatService(settings)

    async def status(request: Request) -> JSONResponse:
        try:
            return JSONResponse(await service.status())
        except RuntimeError as error:
            return JSONResponse({"error": str(error)}, status_code=502)

    async def chat(request: Request) -> JSONResponse:
        try:
            payload = ChatRequest.model_validate(await request.json())
        except (ValidationError, ValueError, json.JSONDecodeError):
            return JSONResponse({"error": "问题不能为空，且最多 2000 个字符。"}, status_code=400)
        try:
            return JSONResponse(await service.answer(payload.message))
        except RuntimeError as error:
            return JSONResponse({"error": str(error)}, status_code=502)

    app = Starlette(
        routes=[
            Route("/", index),
            Route("/healthz", health),
            Route("/api/status", status),
            Route("/api/chat", chat, methods=["POST"]),
        ]
    )
    app.add_middleware(ConsoleAuthMiddleware, settings=settings)
    return app


async def health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


def main() -> None:
    parser = argparse.ArgumentParser(description="U9 MCP human test console")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8001)
    args = parser.parse_args()
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
    try:
        settings = load_chat_settings()
    except (ValidationError, ValueError):
        print("CONFIG_ERROR: 请检查 DashScope 和聊天控制台私有配置。", file=sys.stderr)
        raise SystemExit(2) from None
    uvicorn.run(
        create_console_app(settings), host=args.host, port=args.port, access_log=False, server_header=False
    )


PAGE = """<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>U9 MCP 联调控制台</title>
<style>
body{max-width:900px;margin:32px auto;padding:0 16px;background:#f7f8fa;color:#172033;font:15px system-ui,sans-serif}main{background:#fff;border:1px solid #e2e7ef;border-radius:12px;padding:24px;box-shadow:0 8px 30px #15213a0d}input,textarea,button{font:inherit;border-radius:8px;padding:10px;border:1px solid #c8d1df}input,textarea{width:100%;box-sizing:border-box;margin:6px 0 14px}textarea{height:110px;resize:vertical}button{background:#155eef;color:#fff;border:0;cursor:pointer;margin-right:8px}button:disabled{opacity:.5}#status{color:#526071}.entry{border-top:1px solid #e8ecf2;padding:16px 0;white-space:pre-wrap;line-height:1.6}.user{color:#155eef}.error{color:#b42318}pre{background:#101828;color:#e5e7eb;padding:12px;border-radius:8px;overflow:auto;font-size:12px}</style>
<main><h1>U9 MCP 联调控制台</h1><p id="status">输入控制台访问令牌后，先检查 MCP 工具，再提问。</p>
<label>控制台访问令牌<input id="token" type="password" autocomplete="off" placeholder="CHAT_ACCESS_TOKEN"></label>
<button id="check">检查 MCP 连接</button><label>问题<textarea id="question" placeholder="例如：查询组织 XX 中料号 YY 的料品信息"></textarea></label><button id="ask">发送问题</button><section id="output"></section></main>
<script>
const el=id=>document.getElementById(id), output=el('output');el('token').value=sessionStorage.u9chat||'';
function auth(){return {'X-Chat-Access-Token':el('token').value}}
function add(kind,text){const n=document.createElement('div');n.className='entry '+kind;n.textContent=text;output.prepend(n)}
async function api(path,opts={}){sessionStorage.u9chat=el('token').value;const r=await fetch(path,{...opts,headers:{...auth(),...(opts.headers||{})}});const b=await r.json();if(!r.ok)throw Error(b.error||('HTTP '+r.status));return b}
el('check').onclick=async()=>{try{const b=await api('/api/status');el('status').textContent='模型：'+b.model+'；已发现工具：'+b.tools.join(', ')}catch(e){el('status').textContent='连接失败：'+e.message;el('status').className='error'}};
el('ask').onclick=async()=>{const q=el('question').value.trim();if(!q)return;el('ask').disabled=true;add('user','你：'+q);try{const b=await api('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});add('assistant','助手：'+b.answer);if(b.trace?.length){const n=document.createElement('pre');n.textContent='MCP 调用记录\n'+JSON.stringify(b.trace,null,2);output.prepend(n)}}catch(e){add('error','错误：'+e.message)}finally{el('ask').disabled=false}};
</script></html>"""
