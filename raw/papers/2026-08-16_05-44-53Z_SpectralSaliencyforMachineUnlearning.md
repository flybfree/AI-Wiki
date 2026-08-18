---
title: Spectral Saliency for Machine Unlearning
published: 2026-08-16T05:44:53Z
authors: Cedar Site Bai, Amber Yijia Zheng, Raymond A. Yeh, Brian Bullins
url: http://arxiv.org/abs/2608.15548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spectral Saliency for Machine Unlearning

## Abstract
Machine unlearning (MU) aims to remove the influence of specific training data while preserving model utility. As the name suggests, MU can be viewed as the inverse of learning, using gradient-based updates to reduce the influence of a forget-set by counteracting the previously learned behavior. Recently, Muon, a gradient descent variant, has been introduced. Muon applies spectral magnitude normalization to encourage exploration of rare directions and demonstrates promising performance. Inspired by Muon, we adopt the spectral view for unlearning and propose Spectral Saliency Unlearning (SSU). SSU thresholds weak singular components and updates only those directions supported by a confident unlearning signal. We further provide theoretical justification for this thresholding approach from the perspective of the forgetting-retention trade-off. Experiments across image classifiers, diffusion models, and LLMs demonstrate SSU's effectiveness.

## Metadata
- **Published**: 2026-08-16T05:44:53Z
- **Authors**: Cedar Site Bai, Amber Yijia Zheng, Raymond A. Yeh, Brian Bullins
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15548v1)