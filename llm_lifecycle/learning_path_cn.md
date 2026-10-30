# 中文学习路线

先修：线性代数与概率直觉、Python、命令行。不必先训 70B。  
大型预训练以公开方案和缩小实验为主，**不承诺**在普通电脑复现完整训练。

## 阶段 0 — 分清三件事（0.5 天）

1. 语言模型：下一个 token 的条件分布。  
2. 对齐后的助手：SFT + 偏好优化之后的行为，不等于基座。  
3. 服务：Prefill/Decode、批处理、限流、版本、成本。

读 [`theory/01_math_foundations_cn.md`](theory/01_math_foundations_cn.md) 前半与 [`licenses_cn.md`](licenses_cn.md)。  
产出：能说明某个模型是闭源 API、开放权重，还是训练代码+数据也公开。

## 阶段 1 — 数学与 Transformer（3–7 天）

读 [`theory/01_math_foundations_cn.md`](theory/01_math_foundations_cn.md)、`02_architecture_cn.md`。  
论文（公开确认）：1706.03762、RoPE、GQA、RMSNorm。  
实践：**L01** 从零实现小型 Transformer。

## 阶段 2 — 数据与预训练（3–5 天，可只读）

读 `03_data_engineering_cn.md`、`04_pretraining_cn.md`。  
论文：Kaplan / Chinchilla。完整数据配比对多数模型是 **推测或未知**。

## 阶段 3 — 后训练（4–7 天）

读 `05_posttraining_cn.md`。论文：InstructGPT、LoRA、QLoRA、DPO、PPO、DeepSeekMath（GRPO）。  
实践：**L02** 在 SmolLM2-135M 上做缩小 SFT / LoRA / DPO。训练以 **Linux** 为主。

## 阶段 4 — 推理与本地服务（3–5 天）

读 `07_inference_cn.md`、`08_serving_cn.md`。  
实践：**L03** 量化对比 → **L04** 流式与结构化输出。vLLM 主要 Linux+CUDA，本机未装。

## 阶段 5 — RAG、Agent、生产（1 周）

读 `09_production_cn.md`。Agent 细节见 `/root/ai_agent_resources/`。  
实践：**L05**、**L06**。提示注入文献只作防护，不复现攻击载荷。

## 阶段 6 — 评估（持续）

读 `10_evaluation_cn.md`。记录评测版本与条件，不直接比较不同口径分数。本轮未跑基准。
