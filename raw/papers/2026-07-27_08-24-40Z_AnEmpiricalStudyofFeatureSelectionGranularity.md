---
title: An Empirical Study of Feature Selection Granularity
published: 2026-07-27T08:24:40Z
authors: Muhammad Rajabinasab, Arthur Zimek
url: http://arxiv.org/abs/2607.24145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Empirical Study of Feature Selection Granularity

## Abstract
Feature selection aims to identify the most informative and relevant features for a given dataset, either in terms of capturing the underlying data structure and distribution better, or with respect to the performance on a downstream task. Existing research in this area has largely focused on developing novel algorithms (in both supervised and unsupervised settings), proposing new evaluation metrics and frameworks, or benchmarking the performance of existing methods. In this work, we examine feature selection through an algorithmic design perspective. Conventional feature selection algorithms typically compute feature importance scores globally across the entire feature set and then select the top-ranked features in a single step. However, this approach raises a critical question: Can the presence of less informative (or noisy) features mask or obscure the true importance of other, more relevant features? In other words, would a recursive strategy, where features are removed one by one while re-evaluating importance at each step, yield different and potentially better results than the standard global ranking approach? To answer this question, we conduct an extensive empirical study using five diverse feature selection algorithms. We implement each algorithm under both the conventional global selection design and the greedy recursive elimination design. We then analyze the impact of this algorithmic choice, both individually for each method and collectively across all methods, on a range of standard feature selection evaluation metrics. The empirical evaluation results show that the greedy approach improves the overall feature selection quality almost consistently, albeit on the expense of higher computational cost, supporting our initial expectation that the curse of dimensionality also obscures the ways of mitigating it.

## Metadata
- **Published**: 2026-07-27T08:24:40Z
- **Authors**: Muhammad Rajabinasab, Arthur Zimek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24145v1)