---
title: Bagging Robustly Learns VC Classes with Linear Sample Complexity
published: 2026-08-13T17:36:49Z
authors: Omar Montasser
url: http://arxiv.org/abs/2608.13514v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bagging Robustly Learns VC Classes with Linear Sample Complexity

## Abstract
We revisit the problem of learning predictors robust to adversarial examples at test-time. We prove that VC classes are adversarially robustly learnable with sample complexity linear in the VC dimension $d$, providing an exponential improvement over the previous upper bound of Montasser, Hanneke, and Srebro (2019). Remarkably, this result is achieved with a simple improper algorithm that combines the classic heuristic bagging (bootstrap aggregation) of Breiman (1996) with robust empirical risk minimization (RERM). Our algorithm computes RERMs on $O(d^\star)$ independent bootstrap samples and outputs their majority vote, where $d^\star$ denotes the dual VC dimension. We complement this result with a lower bound showing that this is unavoidable: in general, any learner in this oracle model requires $Ω(d^\star)$ calls to an RERM oracle, even when given arbitrarily many training examples.

## Metadata
- **Published**: 2026-08-13T17:36:49Z
- **Authors**: Omar Montasser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13514v1)