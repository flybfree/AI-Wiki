---
title: CLEAR: Class-wise Expert Aggregation with Structured Sampling for Long-Tailed Classification
published: 2026-08-11T15:45:09Z
authors: Gawon Lim
url: http://arxiv.org/abs/2608.11287v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CLEAR: Class-wise Expert Aggregation with Structured Sampling for Long-Tailed Classification

## Abstract
Long-tailed classification poses a reliability challenge because models trained on imbalanced data are unevenly reliable across frequent and underrepresented classes. While existing methods address imbalance through re-balancing, adjustment, representation learning, or multi-expert modeling, they rarely estimate which expert should be trusted for each class. This paper proposes CLEAR (Class-wise reLiability-aware Expert Aggregation for long-tailed Recognition), a modular ensemble framework for long-tailed classification. CLEAR generates diverse experts through threshold-based structured sampling while preserving the full label space, then estimates a class-wise trust score for each expert using a smoothed class-wise precision formulation. During inference, expert predictions are combined through class-wise generalized product-of-experts aggregation, allowing different experts to be emphasized for different classes. Experiments on CIFAR-100-LT, ImageNet-LT, and Places-LT across multiple backbones show that CLEAR achieves competitive overall accuracy and particularly strong few-shot performance. These results support class-wise expert reliability as a useful design principle for long-tailed ensemble learning.

## Metadata
- **Published**: 2026-08-11T15:45:09Z
- **Authors**: Gawon Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11287v1)