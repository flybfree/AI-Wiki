---
title: When Test-Time Adaptation Helps, Harms, or Becomes Inactive: A Condition-Level Study on CIFAR-10-C
published: 2026-08-23T06:06:38Z
authors: Sreeja Guha Majumdar, Aratrika Saha
url: http://arxiv.org/abs/2608.22233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Test-Time Adaptation Helps, Harms, or Becomes Inactive: A Condition-Level Study on CIFAR-10-C

## Abstract
Test-time adaptation (TTA) aims to improve model robustness under distribution shift by adapting a source model using unlabeled test data. Although methods such as TENT and EATA have demonstrated gains on corrupted data, aggregate accuracy can obscure the conditions under which adaptation fails or provides little benefit. We present a controlled comparison of three TTA strategies---BatchNorm-statistics adaptation (BN-Adapt), entropy-minimization adaptation (TENT), and reliability-filtered adaptation (a scoped re-implementation of EATA)---against an unadapted source model on the full CIFAR-10-C benchmark, covering 15 corruption types and 5 severity levels. All three methods improve mean accuracy over the source model by 12.2--13.3 percentage points (Wilcoxon signed-rank $p < 10^{-12}$). However, each method underperforms the source model on 8.0--9.3\% of conditions, with failures concentrated in low-severity corruptions where the source model already performs near ceiling, particularly brightness, fog, contrast, and defocus blur. We further find that EATA closely tracks the gradient-free BN-Adapt baseline, with a mean absolute difference of 0.09 percentage points, compared with 1.08 percentage points relative to TENT. This suggests that reliability filtering can substantially restrict effective adaptation, causing EATA to behave more like a BatchNorm-statistics baseline than an entropy-minimization method. These results show that aggregate accuracy alone can mask systematic TTA failure modes and motivate condition-level evaluation of when adaptation helps, harms, or becomes effectively inactive.

## Metadata
- **Published**: 2026-08-23T06:06:38Z
- **Authors**: Sreeja Guha Majumdar, Aratrika Saha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22233v1)