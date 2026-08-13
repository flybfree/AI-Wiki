---
title: High-dimensional Multi-objective Bayesian Optimization with Learned Variable Interactions
published: 2026-08-12T06:52:35Z
authors: Hongyan Wang, Jiayu Huang, Haotian Zheng, Xin Gao, Chi Ding, Ying Liu, Xia Wang, Qing Xu, Keqiang Li
url: http://arxiv.org/abs/2608.11713v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# High-dimensional Multi-objective Bayesian Optimization with Learned Variable Interactions

## Abstract
Multi-objective Bayesian optimization (MOBO) is effective in identifying the Pareto fronts for expensive black-box problems. However, most current MOBO approaches are limited to low-dimensional decision space due to its exponential sampling complexity. This paper presents decision variable interaction analysis-based MOBO, ViaMOBO, a generic framework for expensive multi-objective problems with high-dimensional decision space. The key idea of ViaMOBO is that it utilizes a variable interaction analysis model to determine whether the decision space can be completely or partially divided, and then performs local Bayesian optimization in the divided decision subspaces. Through the variable analysis model, it can be derived whether the objectives in black-box problems are separable, partially separable, or non-separable based on the potential independent or interdependent relationships among decision variables without any strong assumptions. We compare ViaMOBO with the state-of-the-art MOBO methods on both synthetic and real-world benchmarks. The experimental results demonstrate that ViaMOBO outperforms other related MOBO baselines in approximating the Pareto front of high-dimensional expensive multi-objective problems.

## Metadata
- **Published**: 2026-08-12T06:52:35Z
- **Authors**: Hongyan Wang, Jiayu Huang, Haotian Zheng, Xin Gao, Chi Ding, Ying Liu, Xia Wang, Qing Xu, Keqiang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11713v1)