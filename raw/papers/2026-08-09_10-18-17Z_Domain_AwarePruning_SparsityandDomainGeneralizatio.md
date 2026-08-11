---
title: Domain-Aware Pruning: Sparsity and Domain Generalization via Regularized Probabilistic Masking
published: 2026-08-09T10:18:17Z
authors: Parham Sazdar, Mostafa Tavassolipour, Reshad Hosseini
url: http://arxiv.org/abs/2608.08624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Domain-Aware Pruning: Sparsity and Domain Generalization via Regularized Probabilistic Masking

## Abstract
Domain generalization (DG) and neural network pruning are conventionally treated as distinct objectives, targeting out-of-distribution (OOD) robustness and model efficiency, respectively. In this work, we bridge this gap by introducing Domain-Aware Pruning (DAP), a framework that leverages network sparsity as a mechanism to implicitly enhance generalization to unseen domains. Diverging from standard binary mask optimization, DAP learns a continuous parameter retention probability $p \in [0, 1]$, framing network compression as a continuous probabilistic masking problem. By introducing a regularization objective that actively penalizes the retention of domain-sensitive weights during the mask training, DAP identifies a domain-invariant subnetwork. Empirical results across five DG benchmark datasets demonstrate that DAP achieves significant sparsity while consistently matching or exceeding the OOD performance of its dense counterparts. Crucially, DAP is an algorithm-agnostic framework that integrates seamlessly with existing DG pipelines without necessitating post-hoc fine-tuning. Beyond efficiency and generalization, we show that DAP natively provides increased robustness to adversarial perturbations and yields highly interpretable models, where the retained weights reliably encapsulate the most domain-invariant and task-critical representations.

## Metadata
- **Published**: 2026-08-09T10:18:17Z
- **Authors**: Parham Sazdar, Mostafa Tavassolipour, Reshad Hosseini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08624v1)