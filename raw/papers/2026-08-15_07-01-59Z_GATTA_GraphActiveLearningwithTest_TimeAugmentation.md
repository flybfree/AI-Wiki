---
title: GATTA: Graph Active Learning with Test-Time Augmentation
published: 2026-08-15T07:01:59Z
authors: Zsombor Bánfi, András Gézsi, András Formanek
url: http://arxiv.org/abs/2608.15084v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GATTA: Graph Active Learning with Test-Time Augmentation

## Abstract
Test-time augmentation (TTA) has proven effective for improving model robustness and uncertainty estimation in computer vision, yet its application to graph-structured data remains largely unexplored. We introduce GATTA (Graph Active Learning with Test-Time Augmentation), a framework for enhancing active learning by aggregating predictions across multiple augmented views to produce more reliable uncertainty estimates. To address the challenge of label-preserving graph augmentations, GATTA incorporates a consistency-based filtering mechanism that discards augmented views yielding unreliable predictions. We systematically evaluate GATTA across multiple graph datasets, GNN architectures, and acquisition strategies. Our results show that simple uncertainty-based methods, such as Entropy and Least Confidence, benefit most from TTA, achieving performance competitive with more sophisticated and computationally expensive approaches. GATTA generalizes across architectures, outperforms model-side ensemble methods such as MC Dropout. We further show that GATTA scales efficiently with both ensemble size and graph size. Extensive analysis of augmentation types, strengths, and filtering strategies provides practical guidelines for effective deployment. Our findings demonstrate that augmenting simple methods with TTA offers a more efficient path to strong active learning performance than engineering complex acquisition functions, enabling practitioners to achieve competitive results with lower computational overhead and reduced implementation complexity.

## Metadata
- **Published**: 2026-08-15T07:01:59Z
- **Authors**: Zsombor Bánfi, András Gézsi, András Formanek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15084v1)