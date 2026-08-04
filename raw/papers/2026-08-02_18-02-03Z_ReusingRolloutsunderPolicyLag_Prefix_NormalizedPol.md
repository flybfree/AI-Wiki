---
title: Reusing Rollouts under Policy Lag: Prefix-Normalized Policy Optimization for LLM Reinforcement Learning
published: 2026-08-02T18:02:03Z
authors: Wenhao Zhang, Yibo Xie, Rui Wang, Jiahua Yang, Lei Jiang, Zibo Yang, Yawei Wang, Jiali Xu,  jasperawang, Haoyang Long, Huan Xiong,  alantzhao
url: http://arxiv.org/abs/2608.01418v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reusing Rollouts under Policy Lag: Prefix-Normalized Policy Optimization for LLM Reinforcement Learning

## Abstract
Autoregressive rollout generation is a major computational cost in reinforcement learning for large language models. Reusing each rollout batch for additional learner updates amortizes this cost, but later updates become increasingly off-policy as the learner departs from the behavior policy. At a token position, exact off-policy correction must account for both the current action and the probability of reaching its prefix. The cumulative importance ratio provides this correction, but its product form can produce an unwieldy dynamic range. We study Prefix-Normalized Policy Optimization (PNPO), which replaces the cumulative ratio with the geometric mean of likelihood ratios along each causal prefix, preserving causal-prefix dependence at each position while compressing the log-weight scale. In controlled long-context mathematical reasoning experiments, we induce two off-policy regimes by using one or four policy-update epochs per rollout batch. PNPO does not consistently outperform GSPO with one epoch. With four epochs, it attains the highest observed Avg@32 on each benchmark; the unweighted mean of the three independently selected benchmark peaks is 50.24, 3.00 percentage points above GSPO. Under a matched 2,400-update budget, four-epoch PNPO reaches a final macro Avg@32 of 49.66 after 150 rollout batches, comparable to the 49.56 reached after 600 batches with one epoch. These results provide preliminary evidence that PNPO can be advantageous as training moves further off-policy.

## Metadata
- **Published**: 2026-08-02T18:02:03Z
- **Authors**: Wenhao Zhang, Yibo Xie, Rui Wang, Jiahua Yang, Lei Jiang, Zibo Yang, Yawei Wang, Jiali Xu,  jasperawang, Haoyang Long, Huan Xiong,  alantzhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01418v1)