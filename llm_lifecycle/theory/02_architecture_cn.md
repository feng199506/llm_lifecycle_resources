# 2 模型架构

## Transformer（公开确认：1706.03762）

编码器-解码器原文；GPT 家族用解码器 only。块结构：注意力 → 残差 → 归一化 → FFN → 残差。现代 LLM 多为 **Pre-Norm**（报告常见，具体以各卡为准）。

多头注意力：

\[
\mathrm{Attn}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
\]

## 位置编码

- 绝对正弦：原文  
- RoPE：2104.09864（RoFormer），Llama/Qwen/DeepSeek 报告广泛采用（**公开确认到报告**）  
- ALiBi：2108.12409  
- YaRN：2309.00071 长上下文外推  

## 归一化与激活

LayerNorm 1607.06450；RMSNorm 1910.07467。FFN 常用 SwiGLU（2002.05202）。GQA：2305.13245。

## Dense / MoE

Switch Transformer 2101.03961；Mixtral 2401.04088。DeepSeek-V3 / Llama 4 / MiniMax-M2 / Kimi K2 为 MoE（各卡）。路由与负载均衡损失以各论文公式为准；工程实现（Megatron/DeepSpeed）是 **第三方/框架**，不是某闭源模型源码。

## 长上下文与 KV cache

Prefill 写满 K/V；Decode 逐步追加。显存大致随 `layers × batch × seq × kv_heads × head_dim × 2(K,V) × dtype` 增长（估算，**未在本机测**）。MLA（DeepSeek-V2 论文）压缩 KV，属该系列公开确认。

## 多模态

早期融合 / 视觉编码器 + 投影 + LLM。GPT-4o、Gemini、Llama 4、Qwen-VL、Gemma 3、Pixtral、Phi-4-multimodal、GLM-4V：以各自报告为准，不要画一张「通用多模态图」当成某厂实现。
