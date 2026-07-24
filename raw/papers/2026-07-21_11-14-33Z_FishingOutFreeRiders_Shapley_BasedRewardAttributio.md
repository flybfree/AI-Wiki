---
title: Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning
published: 2026-07-21T11:14:33Z
authors: Wentao Zhang, Haoyu Zhang, Xinke Jiang, Yuxuan Cheng, Yuhan Pan, Miao Li, Zhipeng Qiao, Tao Feng, Zhen Tao, Dengji Zhao
url: http://arxiv.org/abs/2607.18979v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning

## Abstract
Large Language Models (LLMs) excel at multi-step reasoning, yet current parallel reasoning approaches often fail to distinguish the contributions of individual reasoning paths. Many paths may be redundant, misleading, or even detrimental, but outcome-level rewards assign uniform reward, leading to ambiguous learning signals and unstable training. We propose Parallel Shapley, a reinforcement learning framework that attributes fine-grained, path-level contributions in multi-path reasoning. Treating each path as a player in a cooperative game, we leverage Shapley values to quantify marginal contributions, using a generative reward model to evaluate path utilities and Monte Carlo sampling for efficient approximation. Experiments on mathematical reasoning benchmarks show that Parallel Shapley outperforms existing baselines while providing more stable and interpretable training. Our framework effectively "fishes out the free riders," assigning reward proportionally and improving multi-path reasoning in LLMs.

## Metadata
- **Published**: 2026-07-21T11:14:33Z
- **Authors**: Wentao Zhang, Haoyu Zhang, Xinke Jiang, Yuxuan Cheng, Yuhan Pan, Miao Li, Zhipeng Qiao, Tao Feng, Zhen Tao, Dengji Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18979v1)