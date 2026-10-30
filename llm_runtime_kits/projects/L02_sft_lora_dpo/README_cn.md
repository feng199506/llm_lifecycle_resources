# L02 小型开放模型：指令微调、LoRA、偏好优化

状态：**已整理，未运行验证。**  
训练主平台：**Linux x86-64 CPU**（极慢，仅流程演示）。Windows CPU 不作为一等支持。GPU 可选但本轮未下 CUDA wheel。

模型：`HuggingFaceTB/SmolLM2-135M-Instruct`（Apache-2.0，开放权重，**不是**完整训练开源）。  
本专题只保留分词器/配置，权重地址：[`../../models/hf_small/SmolLM2-135M-Instruct/model.safetensors.url.txt`](../../models/hf_small/SmolLM2-135M-Instruct/model.safetensors.url.txt)。要跑 L02 需自行下载权重。  
估算（未测）：CPU RAM ≥ 8 GiB；勿在 8GB 机器上开大 batch。

```bash
# 未执行
.venv/bin/python src/run_sft_lora.py --config config/sft_lora.json
.venv/bin/python src/run_dpo.py --config config/dpo.json
```

数据：`fixtures/*.jsonl` 合成。细节哪些来自原论文：见专题 `theory/05_posttraining_cn.md`。TRL 默认超参是框架，不是 SmolLM2 原厂配方。
