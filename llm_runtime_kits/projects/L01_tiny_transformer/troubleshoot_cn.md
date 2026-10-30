# L01 排错

- `No module named torch`：未按该项目 wheelhouse 安装；本轮未装。
- loss 不降：语料太短已在 train.py 中重复 20 次；仍可能过拟合，属预期。
- 生成乱码：字符级、步数少，**不是**失败的唯一标志。
- 不要把本模型说成 GPT 官方实现。`nn.TransformerEncoder` 是 PyTorch API，带因果 mask 的解码器近似。
