#!/usr/bin/env python3
"""Measure or estimate GGUF footprints. Does not claim quality scores from papers."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=str(ROOT / "config/models.json"))
    p.add_argument("--llama-cli", default=os.environ.get("LLAMA_CLI", ""))
    args = p.parse_args()
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    rows = []
    for m in cfg["models"]:
        path = (ROOT / m["path"]).resolve()
        rec = {**m, "exists": path.is_file(), "bytes": path.stat().st_size if path.is_file() else 0, "measured": False}
        cli = args.llama_cli
        if cli and path.is_file() and os.access(cli, os.X_OK):
            t0 = time.time()
            proc = subprocess.run(
                [cli, "-m", str(path), "-p", cfg["prompt"], "-n", str(cfg["n_predict"]), "-c", str(m.get("ctx", 512)), "--no-display-prompt"],
                capture_output=True, text=True, timeout=180,
            )
            rec["latency_s"] = round(time.time() - t0, 3)
            rec["returncode"] = proc.returncode
            rec["stdout_tail"] = (proc.stdout or "")[-400:]
            rec["measured"] = True
        else:
            rec["note"] = "binary missing or not executed; ram_est only"
        rows.append(rec)
    out = ROOT / "work/results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"retrieved": "2026-10-30", "verified": False, "rows": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
