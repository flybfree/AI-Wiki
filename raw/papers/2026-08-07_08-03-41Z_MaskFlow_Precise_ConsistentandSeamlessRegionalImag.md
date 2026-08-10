---
title: MaskFlow: Precise, Consistent and Seamless Regional Image Editing
published: 2026-08-07T08:03:41Z
authors: Rui Xu, Yang Yong, Shunzi Yang, Ruihao Gong, Chengtao Lv
url: http://arxiv.org/abs/2608.06929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MaskFlow: Precise, Consistent and Seamless Regional Image Editing

## Abstract
Regional image editing has attracted considerable attention for its spatial controllability. Although instruction-based and mask-reference-based editing methods can achieve strong semantic alignment, reliable regional control remains challenging, where an edit must be accurately localized and naturally integrated with the preserved context. We propose \textbf{MaskFlow}, a training framework for precise localization, consistent background preservation, and seamless boundary transitions. MaskFlow incorporates the mask into the probability path and flow-matching objective, coordinating generation within the editable region with source preservation outside it. The proposed Soft-Poisson de-seaming module further refines the predicted vector field during both training and sampling to improve the smooth integration of the edited foreground with the preserved background. We also design a data synthesis pipeline to construct MEData, a mask-based image editing dataset for training regional image editing models and facilitating further research. Experiments on natural scenes and infographic images demonstrate consistent improvements over competing methods in both quantitative and qualitative evaluations.

## Metadata
- **Published**: 2026-08-07T08:03:41Z
- **Authors**: Rui Xu, Yang Yong, Shunzi Yang, Ruihao Gong, Chengtao Lv
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06929v1)