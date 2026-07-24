---
title: Breaking Feedback-Blindness: Utility-Augmented Transformer for Sequential Decision Making
published: 2026-07-21T09:52:23Z
authors: Yuyang Shen, Shan Dai, Daimin Chen
url: http://arxiv.org/abs/2607.18910v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breaking Feedback-Blindness: Utility-Augmented Transformer for Sequential Decision Making

## Abstract
Sequential decision making in non-stationary and partially observable environments requires rapid adaptation to latent regime changes. However, existing Transformer decision models face a structural bottleneck in the retrieval mechanism: even when reward is used for training or exposed as an input token, attention retrieval remains primarily driven by observation-derived similarity. We formalize this limitation as feedback-blind retrieval, and formally show that, on feedback-informative tasks, observation-equivalent histories with different action-reward outcomes cannot be distinguished by any observation-only attention, resulting in suboptimal choice. To address this mismatch, we propose the Utility-Augmented Transformer (UAT), a new feedback-conditioned retrieval attention architecture in which a compact utility state modulates the query, key, and value projections, allowing action-reward history to directly alter context retrieval during the forward pass. UAT also enjoys an exact zero-gate degradation property that recovers the Vanilla Transformer when feedback is uninformative. Under finite-horizon compactness and Lipschitz assumptions, we prove that UAT strictly enlarges the observation-only Transformer class and can uniformly approximate feedback-dependent decision maps. Across four non-stationary benchmarks: synthetic navigation with hidden goal shifts, non-stationary sepsis treatment, cross-market portfolio allocation, and delayed-feedback recommendation, UAT consistently improves performance over observation-only, test-time adaptation, and input-level feedback baselines, with particularly large gains in noisier regimes that require stronger adaptation.

## Metadata
- **Published**: 2026-07-21T09:52:23Z
- **Authors**: Yuyang Shen, Shan Dai, Daimin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18910v1)