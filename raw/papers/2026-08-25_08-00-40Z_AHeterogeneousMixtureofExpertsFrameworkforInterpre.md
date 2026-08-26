---
title: A Heterogeneous Mixture of Experts Framework for Interpretable Machine Learning
published: 2026-08-25T08:00:40Z
authors: Soham Chatterjee, Rwitobroto Dey, Smarajit Bose
url: http://arxiv.org/abs/2608.24195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Heterogeneous Mixture of Experts Framework for Interpretable Machine Learning

## Abstract
Mixture-of-Experts (MoE) models provide a flexible framework for partitioning complex prediction problems into simpler local learning tasks through an input-dependent gating mechanism. Existing interpretable MoE approaches, such as Mixture of Decision Trees (MoDT), achieve transparency by employing homogeneous decision-tree experts, but this restricts the model to a single inductive bias across all regions of the feature space. We extend the MoDT framework by introducing heterogeneous expert families comprising decision trees, linear support vector machines, and quadratic discriminant analysis under a common probabilistic gating mechanism. To ensure coherent likelihood-based inference, non-probabilistic experts are calibrated to produce conditional class probabilities, allowing parameter estimation within the generalized Expectation-Maximization framework of MoDT. We further establish theoretical monotone ascent guarantees for the proposed heterogeneous gating updates, providing a justification for the optimization procedure. Experiments on a diverse collection of synthetic and real-world benchmark datasets demonstrate that the proposed framework adaptively specializes experts according to local data geometry, yielding interpretable expert assignments while achieving predictive performance competitive with homogeneous MoDT and Random Forests. The proposed approach combines interpretability, adaptive inductive bias selection, and probabilistic coherence within a unified mixture-of-experts framework.

## Metadata
- **Published**: 2026-08-25T08:00:40Z
- **Authors**: Soham Chatterjee, Rwitobroto Dey, Smarajit Bose
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24195v1)