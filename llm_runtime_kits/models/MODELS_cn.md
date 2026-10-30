# 权重地址（不下载文件）

检索日 **2026-10-30**。本专题 **只记录地址，不保存 GGUF / safetensors 等权重**。  
分词器与 `config.json` 可以保留。未加载、未推理。估算均为卡面/经验，本机未测。

完整 JSON 目录：[`WEIGHTS_url_only.json`](WEIGHTS_url_only.json)。每个代表模型有 `{文件名}.url.txt`（一行 URL）。

| ID | 许可 | 格式 | 量化 | 上下文 | 内存/显存估算（未测） | 地址文件 |
|---|---|---|---|---|---|---|
| Qwen2.5-0.5B-Instruct GGUF | Apache-2.0 | GGUF | Q4_K_M | 常用 4k 试跑 | CPU RAM 约 1–2 GiB | [`cpu_baseline/qwen2.5-0.5b-instruct-q4_k_m.gguf.url.txt`](cpu_baseline/qwen2.5-0.5b-instruct-q4_k_m.gguf.url.txt) |
| Qwen2.5-1.5B-Instruct GGUF | Apache-2.0 | GGUF | Q4_K_M | 同上 | 约 3–4 GiB | [`cpu_baseline/qwen2.5-1.5b-instruct-q4_k_m.gguf.url.txt`](cpu_baseline/qwen2.5-1.5b-instruct-q4_k_m.gguf.url.txt) |
| Qwen2.5-3B-Instruct GGUF | Qwen Research | GGUF | Q4_K_M | 同上 | 约 5–8 GiB | [`cpu_baseline/qwen2.5-3b-instruct-q4_k_m.gguf.url.txt`](cpu_baseline/qwen2.5-3b-instruct-q4_k_m.gguf.url.txt) |
| Qwen3-0.6B GGUF | Apache-2.0 | GGUF | Q8_0 | 见 Qwen3 报告 | 约 1.5–2.5 GiB | [`cpu_baseline/Qwen3-0.6B-Q8_0.gguf.url.txt`](cpu_baseline/Qwen3-0.6B-Q8_0.gguf.url.txt) |
| TinyLlama-1.1B-Chat GGUF | Apache-2.0 | GGUF | Q4_K_M 第三方 | 2048 | 约 1.5–2.5 GiB | [`cpu_baseline/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf.url.txt`](cpu_baseline/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf.url.txt) |
| SmolLM2-135M-Instruct | Apache-2.0 | safetensors | 原精度 | 见模型卡 | 约 0.3–1 GiB | [`hf_small/SmolLM2-135M-Instruct/model.safetensors.url.txt`](hf_small/SmolLM2-135M-Instruct/model.safetensors.url.txt) |
| Qwen2.5-0.5B-Instruct HF | Apache-2.0 | safetensors | 原精度 | 见模型卡 | 约 1 GiB | [`hf_small/Qwen2.5-0.5B-Instruct/model.safetensors.url.txt`](hf_small/Qwen2.5-0.5B-Instruct/model.safetensors.url.txt) |
| DeepSeek-R1-Distill-Qwen-1.5B GGUF | MIT | GGUF | Q4_K_M 第三方 | 见 R1 论文 | 约 3–4 GiB | [`gpu_optional/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf.url.txt`](gpu_optional/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf.url.txt) |
| Qwen3-0.6B tokenizer | Apache-2.0 | tokenizer | — | — | 很小 | [`tokenizers/Qwen3-0.6B/`](tokenizers/Qwen3-0.6B/)（已保存配置，不是权重） |

Llama / Gemma 权重同样只记系列页中的官方入口，不下载。7B+ 不收录文件。

Agent 专题 `/root/ai_agent_resources/` 同样只记权重地址，不保存 GGUF/safetensors。
