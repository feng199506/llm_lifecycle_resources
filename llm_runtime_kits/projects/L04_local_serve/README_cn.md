# L04 本地模型服务：流式与结构化输出

状态：**已整理，未启动服务。**  
默认 `LLM_MODE=mock`，无需权重。本地模式需先起 llama-server（脚本未执行）。

Linux CPU 主路径；Windows 可用 mock。GPU 见 COMPAT。

```bash
# 未执行
.venv/bin/uvicorn src.server:app --host 127.0.0.1 --port 8090
.venv/bin/python src/client_stream.py
```
