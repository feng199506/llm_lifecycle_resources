"""OpenAI-compatible client helper. Does not load weights."""
from __future__ import annotations

import os
from typing import Any


def client_kwargs() -> dict[str, Any]:
    base = os.environ.get("LLM_BASE_URL", "").strip()
    key = os.environ.get("LLM_API_KEY", "").strip()
    mode = os.environ.get("LLM_MODE", "mock").strip().lower()
    if mode == "mock":
        return {"mode": "mock"}
    if mode == "cloud":
        if not key:
            raise RuntimeError("cloud mode needs LLM_API_KEY")
        kw: dict[str, Any] = {"api_key": key}
        if base:
            kw["base_url"] = base
        return {"mode": "cloud", "openai_kwargs": kw}
    if not base:
        base = "http://127.0.0.1:8080/v1"
    return {
        "mode": "local",
        "openai_kwargs": {"api_key": key or "local-not-a-secret", "base_url": base},
    }


def model_name() -> str:
    return os.environ.get("LLM_MODEL", "qwen2.5-0.5b-instruct")
