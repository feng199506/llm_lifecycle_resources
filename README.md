# 大模型全生命周期资料库（llm_lifecycle_resources）

覆盖大模型的数学基础、架构、数据、预训练、后训练、分布式训练、推理、服务部署、生产与评测，以及 GPT / Claude / Gemini / Gemma / Llama / Qwen / DeepSeek / Mistral / Phi / GLM / InternLM / MiniMax / Kimi 各系列；附 6 个实践项目（L01 小型 Transformer → L06 生产服务）及其 Linux / Windows 离线依赖。检索日 2026-10-30。

**本分支只含轻量文件**：中文指南（`.md` 与同名 `.html`）、项目源码与配置、清单和脚本。
全文（9 套官方文档离线镜像、74 篇论文、37 个钉死版本源码包、全部 wheel）在 Release **`llm-lifecycle-full-20261030`** 的 tar 附件里。

## 离线阅读（Windows）

1. 从 Release 下载 tar 包（只读资料下载 `…_batch001_cn_en.tar` 即可）。
2. 全部解压到同一个短路径目录，例如 `D:\llm\`（`tar -xf 文件名.tar`，或 7-Zip）。
3. 用浏览器打开 `D:\llm\index_cn.html`，不需要联网，链接可离线跳转。

详见 [`download_restore_cn.md`](download_restore_cn.md)；各文件属于哪个包见 [`archive_index_cn.csv`](archive_index_cn.csv)；发布包相对原资料库的改动见 [`windows_rename_map_cn.csv`](windows_rename_map_cn.csv)；厂商版权所有、单独打包的内容见 [`release_restricted_cn.csv`](release_restricted_cn.csv)。

入口：[`README_cn.md`](README_cn.md) → [`llm_lifecycle/README_cn.md`](llm_lifecycle/README_cn.md) → [`llm_lifecycle/learning_path_cn.md`](llm_lifecycle/learning_path_cn.md) → [`llm_runtime_kits/README_cn.md`](llm_runtime_kits/README_cn.md)。
