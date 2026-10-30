# 4 预训练

## 公开确认的要素

- 初始化：常见 Xavier/正态分布小方差；具体 σ 以各报告为准。  
- 优化器：AdamW 居多；Kimi K2 卡面 Muon。  
- 学习率：warmup + cosine/WSD 等，报告级。  
- 精度：BF16/FP8 混精（DeepSeek-V3 等报告）。  
- 批量与梯度累积：全局 batch tokens 是 scaling 的关键，不是「显卡张数」。  
- 稳定性：loss spike、梯度裁剪、跳过坏 batch——工程经验 + 部分报告。  
- 检查点与恢复：Megatron/DeepSpeed 文档。  
- Scaling laws：Kaplan 2001.08361；Chinchilla 2203.15556。后续模型是否仍服从该拟合是 **不能外推为定律**。

## 算力估算（教学公式，非本机测量）

近似：\(C \approx 6ND\)（参数量 × token 数，Kaplan 量级讨论）。用于数量级，不用于报价。

## 本专题实践边界

L01 只在合成字符级语料上训一个极小 GPT。**不是** Qwen/Llama 预训练复现。完整 7B+ 预训练需要集群，普通电脑不承诺。
