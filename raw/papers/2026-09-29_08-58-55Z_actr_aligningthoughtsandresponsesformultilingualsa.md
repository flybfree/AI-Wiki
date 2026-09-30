---
title: actr: aligning thoughts and responses for multilingual safety in reasoning llms
published: 2026-09-29T08:58:55Z
authors: Xianhui Zhang, Jian Yu, Chengyu Xie, Chenhang Cui, Shuyi Miao, Pengyang Shao, Yu Zheng, Fei Shen, Tat-Seng Chua
url: http://arxiv.org/abs/2609.37054v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# actr: aligning thoughts and responses for multilingual safety in reasoning llms

## Abstract
Ensuring the safety of reasoning large language models (LLMs) across languages is essential for their reliable deployment. However, when exposed to jailbreak attacks in non-high-resource languages, these models may generate unsafe responses even when their reasoning traces identify safety risks. To address this issue, we propose aligning cross-lingual thoughts and responses (ACTR), a framework that improves multilingual safety alignment by strengthening the use of existing safety reasoning. Specifically, we first present the think gap score (TGS) to compare the normalized contributions of reasoning traces to attention outputs during response generation across languages, and use reasoning- trace substitution to measure the cross-lingual safety gap. Next, using a corpus of jailbreak queries, we assess neuron importance through changes in response representations caused by neuron masking and compare the high-importance neuron sets obtained with reasoning enabled and disabled to identify safety think neurons that support the use of safety reasoning. Finally, we devise neuron-selective consistency optimization (NSCO), which uses a frozen judge model to reward agreement between the safety categories of reasoning traces and responses while updating only the parameters associated with the selected neurons, requiring no human-annotated responses or preference data. Across two reasoning models, ACTR achieves lower average attack success rates than the evaluated state-of-the-art methods on AdvBench-X and MultiJail, with safety gains extending to unseen languages, while preserving or improving average performance on multilingual knowledge and mathematical reasoning tasks and limiting false refusals of benign requests. Warning: this paper contains examples with unsafe content.

## Metadata
- **Published**: 2026-09-29T08:58:55Z
- **Authors**: Xianhui Zhang, Jian Yu, Chengyu Xie, Chenhang Cui, Shuyi Miao, Pengyang Shao, Yu Zheng, Fei Shen, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37054v1)