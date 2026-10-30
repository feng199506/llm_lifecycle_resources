# 下载与离线阅读说明（大模型全生命周期资料库，2026-10-30）

## 下载哪些文件

Release `llm-lifecycle-full-20261030` 中有 5 个 tar 包（不压缩，每个 ≤ 1.5 GiB，可分别解压）：

| 包 | 内容 | 约 |
|---|---|---:|
| `llm_lifecycle_resources_20261030_batch001_cn_en.tar` | **全部阅读材料**：离线首页 `index_cn.html`、中文指南（.md 与 .html）、9 套官方文档离线镜像、74 篇论文 PDF、离线公式库、清单、脚本、6 个实践项目的说明/源码/配置、小模型分词器与配置、llama.cpp 运行包，以及 26 个较小的源码包 | 0.93 GiB |
| `…_batch002_cn_en.tar` | 其余 8 个源码包（含 1.1 GB 的 Phi-3 CookBook）、L01 项目 wheel（一部分） | 1.4 GiB |
| `…_batch003_cn_en.tar` | L01–L05 项目 wheel | 1.4 GiB |
| `…_batch004_cn_en.tar` | L05/L06 项目 wheel、下载日志、pip 缓存 `state/pip_cache/` | 1.0 GiB |
| `…_restricted_cn_en.tar` | 厂商版权所有的资料：OpenAI / Anthropic 系统卡（`_local_only/`）、Anthropic 与 DeepSeek API 文档镜像，见 `release_restricted_cn.csv` | 0.14 GiB |

只想阅读：下载 batch001 即可（另加 restricted 包可看系统卡和这两家的 API 文档；不下载时首页里指向它们的链接打不开）。要做实践项目：下载全部。每个文件在哪个包里，见 `archive_index_cn.csv`。

## Windows 解压

1. 建一个**短路径**目录，例如 `D:\llm\`（个别 wheel 文件的相对路径有 180 个字符，加上长目录会超过 Windows 260 字符限制）。
2. 把所有 tar 包解压到**同一个**目录。Windows 10/11 自带 tar：

   ```
   cd /d D:\llm
   tar -xf %USERPROFILE%\Downloads\llm_lifecycle_resources_20261030_batch001_cn_en.tar
   ```

   其余包同样执行；也可用 7-Zip “解压到当前文件夹”。包之间没有重复文件，顺序随意。
3. 用浏览器（Edge / Chrome / Firefox）打开 `D:\llm\index_cn.html`。

## 离线阅读说明

- 不需要联网。首页链接到全部指南、文档镜像入口、论文 PDF、源码包、项目目录和清单。
- 每个 Markdown 指南旁都有同名 `.html`：其中的相对链接、行内路径（如 `models/MODELS_cn.md`）和有本地 PDF 的 arXiv 编号都可以点击跳到包内文件。指向包内没有的文件时显示为灰色说明文字，不会出现坏链接。
- 文档镜像（Hugging Face Transformers / PEFT / TRL、vLLM、DeepSpeed、Qwen、Gemini API、llama.cpp 等）：
  - 样式、图片、字体、公式库已下载到包内，已保存页面之间的链接改为本地相对链接；
  - 镜像中没有保存的页面，链接保留为原站网址（联网时可打开）；
  - 会在本地打开时把正文替换成“页面不存在”或空白的单页应用脚本已停用（Docusaurus、Next.js、Google devsite 加载器），正文是服务器渲染好的 HTML，内容完整；Gemini 文档里的多语言代码示例因此依次全部显示，不再是标签页；
  - llama.cpp 的 GitHub 页面只保留 GitHub 渲染好的正文，做成静态页。
- 搜索框、统计脚本、评论/反馈组件在离线时不可用，不影响阅读。
- 原资料库在 Linux 的 `/root/llm_lifecycle_resources/`；文中出现的这个路径就是解压目录本身。

## 实践项目（可选）

`llm_runtime_kits/projects/L01…L06/environments/` 下有 py310 / py312 的 Linux 和 Windows wheelhouse。Windows 示例：

```
cd /d D:\llm\llm_runtime_kits\projects\L01_tiny_transformer
py -3.12 -m venv .venv
.venv\Scripts\pip install --no-index --find-links environments\py312_windows\wheelhouse -r environments\py312_windows\requirements_direct_en.txt
```

各项目 `README_cn.md` / `troubleshoot_cn.md` 有说明；资料库作者注明这些项目 **已整理，未运行验证**。模型权重只保存了下载地址（`*.url.txt`）。

## 发布包与原资料库的差异

- 全部改动（Windows 改名、离线化修改与新增文件）逐条记录在 `windows_rename_map_cn.csv`。原资料库没有改动。
- 31 个带 `?` 的网页资源文件名改为 `_`（如 `doctools.js?v=9a2dae69` → `doctools.js_v=9a2dae69`），引用同步改写；1 个过长的字体文件名截短。
- 没有排除任何资料文件（`.git/`、`__pycache__/` 除外）。
