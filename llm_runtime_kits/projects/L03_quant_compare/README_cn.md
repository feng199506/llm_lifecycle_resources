# L03 量化对比

状态：**已整理，未运行验证。** 表中数字若无 `work/results.json` 实测记录，只是估算。

比较同一提示下：文件体积、估算内存、（若有 llama-cli）吞吐与延迟。质量用固定 3 条中文题的字符串匹配，**不是** MMLU。

权重档位见 [`config/models.json`](config/models.json)。对应文件是 `*.url.txt`，**本专题不保存 GGUF**。要跑对比需自行按地址下载后改 `path`。
