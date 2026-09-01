---
title: Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents
published: 2026-08-30T09:43:08Z
authors: Zongyue Li, Chengyue Yu, Lei Zang, Chenyi Zhuang, Linjian Mo, Leilei Gan
url: http://arxiv.org/abs/2608.29685v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents

## Abstract
Early failure prediction is important for long-horizon agents, as it enables timely intervention and can reduce inference and tool-use costs. Uncertainty quantification, such as verbal confidence and perplexity, offers a promising approach to detecting agent failures; however, it has not been explored whether these signals retain their discriminative power during the intermediate stages of long-horizon execution. We evaluate mainstream uncertainty signals on deep-research tasks and find that verbal confidence reliably distinguishes failures at trajectory completion, achieving a mean AUROC of 0.85, whereas all evaluated signals offer limited predictive value earlier in execution, with none exceeding a mean AUROC of 0.60 at 50% trajectory progress. We identify an underlying mechanism explaining this gap: path switching, where agents frequently abandon their current search direction in-trajectory, breaking the link between early signal and final outcome. These findings challenge the assumption that intermediate uncertainty can reliably guide early intervention. They also motivate a practical recommendation for agent harnesses in deep-research settings: use final-step confidence to decide whether to restart, an approach that our experiments find more effective than in-trajectory intervention.

## Metadata
- **Published**: 2026-08-30T09:43:08Z
- **Authors**: Zongyue Li, Chengyue Yu, Lei Zang, Chenyi Zhuang, Linjian Mo, Leilei Gan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29685v1)