---
title: How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning
published: 2026-08-07T11:22:09Z
authors: Lichao Ma, Yang Sun, Shuaitao Zhao, Yangyi Fang, Cong Qin, Xiaoliang Fu, Yuhang Tian, Yuchen Wei, Junbo Zhu, Yang Wei, Lu Pan, Jiaye Lin
url: http://arxiv.org/abs/2608.07118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning

## Abstract
Credit assignment in multi-turn agent reinforcement learning operates at two levels: assigning trajectory-level credit to actions and distributing each action's credit across its tokens. In this paper, we introduce FACTOR, which separates these decisions. FACTOR uses checkpoint-calibrated TD residuals to assign per-action credits that telescope to the trajectory advantage, and feedback-conditioned teacher-student likelihood gaps to allocate each credit across the realized action tokens. Per-action normalization preserves the action-average coefficient and prevents token-level sign flips. We pair this construction with an action-mean reduction, removing the implicit dependence of an action's scalar surrogate weight on its token length. At the behavior policy and before clipping, each action's inner action-mean surrogate equals its TD credit. FACTOR consistently improves over competitive baselines across ALFWorld, WebShop, and ScienceWorld, with every environment-seed comparison favoring FACTOR and the largest gains emerging on the longest-horizon environment. The same hyperparameters transfer without retuning to a larger backbone and to a different model family. Ablations identify TD action credit as the dominant driver of the improvement, with hindsight token allocation contributing complementary gains.

## Metadata
- **Published**: 2026-08-07T11:22:09Z
- **Authors**: Lichao Ma, Yang Sun, Shuaitao Zhao, Yangyi Fang, Cong Qin, Xiaoliang Fu, Yuhang Tian, Yuchen Wei, Junbo Zhu, Yang Wei, Lu Pan, Jiaye Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07118v1)