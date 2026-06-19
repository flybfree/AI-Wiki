---
title: Critical Percolation as a Synthetic Data Model for Interpretability
published: 2026-06-18T15:15:57Z
authors: Aryeh Brill, Tom Ingebretsen Carlson
url: http://arxiv.org/abs/2606.20347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Critical Percolation as a Synthetic Data Model for Interpretability

## Abstract
Neural networks learn features that reflect the hierarchical, multi-scale structure of natural data. Synthetic datasets used to evaluate interpretability methods typically lack this structure, limiting their value as realistic toy models. To close this gap, we introduce a family of synthetic datasets consisting of hierarchical functions defined on critical mean-field percolation clusters embedded in a high-dimensional data space. The percolation data consists of sparse, low-dimensional fractal clusters with a power-law size distribution. Latent variables modeling a taxonomic hierarchy generate each data point's target value. The data model is analytically tractable with known critical exponents that fix its properties without requiring hyperparameter tuning. We leverage a mapping between percolation clusters, random trees, and additive coalescence to propose an almost linear-time algorithm to jointly sample a random tree and its hierarchical latent decomposition, enabling data generation at arbitrary scale. Using probing experiments, we find that the model's ground-truth latent variables can be linearly decoded from neural network activations. Together, sparsity, self-similarity, power-law statistics, and analytical tractability make critical percolation a principled testbed for interpretability research.

## Metadata
- **Published**: 2026-06-18T15:15:57Z
- **Authors**: Aryeh Brill, Tom Ingebretsen Carlson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.20347v1)