---
title: Batch Size or Negatives? A Selection Rule for Memory-Constrained Recommender Training
published: 2026-08-11T15:29:01Z
authors: Artyom Sabitov, Daniil Volkov, Alexey Zaytsev
url: http://arxiv.org/abs/2608.11061v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Batch Size or Negatives? A Selection Rule for Memory-Constrained Recommender Training

## Abstract
Large-scale neural recommender systems are typically trained with a softmax cross-entropy objective over the full item vocabulary. For a typical large number of possible items $K$, the final classification layer dominates memory, requiring $O(nK)$ logits and gradients to materialize for a batch of $n$ examples. Sampled softmax reduces this cost by restricting the objective to only $k \ll K$ candidate negative items, resulting in an $O(nk)$ memory. However, for a fixed budget $B = n k$, it remains unclear whether one should prioritize larger batches or the inclusion of more negative items.   We address this question by analyzing sampled-softmax training under a fixed memory constraint. Under standard smoothness and variance assumptions, our theoretical evidence suggests that the fastest convergence arises from an $ n \sim B, k \sim 1$ allocation. So, an actionable rule is to include as many objects as possible given computational constraints.   Our theory is supported by controlled synthetic and synthetic and four real sequential recommendation benchmarks, including MovieLens-20M. The suggested configuration achieve faster convergence and better final recommendation quality than imbalanced alternatives within the same memory constraint. These findings provide a theoretical and empirical foundation for configuring memory during the training of recommender systems. Code, reproducibility materials, and all scripts for generating figures are available at https://anonymous.4open.science/r/LimitedMemoryRule-BBFB

## Metadata
- **Published**: 2026-08-11T15:29:01Z
- **Authors**: Artyom Sabitov, Daniil Volkov, Alexey Zaytsev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11061v1)