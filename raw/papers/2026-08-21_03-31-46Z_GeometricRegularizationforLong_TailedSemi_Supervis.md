---
title: Geometric Regularization for Long-Tailed Semi-Supervised Learning via Gaussian Feature Bridges
published: 2026-08-21T03:31:46Z
authors: Hongyang He, Xinyuan Song, Yan Zhong, Daizong Liu, Yanbin Li, Yang-fan He, Wenqiao Zhang
url: http://arxiv.org/abs/2608.20710v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Geometric Regularization for Long-Tailed Semi-Supervised Learning via Gaussian Feature Bridges

## Abstract
Real-world semi-supervised learning (SSL) often encounters significant challenges with long-tailed label distributions and noisy pseudo-labels, which hinder generalization and amplify confirmation bias. In this work, we introduce a novel framework, Gaussian Bridge Consistency (GBC), to address these challenges by constructing semantic interpolation paths between unlabeled samples and high-quality class anchors. Our method maintains a dynamic Prototype Atlas that stores a diverse and evolving set of labeled and pseudo-labeled exemplars per class. For each unlabeled instance, GBC forms a class-conditional Gaussian Feature Bridge in the latent space, enabling the student model to traverse a smooth trajectory from uncertain predictions to reliable class prototypes. A bridge consistency loss is applied along this path to enforce alignment with a geometrically interpolated target distribution. Furthermore, we propose BridgeMix, a confidence-aware feature mixing strategy that interpolates both sample and anchor pairs to amplify cross-sample generalization. Extensive experiments on CIFAR10-LT and ImageNet-LT (USB benchmarks) validate the robustness and effectiveness of GBC under realistic long-tailed SSL settings, consistently improving long tail-class performance without sacrificing scalability.

## Metadata
- **Published**: 2026-08-21T03:31:46Z
- **Authors**: Hongyang He, Xinyuan Song, Yan Zhong, Daizong Liu, Yanbin Li, Yang-fan He, Wenqiao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20710v1)