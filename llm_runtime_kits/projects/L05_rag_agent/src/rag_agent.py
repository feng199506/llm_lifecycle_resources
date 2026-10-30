#!/usr/bin/env python3
"""Local RAG + one calculator tool. Mock by default. Not executed this round."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def embed(text: str) -> list[int]:
    h = hashlib.sha256(text.encode()).digest()
    return list(h[:16])


def dist(a: list[int], b: list[int]) -> int:
    return sum(x != y for x, y in zip(a, b))


def load_chunks() -> list[dict]:
    docs = ROOT / "fixtures/docs"
    out = []
    for p in docs.glob("*.md"):
        t = p.read_text(encoding="utf-8")
        for i, para in enumerate(t.split("\n\n")):
            para = para.strip()
            if para:
                out.append({"id": f"{p.name}#{i}", "text": para, "vec": embed(para)})
    return out


def calculator(expr: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not expr or set(expr) - allowed:
        return "error: only digits and + - * /"
    return str(eval(expr, {"__builtins__": {}}, {}))  # noqa: S307  # tiny sandbox for demo arithmetic


def mock_answer(q: str, hits: list[dict]) -> dict:
    if any(ch.isdigit() for ch in q) and any(op in q for op in "+*/"):
        return {"thought": "算一下", "action": "calculator", "args": {"expr": "1+1"}, "answer": ""}
    cite = hits[0]["id"] if hits else ""
    return {"thought": "引用本地块", "action": "finish", "answer": f"{hits[0]['text'][:120] if hits else 'no hit'} [{cite}]"}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--q", default="KV cache 是什么？")
    args = p.parse_args()
    chunks = load_chunks()
    qv = embed(args.q)
    hits = sorted(chunks, key=lambda c: dist(qv, c["vec"]))[:2]
    step = mock_answer(args.q, hits)
    obs = None
    if step["action"] == "calculator":
        obs = calculator(step["args"]["expr"])
        step["answer"] = f"calc={obs}"
    rec = {"query": args.q, "hits": [h["id"] for h in hits], "step": step, "obs": obs, "embed": "sha256-prefix-not-semantic", "verified": False}
    print(json.dumps(rec, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
