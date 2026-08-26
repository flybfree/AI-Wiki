---
title: Too much of a good thing -- when knowledge distillation promotes overfitting, and how to avoid it
published: 2026-08-24T18:40:20Z
authors: Irene Trigueros-Lorca, Leonardo Concepción, Christian Wagner, Isaac Triguero, Daniel Molina
url: http://arxiv.org/abs/2608.23752v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Too much of a good thing -- when knowledge distillation promotes overfitting, and how to avoid it

## Abstract
The growing size of Convolutional Neural Networks has led to increasingly large and costly models. Knowledge Distillation (KD) addresses this by transferring knowledge from a large network (teacher) to a small one (student), also reducing the training data required. KD is traditionally applied only at the network's final output. However, its behaviour when applied at intermediate network layers has received little attention. This raises the question of whether intermediate block-wise KD, which provides supervision throughout the network, could offer an advantage under specific conditions, such as few instances per class, which is common in fine-grained datasets. This work proposes a student design based on simple, homogeneous blocks mirroring those of the teacher, distilling knowledge between corresponding blocks. Across eleven datasets, we show that on classic datasets, distilling only the last block is sufficient -- and often best--, whereas fine-grained, data-scarce settings benefit substantially from intermediate supervision, with even a single additional distillation point narrowing the gap considerably. We further study how this supervision should be guided, exploring configurations of varying granularity and informed by an explainability analysis based on attention maps, Centered Kernel Alignment, and Grad-CAM, alongside the impact of teacher and student fine-tuning strategies. This work shows that intermediate block-wise distillation, guided appropriately, is key to building compact data-efficient models without sacrificing accuracy.

## Metadata
- **Published**: 2026-08-24T18:40:20Z
- **Authors**: Irene Trigueros-Lorca, Leonardo Concepción, Christian Wagner, Isaac Triguero, Daniel Molina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23752v1)