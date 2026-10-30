# 信息来源标记用法

全文三种标记：

1. **公开确认**：官方论文、模型卡、系统卡、LICENSE、API 文档、检索日仓库 README。  
2. **第三方复现**：GGUF 社区量化、框架默认超参、非官方基准复现。  
3. **推测或未知**：未公开数据配比、闭源内核、本机未测的延迟显存。

L01 使用 PyTorch `TransformerEncoder` + 因果 mask，这是教学近似，**不是** OpenAI/Anthropic 实现。  
vLLM 示例不能标成 DeepSeek-V3 原厂推理栈的逐行复现（即使官方推荐该引擎）。
