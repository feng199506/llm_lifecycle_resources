"""Minimal decoder-only Transformer. Teaching code, not a vendor implementation."""
from __future__ import annotations

import math
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class Cfg:
    vocab: int
    seq_len: int = 64
    d_model: int = 64
    n_head: int = 4
    n_layer: int = 2
    d_ff: int = 256


class TinyGPT(nn.Module):
    def __init__(self, cfg: Cfg) -> None:
        super().__init__()
        self.cfg = cfg
        self.tok = nn.Embedding(cfg.vocab, cfg.d_model)
        self.pos = nn.Embedding(cfg.seq_len, cfg.d_model)
        layer = nn.TransformerEncoderLayer(
            d_model=cfg.d_model,
            nhead=cfg.n_head,
            dim_feedforward=cfg.d_ff,
            batch_first=True,
            activation="gelu",
            norm_first=True,
        )
        self.blocks = nn.TransformerEncoder(layer, num_layers=cfg.n_layer)
        self.ln = nn.LayerNorm(cfg.d_model)
        self.head = nn.Linear(cfg.d_model, cfg.vocab, bias=False)

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        b, t = idx.shape
        x = self.tok(idx) + self.pos(torch.arange(t, device=idx.device))
        causal = torch.triu(torch.ones(t, t, device=idx.device, dtype=torch.bool), 1)
        x = self.blocks(x, mask=causal)
        return self.head(self.ln(x))

    def loss(self, idx: torch.Tensor) -> torch.Tensor:
        logits = self.forward(idx[:, :-1])
        return F.cross_entropy(logits.reshape(-1, logits.size(-1)), idx[:, 1:].reshape(-1))
