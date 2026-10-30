# Qwen（通义千问）

检索日 **2026-10-30**。官方 `Qwen` / `QwenLM`。多数开放权重为 Apache-2.0，**不是**完整数据与训练日志开源。

| 完整名称 | 类型 | 论文/时间 | 许可 | 本库权重 |
|---|---|---|---|---|
| Qwen2.5-0.5B-Instruct | 指令 | 2412.15115（2025-01-03 提交） | Apache-2.0 | GGUF/HF **只记 URL**；分词器已保存 |
| Qwen2.5-1.5B/3B-Instruct | 指令 | 同上 | 0.5/1.5B Apache；**3B 为 Qwen Research** | GGUF **只记 URL** |
| Qwen2.5-7B-Instruct | 指令 | 同上；上下文 128K | Apache-2.0 | 本轮不下载 7B，作 GPU 档说明 |
| Qwen2.5-Coder / Qwen2.5-VL | 代码 / 多模态 | 系列卡 | 见各尺寸许可 | 文献覆盖，不下全尺寸 |
| Qwen3-0.6B | 基础（含思考/非思考模式） | 2505.09388（2025-05-14） | Apache-2.0（报告称全部 Qwen3 公开 Apache-2.0） | 官方 GGUF **只记 URL**（`Qwen3-0.6B-Q8_0.gguf.url.txt`） |
| Qwen3 MoE 至 235B | 代表阅读 | 同上 | Apache-2.0 | 不下权重 |

训练：报告描述稠密+MoE、思考模式与 thinking budget。数据配比细节仍多为报告级，复现全量预训练为 **推测或未知**。  
推理：transformers / llama.cpp / vLLM。分词器单独保存在 `models/tokenizers/Qwen3-0.6B/`。
