#!/usr/bin/env python3
"""Tiny LoRA-SFT. Not executed this round. Not a vendor training recipe."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=str(ROOT / "config/sft_lora.json"))
    args = p.parse_args()
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    # Imports inside main so collection machines without venv can still read the file.
    from datasets import Dataset
    from peft import LoraConfig, get_peft_model
    from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling

    rows = [json.loads(l) for l in (ROOT / cfg["train_file"]).read_text(encoding="utf-8").splitlines() if l.strip()]
    tok = AutoTokenizer.from_pretrained(cfg["model_dir"])
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    texts = [r["instruction"] + "\n" + r["output"] + (tok.eos_token or "") for r in rows]
    ds = Dataset.from_dict({"text": texts})

    def tokenize(ex):
        return tok(ex["text"], truncation=True, max_length=cfg["max_seq"])

    ds = ds.map(tokenize, batched=True, remove_columns=["text"])
    model = AutoModelForCausalLM.from_pretrained(cfg["model_dir"])
    model = get_peft_model(model, LoraConfig(r=cfg["lora_r"], lora_alpha=cfg["lora_alpha"], lora_dropout=0.05, bias="none", task_type="CAUSAL_LM"))
    out = ROOT / cfg["output_dir"]
    targs = TrainingArguments(
        output_dir=str(out),
        max_steps=cfg["max_steps"],
        per_device_train_batch_size=cfg["batch_size"],
        learning_rate=cfg["lr"],
        logging_steps=1,
        save_steps=cfg["max_steps"],
        report_to=[],
        fp16=False,
        bf16=False,
    )
    trainer = Trainer(model=model, args=targs, train_dataset=ds, data_collator=DataCollatorForLanguageModeling(tok, mlm=False))
    trainer.train()
    model.save_pretrained(out)
    tok.save_pretrained(out)
    print("saved", out)


if __name__ == "__main__":
    main()
