---
title: DisMix: Order-Aware Mixup for Medical Imaging via Disentangling Ordinal and Non-Ordinal Features
published: 2026-08-05T10:10:21Z
authors: Dileepa Pitawela, Gustavo Carneiro, Hsiang-Ting Chen
url: http://arxiv.org/abs/2608.04652v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DisMix: Order-Aware Mixup for Medical Imaging via Disentangling Ordinal and Non-Ordinal Features

## Abstract
Image mixup is a widely adopted data augmentation strategy, yet it is ill-suited for ordinal classification tasks such as medical disease grading, where labels encode a progression of severity. By indiscriminately blending disease-severity cues (ordinal) with appearance-level variation (non-ordinal), standard mixup produces samples that distort the very ordinal structure that underpins clinical severity grading. We introduce DisMix, an order-aware mixup framework for ordinal classification. DisMix disentangles ordinal and non-ordinal features via a dual-codebook VQ-VAE, allowing each subspace to be mixed independently: ordinal codes are interpolated to produce meaningful intermediate ranks, while non-ordinal codes are varied to introduce appearance diversity without corrupting the ordinal signal. Across four medical imaging datasets, DisMix shows the best aggregate performance among six image mixup baselines paired with six ordinal classifiers and remains effective under data scarcity and clinical grading variability.

## Metadata
- **Published**: 2026-08-05T10:10:21Z
- **Authors**: Dileepa Pitawela, Gustavo Carneiro, Hsiang-Ting Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04652v1)