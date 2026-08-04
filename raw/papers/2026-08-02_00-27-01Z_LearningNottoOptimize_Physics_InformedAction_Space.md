---
title: Learning Not to Optimize: Physics-Informed Action-Space Reshaping for Intent-Based Network Control
published: 2026-08-02T00:27:01Z
authors: Zuyuan Zhang, Vaneet Aggarwal, Tian Lan
url: http://arxiv.org/abs/2608.00908v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Not to Optimize: Physics-Informed Action-Space Reshaping for Intent-Based Network Control

## Abstract
Modern network policy control maps intent to sequential placement-control decisions. Bellman-style policy optimization primarily asks which action to optimize, while constraints are commonly handled through penalty, barrier, or Lagrangian mechanisms. We observe that before a value function can certify the best deployment, intermediate signals may already identify many candidates that should be excluded from further optimization. This motivates a complementary direction: \emph{Learning Not to Optimize}. Before a value function is accurate enough to select the best placement-control decision, intermediate signals may already show that candidates are equivalent under state--intent relabeling (quotienting), lead to a uniformly worse future state (dominance), or violate executable network laws (residual screening). \LNOQRD{} uses these computed or learned signals as a shadow process to reshape the domain on which primal policy optimization is performed, thereby reducing the action space. We prove lossless quotienting and dominance under explicit equivariance and monotonicity conditions, bound frontier size and ranking cost, and quantify losses from approximate certificates and primal estimates. Experiments show that \LNOQRD{} reduces small-instance candidates by $75.9\%$ while retaining $90.8\%$ near-oracle coverage and, on large instances, achieves the highest utility and intent satisfaction, the lowest hard-law violation and post-generation latency, and a $73.0\%$ average reduction among candidate-based baselines.

## Metadata
- **Published**: 2026-08-02T00:27:01Z
- **Authors**: Zuyuan Zhang, Vaneet Aggarwal, Tian Lan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00908v1)