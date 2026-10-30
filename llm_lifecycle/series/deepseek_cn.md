# DeepSeek（开放权重，许可分模型）

检索日 **2026-10-30**。官方组织 `deepseek-ai`。开放权重 ≠ 完整训练过程开源。

| 完整名称 | 类型 | 发布/论文 | 许可（公开确认） | 架构要点 |
|---|---|---|---|---|
| DeepSeek-V2 | 基础/对话 MoE | 论文 2405.04434（2024-05） | 见当时模型卡 | MLA + MoE |
| DeepSeek-V3-Base / V3 | 基础 / 指令 MoE 671B-A37B | 论文 2412.19437 | 代码 MIT；**权重** DeepSeek Model License | 128K 上下文 |
| DeepSeek-R1 / R1-Zero | 推理 | 论文 2501.12948（2025-01-22） | 官方卡：代码与权重 MIT | 基于 V3-Base 的 RL；R1-Zero 无 SFT 冷启动 |
| DeepSeek-R1-Distill-Qwen-1.5B | 蒸馏推理 | 同 R1 论文 | MIT | 本库可选 GPU/CPU 套件，GGUF 为**第三方量化** |
| DeepSeek-Coder / Coder-V2 | 代码 | 2401.14196 等 | 见各卡 | 代码代表 |

推理代码：`implementations/deepseek-ai__DeepSeek-V3_*.tar.gz`、`DeepSeek-R1_*.tar.gz`（下载成功才算落地）。  
部署：官方推荐 vLLM / SGLang（Linux+GPU）。本专题 CPU 路径用 llama.cpp 跑蒸馏小模型，**不能**称为 V3/R1 671B 的复现。
