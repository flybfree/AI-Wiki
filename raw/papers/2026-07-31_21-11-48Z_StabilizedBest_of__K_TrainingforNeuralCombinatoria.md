---
title: Stabilized Best-of-$K$ Training for Neural Combinatorial Optimization
published: 2026-07-31T21:11:48Z
authors: Melveena Jolly, Midhun Xavier
url: http://arxiv.org/abs/2608.00296v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stabilized Best-of-$K$ Training for Neural Combinatorial Optimization

## Abstract
Leader Reward modifies POMO training to emphasize the best trajectory produced by repeated inference. We test a narrow extension: replace its binary leader/non-leader distinction with a stabilized rank signal indexed by a sampling budget $K$. With the POMO architecture, 3,050-epoch schedule, and TSP-100 test set held fixed, the Leader Reward reimplementation obtains $7.7662$ under 100-start, 8-augmentation greedy decoding, matching the reported $7.766$ at its displayed precision. Under independent sampling, the stabilized $K=8$ recipe lowers realized Best-of-8 cost in all three paired training seeds: $7.7944$ versus $7.8136$. This observation is estimation-only and decoder-specific: three seeds are below the six-seed testing floor, Leader Reward is better at sampled $K=1$, and it remains slightly better under its original augmented-greedy protocol. We make no unbiased-estimator, universal superiority, or state-of-the-art claim.

## Metadata
- **Published**: 2026-07-31T21:11:48Z
- **Authors**: Melveena Jolly, Midhun Xavier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00296v1)