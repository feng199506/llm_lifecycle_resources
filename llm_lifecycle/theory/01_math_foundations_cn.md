# 1 数学与基础

状态：**已整理，未运行验证。** 证据以论文为准。

## 线性代数

向量、矩阵乘法、特征值只服务于「把 token 变成向量再线性变换」。注意力里的 \(Q=XW_Q\) 是仿射映射。**公开确认**：Vaswani et al. 1706.03762。

## 概率与语言建模目标

自回归：\(p(x)=\prod_t p(x_t\mid x_{<t})\)。训练常用交叉熵 / 负对数似然 \(\mathcal{L}=-\sum_t \log p_\theta(x_t\mid x_{<t})\)。这是 **公开确认** 的标准目标；闭源模型是否另加辅助损失属于 **推测或未知**。

## 信息论

交叉熵 \(H(p,q)=-\mathbb{E}_{p}\log q\)；KL 出现在 RLHF/蒸馏。不要把「降低 loss」直接说成「降低困惑度已在业务达标」。

## 优化与自动微分

Adam（1412.6980）及其变体是公开确认的常用优化器。Llama 3 / Qwen 报告会写 AdamW 设定；Kimi K2 卡面写 Muon——以卡为准。自动微分是框架实现（PyTorch），不是模型论文的贡献。

## Tokenization 与嵌入

BPE 1508.07909、SentencePiece 1808.06226 为 **公开确认**。嵌入矩阵 \(E\in\mathbb{R}^{V\times d}\)；部分小模型 tying（Qwen2.5-0.5B 报告表：Tie Embedding = Yes）。

## 损失函数

预训练：next-token CE。SFT：同样 CE，数据换成指令对。偏好：DPO 的 logistic 目标见 2305.18290，不要把框架默认超参写成原论文唯一设定。
