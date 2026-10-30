#!/usr/bin/env python3
"""Download LLM full-lifecycle literature, pinned sources, docs, and wheels.

Model WEIGHT files are never downloaded: only Hugging Face / official URLs
are recorded. Tokenizers and configs may still be fetched.

Root: /root/llm_lifecycle_resources
Collection only: no install, no training, no serving. Resume-safe.
Retrieval date: 2026-10-30.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

LIB = Path("/root/llm_lifecycle_resources")
PYROOT = Path("/root/linux_python_offline_resources")
AGENT = Path("/root/ai_agent_resources")
PIP_PYZ = LIB / "scripts" / "pip.pyz"
CACHE = LIB / "state" / "pip_cache"
LOG = LIB / "state" / "logs" / "llm_topic"
UA = "llm-lifecycle-resources/2026-10-30"
RETRIEVED = "2026-10-30"

TOPIC = LIB / "llm_lifecycle"
PAPERS = LIB / "_public" / "papers" / "llm"
LOCAL_PAPERS = LIB / "_local_only" / "papers" / "llm"
SRC = TOPIC / "implementations"
DOCS = TOPIC / "docs_html"
EVALS = TOPIC / "experiments"
KITS = LIB / "llm_runtime_kits"
FAIL = LIB / "inventories" / "llm_download_failures_cn.csv"
OKCSV = LIB / "inventories" / "llm_downloads_cn.csv"
AGENT_MODELS = AGENT / "agent_runtime_kits" / "models" / "cpu_baseline"
AGENT_LLAMA = AGENT / "agent_runtime_kits" / "runtimes" / "linux_x86_64" / "llama_cpp"

LINUX_PLATS = [
    "manylinux2014_x86_64",
    "manylinux_2_17_x86_64",
    "manylinux_2_24_x86_64",
    "manylinux_2_27_x86_64",
    "manylinux_2_28_x86_64",
    "manylinux_2_31_x86_64",
    "manylinux_2_34_x86_64",
    "manylinux_2_35_x86_64",
    "linux_x86_64",
    "any",
]

# arXiv id, short name, topic bucket, note
PAPER_SEED = [
    ("1706.03762", "Attention_is_All_You_Need", "architecture", "Transformer"),
    ("1412.6980", "Adam", "math", "Adam optimizer"),
    ("1508.07909", "BPE", "math", "byte-pair encoding"),
    ("1808.06226", "SentencePiece", "math", "SentencePiece"),
    ("1607.06450", "LayerNorm", "architecture", "Layer Normalization"),
    ("1910.07467", "RMSNorm", "architecture", "RMSNorm"),
    ("2002.05202", "GLU_variants", "architecture", "SwiGLU"),
    ("2104.09864", "RoFormer", "architecture", "RoPE"),
    ("2108.12409", "ALiBi", "architecture", "ALiBi"),
    ("2305.13245", "GQA", "architecture", "grouped-query attention"),
    ("2205.14135", "FlashAttention", "architecture", "FlashAttention"),
    ("2307.08691", "FlashAttention2", "architecture", "FlashAttention-2"),
    ("2101.03961", "Switch_Transformer", "architecture", "MoE Switch"),
    ("2401.04088", "Mixtral", "architecture", "Mixtral of Experts"),
    ("2309.00071", "YaRN", "architecture", "YaRN long context"),
    ("2005.14165", "GPT3", "series", "GPT-3"),
    ("1810.04805", "BERT", "architecture", "BERT"),
    ("2001.08361", "Kaplan_scaling", "pretrain", "Kaplan scaling laws"),
    ("2203.15556", "Chinchilla", "pretrain", "Hoffmann Chinchilla"),
    ("2204.02311", "PaLM", "pretrain", "PaLM"),
    ("2302.13971", "LLaMA", "series", "LLaMA 1"),
    ("2307.09288", "Llama2", "series", "Llama 2"),
    ("2407.21783", "Llama3", "series", "Llama 3"),
    ("2203.02155", "InstructGPT", "posttrain", "InstructGPT / RLHF"),
    ("2106.09685", "LoRA", "posttrain", "LoRA"),
    ("2305.14314", "QLoRA", "posttrain", "QLoRA"),
    ("2305.18290", "DPO", "posttrain", "DPO"),
    ("1707.06347", "PPO", "posttrain", "PPO"),
    ("2212.08073", "Constitutional_AI", "posttrain", "Constitutional AI"),
    ("2212.10560", "Self_Instruct", "posttrain", "Self-Instruct"),
    ("2402.03300", "DeepSeekMath", "posttrain", "GRPO in DeepSeekMath"),
    ("1503.02531", "Distillation", "posttrain", "Hinton distillation"),
    ("1909.08053", "MegatronLM", "distributed", "Megatron-LM"),
    ("1910.02054", "ZeRO", "distributed", "ZeRO"),
    ("1811.06965", "GPipe", "distributed", "GPipe"),
    ("2006.16668", "GShard", "distributed", "GShard"),
    ("2309.06180", "vLLM_PagedAttention", "inference", "PagedAttention"),
    ("2211.17192", "Speculative_decoding", "inference", "Leviathan speculative"),
    ("2210.17323", "GPTQ", "inference", "GPTQ"),
    ("2306.00978", "AWQ", "inference", "AWQ"),
    ("2211.10438", "SmoothQuant", "inference", "SmoothQuant"),
    ("2401.10774", "Medusa", "inference", "Medusa"),
    ("2107.03374", "HumanEval", "eval", "HumanEval"),
    ("2110.14168", "GSM8K", "eval", "GSM8K"),
    ("2009.03300", "MMLU", "eval", "MMLU"),
    ("2211.09110", "HELM", "eval", "HELM"),
    ("2306.05685", "LLM_as_judge", "eval", "MT-Bench / LLM-as-judge"),
    ("2109.07958", "TruthfulQA", "eval", "TruthfulQA"),
    ("2303.08774", "GPT4", "series", "GPT-4 technical report"),
    ("2312.11805", "Gemini", "series", "Gemini 1"),
    ("2403.05530", "Gemini_1_5", "series", "Gemini 1.5"),
    ("2507.06261", "Gemini_2_5", "series", "Gemini 2.5"),
    ("2403.08295", "Gemma", "series", "Gemma 1"),
    ("2408.00118", "Gemma2", "series", "Gemma 2"),
    ("2503.19786", "Gemma3", "series", "Gemma 3"),
    ("2310.06825", "Mistral7B", "series", "Mistral 7B"),
    ("2306.11644", "Phi1", "series", "Phi-1"),
    ("2404.14219", "Phi3", "series", "Phi-3"),
    ("2412.08905", "Phi4", "series", "Phi-4"),
    ("2309.16609", "Qwen", "series", "Qwen"),
    ("2407.10671", "Qwen2", "series", "Qwen2"),
    ("2412.15115", "Qwen2_5", "series", "Qwen2.5"),
    ("2505.09388", "Qwen3", "series", "Qwen3"),
    ("2401.14196", "DeepSeekCoder", "series", "DeepSeek-Coder"),
    ("2405.04434", "DeepSeekV2", "series", "DeepSeek-V2 MLA/MoE"),
    ("2412.19437", "DeepSeekV3", "series", "DeepSeek-V3"),
    ("2501.12948", "DeepSeekR1", "series", "DeepSeek-R1 GRPO"),
    ("2403.17201", "InternLM2", "series", "InternLM2"),
    ("2406.12793", "ChatGLM", "series", "GLM / ChatGLM related"),
    ("2508.06471", "GLM45", "series", "GLM-4.5 if present"),
    ("2507.20534", "KimiK2", "series", "Kimi K2 if present"),
    ("2401.06954", "MiniMax", "series", "MiniMax related if present"),
    ("2005.11401", "RAG", "production", "Lewis RAG; also in agent topic"),
    ("2404.16130", "GraphRAG", "production", "GraphRAG; also in agent topic"),
    ("2302.13971", "LLaMA_dup", "skip", "duplicate guard unused"),
]

# drop the accidental duplicate sentinel
PAPER_SEED = [p for p in PAPER_SEED if p[1] != "LLaMA_dup"]

VENDOR_PDF = [
    ("https://cdn.openai.com/gpt-5-system-card.pdf", "openai_gpt5_system_card.pdf", "OpenAI GPT-5 system card 2025-08-13"),
    ("https://cdn.openai.com/gpt-4o-system-card.pdf", "openai_gpt4o_system_card.pdf", "OpenAI GPT-4o system card 2024-08-08"),
    ("https://cdn.openai.com/o1-system-card-20241205.pdf", "openai_o1_system_card.pdf", "OpenAI o1 system card 2024-12-05"),
    ("https://cdn.openai.com/papers/gpt-4-system-card.pdf", "openai_gpt4_system_card.pdf", "GPT-4 system card alt URL"),
    ("https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/Claude_4_System_Card.pdf", "anthropic_claude4_system_card.pdf", "Claude Opus 4 / Sonnet 4 May 2025"),
    ("https://www-cdn.anthropic.com/c7822cdc35ad788ec87e14b3a9d45010f1f86c38.pdf", "anthropic_claude35_addendum.pdf", "Claude 3.5 Haiku/Sonnet addendum"),
    ("https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3.pdf", "anthropic_claude3_model_card.pdf", "Claude 3 model card"),
]

SOURCE_SEED = [
    ("karpathy/nanoGPT", "master", "MIT", "from-scratch GPT training"),
    ("karpathy/minGPT", "master", "MIT", "minimal GPT"),
    ("huggingface/transformers", "v4.51.3", "Apache-2.0", "transformers pin; fallback latest"),
    ("huggingface/trl", "v0.16.1", "Apache-2.0", "TRL SFT/DPO/PPO/GRPO"),
    ("huggingface/peft", "v0.15.2", "Apache-2.0", "LoRA/QLoRA"),
    ("huggingface/accelerate", "v1.6.0", "Apache-2.0", "accelerate"),
    ("deepspeedai/DeepSpeed", "v0.16.7", "Apache-2.0", "ZeRO / DeepSpeed"),
    ("NVIDIA/Megatron-LM", "core_r0.12.0", "BSD-3", "Megatron-LM"),
    ("vllm-project/vllm", "v0.8.5", "Apache-2.0", "vLLM PagedAttention"),
    ("sgl-project/sglang", "v0.4.6", "Apache-2.0", "SGLang"),
    ("ggml-org/llama.cpp", "b11998", "MIT", "llama.cpp; binaries already in agent kits"),
    ("hiyouga/LLaMA-Factory", "v0.9.3", "Apache-2.0", "LLaMA-Factory"),
    ("axolotl-ai-cloud/axolotl", "v0.8.1", "Apache-2.0", "Axolotl"),
    ("unslothai/unsloth", "August-2025-v2", "Apache-2.0", "Unsloth; tag probed"),
    ("EleutherAI/lm-evaluation-harness", "v0.4.8", "MIT", "lm-eval"),
    ("dottxt-ai/outlines", "0.2.3", "Apache-2.0", "structured generation"),
    ("Dao-AILab/flash-attention", "v2.7.4.post1", "BSD-3", "FlashAttention"),
    ("bitsandbytes-foundation/bitsandbytes", "0.45.5", "MIT", "bitsandbytes"),
    ("volcengine/verl", "v0.4.1", "Apache-2.0", "verl RL post-training"),
    ("OpenRLHF/OpenRLHF", "v0.6.3", "Apache-2.0", "OpenRLHF"),
    ("deepseek-ai/DeepSeek-V3", "main", "MIT code / model license weights", "DeepSeek-V3 inference code"),
    ("deepseek-ai/DeepSeek-R1", "main", "MIT", "DeepSeek-R1"),
    ("QwenLM/Qwen3", "main", "Apache-2.0", "Qwen3 official repo"),
    ("QwenLM/Qwen2.5", "main", "Apache-2.0", "Qwen2.5 official repo"),
    ("meta-llama/llama-models", "main", "Llama community + code", "official Llama model cards/code; weights gated"),
    ("InternLM/InternLM", "main", "Apache-2.0", "InternLM"),
    ("THUDM/GLM-4", "main", "MIT / Apache see repo", "GLM-4"),
    ("MiniMax-AI/MiniMax-M2", "main", "Modified MIT", "MiniMax-M2"),
    ("MoonshotAI/Kimi-K2", "main", "Modified MIT", "Kimi K2"),
    ("mistralai/mistral-inference", "v1.6.0", "Apache-2.0", "Mistral inference"),
    ("microsoft/Phi-3CookBook", "main", "MIT", "Phi-3 cookbook"),
    ("huggingface/text-generation-inference", "v3.2.3", "Apache-2.0", "TGI"),
    ("openai/simple-evals", "main", "MIT", "OpenAI simple-evals"),
    ("mlc-ai/mlc-llm", "v0.19.0", "Apache-2.0", "MLC-LLM"),
    ("sgl-project/sgl-kernel", "main", "Apache-2.0", "optional; skip if huge"),
]

DOC_MIRRORS = [
    ("vllm", "https://docs.vllm.ai/en/latest/", 40),
    ("transformers", "https://huggingface.co/docs/transformers/", 40),
    ("peft", "https://huggingface.co/docs/peft/", 20),
    ("trl", "https://huggingface.co/docs/trl/", 20),
    ("deepspeed", "https://www.deepspeed.ai/", 30),
    ("qwen", "https://qwen.readthedocs.io/en/latest/", 30),
    ("llama_cpp", "https://github.com/ggml-org/llama.cpp/blob/master/README.md", 5),
    ("openai_api", "https://platform.openai.com/docs/api-reference/introduction", 20),
    ("anthropic_api", "https://docs.anthropic.com/en/api/getting-started", 20),
    ("deepseek_api", "https://api-docs.deepseek.com/", 20),
    ("gemini_api", "https://ai.google.dev/gemini-api/docs", 20),
]

DOC_PAGE_FALLBACKS = {
    "peft": [
        ("https://raw.githubusercontent.com/huggingface/peft/v0.15.2/README.md", "README.md"),
        ("https://huggingface.co/docs/peft/en/index", "en_index.html"),
        ("https://huggingface.co/docs/peft/en/quicktour", "en_quicktour.html"),
        ("https://huggingface.co/docs/peft/en/conceptual_guides/lora", "en_lora.html"),
        ("https://huggingface.co/docs/peft/en/package_reference/peft_model", "en_peft_model.html"),
        ("https://huggingface.co/docs/peft/en/developer_guides/quantization", "en_quantization.html"),
    ],
    "trl": [
        ("https://raw.githubusercontent.com/huggingface/trl/v0.16.1/README.md", "README.md"),
        ("https://huggingface.co/docs/trl/en/index", "en_index.html"),
        ("https://huggingface.co/docs/trl/en/sft_trainer", "en_sft_trainer.html"),
        ("https://huggingface.co/docs/trl/en/dpo_trainer", "en_dpo_trainer.html"),
        ("https://huggingface.co/docs/trl/en/grpo_trainer", "en_grpo_trainer.html"),
        ("https://huggingface.co/docs/trl/en/ppo_trainer", "en_ppo_trainer.html"),
    ],
    "openai_api": [
        ("https://raw.githubusercontent.com/openai/openai-python/main/README.md", "openai_python_README.md"),
        ("https://raw.githubusercontent.com/openai/openai-openapi/master/openapi.yaml", "openapi.yaml"),
        ("https://platform.openai.com/docs/api-reference/introduction", "introduction.html"),
    ],
}

DOC_TARBALL_FALLBACKS = {
    "peft": "huggingface__peft_v0.15.2.tar.gz",
    "trl": "huggingface__trl_v0.16.1.tar.gz",
}

PROJECTS = {
    "L01_tiny_transformer": {
        "title": "从零实现小型 Transformer",
        "py": ["3.10", "3.12"],
        "req": ["numpy>=1.26,<3", "torch"],
        "extra_index": "https://download.pytorch.org/whl/cpu",
        "plats": ["linux", "windows"],
    },
    "L02_sft_lora_dpo": {
        "title": "小型开放模型 SFT / LoRA / DPO",
        "py": ["3.10", "3.12"],
        "req": [
            "torch",
            "transformers>=4.44",
            "peft>=0.14",
            "trl>=0.14",
            "datasets>=3.0",
            "accelerate>=1.0",
            "safetensors",
            "sentencepiece",
            "protobuf",
        ],
        "extra_index": "https://download.pytorch.org/whl/cpu",
        "plats": ["linux", "windows"],
        "note": "训练以 Linux 为主；Windows CPU 可跑缩小示例，未验证",
    },
    "L03_quant_compare": {
        "title": "量化对比",
        "py": ["3.10", "3.12"],
        "req": ["numpy>=1.26,<3"],
        "plats": ["linux", "windows"],
        "note": "测速走 llama.cpp 二进制，不强制 llama-cpp-python",
    },
    "L04_local_serve": {
        "title": "本地模型服务、流式与结构化输出",
        "py": ["3.10", "3.12"],
        "req": [
            "fastapi>=0.115",
            "uvicorn>=0.32",
            "pydantic>=2.7,<3",
            "openai>=1.54,<5",
            "httpx>=0.27",
            "python-dotenv>=1.0",
        ],
        "plats": ["linux", "windows"],
    },
    "L05_rag_agent": {
        "title": "本地文档 RAG 与工具调用 Agent",
        "py": ["3.10", "3.12"],
        "req": [
            "fastapi>=0.115",
            "uvicorn>=0.32",
            "pydantic>=2.7,<3",
            "openai>=1.54,<5",
            "httpx>=0.27",
            "numpy>=1.26,<3",
            "pypdf>=5.0",
            "python-dotenv>=1.0",
        ],
        "plats": ["linux", "windows"],
        "note": "嵌入可复用 agent_runtime_kits 的 bge-small；本轮不重复下大权重",
    },
    "L06_prod_service": {
        "title": "带评测、日志、限流、监控、版本管理的服务示例",
        "py": ["3.10", "3.12"],
        "req": [
            "fastapi>=0.115",
            "uvicorn>=0.32",
            "pydantic>=2.7,<3",
            "openai>=1.54,<5",
            "httpx>=0.27",
            "prometheus-client>=0.21",
            "python-dotenv>=1.0",
        ],
        "plats": ["linux", "windows"],
    },
}

MODELS = [
    {
        "id": "qwen25_05b_q4km",
        "tier": "cpu_baseline",
        "repo": "Qwen/Qwen2.5-0.5B-Instruct-GGUF",
        "file": "qwen2.5-0.5b-instruct-q4_k_m.gguf",
        "license": "Apache-2.0",
        "hw": "CPU RAM 约 1–2 GiB；本机未测。Agent 专题同样只记地址，不复制权重。",
        "fmt": "GGUF Q4_K_M",
        "ctx": "常用 4k 试跑（未测）",
        "dest": "cpu_baseline",
        "public": True,
    },
    {
        "id": "qwen25_15b_q4km",
        "tier": "cpu_baseline",
        "repo": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "file": "qwen2.5-1.5b-instruct-q4_k_m.gguf",
        "license": "Apache-2.0",
        "hw": "CPU RAM 约 3–4 GiB；本机未测",
        "fmt": "GGUF Q4_K_M",
        "ctx": "常用 4k 试跑（未测）",
        "dest": "cpu_baseline",
        "public": True,
    },
    {
        "id": "qwen25_3b_q4km",
        "tier": "cpu_baseline",
        "repo": "Qwen/Qwen2.5-3B-Instruct-GGUF",
        "file": "qwen2.5-3b-instruct-q4_k_m.gguf",
        "license": "Qwen Research（非 Apache-2.0）",
        "hw": "CPU RAM 约 5–8 GiB；本机未测",
        "fmt": "GGUF Q4_K_M",
        "ctx": "常用 4k 试跑（未测）",
        "dest": "cpu_baseline",
        "public": False,
    },
    {
        "id": "qwen3_06b_q8",
        "tier": "cpu_baseline",
        "repo": "Qwen/Qwen3-0.6B-GGUF",
        "file": "Qwen3-0.6B-Q8_0.gguf",
        "license": "Apache-2.0",
        "hw": "CPU RAM 约 1.5–2.5 GiB；官方 GGUF 目前提供 Q8_0",
        "fmt": "GGUF Q8_0",
        "ctx": "见 Qwen3 技术报告 / 模型卡；本机未测",
        "dest": "cpu_baseline",
        "public": True,
    },
    {
        "id": "tinyllama_11b_q4km",
        "tier": "cpu_baseline",
        "repo": "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
        "file": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "license": "Apache-2.0 (TinyLlama)",
        "hw": "CPU RAM 约 1.5–2.5 GiB",
        "fmt": "GGUF Q4_K_M",
        "ctx": "2048 tokens（原卡）",
        "dest": "cpu_baseline",
        "public": True,
        "alts": [
            ("TinyLlama/TinyLlama-1.1B-Chat-v1.0-GGUF", "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"),
        ],
    },
    {
        "id": "ds_r1_distill_qwen15_q4km",
        "tier": "gpu_optional",
        "repo": "bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
        "file": "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
        "license": "MIT (DeepSeek-R1 distill)",
        "hw": "CPU RAM 约 3–4 GiB 或 GPU VRAM ≥ 3 GiB；本机未测",
        "fmt": "GGUF Q4_K_M（第三方量化，非官方预量化包）",
        "ctx": "见 DeepSeek-R1 论文蒸馏设定；本机未测",
        "dest": "gpu_optional",
        "public": True,
        "alts": [
            ("unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF", "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf"),
        ],
    },
]

HF_SMALL = [
    {
        "repo": "HuggingFaceTB/SmolLM2-135M-Instruct",
        "files": [
            "config.json",
            "generation_config.json",
            "tokenizer.json",
            "tokenizer_config.json",
            "special_tokens_map.json",
            "vocab.json",
            "merges.txt",
            "README.md",
            "LICENSE",
        ],
        "weight_files": ["model.safetensors"],
        "dest": "hf_small/SmolLM2-135M-Instruct",
        "license": "Apache-2.0",
        "hw": "CPU 即可；权重约 270 MiB（卡面）。本专题不下载权重。",
        "note": "L02 LoRA/SFT 主模型。开放权重，不是完整训练过程开源。",
    },
    {
        "repo": "Qwen/Qwen2.5-0.5B-Instruct",
        "files": [
            "config.json",
            "generation_config.json",
            "tokenizer.json",
            "tokenizer_config.json",
            "vocab.json",
            "merges.txt",
            "README.md",
            "LICENSE",
        ],
        "weight_files": ["model.safetensors", "model.safetensors.index.json"],
        "dest": "hf_small/Qwen2.5-0.5B-Instruct",
        "license": "Apache-2.0",
        "hw": "HF 权重约 1 GiB（卡面）。本专题不下载权重。",
        "note": "只保存配置、分词器和权重 URL。",
    },
    {
        "repo": "Qwen/Qwen3-0.6B",
        "files": [
            "config.json",
            "generation_config.json",
            "tokenizer.json",
            "tokenizer_config.json",
            "vocab.json",
            "merges.txt",
            "README.md",
            "LICENSE",
        ],
        "dest": "tokenizers/Qwen3-0.6B",
        "license": "Apache-2.0",
        "hw": "仅配置与分词器",
        "note": "不是权重。",
    },
]


def log(msg: str) -> None:
    LOG.mkdir(parents=True, exist_ok=True)
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
    print(line, flush=True)
    (LOG / "fetch_en.log").open("a", encoding="utf-8").write(line + "\n")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def record(kind: str, name: str, status: str, path: str, source: str, note: str, size: int = 0) -> None:
    OKCSV.parent.mkdir(parents=True, exist_ok=True)
    new = not OKCSV.exists()
    with OKCSV.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["kind", "name", "status", "path", "source", "bytes", "retrieved", "note"])
        w.writerow([kind, name, status, path, source, size, RETRIEVED, note])


def fail(kind: str, name: str, source: str, reason: str) -> None:
    FAIL.parent.mkdir(parents=True, exist_ok=True)
    new = not FAIL.exists()
    with FAIL.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["kind", "name", "source", "reason", "retrieved"])
        w.writerow([kind, name, source, reason, RETRIEVED])
    log(f"FAIL {kind} {name}: {reason}")


def curl_to(url: str, dest: Path, min_bytes: int, timeout: int = 180) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size >= min_bytes:
        return True
    tmp = dest.with_suffix(dest.suffix + ".part")
    cmd = [
        "curl", "-L", "--fail", "--retry", "3", "--retry-delay", "2",
        "--connect-timeout", "20", "--max-time", str(timeout),
        "-A", UA, "-o", str(tmp), "--", url,
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0 or not tmp.exists() or tmp.stat().st_size < min_bytes:
        if tmp.exists():
            tmp.unlink()
        return False
    tmp.replace(dest)
    return True


def download(url: str, dest: Path, min_bytes: int = 64, timeout: int = 180, retries: int = 4) -> bool:
    if dest.exists() and dest.stat().st_size >= min_bytes:
        return True
    for i in range(retries):
        if curl_to(url, dest, min_bytes, timeout=timeout):
            return True
        time.sleep(2 + i * 3)
    return False


def gh_api(path: str):
    url = "https://api.github.com" + path
    dest = LOG / "gh_cache" / (path.strip("/").replace("/", "_") + ".json")
    if not download(url, dest, min_bytes=2, timeout=60):
        return None
    try:
        return json.loads(dest.read_text(encoding="utf-8"))
    except Exception as e:
        log(f"github json fail {path}: {e}")
        return None


def try_github_tarball(repo: str, ref: str, dest: Path) -> str | None:
    urls = [
        f"https://github.com/{repo}/archive/refs/tags/{ref}.tar.gz",
        f"https://codeload.github.com/{repo}/tar.gz/refs/tags/{ref}",
        f"https://github.com/{repo}/archive/{ref}.tar.gz",
        f"https://codeload.github.com/{repo}/tar.gz/{ref}",
    ]
    for u in urls:
        if download(u, dest, min_bytes=2000, timeout=180):
            head = dest.read_bytes()[:4]
            if head.startswith(b"\x1f\x8b") or head.startswith(b"PK"):
                return u
            dest.unlink(missing_ok=True)
    return None


def fetch_papers() -> None:
    PAPERS.mkdir(parents=True, exist_ok=True)
    seen = set()
    for arid, words, topic, note in PAPER_SEED:
        if arid in seen:
            continue
        seen.add(arid)
        dest = PAPERS / f"{arid.replace('.', '_')}_{words}.pdf"
        urls = [
            f"https://arxiv.org/pdf/{arid}.pdf",
            f"https://export.arxiv.org/pdf/{arid}.pdf",
            f"https://arxiv.org/pdf/{arid}v1.pdf",
        ]
        ok = False
        used = ""
        for u in urls:
            if download(u, dest, min_bytes=20_000, timeout=120):
                if dest.read_bytes()[:8].startswith(b"%PDF"):
                    ok = True
                    used = u
                    break
                dest.unlink(missing_ok=True)
        if ok:
            record("paper", arid, "ok", str(dest), used, f"{note}; topic={topic}", dest.stat().st_size)
            log(f"paper ok {arid} {dest.stat().st_size}")
        else:
            fail("paper", arid, urls[0], "download or PDF header failed")
        time.sleep(0.8)
    LOCAL_PAPERS.mkdir(parents=True, exist_ok=True)
    (LOCAL_PAPERS / "DO_NOT_PUBLISH.txt").write_text(
        "Vendor system cards for personal offline reading. Do not include in public Release.\n",
        encoding="utf-8",
    )
    for url, name, note in VENDOR_PDF:
        dest = LOCAL_PAPERS / name
        if download(url, dest, min_bytes=20_000, timeout=120):
            if dest.read_bytes()[:8].startswith(b"%PDF"):
                record("vendor_pdf", name, "ok_local_only", str(dest), url, note, dest.stat().st_size)
            else:
                dest.unlink(missing_ok=True)
                fail("vendor_pdf", name, url, "not PDF")
        else:
            fail("vendor_pdf", name, url, note)


def fetch_sources() -> None:
    SRC.mkdir(parents=True, exist_ok=True)
    for repo, tag, lic, note in SOURCE_SEED:
        slug = repo.replace("/", "__") + f"_{tag}"
        if repo == "sgl-project/sgl-kernel":
            dest = SRC / f"{slug}.url.txt"
            url = f"https://github.com/{repo}/archive/{tag}.tar.gz"
            dest.write_text(url + "\n", encoding="utf-8")
            record("source", repo, "url_only", str(dest), url, f"{lic}; {note}", 0)
            log(f"source url only {repo} {url}")
            continue
        dest = SRC / f"{slug}.tar.gz"
        used = try_github_tarball(repo, tag, dest)
        used_tag = tag
        if not used and tag not in {"main", "master"}:
            data = gh_api(f"/repos/{repo}/releases/latest")
            if isinstance(data, dict) and data.get("tag_name"):
                used_tag = data["tag_name"]
                dest = SRC / f"{repo.replace('/', '__')}_{used_tag}.tar.gz"
                used = try_github_tarball(repo, used_tag, dest)
                note = note + f"; used latest {used_tag}"
        if not used:
            for fallback in ("main", "master"):
                dest = SRC / f"{repo.replace('/', '__')}_{fallback}.tar.gz"
                used = try_github_tarball(repo, fallback, dest)
                if used:
                    note = note + f"; fell back to {fallback}"
                    break
        if used and dest.exists():
            record("source", repo, "ok", str(dest), used, f"{lic}; {note}", dest.stat().st_size)
            log(f"source ok {repo} {dest.name} {dest.stat().st_size}")
        else:
            fail("source", repo, f"github:{tag}", note)


def _docs_files(out: Path) -> list[Path]:
    return [
        p for p in out.rglob("*")
        if p.is_file() and p.suffix.lower() in {".html", ".md", ".rst", ".txt", ".yaml", ".yml"}
        and p.name not in {"_MIRROR_en.txt", "OFFICIAL_URL.txt"}
    ]


def _extract_repo_docs(tarball: Path, out: Path) -> int:
    if not tarball.is_file():
        return 0
    dest = out / "from_pinned_source"
    dest.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        ["tar", "-tzf", str(tarball)],
        capture_output=True, text=True, timeout=60,
    )
    if proc.returncode != 0:
        return 0
    members = [
        line.strip() for line in proc.stdout.splitlines()
        if "/docs/" in line or line.endswith("README.md") or "/README.md" in line
    ]
    if not members:
        return 0
    listfile = dest / "_members.txt"
    listfile.write_text("\n".join(members) + "\n", encoding="utf-8")
    subprocess.run(
        ["tar", "-xzf", str(tarball), "-C", str(dest), "--strip-components=1", "-T", str(listfile)],
        check=False, timeout=120,
    )
    return len(list(dest.rglob("*")))


def fetch_docs() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    for name, url, quota_mb in DOC_MIRRORS:
        out = DOCS / name
        out.mkdir(parents=True, exist_ok=True)
        (out / "OFFICIAL_URL.txt").write_text(url + "\n", encoding="utf-8")
        marker = out / "_MIRROR_en.txt"
        existing = _docs_files(out)
        if existing:
            if not marker.exists():
                marker.write_text(
                    f"url={url}\nretrieved={RETRIEVED}\nfiles={len(existing)}\nquota_mb={quota_mb}\nrelease=local_only\n",
                    encoding="utf-8",
                )
            record("docs", name, "ok_cached", str(out), url, f"existing mirror files={len(existing)}", 0)
            continue
        cmd = [
            "wget", "-q", "-r", "-l", "2", "-np", "-nH", "--cut-dirs=0",
            "-p", "-k", "-E",
            f"--quota={quota_mb}m",
            "--timeout=20", "--tries=2",
            "-R", "woff,woff2,ttf,mp4,webm,zip,tar,gz",
            "-U", UA, "-P", str(out), url,
        ]
        log("docs wget " + name)
        try:
            subprocess.run(cmd, check=False, timeout=240)
        except Exception as e:
            log(f"docs wget timeout/error {name}: {e}")
        for page_url, fname in DOC_PAGE_FALLBACKS.get(name, []):
            download(page_url, out / "pages" / fname, min_bytes=40, timeout=60)
        tb_name = DOC_TARBALL_FALLBACKS.get(name)
        if tb_name:
            _extract_repo_docs(SRC / tb_name, out)
        htmls = _docs_files(out)
        marker.write_text(
            f"url={url}\nretrieved={RETRIEVED}\nfiles={len(htmls)}\nquota_mb={quota_mb}\nrelease=local_only\n",
            encoding="utf-8",
        )
        if htmls:
            record("docs", name, "ok", str(out), url, f"files={len(htmls)} quota={quota_mb}m", sum(p.stat().st_size for p in htmls if p.is_file()))
        else:
            fail("docs", name, url, "no html/md files after wget and fallbacks")


def hf_url(repo: str, file: str) -> str:
    return f"https://huggingface.co/{repo}/resolve/main/{file}?download=true"


def hardlink_or_copy(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return
    try:
        os.link(src, dest)
    except OSError:
        shutil.copy2(src, dest)


WEIGHT_SUFFIXES = {".gguf", ".safetensors", ".bin", ".pt", ".pth", ".onnx", ".ckpt"}


def write_url_file(dest: Path, url: str, extra: dict | None = None) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(url.rstrip() + "\n", encoding="utf-8")
    meta = {
        "url": url,
        "retrieved": RETRIEVED,
        "downloaded": False,
        "policy": "url_only_no_weight_file",
    }
    if extra:
        meta.update(extra)
    dest.with_suffix(dest.suffix + ".json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def fetch_models() -> None:
    """Record weight URLs only. Do not download GGUF/safetensors/bin/pt."""
    catalog = []
    for m in MODELS:
        url = hf_url(m["repo"], m["file"])
        dest = KITS / "models" / m["dest"] / (m["file"] + ".url.txt")
        extra = {k: v for k, v in m.items() if k != "alts"}
        extra["alts"] = [
            {"repo": r, "file": f, "url": hf_url(r, f)} for r, f in m.get("alts", [])
        ]
        write_url_file(dest, url, extra)
        record("model_url", m["id"], "url_only", str(dest), url, m.get("hw", ""), 0)
        catalog.append({"id": m["id"], "url": url, "path": str(dest), **extra})
        log(f"model url only {m['id']} {url}")
        weight = KITS / "models" / m["dest"] / m["file"]
        if weight.exists():
            weight.unlink()
            log(f"removed weight {weight}")
    for spec in HF_SMALL:
        base = KITS / "models" / spec["dest"]
        any_ok = False
        for fn in spec["files"]:
            dest = base / fn
            url = hf_url(spec["repo"], fn)
            if Path(fn).suffix.lower() in WEIGHT_SUFFIXES:
                write_url_file(Path(str(dest) + ".url.txt"), url, {"repo": spec["repo"], "file": fn})
                record("model_url", f"{spec['repo']}/{fn}", "url_only", str(dest) + ".url.txt", url, spec["license"], 0)
                if dest.exists():
                    dest.unlink()
                continue
            if download(url, dest, min_bytes=20, timeout=180):
                any_ok = True
                record("model", f"{spec['repo']}/{fn}", "ok", str(dest), url, spec["license"], dest.stat().st_size)
            else:
                fail("model", f"{spec['repo']}/{fn}", url, "hf sidecar")
        weight_urls = []
        for fn in spec.get("weight_files", []):
            url = hf_url(spec["repo"], fn)
            dest = base / (fn + ".url.txt")
            write_url_file(dest, url, {"repo": spec["repo"], "file": fn, "license": spec["license"]})
            record("model_url", f"{spec['repo']}/{fn}", "url_only", str(dest), url, spec["license"], 0)
            weight_urls.append({"file": fn, "url": url})
            blob = base / fn
            if blob.exists():
                blob.unlink()
                log(f"removed weight {blob}")
        payload = {**spec, "retrieved": RETRIEVED, "sidecar_ok": any_ok, "downloaded_weights": False, "weight_urls": weight_urls}
        (base / "SOURCE_en.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    cat_path = KITS / "models" / "WEIGHTS_url_only.json"
    cat_path.write_text(json.dumps({"retrieved": RETRIEVED, "downloaded": False, "models": catalog}, ensure_ascii=False, indent=2), encoding="utf-8")
    (KITS / "models" / "DO_NOT_DOWNLOAD_WEIGHTS.txt").write_text(
        "This topic records official/HF URLs for weights and does not store GGUF or safetensors.\n"
        f"retrieved={RETRIEVED}\n",
        encoding="utf-8",
    )


def pip_cmd(dest: Path, py: str, platform: str) -> list[str]:
    tag = py.replace(".", "")
    cmd = [
        sys.executable, str(PIP_PYZ), "download",
        "--dest", str(dest),
        "--python-version", py,
        "--implementation", "cp",
        "--abi", f"cp{tag}",
        "--abi", "abi3",
        "--abi", "none",
        "--only-binary", ":all:",
        "--cache-dir", str(CACHE),
        "--disable-pip-version-check",
        "--timeout", "120",
        "--retries", "4",
    ]
    if platform == "linux":
        for plat in LINUX_PLATS:
            cmd.extend(["--platform", plat])
    else:
        cmd.extend(["--platform", "win_amd64", "--platform", "any"])
    return cmd


def fetch_wheels() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    LOG.mkdir(parents=True, exist_ok=True)
    for key, spec in PROJECTS.items():
        parent = spec.get("parent", key)
        for py in spec["py"]:
            reqs = spec.get("req", [])
            for platform in spec.get("plats", ["linux"]):
                envroot = KITS / "projects" / parent / "environments" / f"py{py.replace('.', '')}_{platform}"
                envroot.mkdir(parents=True, exist_ok=True)
                dest = envroot / "wheelhouse"
                dest.mkdir(parents=True, exist_ok=True)
                existing = sorted(dest.glob("*.whl"))
                lock = envroot / "requirements_lock_en.txt"
                if existing and lock.exists() and lock.stat().st_size > 1:
                    record(
                        "wheels",
                        f"{key}/{py}/{platform}",
                        "ok_cached",
                        str(dest),
                        "pypi",
                        f"n={len(existing)}",
                        sum(p.stat().st_size for p in existing),
                    )
                    log(f"wheels skip {key}/{py}/{platform} n={len(existing)}")
                    continue
                reqfile = envroot / "requirements_direct_en.txt"
                reqfile.write_text("\n".join(reqs) + "\n", encoding="utf-8")
                (envroot / "SNAPSHOT_en.txt").write_text(
                    f"project={key}\npython={py}\nplatform={platform}\nretrieved={RETRIEVED}\n"
                    f"note={spec.get('note', '')}\nstatus=downloaded_only_not_installed\n",
                    encoding="utf-8",
                )
                cmd = pip_cmd(dest, py, platform)
                extra = spec.get("extra_index")
                if extra:
                    cmd.extend(["--extra-index-url", extra])
                cmd.extend(["-r", str(reqfile)])
                logf = LOG / f"wheels_{key}_{py}_{platform}.log"
                log(" ".join(cmd))
                with logf.open("w", encoding="utf-8") as fh:
                    fh.write("$ " + " ".join(cmd) + "\n")
                    fh.flush()
                    proc = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT, text=True)
                    fh.write(f"\n[exit {proc.returncode}]\n")
                wheels = sorted(dest.glob("*.whl"))
                (envroot / "requirements_lock_en.txt").write_text("\n".join(p.name for p in wheels) + "\n", encoding="utf-8")
                inv = envroot / "wheel_inventory_cn.csv"
                with inv.open("w", encoding="utf-8", newline="") as f:
                    w = csv.writer(f)
                    w.writerow(["filename", "bytes", "sha256"])
                    for p in wheels:
                        w.writerow([p.name, p.stat().st_size, sha256(p)])
                if proc.returncode == 0 and wheels:
                    record("wheels", f"{key}/{py}/{platform}", "ok", str(dest), "pypi", f"n={len(wheels)}", sum(p.stat().st_size for p in wheels))
                else:
                    fail("wheels", f"{key}/{py}/{platform}", "pypi", f"exit={proc.returncode} wheels={len(wheels)} see {logf}")


def fetch_eval_small() -> None:
    EVALS.mkdir(parents=True, exist_ok=True)
    samples = [
        ("https://raw.githubusercontent.com/openai/human-eval/master/README.md", EVALS / "HumanEval_README.md"),
        ("https://raw.githubusercontent.com/EleutherAI/lm-evaluation-harness/main/README.md", EVALS / "lm_eval_README.md"),
        ("https://raw.githubusercontent.com/openai/simple-evals/main/README.md", EVALS / "simple_evals_README.md"),
        ("https://raw.githubusercontent.com/openai/grade-school-math/master/README.md", EVALS / "GSM8K_README.md"),
    ]
    for url, dest in samples:
        if download(url, dest, min_bytes=80, timeout=60):
            record("eval_doc", dest.name, "ok", str(dest), url, "readme only; datasets not claimed complete", dest.stat().st_size)
        else:
            fail("eval_doc", dest.name, url, "readme")


def reuse_llama_cpp_note() -> None:
    dest = KITS / "runtimes" / "linux_x86_64" / "llama_cpp"
    dest.mkdir(parents=True, exist_ok=True)
    src = AGENT_LLAMA
    (dest / "REUSE_agent_kits_en.txt").write_text(
        "Reuse llama.cpp binaries from agent_runtime_kits; do not duplicate.\n"
        f"source={src}\nretrieved={RETRIEVED}\nexecuted=no\n",
        encoding="utf-8",
    )
    if src.exists():
        for p in src.glob("*"):
            if p.is_file():
                hardlink_or_copy(p, dest / p.name)
        record("runtime", "llama.cpp", "hardlink", str(dest), str(src), "reuse agent kits", 0)
    else:
        fail("runtime", "llama.cpp", str(src), "agent runtime missing")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "stage",
        nargs="?",
        default="all",
        choices=["all", "papers", "sources", "docs", "runtimes", "models", "wheels", "eval"],
    )
    args = p.parse_args()
    LOG.mkdir(parents=True, exist_ok=True)
    stage = args.stage
    log(f"start stage={stage} root={LIB}")
    if stage in ("all", "papers"):
        fetch_papers()
    if stage in ("all", "sources"):
        fetch_sources()
    if stage in ("all", "docs"):
        fetch_docs()
    if stage in ("all", "eval"):
        fetch_eval_small()
    if stage in ("all", "runtimes"):
        reuse_llama_cpp_note()
    if stage in ("all", "models"):
        fetch_models()
    if stage in ("all", "wheels"):
        fetch_wheels()
    log(f"done stage={stage}")


if __name__ == "__main__":
    main()
