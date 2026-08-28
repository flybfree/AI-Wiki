---
title: When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy
published: 2026-08-27T06:08:11Z
authors: Jin Liu, Junkang Liu, Ning Xi, Yinbin Miao, Dawei Wei, Ke Cheng, Jianfeng Ma
url: http://arxiv.org/abs/2608.26655v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy

## Abstract
Model merging promises to construct a single multi-task model from independently fine-tuned task models without accessing the original task data. This makes it attractive when task data cannot be centralized, but released task models may still leak private fine-tuning data. Differential privacy (DP) provides a principled mechanism for limiting such leakage, yet its effect on model merging remains poorly understood. In this paper, we study the geometry of differentially private model merging and identify two geometric obstacles that make private task models difficult to merge: \emph{local sharpness}, which makes task losses sensitive to the parameter displacement induced by merging, and \emph{reference drift}, which measures the displacement of private task models from the shared pretrained initialization and amplifies cross-task interference. Based on these observations, we propose \textbf{DP-Merging}, a geometry-aware framework that improves the mergeability of differentially private task models. DP-Merging uses a DP-compatible sharpness-aware objective to guide each private task model toward flatter loss regions, and a reference-based alignment regularizer to keep task models close to the shared pretrained initialization. We derive a merge-gap upper bound showing that reducing local curvature and reference drift tightens the bound on the loss increase induced by merging. Experiments on vision and language tasks across multiple privacy budgets show that DP-Merging consistently improves private merged-model performance while preserving the privacy guarantees of the underlying DP fine-tuning procedures.

## Metadata
- **Published**: 2026-08-27T06:08:11Z
- **Authors**: Jin Liu, Junkang Liu, Ning Xi, Yinbin Miao, Dawei Wei, Ke Cheng, Jianfeng Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26655v1)