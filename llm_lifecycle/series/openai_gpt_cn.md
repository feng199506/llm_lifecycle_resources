# GPT / OpenAI（闭源 API）

检索日 **2026-10-30**。开放程度：无权重、无训练代码、无训练数据。本专题保存公开论文、系统卡、API 文档与工程示例。系统卡在 `_local_only`，**不可**打入公开 Release。  
下列实现细节若未在系统卡/论文出现，一律标 **推测或未知**。不得把 llama.cpp / vLLM 示例写成 GPT 的真实实现。

| 完整名称 | 类型 | 发布时间（公开确认） | 资料 |
|---|---|---|---|
| GPT-3 (`davinci` 等) | 基础 | 2020-05-28 论文 2005.14165 | [`_public/papers/llm/2005_14165_GPT3.pdf`](../../_public/papers/llm/2005_14165_GPT3.pdf) |
| GPT-4 | 多模态（报告） | 2023-03-27 论文 2303.08774 | 技术报告；权重未公开 |
| GPT-4o | 多模态 omni | 系统卡 2024-08-08 | [`_local_only/papers/llm/openai_gpt4o_system_card.pdf`](../../_local_only/papers/llm/openai_gpt4o_system_card.pdf) |
| OpenAI o1 / o1-mini | 推理 | 系统卡 2024-12-05 | 大规模 RL + CoT；**公开确认**来自系统卡，训练超参未知 |
| GPT-5（gpt-5-main / gpt-5-thinking） | 统一系统（快模型+思考+路由） | 介绍页 2025-08-07；系统卡 2025-08-13 | `_local_only/.../openai_gpt5_system_card.pdf` |

代码模型、结构化输出、工具调用：以检索日官方 API 文档为准（`docs_html/openai_api/`，镜像可能不完整）。  
评测：只摘系统卡/技术报告中的设定，不与开源模型分数横比。
