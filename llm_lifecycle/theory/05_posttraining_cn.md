# 5 后训练

只把写进原论文/官方报告的内容标 **公开确认**。TRL/LLaMA-Factory 默认配置是框架行为。

| 方法 | 公开确认文献 | 本库实践 | 注意 |
|---|---|---|---|
| SFT | InstructGPT 2203.02155；Self-Instruct 2212.10560 | L02 合成指令 JSONL | 小模型会过拟合 |
| LoRA | 2106.09685 | L02 | 秩、α、目标模块是超参 |
| QLoRA | 2305.14314 | 文档级；CPU 套件不强制 4bit 训练 | bitsandbytes 主 Linux+CUDA |
| 偏好数据 / RM | InstructGPT | 示意成对数据 | 无人类标注库 |
| DPO | 2305.18290 | L02 缩小 | 参考模型与 β 要记录 |
| PPO | 1707.06347；RLHF 应用见 InstructGPT | 不跑全量 PPO | 价值模型、KL 系数未公开者未知 |
| GRPO | DeepSeekMath 2402.03300；R1 2501.12948 引用 | 源码包 verl/OpenRLHF | 本轮不训练 |
| 推理能力训练 | o1 系统卡；R1 论文 | 蒸馏小模型可选 | o1 实现未知 |
| 蒸馏 | Hinton 1503.02531；R1 蒸馏设定 | R1-Distill-Qwen-1.5B GGUF（第三方量化） | |
| 拒绝采样 | 多篇对齐论文提及 | 不实现完整流水线 | |

Constitutional AI 2212.08073 是 Claude 系列公开对齐方法之一，不是 Claude 4 的完整配方。
