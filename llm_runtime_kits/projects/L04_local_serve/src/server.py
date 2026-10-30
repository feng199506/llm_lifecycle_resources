"""OpenAI-compatible subset. Not started this round."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "shared"))
from local_openai_en import client_kwargs, model_name  # noqa: E402

app = FastAPI(title="L04 local serve", version="0.1.0-unverified")
SCHEMA = {
    "type": "object",
    "properties": {"answer": {"type": "string"}, "confidence": {"type": "number"}},
    "required": ["answer"],
}


class ChatReq(BaseModel):
    messages: list[dict] = Field(default_factory=list)
    stream: bool = False
    structured: bool = False


def mock_text(messages: list[dict]) -> str:
    last = messages[-1]["content"] if messages else ""
    return json.dumps({"answer": f"mock:{last[:80]}", "confidence": 0.0}, ensure_ascii=False)


@app.get("/health")
def health() -> dict:
    return {"ok": True, "mode": os.environ.get("LLM_MODE", "mock"), "verified": False}


@app.post("/v1/chat/completions")
def chat(req: ChatReq):
    text = mock_text(req.messages)
    if client_kwargs()["mode"] != "mock":
        from openai import OpenAI

        client = OpenAI(**client_kwargs()["openai_kwargs"])
        resp = client.chat.completions.create(model=model_name(), messages=req.messages, stream=req.stream)
        if req.stream:
            def gen():
                for chunk in resp:
                    delta = chunk.choices[0].delta.content or ""
                    if delta:
                        yield f"data: {json.dumps({'content': delta})}\n\n"
                yield "data: [DONE]\n\n"
            return StreamingResponse(gen(), media_type="text/event-stream")
        text = resp.choices[0].message.content or ""
    if req.structured:
        try:
            json.loads(text)
        except json.JSONDecodeError:
            text = mock_text(req.messages)
    if req.stream:
        def gen_mock():
            for ch in text:
                yield f"data: {json.dumps({'content': ch})}\n\n"
                time.sleep(0)
            yield "data: [DONE]\n\n"
        return StreamingResponse(gen_mock(), media_type="text/event-stream")
    return {"id": "l04", "choices": [{"message": {"role": "assistant", "content": text}}]}
