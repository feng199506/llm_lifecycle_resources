# 7 推理优化

## Prefill / Decode

Prefill：整段提示一次前向，计算重、易批处理。Decode：逐步生成，易受内存带宽限制。长上下文时 KV 随 seq 线性增，成本与延迟都升——L03 用估算表，**未测**。

## 技术与文献

| 技术 | 公开确认 | 本库 |
|---|---|---|
| 动态批处理 / PagedAttention | 2309.06180 vLLM | 源码包；Linux+CUDA 为主 |
| 量化 GPTQ/AWQ/SmoothQuant | 2210.17323 / 2306.00978 / 2211.10438 | L03 对比 GGUF 档位 |
| 推测解码 | 2211.17192 | 文档；本轮不跑 |
| 前缀缓存 | vLLM/sglang 文档 | 服务配置项 |
| 结构化生成 | Outlines 等 | L04 JSON schema（规则或提示，不保证小模型遵守） |
| 工具调用 | 模型卡 + Agent 专题 | L05；小模型常失败 |

GGUF Q4_K_M 是 llama.cpp 量化，**第三方格式**，不是原厂训练精度。
