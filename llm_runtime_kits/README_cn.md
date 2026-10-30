# 大模型实践运行套件

路径：`/root/llm_lifecycle_resources/llm_runtime_kits/`  
检索日 **2026-10-30**。本轮 **未安装、未训练、未启动服务**。

已有 Python 环境（`linux_python_offline_resources/environments/09_huggingface_llm_*` 等）**不能**直接当作下列项目的运行环境。每项目独立 `environments/py3xx_linux`（及可选 Windows）wheelhouse。

## 项目

| ID | 目标 | 主平台 | 权重 |
|---|---|---|---|
| L01 | 从零小型 Transformer | Linux/Windows CPU | 无（合成语料） |
| L02 | SFT / LoRA / DPO | **Linux 为主**；Windows CPU 缩小未验证 | SmolLM2-135M **仅地址** |
| L03 | 量化对比 | Linux CPU；GPU 可选 | 代表 GGUF **仅地址** |
| L04 | 本地服务、流式、结构化输出 | Linux CPU | 自备权重；默认 mock |
| L05 | 本地 RAG + 工具 Agent | Linux CPU | 默认 mock；嵌入地址见 Agent 专题 |
| L06 | 评测、日志、限流、监控、版本 | Linux/Windows 代码 | mock 或 L04 |

## 权重与运行时

- 权重：**只记 URL**，见 [`models/MODELS_cn.md`](models/MODELS_cn.md) 与 `*.url.txt`。本专题不保存 GGUF/safetensors。
- llama.cpp 二进制：可指向 `/root/ai_agent_resources/agent_runtime_kits/runtimes/`（运行时，不是权重）。

## 启动

各项目 [`README_cn.md`](README_cn.md)。先解压运行时、用该项目 wheelhouse 建 venv（本轮未做）。资源估算见各 README，条件写在文件里。
