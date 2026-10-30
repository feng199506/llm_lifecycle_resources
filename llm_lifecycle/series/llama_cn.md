# Llama（Meta）

检索日 **2026-10-30**。官方 `meta-llama`、`llama-models`。权重受 **Llama Community License** 约束，HF 需接受协议。本库：源码与模型卡可下；**权重默认不进公开包、本轮不下载门禁权重。**

| 完整名称 | 类型 | 发布（公开确认） | 许可 | 备注 |
|---|---|---|---|---|
| LLaMA 1 | 基础 | 论文 2302.13971（2023-02） | 当时非商业研究许可 | 历史 |
| Llama 2 | 基础/对话 | 2307.09288（2023-07） | Llama 2 Community | 7B–70B |
| Llama 3 / 3.1 | 基础/指令 | 2407.21783；3.1 含 405B | Llama 3 社区许可 | 8B 常见本地代表，本轮未下权重 |
| Llama 3.2 1B/3B | 指令（文本） | 模型卡发布 2024-10-24；许可文本日期 2024-09-25 | Llama 3.2 Community | 须接受许可后自下 |
| Llama 3.2-Vision 11B/90B | 多模态 | 同上系列 | 同上 | 不下权重 |
| Llama 4 Scout 17B×16E | 多模态 MoE | 模型卡发布 **2025-04-05** | Llama 4 Community | 109B 总参、10M 上下文（卡面） |
| Llama 4 Maverick 17B×128E | 多模态 MoE | 2025-04-05 | 同上 | 400B 总参 |
| Code Llama | 代码 | Llama 2 衍生 | 见当时许可 | 文献覆盖 |

官方代码包：`implementations/meta-llama__llama-models_*.tar.gz`。本地实验用 Apache 小模型（SmolLM2/Qwen）代替。
