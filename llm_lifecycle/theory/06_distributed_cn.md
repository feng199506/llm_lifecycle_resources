# 6 分布式与系统

训练项目 **主要支持 Linux + GPU 集群**。Windows 不作为 3D 并行训练平台。本轮不启动分布式作业。

| 技术 | 文献/实现 | 作用 |
|---|---|---|
| 数据并行 | 通用 | 每卡一份模型，切 batch |
| 张量并行 | Megatron-LM 1909.08053 | 切矩阵 |
| 流水线并行 | GPipe 1811.06965 | 切层 |
| 专家并行 | GShard 2006.16668、MoE 论文 | 切专家 |
| ZeRO | 1910.02054 / DeepSpeed | 切优化器状态与梯度 |
| FSDP | PyTorch 文档 | ZeRO-3 类 |

通信（NCCL）、激活重计算、故障恢复见 DeepSpeed/Megatron 源码包与文档镜像。GPU 利用率数字若无本机 nsys 记录，不得填写。

源码：`implementations/` 中 DeepSpeed、Megatron-LM、verl、OpenRLHF tarball。
