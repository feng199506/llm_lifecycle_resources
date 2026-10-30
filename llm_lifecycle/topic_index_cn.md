# 按技术主题交叉索引

从基础理论到生产应用。每章含：原论文、中文导读、关键公式、与系列/项目的交叉引用。

| 主题 | 导读 | 关键论文（公开确认） | 实践 |
|---|---|---|---|
| 1 数学与基础 | [01_math_foundations_cn.md](theory/01_math_foundations_cn.md) | Adam、BPE、SentencePiece | L01 |
| 2 模型架构 | [02_architecture_cn.md](theory/02_architecture_cn.md) | Transformer、RoPE、GQA、MoE、FlashAttention | L01 |
| 3 数据工程 | [03_data_engineering_cn.md](theory/03_data_engineering_cn.md) | 各系列技术报告中的数据节 | L01 合成语料 |
| 4 预训练 | [04_pretraining_cn.md](theory/04_pretraining_cn.md) | Kaplan、Chinchilla、Llama/Qwen/DeepSeek 报告 | L01 缩小训练 |
| 5 后训练 | [05_posttraining_cn.md](theory/05_posttraining_cn.md) | InstructGPT、LoRA、QLoRA、DPO、PPO、GRPO | L02 |
| 6 分布式与系统 | [06_distributed_cn.md](theory/06_distributed_cn.md) | Megatron、ZeRO、GPipe、GShard | 公开方案阅读 |
| 7 推理优化 | [07_inference_cn.md](theory/07_inference_cn.md) | PagedAttention、GPTQ、AWQ、speculative | L03 |
| 8 部署与服务 | [08_serving_cn.md](theory/08_serving_cn.md) | vLLM/llama.cpp/TGI 文档 | L04 |
| 9 生产应用 | [09_production_cn.md](theory/09_production_cn.md) | RAG 2005.11401；Agent 见独立专题 | L05、L06 |
| 10 评估 | [10_evaluation_cn.md](theory/10_evaluation_cn.md) | MMLU、GSM8K、HumanEval、HELM、MT-Bench | L03、L06 |

Agent 机制、工具循环、提示注入评测以 `/root/ai_agent_resources/` 为准，本专题只接生命周期接口。
