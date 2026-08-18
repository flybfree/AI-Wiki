---
title: Geometry of Forgetting: Representation Flux in Continual Learning
published: 2026-08-16T16:59:03Z
authors: Maksim A. Kazanskii
url: http://arxiv.org/abs/2608.15854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Geometry of Forgetting: Representation Flux in Continual Learning

## Abstract
Catastrophic forgetting remains a fundamental obstacle to continual learning, where neural networks lose previously acquired knowledge while learning new tasks. Existing methods primarily mitigate forgetting through parameter regularization or experience replay, while the representation-space dynamics associated with forgetting remain less understood. We investigate latent representation evolution during sequential learning and introduce representation flux, a geometric measure of sample-level representation displacement across training. We show that representation flux is strongly associated with catastrophic forgetting across multiple benchmarks, with temporal analyses indicating that elevated flux can precede subsequent performance degradation. Representation displacement is also associated with confidence degradation, while complementary geometric properties provide additional information about sample-level forgetting. Motivated by these observations, we propose FlowLess-R, a representation-space regularization method that constrains replay representations relative to stored references while allowing continued learning. FlowLess-R is architecture-agnostic and integrates into replay-based methods through a representation-matching term. Experiments on SplitMNIST, SplitFashionMNIST, SplitCIFAR10, and SplitTinyImageNet show improved final average accuracy and reduced forgetting with ER, DER++, and ER-ACE. Our results identify representation flux as an informative geometric marker of forgetting and show that stabilizing latent representations provides a simple strategy for mitigating catastrophic forgetting.

## Metadata
- **Published**: 2026-08-16T16:59:03Z
- **Authors**: Maksim A. Kazanskii
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15854v1)