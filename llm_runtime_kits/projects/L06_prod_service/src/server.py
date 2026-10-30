"""Production-shaped toy service. Not started this round."""
from __future__ import annotations

import json
import threading
import time
import uuid
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from starlette.responses import Response

ROOT = Path(__file__).resolve().parents[1]
REQS = Counter("l06_requests_total", "requests", ["version", "code"])
LAT = Histogram("l06_latency_seconds", "latency")
LOCK = threading.Lock()
STATE = {"version": "v1", "inflight": 0, "tokens": 5.0, "ts": time.time()}


def load_ver(name: str) -> dict:
    return json.loads((ROOT / "config/versions" / f"{name}.json").read_text(encoding="utf-8"))


app = FastAPI(title="L06 prod toy", version="0.1.0-unverified")
LOG = ROOT / "work/service.jsonl"


class Chat(BaseModel):
    q: str


def rate_ok(max_qps: float) -> bool:
    now = time.time()
    with LOCK:
        STATE["tokens"] = min(max_qps, STATE["tokens"] + (now - STATE["ts"]) * max_qps)
        STATE["ts"] = now
        if STATE["tokens"] < 1:
            return False
        STATE["tokens"] -= 1
        return True


@app.get("/health")
def health() -> dict:
    return {"version": STATE["version"], "verified": False}


@app.get("/metrics")
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/admin/rollback")
def rollback(to: str = "v1") -> dict:
    load_ver(to)
    STATE["version"] = to
    return {"version": to}


@app.post("/v1/chat")
def chat(req: Chat) -> dict:
    ver = load_ver(STATE["version"])
    if not rate_ok(ver["max_qps"]):
        REQS.labels(ver["version"], "429").inc()
        raise HTTPException(429, "rate limited")
    with LOCK:
        if STATE["inflight"] >= ver["max_inflight"]:
            REQS.labels(ver["version"], "503").inc()
            raise HTTPException(503, "queue full")
        STATE["inflight"] += 1
    t0 = time.time()
    rid = str(uuid.uuid4())
    try:
        ans = f"[{ver['model']}] " + ("2" if "1+1" in req.q.replace(" ", "") else req.q[:80])
        rec = {"request_id": rid, "q": req.q, "version": ver["version"], "ms": round((time.time() - t0) * 1000, 2)}
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        REQS.labels(ver["version"], "200").inc()
        LAT.observe(time.time() - t0)
        return {"request_id": rid, "answer": ans, "version": ver["version"]}
    finally:
        with LOCK:
            STATE["inflight"] -= 1
