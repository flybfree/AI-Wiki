---
title: Shape Operator PCA: Curvature-Aware Projections for Geometric Machine Learning
published: 2026-08-15T16:37:47Z
authors: Alexandre L. M. Levada
url: http://arxiv.org/abs/2608.15313v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Shape Operator PCA: Curvature-Aware Projections for Geometric Machine Learning

## Abstract
In this paper, we propose SHOPCA (Shape Operator-based Principal Component Analysis), a novel method for unsupervised metric learning and dimensionality reduction that incorporates differential geometric information into the covariance structure of classical PCA. SHOPCA regularizes the global covariance matrix using the mean shape operator, defined as the average of the absolute local shape operators estimated from the data manifold, steering principal components toward directions of both maximum variance and informative curvature. A single trace-normalized mixing coefficient $α$ controls the regularization, recovering standard PCA at $α= 0$ and a curvature-driven embedding as $α\to \infty$. We further introduce a fully unsupervised criterion for selecting $α$ based on the spectral eigengap of the regularized covariance matrix, maximizing the relative separation between the top-$d$ and remaining eigenvalues without using class labels. We evaluate SHOPCA on more than 50 real-world benchmark datasets, comparing it with PCA, ISOMAP, and UMAP using Adjusted Rand Index (ARI), Normalized Mutual Information (NMI), Fowlkes-Mallows index (FM), and V-measure. Results show that SHOPCA consistently improves clustering quality over PCA across a broad range of datasets and surpasses UMAP on small-sample settings, where iterative neighborhood-based manifold estimation can degrade. SHOPCA is computationally tractable, parameter-efficient, and applicable to domains requiring fully unsupervised, geometry-aware dimensionality reduction.

## Metadata
- **Published**: 2026-08-15T16:37:47Z
- **Authors**: Alexandre L. M. Levada
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15313v1)