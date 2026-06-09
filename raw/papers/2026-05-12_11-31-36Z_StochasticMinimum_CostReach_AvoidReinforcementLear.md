---
title: Stochastic Minimum-Cost Reach-Avoid Reinforcement Learning
published: 2026-05-12T11:31:36Z
authors: Jingduo Pan, Taoran Wu, Yiling Xue, Bai Xue
url: http://arxiv.org/abs/2605.11975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stochastic Minimum-Cost Reach-Avoid Reinforcement Learning

## Abstract
We study stochastic minimum-cost reach-avoid reinforcement learning, where an agent must satisfy a reach-avoid specification with probability at least $p$ while minimizing expected cumulative costs in stochastic environments. Existing safe and constrained reinforcement learning methods typically fail to jointly enforce probabilistic reach-avoid constraints and optimize cost in the learning setting in stochastic environments. To address this challenge, we introduce reach-avoid probability certificates (RAPCs), which identify states from which stochastic reach-avoid constraints are satisfiable. Building on RAPCs, we develop a contraction-based Bellman formulation that serves as a principled surrogate for integrating reach-avoid considerations into reinforcement learning, enabling cost optimization under probabilistic constraints. We establish almost sure convergence of the proposed algorithms to locally optimal policies with respect to the resulting objective. Experiments in the MuJoCo simulator demonstrate improved cost performance and consistently higher reach-avoid satisfaction rates.

## Metadata
- **Published**: 2026-05-12T11:31:36Z
- **Authors**: Jingduo Pan, Taoran Wu, Yiling Xue, Bai Xue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.11975v1)