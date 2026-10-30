#!/usr/bin/env python3
"""Offline fixture eval against a running L06 or mock. Collection round: not executed."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def mock(q: str) -> str:
    if "开放权重" in q:
        return "不等于。开放权重通常没有完整数据。"
    if "1+1" in q.replace(" ", ""):
        return "2"
    if "KV" in q:
        return "保存已计算的键和值"
    return ""


def main() -> None:
    rows = [json.loads(l) for l in (ROOT / "fixtures/eval.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    out = []
    for r in rows:
        pred = mock(r["q"])
        out.append({**r, "pred": pred, "hit": r["expect"] in pred, "eval_version": "fixture-v1", "verified": False})
    dest = ROOT / "work/eval.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("hits", sum(x["hit"] for x in out), "/", len(out), dest)


if __name__ == "__main__":
    main()
