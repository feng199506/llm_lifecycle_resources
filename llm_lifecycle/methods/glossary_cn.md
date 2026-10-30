# 术语表

| 中文 | English | 一句话 |
|---|---|---|
| 基座模型 | base / foundation | 预训练后、未指令对齐 |
| 指令模型 | instruct / chat | SFT 及之后 |
| 开放权重 | open weights | 可下载参数；不等于数据开源 |
| 稠密 | dense | 每层全部参数参与 |
| 专家混合 | MoE | 路由到部分专家 |
| 预填充 | prefill | 提示一次性编码 |
| 解码 | decode | 逐步生成 |
| KV 缓存 | KV cache | 已算过的键值 |
| 量化 | quantization | 降精度存算 |
| 推测解码 | speculative decoding | 草稿模型 + 验证 |
| 偏好优化 | preference optimization | DPO/PPO 等 |
| 评分污染 | contamination | 评测题进了训练 |
| 系统卡 | system card | 能力与安全评估公开文档 |
