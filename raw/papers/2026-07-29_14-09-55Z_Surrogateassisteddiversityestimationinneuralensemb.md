---
title: Surrogate assisted diversity estimation in neural ensemble search
published: 2026-07-29T14:09:55Z
authors: Alexandr Udeneev, Petr Babkin, Oleg Bakhteev
url: http://arxiv.org/abs/2607.26940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Surrogate assisted diversity estimation in neural ensemble search

## Abstract
Ensembles are a standard way to improve the performance and robustness of deep neural networks, but their effectiveness crucially depends on both the quality and the diversity of individual models. Most neural architecture search (NAS) methods are computationally expensive. Extending them to neural ensemble search (NES), which requires joint optimization of individual architectures and their ensemble composition, leads to an exponential growth of the search space and makes the problem computationally intractable. To address this, we introduce a dual-objective surrogate-guided ensemble search: candidate architectures are represented as directed acyclic graphs, and two surrogate models are trained independently to estimate predictive accuracy and diversity potential. Their combined estimates guide an NES framework that efficiently identifies architectures that are both individually strong and collectively diverse. Our final ensemble achieves competitive or superior performance compared to standard baselines such as Deep Ensembles and Random Search on FashionMNIST, CIFAR-10, and CIFAR-100.

## Metadata
- **Published**: 2026-07-29T14:09:55Z
- **Authors**: Alexandr Udeneev, Petr Babkin, Oleg Bakhteev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26940v1)