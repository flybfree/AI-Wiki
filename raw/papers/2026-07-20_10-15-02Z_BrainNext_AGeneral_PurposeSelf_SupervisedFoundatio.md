---
title: BrainNext: A General-Purpose Self-Supervised Foundation Model for Brain MRI Analysis
published: 2026-07-20T10:15:02Z
authors: Moona Mazher, Abdul Qayyum, Steven A. Niederer, Daniel C. Alexander
url: http://arxiv.org/abs/2607.17782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BrainNext: A General-Purpose Self-Supervised Foundation Model for Brain MRI Analysis

## Abstract
Foundation models pretrained using self-supervised learning have transformed computer vision by learning transferable representations from large-scale unlabeled data. However, existing foundation models for neuroimaging remain limited by task-specific training, slice-based learning strategies, or relatively small pretraining datasets, restricting their generalizability across diverse brain MRI applications. In this work, we present BrainNext, a general-purpose self-supervised foundation model for volumetric brain MRI analysis. BrainNext combines masked autoencoder (MAE) pretraining with a native three-dimensional Bi-Directional xLSTM-UNet architecture to learn rich anatomical representations from 60,551 unlabeled brain MRI examinations spanning multiple MRI modalities. The pretrained model is subsequently adapted to downstream tasks through lightweight task-specific fine-tuning. We evaluate BrainNext on the Foundation Models for Medical Imaging (FOMO) 2025 Method Track, encompassing classification, segmentation, and brain-age estimation, where it achieved second place overall and ranked first in the meningioma segmentation task on the official FOMO 2025 challenge leaderboard, demonstrating strong transferability across heterogeneous neuroimaging tasks. These results highlight the potential of large-scale self-supervised pretraining to learn robust and transferable volumetric representations, establishing BrainNext as a scalable foundation model for diverse brain MRI applications.

## Metadata
- **Published**: 2026-07-20T10:15:02Z
- **Authors**: Moona Mazher, Abdul Qayyum, Steven A. Niederer, Daniel C. Alexander
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17782v1)