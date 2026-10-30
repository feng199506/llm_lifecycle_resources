#!/usr/bin/env python3
"""Tiny DPO on synthetic pairs. Not executed. Hyperparameters are demo-only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=str(ROOT / "config/dpo.json"))
    args = p.parse_args()
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    from datasets import Dataset
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import DPOConfig, DPOTrainer

    rows = [json.loads(l) for l in (ROOT / cfg["train_file"]).read_text(encoding="utf-8").splitlines() if l.strip()]
    ds = Dataset.from_list(rows)
    tok = AutoTokenizer.from_pretrained(cfg["model_dir"])
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    base = AutoModelForCausalLM.from_pretrained(cfg["model_dir"])
    adapter = ROOT / cfg["adapter_dir"]
    model = PeftModel.from_pretrained(base, str(adapter)) if adapter.exists() else base
    out = ROOT / cfg["output_dir"]
    targs = DPOConfig(
        output_dir=str(out),
        max_steps=cfg["max_steps"],
        per_device_train_batch_size=cfg["batch_size"],
        beta=cfg["beta"],
        max_length=cfg["max_seq"],
        max_prompt_length=cfg["max_seq"] // 2,
        report_to=[],
        remove_unused_columns=False,
    )
    trainer = DPOTrainer(model=model, args=targs, train_dataset=ds, processing_class=tok)
    trainer.train()
    model.save_pretrained(out)
    print("saved", out)


if __name__ == "__main__":
    main()
