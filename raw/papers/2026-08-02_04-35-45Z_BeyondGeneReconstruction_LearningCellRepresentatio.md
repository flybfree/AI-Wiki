---
title: Beyond Gene Reconstruction: Learning Cell Representations through Complementary Transcriptomic Views
published: 2026-08-02T04:35:45Z
authors: Jiaqi Xiong, Yuntao hu, Yu Zheng, Yifei Shi, Xinyue Guo, Jiaxin Qi
url: http://arxiv.org/abs/2608.00985v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Gene Reconstruction: Learning Cell Representations through Complementary Transcriptomic Views

## Abstract
The rapid growth of single-cell transcriptomic data has enabled the development of foundation models pretrained primarily by reconstructing masked expression values. This objective encourages these models to learn gene dependencies but does not directly optimize whole-cell representations, which are essential for many downstream tasks. To bridge this gap, we propose a contrastive pretraining framework that learns cell representations through complementary transcriptomic views. Since standard contrastive learning is not readily applicable to single-cell pretraining, we introduce specific adaptations along three dimensions --- co-expression-guided gene partitioning, expression-aware contrast-set construction, and competence-gated contrastive onset. Specifically, we first construct two complementary views of each cell by partitioning its genes according to their co-expression structure. Then, to prevent the model from using gene-set identity as a shortcut, we construct hard negatives by permuting expression values while keeping gene identities unchanged. Finally, we introduce a competence-aware controller to determine how the contrastive objective is applied. Experiments on cell-type annotation and gene regulatory network inference demonstrate competitive transfer under the evaluated protocols. In the six-network GRN evaluation, our method records the highest mean AUROC and AUPRC point estimates among the compared variants, while the highest-scoring variant differs across individual networks. These results establish complementary-view contrastive learning as an effective direction for single-cell pretraining beyond gene reconstruction.

## Metadata
- **Published**: 2026-08-02T04:35:45Z
- **Authors**: Jiaqi Xiong, Yuntao hu, Yu Zheng, Yifei Shi, Xinyue Guo, Jiaxin Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00985v1)