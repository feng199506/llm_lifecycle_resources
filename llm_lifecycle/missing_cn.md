# 仍缺内容与未验证项

检索日 **2026-10-30**。本轮不以下载容量代替完成度。覆盖条目见 [`coverage_cn.md`](coverage_cn.md)。

## 有意不做

- **不下载模型权重**（GGUF / safetensors 等），只写官方或 Hugging Face 地址
- 不下载全系列全部历史尺寸与量化档
- 不下载 Llama / Gemma 门禁或特殊条款权重
- 不下载 70B+ / 671B / 1T 权重
- 不抓取训练网页语料
- 不安装、不训练、不启动服务
- 不把 vLLM CUDA wheel 作为默认（体积与驱动绑定）
- sgl-kernel 只记 GitHub 地址（可选、体积大）

## 镜像不完整（站点限制）

- Hugging Face `docs/transformers`：有限额 wget，约 174 页，不是全书
- OpenAI / Anthropic 文档站以脚本渲染为主：本库保存官方 URL、OpenAI OpenAPI YAML 与 Python SDK README
- SmolLM2 仓库无独立 `LICENSE` 文件（404）；许可以模型卡 / README 为准（Apache-2.0，公开确认来自卡面）

## 运行时缺口

- Windows llama.cpp 二进制未放入本专题，见 [`llm_runtime_kits/runtimes/windows_x86_64/llama_cpp/REUSE_or_url_en.txt`](../llm_runtime_kits/runtimes/windows_x86_64/llama_cpp/REUSE_or_url_en.txt)
- Windows GPU / CUDA 训练未覆盖

## 评测数据

- MMLU / HumanEval / GSM8K 全量试题未下，仅 README 与论文
- 多模态权重（VL）未下

## 清单里的过期失败行

[`inventories/llm_download_failures_cn.csv`](../inventories/llm_download_failures_cn.csv) 仍保留早先失败记录（例如 pip.pyz 一度缺失导致的 L03–L06 wheel `exit=2`）。**以目录实况为准**：上述 wheelhouse 已补齐；peft/trl 已有备用页。不要把旧 CSV 行当成当前缺口。

## 未验证

所有延迟、显存、质量分数、工具调用成功率均为 **未运行验证**。论文表格不是本机结果。
