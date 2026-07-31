---
title: Understanding Submodular Information Measure Based Objectives for Representation Learning: A Variance and Separation Perspective
published: 2026-07-30T04:17:17Z
authors: Rishabh Iyer, Truong Pham, Anay Majee
url: http://arxiv.org/abs/2607.27660v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Submodular Information Measure Based Objectives for Representation Learning: A Variance and Separation Perspective

## Abstract
Submodular Information Measures (SIMs) have recently emerged as a powerful framework for representation learning and multimodal learning. In particular, the SCORE framework~\cite{majee2024score} demonstrated that SIMs can serve as effective objectives for supervised contrastive learning. Despite their empirical success, however, the geometric and statistical properties induced by different submodular information measures remain poorly understood.   In this work, we develop a unified theoretical framework connecting SIMs to classical concepts in representation learning and statistical pattern recognition. We show that Total Information (TI) objectives characterize intra-class structure: Graph Cut TI recovers within-class variance, LogDet TI recovers generalized variance and covariance volume, and Facility Location TI induces imbalance-aware separation that emphasizes rare and confusable classes. We further show that Mutual Information (MI) objectives capture complementary notions of inter-class structure: Graph Cut MI is closely related to centroid separation and Fisher-style discrimination, LogDet MI captures covariance-aware separation through Mahalanobis distance, and Facility Location MI measures nearest-mode representational overlap.   We validate these theoretical characterizations using controlled synthetic experiments that independently vary variance, covariance, class imbalance, class separation, and multimodal overlap. Across all settings, the empirical behavior closely matches the proposed theory. Our results provide the first unified geometric and statistical understanding of submodular information measures and offer principled guidance for selecting and designing SIM-based objectives for representation learning.

## Metadata
- **Published**: 2026-07-30T04:17:17Z
- **Authors**: Rishabh Iyer, Truong Pham, Anay Majee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27660v1)