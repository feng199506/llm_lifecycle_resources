# L01 从零实现并训练小型 Transformer

状态：**已整理，未运行验证。**  
平台：Linux / Windows CPU。无 GPU 要求。内存估算：约 0.5–2 GiB（batch=8、seq=64、d=64，条件写在 [`config/train.json`](config/train.json)）。

## 目标

字符级分词 + 单层解码器，在 [`fixtures/corpus.txt`](fixtures/corpus.txt) 上最小化训练，理解 embedding、注意力、残差、CE loss、检查点。**不是** GPT-4/Qwen 预训练。

## 依赖

[`environments/py310_linux`](environments/py310_linux/) 或 `py312_linux`（及 windows 对应目录）。本轮只下载 wheel，未建 venv。

```bash
# 未执行。示例：
python -m venv .venv
.venv/bin/pip install --no-index --find-links environments/py312_linux/wheelhouse -r environments/py312_linux/requirements_direct_en.txt
.venv/bin/python src/train.py --config config/train.json
.venv/bin/python src/generate.py --ckpt work/ckpt.pt --prompt "hello"
```

数据来源：本目录合成英语短句，许可：与专题原创文档相同。排错：见 [`troubleshoot_cn.md`](troubleshoot_cn.md)。
