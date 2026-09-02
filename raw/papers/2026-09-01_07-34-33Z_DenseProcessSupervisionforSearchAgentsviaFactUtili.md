---
title: Dense Process Supervision for Search Agents via Fact Utility Estimation
published: 2026-09-01T07:34:33Z
authors: Rongzhi Zhu, Xiangyu Liu, Yi Liu, Shuo Zhang, Ruirui Zhang, Rui Wu, Tao Jiang, Zequn Sun, Wenhao Xu, Wei Hu
url: http://arxiv.org/abs/2609.00833v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dense Process Supervision for Search Agents via Fact Utility Estimation

## Abstract
Reinforcement learning (RL) for search agents typically relies on outcome rewards. However, it often fails to achieve effective credit assignment, due to the unclear value of intermediate steps. It is hard to separate their contributions from the final result. In this paper, we propose a dense process supervision method based on fact utility estimation, which models the reasoning process as the accumulation of discrete evidence facts. We first extract structured facts from raw observations and organize them into an explicit fact store. To support credit assignment, we then cluster semantically equivalent facts and infer the posterior utility of each fact cluster using Bayesian estimation over group rollouts. Finally, we convert the estimated fact utilities into dense step-level rewards to guide RL training. Experiments on seven single-hop and multi-hop QA benchmarks show that our method consistently outperforms existing baselines. Ablation studies validate clear relative improvements on multi-hop QA compared to outcome reward-only training.

## Metadata
- **Published**: 2026-09-01T07:34:33Z
- **Authors**: Rongzhi Zhu, Xiangyu Liu, Yi Liu, Shuo Zhang, Ruirui Zhang, Rui Wu, Tao Jiang, Zequn Sun, Wenhao Xu, Wei Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00833v1)