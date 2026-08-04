---
title: Learning the Pareto Frontier of Predictive Models under Distribution Shift
published: 2026-08-01T12:40:52Z
authors: Yiming Dong, Jiwei Zhao, Yang Young Lu
url: http://arxiv.org/abs/2608.00632v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning the Pareto Frontier of Predictive Models under Distribution Shift

## Abstract
Modern machine learning pipelines increasingly rely on reusing pretrained and foundation models across downstream tasks. These pretrained models can differ not only in performance but also in how they can be used: some only provide black-box predictions, while others may permit white-box access to internal representations that can be probed or fine-tuned. When deployed to the target domain in the presence of distribution shift, no single strategy, including zero-shot application, fine-tuning, or directly training a target-specific model, is uniformly the best.   In this work, we propose Frontier Learning, a framework that treats a library of candidate models spanning different training histories and access regimes as complementary sources of information rather than mutually exclusive alternatives. Frontier Learning constructs a unified target-domain feature by concatenating internal representations from white-box candidates as well as prediction outputs from black-box candidates, then fits a lightweight, regularized supervised learner on this concatenated representation using labeled target data. Because the resulting hypothesis class contains predictors obtained by zero-shot reuse, fine-tuning, and direct training as special cases, empirical risk minimization over the frontier learner is guaranteed to be no worse, on the training sample, than any individual baseline.   We evaluate the framework in simulations spanning varying degrees of source-target compatibility and in two real-world distribution-shift settings: visual domain adaptation on DomainNet/VisDA and clinical mortality prediction across intensive care unit domains using MIMIC-IV-Notes. Across all settings, Frontier Learning matches or outperforms the strongest individual reuse strategy, with the largest gains arising precisely when no single baseline is reliable across the range of shift considered.

## Metadata
- **Published**: 2026-08-01T12:40:52Z
- **Authors**: Yiming Dong, Jiwei Zhao, Yang Young Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00632v1)