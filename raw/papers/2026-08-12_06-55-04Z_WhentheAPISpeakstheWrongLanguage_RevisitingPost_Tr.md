---
title: When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use
published: 2026-08-12T06:55:04Z
authors: Siddharth Chauhan, Thomas Butler, Abhishek Singhania, Pankaj Porwal, Honey Gupta
url: http://arxiv.org/abs/2608.11715v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use

## Abstract
The reliability of Large Language Models (LLMs) for API calling degrades in multilingual settings. A common failure occurs when a model selects the correct tool but generates argument values in an inconsistent language, which we term Argument Language Mismatch (ALM). Although semantically correct, such outputs are operationally invalid and not captured by standard API-calling metrics. We revisit post-training strategies for mitigating ALM and find that, in our benchmark, supervised fine-tuning (SFT) provides a strong baseline, substantially improving argument language consistency and end-to-end function call accuracy. Under consistent model selection, SFT achieves performance comparable to, and sometimes exceeding more complex reinforcement learning (RL) approaches. We further examine whether RL with structured, argument-aware rewards offers additional benefits. While methods such as Group Relative Policy Optimization (GRPO) can improve language consistency and better preserve general reasoning ability, these gains are incremental and most pronounced in generalization and multi-objective trade-offs. Overall, our results suggest that much of the performance in multilingual API grounding can be achieved through careful supervised training, with RL providing targeted rather than fundamental improvements.

## Metadata
- **Published**: 2026-08-12T06:55:04Z
- **Authors**: Siddharth Chauhan, Thomas Butler, Abhishek Singhania, Pankaj Porwal, Honey Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11715v1)