---
title: A Momentum-Based Variance-Reduced Algorithm for Federated Multiobjective Optimization
published: 2026-08-24T08:14:44Z
authors: Yong Zhao, Chunlin You, Minh N. Dao, Zai-Yun Peng
url: http://arxiv.org/abs/2608.22945v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Momentum-Based Variance-Reduced Algorithm for Federated Multiobjective Optimization

## Abstract
Federated learning has traditionally been formulated as a single-objective optimization problem, primarily focused on maximizing model utility. In real-world applications, however, machine learning models often need to optimize multiple and potentially conflicting objectives simultaneously. This motivates federated multiobjective optimization (FMOO), which provides a natural framework for jointly handling multiple task-specific objectives in federated learning. In this paper, we propose a momentum-based variance-reduced algorithm for federated multiobjective optimization. The method incorporates a momentum-driven gradient estimator into the local updates to reduce the variance of stochastic updates, leading to an improved convergence rate. We establish theoretical guarantees showing that the expected Pareto stationarity measure of a randomly selected output iterate decays at a rate of $\mathcal{O}(T^{-2/3})$, improving upon the $\mathcal{O}(T^{-1/2})$ rates established for existing methods such as FSMGDA and FedCMOO. Numerical experiments on federated multiobjective optimization benchmarks demonstrate the effectiveness and competitive performance of the proposed algorithm.

## Metadata
- **Published**: 2026-08-24T08:14:44Z
- **Authors**: Yong Zhao, Chunlin You, Minh N. Dao, Zai-Yun Peng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22945v1)