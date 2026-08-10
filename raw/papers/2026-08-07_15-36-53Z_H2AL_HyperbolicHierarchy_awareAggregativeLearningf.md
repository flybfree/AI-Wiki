---
title: H2AL: Hyperbolic Hierarchy-aware Aggregative Learning for Registration-based Few-shot Medical Image Segmentation
published: 2026-08-07T15:36:53Z
authors: Jia Wang, Jiaming Cai, Zunying Hu, Zhanjie Wu, Jinyuan Liu, Hua Cheng, Yun Peng
url: http://arxiv.org/abs/2608.07340v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# H2AL: Hyperbolic Hierarchy-aware Aggregative Learning for Registration-based Few-shot Medical Image Segmentation

## Abstract
Registration-based Few-shot medical image segmentation (RFMIS) aims to generate pseudo-labels for unlabeled images by warping a labeled image through registration. However, existing methods primarily perform pixel-level optimization and inference in Euclidean space, treating anatomical structures as flat and disjoint. This neglect of inherent hierarchies degrades pseudo-label quality and weakens the discrimination of ambiguous regions, limiting the segmentation performance. To overcome this challenge, we propose a Hyperbolic Hierarchy-aware Aggregative Learning framework for RFMIS, termed H2AL, that enhances both deformation plausibility and anatomical discrimination for dual-task learning. Specifically, we introduce a Hyperbolic Hierarchy-aware Infusion (H2I) module, which leverages the hierarchical modeling capability of hyperbolic space to learn precise hierarchy-aware representations via transformation-guided supervised hyperbolic contrastive learning, and injects such hierarchical priors into Euclidean space through a gated infusion block while preserving semantic richness. Furthermore, we propose an end-to-end joint optimization algorithm by gradient aggregation, where the gradients from the registration and segmentation decoders, embedding semantic and hierarchical cues, are aggregated to update the shared encoder to promote collaborative learning across tasks. Extensive experiments on two anatomical regions, with five experimental settings, demonstrate the effectiveness and efficiency of our method in both registration and segmentation. The code is publicly available at https://github.com/JiamingCai469/H2AL.

## Metadata
- **Published**: 2026-08-07T15:36:53Z
- **Authors**: Jia Wang, Jiaming Cai, Zunying Hu, Zhanjie Wu, Jinyuan Liu, Hua Cheng, Yun Peng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07340v1)