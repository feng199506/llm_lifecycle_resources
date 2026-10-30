# L06 排错

- 429：令牌桶空了，属演示。
- 503：inflight 超限。
- 回滚只改内存里的 version 指针，没有真实模型热加载。
- `/metrics` 需要 prometheus-client 已安装（本轮未装）。
