# 8 部署与服务

## 平台支持（本专题）

| 环境 | 支持声明 |
|---|---|
| Linux x86-64 CPU | 主路径：llama.cpp CPU 二进制 + 小 GGUF；项目 wheel 按 3.10/3.12 下载 |
| Linux + NVIDIA GPU | 可选：llama.cpp CUDA 包（复用 Agent 专题若已有）；vLLM/SGLang **未安装**，源码仅供阅读。驱动/CUDA/框架须匹配，见 [`llm_runtime_kits/COMPAT_cn.md`](../../llm_runtime_kits/COMPAT_cn.md) |
| Windows x86-64 CPU | 服务示例代码可看；wheel 若下载到 `windows/`。llama.cpp win-cpu 复用 Agent 专题 |
| Windows GPU | 不作为一等支持 |
| macOS / ARM | 未覆盖 |

## 能力清单（代码已整理，未启动）

L04：本地 OpenAI 兼容反向代理、SSE 流式、JSON schema 校验。  
L06：限流、队列、版本号、回滚配置、日志字段。  
容器：[`llm_runtime_kits/containers/`](../../llm_runtime_kits/containers/) 的 Dockerfile **未构建**。

单卡/多卡：CPU 单进程；多卡张量并行属 GPU 可选文档。
