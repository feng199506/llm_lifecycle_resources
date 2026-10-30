# L06 生产服务示例：评测、日志、限流、监控、版本

状态：**已整理，未启动。** mock 后端即可阅读代码。无真实流量、无灰度集群。

| 能力 | 实现 |
|---|---|
| 日志 | JSON 行，`request_id` |
| 限流 | 进程内令牌桶 |
| 监控 | `GET /metrics` Prometheus 文本 |
| 版本 | `config/versions/*.json`，`POST /admin/rollback` |
| 评测 | [`src/eval_harness.py`](src/eval_harness.py) 对 fixture 3 题 |
| 队列 | 同步处理 + 拒绝过载（503） |

资源：CPU 很小。不要把 mock 延迟当模型 SLA。
