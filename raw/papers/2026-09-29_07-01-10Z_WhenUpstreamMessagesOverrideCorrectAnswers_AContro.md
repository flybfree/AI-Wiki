---
title: When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration
published: 2026-09-29T07:01:10Z
authors: Yaxin Gong, Gangyi Zhang, Chongming Gao, Leyang Shen, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Wenjie Wang, Xiangnan He
url: http://arxiv.org/abs/2609.36855v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration

## Abstract
Multi-agent LLM systems rely on message passing among specialized agents to accomplish complex tasks. However, an upstream agent may provide useful information or an incorrect answer that causes a downstream agent to override a correct answer supported by its own evidence. Prior work has not clearly separated the benefits of communication from the damage caused by incorrect messages. We study this problem with controlled experiments across five benchmarks and five receivers, keeping the downstream task and evidence fixed while comparing answers under three conditions: no message, the upstream agent's original message, or a message with the opposite conclusion. Our experiments reveal three key findings. First, messages often help when the downstream agent would otherwise answer incorrectly. Second, messages can also hurt: when the downstream agent would answer correctly without a message, an incorrect upstream message changes the answer in up to 32% of cases. Third, in 94% of audited harmful cases, the downstream agent copies the upstream's specific wrong answer--a pattern we term answer substitution. Removing unreliable messages recovers part of the lost accuracy, suggesting that communication should be selective based on upstream reliability and the evidence already available to the downstream agent.

## Metadata
- **Published**: 2026-09-29T07:01:10Z
- **Authors**: Yaxin Gong, Gangyi Zhang, Chongming Gao, Leyang Shen, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Wenjie Wang, Xiangnan He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36855v1)