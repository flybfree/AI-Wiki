---
title: Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation
published: 2026-08-18T16:01:00Z
authors: Zhizhao Liu, Zhiliang Tian, Xi Wang, Zhihua Wen, Yihang Xiong, Zhiquan Lai, Dongsheng Li
url: http://arxiv.org/abs/2608.17941v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation

## Abstract
Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models but relies on costly rollout exploration. Assigning the same exploration budget to samples with different difficulty levels is inefficient: easy samples may receive redundant rollouts, whereas difficult but learnable samples may receive too little exploration. Existing adaptive schedulers address this mismatch through curriculum-based sample selection or non-uniform rollout allocation based on estimated sample difficulty. However, obtaining reliable online difficulty estimates remains challenging: dedicated probing adds substantial generation overhead, whereas history-based estimators face a cold start with no initial observations and stale feedback, and typically ignore relations among samples. To address these limitations, we propose a plug-and-play graph-based online difficulty estimator that shares rollout feedback across related samples and continuously updates their difficulty estimates, mitigating cold start and staleness without dedicated probing. Specifically, we first construct a difficulty-aware sample graph based on semantic and reasoning similarities. Based on this graph, we introduce latent difficulty states and use a Potts prior to encourage neighboring samples to share the same state. We then employ a state-level Beta-Binomial model to aggregate the rollout outcomes associated with each state. Finally, we use an online mean-field variational algorithm to continuously update the latent-state assignments and state-level difficulty as new feedback arrives. Our framework can be integrated into sample-selection and rollout-allocation schedulers, enabling difficulty-adaptive exploration without dedicated probing. Experiments across multiple base models, RL schedulers, and benchmarks demonstrate that our framework achieves better performance.

## Metadata
- **Published**: 2026-08-18T16:01:00Z
- **Authors**: Zhizhao Liu, Zhiliang Tian, Xi Wang, Zhihua Wen, Yihang Xiong, Zhiquan Lai, Dongsheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17941v1)