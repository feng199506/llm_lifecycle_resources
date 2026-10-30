#!/usr/bin/env python3
"""Train TinyGPT on the bundled corpus. Not executed in the collection round."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch

from model import Cfg, TinyGPT

ROOT = Path(__file__).resolve().parents[1]


def pack(text: str, seq: int) -> torch.Tensor:
    vocab = sorted(set(text))
    stoi = {c: i for i, c in enumerate(vocab)}
    ids = [stoi[c] for c in text]
    out = []
    for i in range(0, max(len(ids) - seq, 1), seq):
        chunk = ids[i : i + seq]
        if len(chunk) < seq:
            chunk = chunk + [0] * (seq - len(chunk))
        out.append(chunk)
    return torch.tensor(out, dtype=torch.long), vocab


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=str(ROOT / "config/train.json"))
    args = p.parse_args()
    cfgj = json.loads(Path(args.config).read_text(encoding="utf-8"))
    text = (ROOT / cfgj["corpus"]).read_text(encoding="utf-8")
    data, vocab = pack(text * 20, cfgj["seq_len"])
    model = TinyGPT(Cfg(vocab=len(vocab), seq_len=cfgj["seq_len"], d_model=cfgj["d_model"], n_head=cfgj["n_head"], n_layer=cfgj["n_layer"], d_ff=cfgj["d_ff"]))
    opt = torch.optim.AdamW(model.parameters(), lr=cfgj["lr"])
    model.train()
    for step in range(cfgj["steps"]):
        batch = data[torch.randint(0, data.size(0), (cfgj["batch_size"],))]
        loss = model.loss(batch)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if step % 20 == 0:
            print(f"step={step} loss={loss.item():.4f}", flush=True)
    ckpt = ROOT / cfgj["ckpt"]
    ckpt.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model": model.state_dict(), "vocab": vocab, "cfg": cfgj}, ckpt)
    print("wrote", ckpt)


if __name__ == "__main__":
    main()
