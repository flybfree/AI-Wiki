---
title: A Deep Learning Model for Spatially Clustered Data via Differentiable Cluster Assignment
published: 2026-08-15T01:39:56Z
authors: Kexuan Li, Weidong Ma
url: http://arxiv.org/abs/2608.14968v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Deep Learning Model for Spatially Clustered Data via Differentiable Cluster Assignment

## Abstract
We consider nonparametric regression when the association between a response and its covariates changes across an unknown partition of a spatial domain. The proposed estimator learns the partition and the cluster-specific regression functions jointly. A neural network depending only on location determines cluster membership, while separate neural networks describe the covariate--response relationship within the clusters. An annealed softmax relaxation permits gradient-based estimation of the otherwise discrete assignments. Graph-Laplacian and occupancy penalties are used to discourage fragmented regions and degenerate solutions. We establish identifiability up to label permutation, bound partition error under a margin condition, and decompose prediction risk into regression and assignment components. The resulting rate agrees with that of an oracle estimator when the partition is estimated sufficiently accurately. Simulations show that joint estimation is useful when regression surfaces change abruptly across spatial boundaries, including settings with nonlinear effects, unequal region sizes, preferential sampling, and spatially correlated errors. Finally, a real data analysis is provided to demonstrate the validity and effectiveness of the proposed method.

## Metadata
- **Published**: 2026-08-15T01:39:56Z
- **Authors**: Kexuan Li, Weidong Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14968v1)