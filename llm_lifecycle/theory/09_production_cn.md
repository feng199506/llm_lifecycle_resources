# 9 生产应用

Agent 循环、MCP、浏览器工具见 `/root/ai_agent_resources/`，此处只接生命周期。

| 主题 | 公开确认 | 本库 |
|---|---|---|
| RAG | 2005.11401；综述见 Agent 专题 | L05 本地文档；hash 嵌入默认，bge 可选用 Agent 已下权重 |
| 检索与重排 | bge 模型卡 | 可选用 `ai_agent_resources` 的 bge-reranker-base |
| Agent / 工具 | 各模型工具调用卡 | L05 mock + 本地服务 |
| 提示与配置管理 | 工程实践 | L06 `config/versions/` |
| 隐私与权限 | 法规与系统卡 | 示例只处理本地 fixture |
| 提示注入 | Agent 专题文献 | 防护清单，不附攻击载荷 |
| 监控追踪 | OpenTelemetry 等 | L06 `/metrics` Prometheus 文本 |
| 灰度与成本 | 工程实践 | 配置项；无真实流量 |
| 故障排查 | 日志字段 | `troubleshoot_cn.md` |

数据不得离开本机示例目录。不要把 mock 成功率写成模型能力。
