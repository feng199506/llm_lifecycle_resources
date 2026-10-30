# 覆盖度（按条目，不按下载体积）

检索日 **2026-10-30**。根目录 [`/root/llm_lifecycle_resources/`](../README_cn.md)。  
本轮：**已整理，未安装、未训练、未启动服务。** 权重只记地址，专题内 **0** 个 `.gguf` / `.safetensors`。

## 系列（13/13 导读）

| 系列 | 导读 | 论文/系统卡 | 钉死源码 | 代表权重 |
|---|---|---|---|---|
| GPT / OpenAI | 有 | 技术报告 + 4 张系统卡（`_local_only`） | 无训练实现（公开确认） | 无；API 文档有限额镜像 |
| DeepSeek | 有 | V2/V3/R1 等 arXiv | V3、R1 仓库 | R1-Distill-Qwen-1.5B **仅 URL** |
| Qwen | 有 | Qwen / 2 / 2.5 / 3 | Qwen2.5、Qwen3 仓库 | 0.5/1.5/3B GGUF、Qwen3-0.6B **仅 URL** |
| Llama | 有 | LLaMA 1/2/3 | llama-models（无门禁权重） | 不下载 |
| Claude | 有 | 3 张系统卡（`_local_only`） | 无 | 无 |
| Gemini | 有 | 1 / 1.5 / 2.5 报告 | 无 | 无 |
| Gemma | 有 | 1 / 2 / 3 | 条款见系列页 | 不下载 |
| Mistral | 有 | 7B、Mixtral | mistral-inference | 不下载大权重 |
| Phi | 有 | Phi-1/3/4 | Phi-3 CookBook | 不下载 7B+ |
| GLM | 有 | GLM 相关 arXiv | GLM-4 仓库 | 不下载大权重 |
| InternLM | 有 | InternLM2 | InternLM 仓库 | 不下载大权重 |
| MiniMax | 有 | 相关 arXiv | MiniMax-M2 | 不下载大权重 |
| Kimi | 有 | K2 相关 arXiv | Kimi-K2 | 不下载 1T 权重 |

交叉索引：[`series_index_cn.md`](series_index_cn.md)。

## 十个技术主题（10/10）

`theory/01`–`10` 均有中文导读，交叉索引见 [`topic_index_cn.md`](topic_index_cn.md)。  
公式与证据分级：`methods/`。

## 论文与系统卡

| 类别 | 条目 |
|---|---|
| 可再分发 arXiv PDF | **74**（[`_public/papers/llm/`](../_public/papers/llm/)） |
| 厂商系统卡 / 模型卡 | **7**（[`_local_only/papers/llm/`](../_local_only/papers/llm/)，不可进公开包） |

## 钉死源码

| 状态 | 条目 |
|---|---|
| GitHub tarball | **34**（`implementations/*.tar.gz`） |
| 只记地址 | sgl-kernel（[`implementations/sgl-project__sgl-kernel_main.url.txt`](implementations/sgl-project__sgl-kernel_main.url.txt)） |

清单见 [`implementations/README_cn.md`](implementations/README_cn.md)。

## 官方文档镜像（有限额；`docs_html/` 默认 local_only）

| 站点 | 离线页（html/md/rst/yaml） |
|---|---|
| vLLM | 157 |
| transformers | 174（wget 限额，不完整） |
| peft | 79（含 README / 关键页备用） |
| trl | 134（含 README / SFT·DPO·GRPO·PPO 页备用） |
| DeepSpeed | 101 |
| Qwen docs | 30 |
| llama.cpp README | 14 |
| DeepSeek API | 76 |
| Gemini API | 79 |
| Anthropic API | 1（站点多为脚本页） |
| OpenAI API | 2（Python SDK README + OpenAPI YAML；官网为脚本页） |

## 实践项目 L01–L06

| 项目 | 代码 | Linux/Windows wheel（py3.10 + py3.12） |
|---|---|---|
| L01 从零 Transformer | 有 | 各 11 个 wheel |
| L02 SFT / LoRA / DPO | 有 | 57–58 个 wheel |
| L03 量化对比 | 有 | 各 1 个（numpy）；测速依赖 llama.cpp 二进制 |
| L04 本地服务 | 有 | 各 24 个 wheel |
| L05 RAG + 工具 | 有 | 各 26 个 wheel |
| L06 生产服务示例 | 有 | 各 25 个 wheel |

环境共 **24** 套 wheelhouse，状态均为 **只下载、未安装**。

## 权重策略

代表 GGUF / HF 权重：**只写 URL**（`llm_runtime_kits/models/**/*.url.txt`，9 个地址文件 + 分词器/配置）。  
不下载 Llama / Gemma 门禁权重，不下载 70B+。

## 评测

HumanEval / GSM8K / lm-eval / simple-evals：**仅 README**。全量试题未下。

## 本轮明确不做

安装、训练、启动服务、下载权重文件、全历史尺寸、训练语料、vLLM CUDA wheel 作为默认。
