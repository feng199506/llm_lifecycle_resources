# 平台与 CUDA 兼容（文档，未实测）

检索日 **2026-10-30**。下列是根据官方文档整理的**兼容关系说明**，不是本机 `nvidia-smi` 结果。

## CPU

- Linux x86-64 glibc（参考 Ubuntu 22.04/24.04）：L01–L06 代码按此编写。
- Windows x86-64：代码与 wheel 计划提供；训练（L02）不作为一等支持。
- llama.cpp CPU 二进制：复用 Agent 专题 ubuntu-x64 / win-cpu-x64。

## GPU（可选）

| 组件 | 常见官方组合 | 本库状态 |
|---|---|---|
| NVIDIA 驱动 | 需满足所选 CUDA 运行时最低要求 | 未装、未查 |
| CUDA 12.x | PyTorch cu124 / llama.cpp cuda-12 构建常见 | 可选包若存在于 Agent 专题则硬链接；本专题不另下完整 CUDA toolkit |
| PyTorch GPU | 与 CUDA 大版本绑定 | **未下载** GPU wheel，避免与 CPU 套件混装 |
| vLLM | Linux + CUDA，Windows 官方支持弱 | 仅源码包 |
| SGLang | 同上 | 仅源码包 |
| bitsandbytes | Linux CUDA 为主 | L02 CPU 路径不依赖 |
| FlashAttention | 源码编译，Linux CUDA | 仅源码包，未编译 |

不要把 CPU torch wheel 与 cu12 wheel 装进同一 venv。
