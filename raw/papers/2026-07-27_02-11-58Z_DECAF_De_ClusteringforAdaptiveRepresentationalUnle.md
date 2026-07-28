---
title: DECAF: De-Clustering for Adaptive Representational Unlearning
published: 2026-07-27T02:11:58Z
authors: Anjie Le, Can Peng, Hongcheng Guo, J. Alison Noble
url: http://arxiv.org/abs/2607.23934v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DECAF: De-Clustering for Adaptive Representational Unlearning

## Abstract
Machine unlearning, which aims to remove the influence of specific training data from a trained model, is a key requirement for privacy, accountability, and adaptive deployment. We argue that many unlearning methods are vulnerable to a simple clustering attack, which can recover class structure in an unsupervised manner, limiting their suitability for continual deployment where removal requests must be handled reliably on demand. To address this, we propose DECAF (DE-Clustering for Adaptive Forgetting), a post-hoc method that operates only on the forget set and is designed to break the cluster. DECAF combines input noise, confidence suppression, and entropy-based output diversification to disrupt the residual feature-space structure associated with forgotten data. On CIFAR-10 with ResNet-18, DECAF attains 0.10% forget-class accuracy, 79.4% retain accuracy, and an AUS of 0.88, surpassing all other baselines. In cluster-based analysis, it attains performance comparable to that of unlearning methods that use the full training set, while being significantly more efficient. Code: https://github.com/ale256/representation_unlearning.

## Metadata
- **Published**: 2026-07-27T02:11:58Z
- **Authors**: Anjie Le, Can Peng, Hongcheng Guo, J. Alison Noble
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23934v1)