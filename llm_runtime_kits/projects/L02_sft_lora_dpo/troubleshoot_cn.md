# L02 排错

- 找不到模型目录：先完成 `fetch_llm_topic_en.py models`。
- CUDA / bitsandbytes 报错：本项目默认 CPU，不要启用 4bit。
- TRL API 因版本变化改参数名：以本项目 wheel 内文档为准。
- Windows 内存不足：停止；到 Linux 或减 `max_seq`。
- 不能把 loss 下降说成「复现了 Qwen 官方 SFT」。
