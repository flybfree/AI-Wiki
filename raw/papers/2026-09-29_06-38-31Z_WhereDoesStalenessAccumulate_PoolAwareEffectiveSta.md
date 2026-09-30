---
title: Where Does Staleness Accumulate? Pool Aware Effective Staleness Control for Asynchronous RL in LLM Post-Training
published: 2026-09-29T06:38:31Z
authors: Chenliang Li, Neiwen Ling, Zijun Wei, Alfredo Garcia
url: http://arxiv.org/abs/2609.36830v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Does Staleness Accumulate? Pool Aware Effective Staleness Control for Asynchronous RL in LLM Post-Training

## Abstract
Fully asynchronous reinforcement learning (RL) improves resource utilization in large language model post-training by overlapping rollout generation with policy optimization, but it also introduces policy lag as trajectories are generated and queued while the trainer continues to update. We study how this lag accumulates over a trajectory's lifetime and how it can be controlled without sacrificing the wall-clock benefits of asynchronous execution. We decompose trajectory staleness into Generation Staleness, accumulated before rollout completion, and Waiting Staleness, accumulated after a completed trajectory enters the pool. Motivated by this decomposition, we introduce PACE (Pool-Aware Control of Effective Staleness). PACE converts excess pool occupancy into an adaptive rejection budget and ranks completed trajectories using an effective-staleness score that combines Waiting Staleness with prefix-aware Generation Staleness. This avoids penalizing long or interrupted rollouts solely because they span multiple policy versions. In single-turn mathematical reasoning, PACE improves the six-benchmark average validation accuracy by 18.7\% over unfiltered asynchronous RL at the same wall-clock budget and matches synchronous RL performance with 47.1\% less GPU time. PACE also improves validation performance in multi-turn tool-integrated reasoning, outperforming both synchronous and unfiltered asynchronous RL. Further experiments with the mixture-of-experts model and an alternative RL algorithm support its applicability across model architectures and training algorithms.

## Metadata
- **Published**: 2026-09-29T06:38:31Z
- **Authors**: Chenliang Li, Neiwen Ling, Zijun Wei, Alfredo Garcia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36830v1)