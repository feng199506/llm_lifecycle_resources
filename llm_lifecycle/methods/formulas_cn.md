# 关键公式（教学用）

均来自公开论文；实现以 L01 代码为准，不是某闭源内核。

**交叉熵** \(\mathcal{L}=-\sum_t \log p_\theta(x_t\mid x_{<t})\)

**缩放点积注意力** \(\mathrm{softmax}(QK^\top/\sqrt{d_k})V\)  （1706.03762）

**LoRA** \(W'=W+\frac{\alpha}{r}BA\)  （2106.09685）

**DPO** 对偏好对 \((x,y_w,y_l)\) 的 logistic 目标见 2305.18290 原文式 (7)。β 是超参，不是「越大越对齐」。

**PPO 裁剪** 见 1707.06347。RLHF 还要加 KL 到参考模型（InstructGPT 叙述）。

**GRPO** 见 DeepSeekMath 2402.03300；组内相对优势，无独立 critic——以该论文为准。

**Chinchilla** 最优 token 数随参数量近似线性（2203.15556 拟合），后续模型可偏离。
