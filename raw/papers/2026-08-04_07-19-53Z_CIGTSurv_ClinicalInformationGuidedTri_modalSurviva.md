---
title: CIGTSurv: Clinical Information Guided Tri-modal Survival Prediction with Local Prototype Association and Global Feature Alignment
published: 2026-08-04T07:19:53Z
authors: Jing Dai, Qibin Zhang, Weiwei Zhou, Mingde Xu, Jingsong Liu, Jingdong Zhang, Hongming Xu
url: http://arxiv.org/abs/2608.03247v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CIGTSurv: Clinical Information Guided Tri-modal Survival Prediction with Local Prototype Association and Global Feature Alignment

## Abstract
Multimodal learning has significantly advanced survival prediction by integrating pathology images with genomic data. However, clinical information, despite its critical role in reflecting a patient' s overall health, remains underutilized due to its discrete, sparse, and low-dimensional nature. Furthermore, the inherent heterogeneity across these modalities pose significant challenges in modeling cross-modal interactions. In this paper, we propose CIGTSurv, a Clinical Information Guided Tri-modal framework for Survival prediction. Specifically, we first design a holistic text template and use pretrained foundation models to transform clinical tabular data into high-dimensional tokenized embeddings. Using clinical information as an anchor, we then introduce a dual-level interaction mechanism: 1) a local prototype association (LPA) module based on cross-attention to explicitly learn token-level correspondences between different modalities, and 2) a global feature alignment (GFA) loss based on Maximum Mean Discrepancy (MMD) to implicitly enhance cross-modal distribution consistency. Extensive experiments on five TCGA cancer cohorts demonstrate that CIGTSurv achieves state-of-the-art (SOTA) survival prediction performance. Our source code is publicly available at https://github.com/Daijing-ai/CIGT-Surv.git.

## Metadata
- **Published**: 2026-08-04T07:19:53Z
- **Authors**: Jing Dai, Qibin Zhang, Weiwei Zhou, Mingde Xu, Jingsong Liu, Jingdong Zhang, Hongming Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03247v1)