#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import torch
import torch.nn.functional as F

from model import Cfg, TinyGPT

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--ckpt", default=str(ROOT / "work/ckpt.pt"))
    p.add_argument("--prompt", default="hello")
    p.add_argument("--n", type=int, default=80)
    args = p.parse_args()
    blob = torch.load(args.ckpt, map_location="cpu", weights_only=False)
    vocab = blob["vocab"]
    stoi = {c: i for i, c in enumerate(vocab)}
    itos = {i: c for c, i in stoi.items()}
    c = blob["cfg"]
    model = TinyGPT(Cfg(vocab=len(vocab), seq_len=c["seq_len"], d_model=c["d_model"], n_head=c["n_head"], n_layer=c["n_layer"], d_ff=c["d_ff"]))
    model.load_state_dict(blob["model"])
    model.eval()
    ids = [stoi.get(ch, 0) for ch in args.prompt]
    for _ in range(args.n):
        ctx = torch.tensor([ids[-c["seq_len"] :]], dtype=torch.long)
        logits = model(ctx)[0, -1]
        nxt = int(torch.multinomial(F.softmax(logits, dim=-1), 1))
        ids.append(nxt)
    print("".join(itos[i] for i in ids))


if __name__ == "__main__":
    main()
