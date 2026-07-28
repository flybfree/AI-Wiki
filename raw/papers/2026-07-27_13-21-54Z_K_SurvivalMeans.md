---
title: K-Survival Means
published: 2026-07-27T13:21:54Z
authors: Abdallah Alabdallah
url: http://arxiv.org/abs/2607.24405v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# K-Survival Means

## Abstract
In this work, we propose K-SurvMeans, a novel extension of K-Means for clustering survival data. The method explicitly uses the survival outcome in the clustering process to optimize cluster centers, thereby maximizing pairwise survival differences between clusters. The objective function encourages the clusters to be well-separated from the survival perspective. Since the resulting optimization problem is non-differentiable, we employ the Particle Swarm algorithm for the Optimization process.   To further improve flexibility and mitigate the curse of dimensionality, we extend the framework to operate in a learned low-dimensional latent space obtained via a dimensionality reduction. This allows the method to capture better-separated clusters and enhance optimization efficiency by reducing the search space.   Experiments on multiple publicly available benchmark survival datasets demonstrate that K-SurvMeans consistently yields clusters with improved separation in survival distributions compared to existing deep learning-based survival clustering methods.

## Metadata
- **Published**: 2026-07-27T13:21:54Z
- **Authors**: Abdallah Alabdallah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24405v1)