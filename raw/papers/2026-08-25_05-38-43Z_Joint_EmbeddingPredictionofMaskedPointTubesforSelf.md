---
title: Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos
published: 2026-08-25T05:38:43Z
authors: Jheng-Ling Lee, Shang-Tse Chen
url: http://arxiv.org/abs/2608.24093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos

## Abstract
Self-supervised representation learning for 4D point cloud videos is challenging because annotations are costly and reconstruction-based pretraining can overemphasize low-level geometric details. We propose a JEPA-style framework that learns from unlabeled spatiotemporal point clouds through latent point-tube prediction. Instead of reconstructing raw coordinates, the model masks spatiotemporal regions and predicts their target representations from visible context representations in feature space. To stabilize latent prediction, we incorporate Sketched Isotropic Gaussian Regularization, which encourages non-collapsed embeddings without relying on explicit reconstruction targets. This formulation aims to capture both spatial structure and temporal dynamics while keeping the pretraining objective aligned with downstream semantic recognition. Experiments on action and gesture recognition benchmarks show that the learned representations improve downstream fine-tuning, limited-label learning, and cross-dataset transfer. These results suggest that JEPA-style latent prediction is a promising alternative to reconstruction-centered pretraining for 4D point cloud videos.

## Metadata
- **Published**: 2026-08-25T05:38:43Z
- **Authors**: Jheng-Ling Lee, Shang-Tse Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24093v1)