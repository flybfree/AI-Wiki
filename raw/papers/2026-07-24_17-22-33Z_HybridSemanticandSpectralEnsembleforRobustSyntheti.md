---
title: Hybrid Semantic and Spectral Ensemble for Robust Synthetic Image Source Attribution
published: 2026-07-24T17:22:33Z
authors: Md. Ajwad Hossain
url: http://arxiv.org/abs/2607.22808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hybrid Semantic and Spectral Ensemble for Robust Synthetic Image Source Attribution

## Abstract
The rapid advancement of text-to-image (T2I) models has necessitated robust Synthetic Image Source Attribution (SIA) methodologies. A critical challenge in SIA is the distribution shift between pristine training images and real-world deployed images, which undergo unknown post-processing operations such as JPEG compression and blurring. In this work, proposed for the DLMMDD Challenge at ICANN 2026, we introduce a dual-branch ensemble framework fusing Semantic Deep Learning with Mathematical Forensic Feature Extraction. The semantic branch employs EfficientNet-B0 regularized with Exponential Moving Averaging (EMA) and Label Smoothing. The forensic branch extracts 126 mathematical features -- including SVD spectral profiles and Local Binary Patterns -- from high-pass noise residuals, compressed via Truncated SVD and classified with XGBoost. Evaluated on a dataset of 10 generators where 55% of the test set is degraded, our approach achieves a private leaderboard accuracy of 95.60%. Furthermore, the entire pipeline is highly computationally efficient, requiring no GPU acceleration and executing end-to-end on a standard CPU in under 6.5 hours, highlighting the practicality and scalability of mathematical forensics for real-world deployment.

## Metadata
- **Published**: 2026-07-24T17:22:33Z
- **Authors**: Md. Ajwad Hossain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22808v1)