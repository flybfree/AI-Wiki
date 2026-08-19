---
title: CORAM: Coherent Orthogonal Rotation for Model Merging
published: 2026-08-18T04:44:24Z
authors: Xinyi Sui, Ziran Liu, Nam Ling, Wei Wang, Wei Jiang
url: http://arxiv.org/abs/2608.17366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CORAM: Coherent Orthogonal Rotation for Model Merging

## Abstract
Merging finetuned models combines specialized capabilities without joint training or access to the original data. Most methods operate by linear arithmetic in Euclidean weight space, which cannot carry the geometry of the update. Orthogonal Model Merging (OrthoMerge) uses a single orthogonal transform for each weight matrix, but such a transform cannot change singular values. We propose CORAM, which partitions each target matrix into row slices, represents every expert slice by its singular value decomposition in the corresponding base-model SVD frame, and merges the task-specific factors on their corresponding manifolds. Because manifold averaging contracts the merged update, CORAM applies an amplification coefficient $λ=κ\hat{c}$. The scale c_hat is estimated from the expert and merged update norms and is approximately $\sqrt{N}$ for $N$ experts with comparable update magnitudes. The restoration strength kappa is selected from the dispersion of expert updates without evaluating candidate merged models. This rule remains within 0.72 points of the best swept value on all evaluated suites. CORAM also includes spread slicing to distribute highly updated rows across slices and a residual pathway for non-target layers. Across four suites covering three model families, 3B to 9B scales, and language and vision-language experts, CORAM improves over OrthoMerge by 0.25 to 1.35 points and matches or exceeds the strongest weight-space baselines.

## Metadata
- **Published**: 2026-08-18T04:44:24Z
- **Authors**: Xinyi Sui, Ziran Liu, Nam Ling, Wei Wang, Wei Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17366v1)