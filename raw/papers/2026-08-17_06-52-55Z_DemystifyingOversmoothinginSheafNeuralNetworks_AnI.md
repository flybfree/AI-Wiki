---
title: Demystifying Oversmoothing in Sheaf Neural Networks: An Index-Theoretic Criterion
published: 2026-08-17T06:52:55Z
authors: Junwen Dong, Yuhan Peng, Hao Li, Huitao Feng, Kelin Xia
url: http://arxiv.org/abs/2608.16180v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Demystifying Oversmoothing in Sheaf Neural Networks: An Index-Theoretic Criterion

## Abstract
To combat oversmoothing in Graph Convolutional Networks, Sheaf Neural Networks (SNNs) were proposed as a generalization by equipping the graph with a sheaf structure and replacing the graph Laplacian with a sheaf Laplacian $\mathcal{L}$. Existing analyses connect sheaf diffusion to oversmoothing via the harmonic space ($\ker\mathcal{L}$), taking its absolute dimension as an indicator of anti-oversmoothing capacity. However, absolute dimension alone is not a reliable measure: certain sheaf configurations inflate $\dim \ker \mathcal{L}$ while their harmonic sections remain entirely constant, without enriching discriminative capacity. We instead introduce the first relative, geometric approach, yielding a precise characterisation of anti-oversmoothing capacity. Under natural conditions on stalk transportation and global sheaf structure, we establish an index-theoretic comparison criterion showing that one sheaf's harmonic space genuinely contains another's beyond trivial inflation. We illustrate this with a concrete instance and further introduce \textit{GyroSheaf}, a sheaf with curved gyrovector-space stalks, extending the criterion to the non-linear setting via local tangent-space linearization. Experiments across ten models confirm the theoretical criterion: sheaf models violating the criterion collapse despite possessing index jumps, while compliant models maintain depth-stable representations.

## Metadata
- **Published**: 2026-08-17T06:52:55Z
- **Authors**: Junwen Dong, Yuhan Peng, Hao Li, Huitao Feng, Kelin Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16180v1)