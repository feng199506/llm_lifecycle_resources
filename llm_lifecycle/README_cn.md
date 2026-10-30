# 大模型全生命周期专题

目录：`/root/llm_lifecycle_resources/llm_lifecycle/`  
检索日：**2026-10-30**。独立专题，不与信号处理资料库或 Python wheel Release 混放。

本轮只做资料获取、源码与依赖下载、配置和文档整理：不安装、不训练、不启动服务。  
不把「开放权重」写成「完整训练过程开源」。

状态：本轮项目均为 **已整理，未运行验证**。路径见 [`PATHS_cn.md`](PATHS_cn.md)。  
运行套件：[`../llm_runtime_kits/README_cn.md`](../llm_runtime_kits/README_cn.md)。

## 覆盖范围

| 子目录 | 内容 |
|---|---|
| `series/` | 按模型系列：版本、架构、训练、推理、评测、部署 |
| `theory/` | 按技术主题：数学 → 生产评估 |
| `methods/` | 公式、证据分级、术语 |
| `implementations/` | 钉死版本源码包 |
| `docs_html/` | 官方文档有限额镜像（默认不可公开再分发） |
| `experiments/` | 评测说明；完整基准数据大多未下 |

交叉索引：[`series_index_cn.md`](series_index_cn.md) · [`topic_index_cn.md`](topic_index_cn.md) · [`learning_path_cn.md`](learning_path_cn.md) · [`licenses_cn.md`](licenses_cn.md)  
覆盖度：[`coverage_cn.md`](coverage_cn.md) · 缺口：[`missing_cn.md`](missing_cn.md)

论文：[`../_public/papers/llm/`](../_public/papers/llm/)  
系统卡：[`../_local_only/papers/llm/`](../_local_only/papers/llm/)  
清单：[`../inventories/llm_downloads_cn.csv`](../inventories/llm_downloads_cn.csv)

## 证据分级

| 标记 | 含义 |
|---|---|
| **公开确认** | 官方论文、模型卡、系统卡、LICENSE、API 文档 |
| **第三方复现** | 社区量化、框架示例、非官方复现 |
| **推测或未知** | 未公开数据配方、闭源实现、未实测延迟/显存 |

框架示例不能标成某闭源模型的真实实现。
