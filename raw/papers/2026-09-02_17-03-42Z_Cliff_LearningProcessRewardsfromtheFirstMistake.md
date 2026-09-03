---
title: Cliff: Learning Process Rewards from the First Mistake
published: 2026-09-02T17:03:42Z
authors: Peixuan Han, Runhui Wang, Ketan Ramaneti, Jie Hao, Gerald Friedland, Chris Kong
url: http://arxiv.org/abs/2609.02817v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cliff: Learning Process Rewards from the First Mistake

## Abstract
Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for large language model (LLM) post-training, but its reliance on coarse outcome rewards leads to limited guidance on intermediate reasoning processes. Existing approaches such as process reward modeling and on-policy distillation introduce additional constraints, such as reliance on a specialized reward model or assuming identical reasoning patterns between teacher and student. Nevertheless, we observe that once a reasoning process first goes wrong, evaluating the subsequent reasoning provides limited additional information, as it is already conditioned on an invalid prefix. Therefore, we propose Cliff, a reward shaping strategy that utilizes an off-the-shelf LLM as a teacher to identify the first mistake in each rollout. As a result, the rollout is naturally decomposed into two parts: a correct prefix and an incorrect suffix. Cliff then converts this signal into token-level advantages, assigning positive advantages for the correct prefix and negative feedback afterward. Experiments across 12 different scenarios demonstrate that Cliff consistently improves reasoning performance, outperforming on-policy distillation by 15% and standard GRPO by 7%, even with teachers of modest capability. Furthermore, we analyse the role of ``ground truth'' in Cliff and investigate its training dynamics. These results establish Cliff as a simple, general and effective approach for improving RLVR with richer, fine-grained supervision.

## Metadata
- **Published**: 2026-09-02T17:03:42Z
- **Authors**: Peixuan Han, Runhui Wang, Ketan Ramaneti, Jie Hao, Gerald Friedland, Chris Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02817v1)