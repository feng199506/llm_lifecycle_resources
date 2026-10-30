# 许可与开放程度

检索日 **2026-10-30**。再分发前逐项核对原 LICENSE。

## 三类「开放」不要混用

| 说法 | 通常包含 | 通常不包含 |
|---|---|---|
| 开放权重 | 权重、配置、分词器、推理代码 | 完整训练数据、逐步检查点、内部配比 |
| 训练代码开源 | 公开仓库中的训练/微调脚本 | 复现原厂曲线所需的全部数据与超参 |
| 闭源 API | 论文、系统卡、API 文档、示例 | 权重、训练代码、数据 |

## 代表系列（公开确认，检索日）

| 系列 | 权重许可 | 源码 | 训练数据 | 本库公开包 |
|---|---|---|---|---|
| GPT / OpenAI | 无开放权重 | 无训练实现 | 未公开 | 论文可公开；系统卡 `_local_only` |
| Claude | 无开放权重 | 无 | 未公开 | 系统卡 `_local_only` |
| Gemini | 无开放权重 | 无 | 未公开 | arXiv 技术报告可公开 |
| Gemma | Gemma Terms（非 Apache） | 部分工具 | 未公开完整数据 | 权重默认不进公开包 |
| Llama | Llama Community License（门禁、使用限制） | llama-models 等 | 未公开完整数据 | 权重默认不进公开包 |
| Qwen2.5 0.5/1.5/7/14/32B、Qwen3 | Apache-2.0（2.5-3B 为 Qwen Research，72B 为 Qwen） | 官方仓库 | 未公开完整数据 | Apache 模型可公开 |
| DeepSeek-R1 | MIT（官方卡） | MIT | 未公开完整数据 | 可公开 |
| DeepSeek-V3 权重 | DeepSeek Model License | MIT | 未公开 | 须核对 Model License |
| Mistral 7B / Mixtral | Apache-2.0（部分新模型 Modified MIT） | 推理仓库 | 未公开 | Apache 可公开 |
| Phi-3 / Phi-4 | MIT | cookbook MIT | 未公开完整数据 | 可公开 |
| GLM-4.5 | MIT（官方卡） | 见仓库 | 未公开完整数据 | 可公开 |
| InternLM3 | Apache-2.0 | Apache-2.0 | 未公开完整数据 | 可公开 |
| MiniMax-M2 | Modified MIT（超阈值需展示名称） | 同左 | 未公开完整数据 | 可公开但保留修改条款 |
| Kimi K2 | Modified MIT（超 1 亿 MAU / 2000 万美元月收需展示名称） | 同左 | 未公开完整数据 | 可公开但保留修改条款 |
| SmolLM2 / TinyLlama | Apache-2.0 | 有 | 部分公开配方 ≠ 原厂全量数据 | 可公开 |

第三方 GGUF 量化是 **第三方复现**，须同时满足基座许可与量化仓库许可。
