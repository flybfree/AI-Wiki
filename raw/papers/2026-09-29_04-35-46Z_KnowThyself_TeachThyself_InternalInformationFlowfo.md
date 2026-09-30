---
title: Know Thyself, Teach Thyself: Internal Information Flow for Selective Self-Distillation
published: 2026-09-29T04:35:46Z
authors: Rui Wang, Ruijie Wang, Bo Chen, Jiangxuan Long, Yingyu Liang
url: http://arxiv.org/abs/2609.36695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Know Thyself, Teach Thyself: Internal Information Flow for Selective Self-Distillation

## Abstract
Self-distillation turns knowledge distillation into a closed learning loop and offers a path toward recursive self-improvement. Without an external teacher, however, the model must determine both what information can improve its supervision and which induced changes should be learned. Existing methods typically improve teacher-generated data or select training examples in isolation, leaving the information transferred between these stages unmeasured. We introduce InFlow, a retrieval-guided on-policy self-distillation framework that models this process as potential-to-realized information flow. InFlow first retrieves potentially informative sources using certainty-calibrated hidden-state trajectories, then measures their realized effect through the Jensen--Shannon divergence between the teacher's initial and retrieval-conditioned answer beliefs. Examples with larger belief shifts are selected for on-policy distillation. Our analysis formalizes the information optimized by retrieval and selection and relates the answer-level shift to the teacher--student distillation gap. Across four open-weight language models and three knowledge domains, InFlow achieves the strongest cross-model average among the compared selection methods, with ablations supporting both stages of the framework. Our code is available at https://github.com/1240148048/INFLOW.

## Metadata
- **Published**: 2026-09-29T04:35:46Z
- **Authors**: Rui Wang, Ruijie Wang, Bo Chen, Jiangxuan Long, Yingyu Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36695v1)