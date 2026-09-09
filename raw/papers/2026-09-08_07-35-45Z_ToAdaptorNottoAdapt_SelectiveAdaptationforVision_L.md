---
title: To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models
published: 2026-09-08T07:35:45Z
authors: Siru Jiang, Yuwei Liang, Jian Liang, Ran He, Tieniu Tan
url: http://arxiv.org/abs/2609.08367v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models

## Abstract
Test-time adaptation (TTA) has emerged as a prominent strategy for adapting vision-language models to distribution shifts during inference. We conduct a per-sample analysis of model predictions before and after adaptation, and observe two failure modes in existing TTA methods that echo previous work. Adaptations are frequently negligible, yielding no change in the model's predictions, and more severely, they can be detrimental by flipping previously correct predictions to incorrect ones. This naturally raises a question: Can we identify and skip such negligible or harmful adaptations? In this work, we introduce a new problem of selective adaptation, which aims to determine whether a given test sample should undergo adaptation or be skipped. To this end, we propose Cross-Augmentation Similarity (CAS), a simple baseline that performs adaptation only when predictions across augmented views exhibit low similarity. Notably, CAS not only preserves but in some cases improves overall accuracy, even when skipping nearly 85% of the adaptation process. We hope other researchers will explore this new direction and surpass the performance of our baseline. Our code is available at https://github.com/sirujiang/selective-adaptation.

## Metadata
- **Published**: 2026-09-08T07:35:45Z
- **Authors**: Siru Jiang, Yuwei Liang, Jian Liang, Ran He, Tieniu Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08367v1)