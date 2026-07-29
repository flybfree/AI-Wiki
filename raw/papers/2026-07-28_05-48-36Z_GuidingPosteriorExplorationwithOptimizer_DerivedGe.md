---
title: Guiding Posterior Exploration with Optimizer-Derived Geometry
published: 2026-07-28T05:48:36Z
authors: Moritz Schlager, Emanuel Sommer, Thomas Möllenhoff, David Rügamer
url: http://arxiv.org/abs/2607.25312v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Guiding Posterior Exploration with Optimizer-Derived Geometry

## Abstract
Sampling-based methods offer a principled approach to uncertainty quantification in Bayesian neural networks. Their practical use, however, is often challenged by the computational cost of exploring high-dimensional and multimodal posterior distributions. To overcome these difficulties, Bayesian Deep Ensembles, i.e., warmstarting the sampling from several optimized solutions, have proven to be an effective strategy. In this paper, we demonstrate that curvature estimates computed during the warmstart as a byproduct in adaptive optimizers such as AdamW can inform the sampling phase at negligible additional cost. Specifically, our proposed preconditioned sampling strategy based on optimizer-derived geometries can substantially reduce or even eliminate the need for a lengthy sampling burn-in phase and leads to greater numerical stability. This approach consistently maintains or improves predictive performance and uncertainty quantification without any additional computational costs. We confirm the consistency of our findings across various datasets and network architectures.

## Metadata
- **Published**: 2026-07-28T05:48:36Z
- **Authors**: Moritz Schlager, Emanuel Sommer, Thomas Möllenhoff, David Rügamer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25312v1)