---
title: Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization
published: 2026-08-17T04:07:50Z
authors: Yixuan Wang, Yifei Chen, Haichao Zhang, Haozheng Luo, Xander Wu, Jie Ni, Yun Fu, Nuno Vasconcelos, Yijiang Li
url: http://arxiv.org/abs/2608.16072v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization

## Abstract
Reinforcement learning (RL) with group-relative advantages has become the de facto standard for post-training language model reasoners. However, when optimizing multiple reward objectives, existing methods typically scalarize the reward vector with a fixed weighted sum before group-wise standardization. We show that this design leads to two fundamental problems: rollouts with distinct reward profiles can receive identical advantages, and all objectives are optimized with fixed relative weights regardless of their current level of saturation. As a result, training continues to allocate gradient budget to already-solved objectives instead of focusing on those with greater remaining headroom. We introduce \textbf{Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization} (SA-MRPO), which standardizes each reward objective independently and adaptively discounts its contribution according to a batch-level estimate of objective saturation. This dynamically reallocates optimization effort toward under-optimized objectives while empirically maintaining performance on those that are already well satisfied. We further show that saturation-aware reweighting can reverse the sign of an update, rather than merely rescale its magnitude. Across mathematical reasoning with two- and three-objective reward combinations, SA-MRPO improves the harder correctness objective over GDPO in 12 of 15 benchmark comparisons, with gains of up to $5\%$ on AIME24. On adaptive reasoning it improves accuracy on all five benchmarks, by $3.8\%$ on average and up to $9.2 \%$ on AMC23, and on coding benchmarks it improves pass rate by up to $2.3\%$, while in all settings maintaining the easier objectives near their already satisfied levels.

## Metadata
- **Published**: 2026-08-17T04:07:50Z
- **Authors**: Yixuan Wang, Yifei Chen, Haichao Zhang, Haozheng Luo, Xander Wu, Jie Ni, Yun Fu, Nuno Vasconcelos, Yijiang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16072v1)