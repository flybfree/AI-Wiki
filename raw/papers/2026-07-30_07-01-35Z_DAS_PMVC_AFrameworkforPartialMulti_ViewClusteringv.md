---
title: DAS-PMVC: A Framework for Partial Multi-View Clustering via Dual Alignment and Structure Enhancement
published: 2026-07-30T07:01:35Z
authors: Shubin Ma, Liang Zhao, Chuanye He, Zhenjiao Liu, Liang Zou, Lin Yuanbo Wu, Yu Shao
url: http://arxiv.org/abs/2607.27761v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DAS-PMVC: A Framework for Partial Multi-View Clustering via Dual Alignment and Structure Enhancement

## Abstract
In recent years, multi-view clustering has attracted widespread research interest. However, due to limitations in data collection devices, data across different views often suffer from misalignment, leading to the partial view alignment problem (PVAP). To mitigate the impact of view asymmetry and irrelevant samples, this paper proposes a framework for partial multi-view clustering via dual alignment and structure enhancement (DAS-PMVC), which leverages view structure consistency and semantic relevance. Specifically, DAS-PMVC includes three parts: \textbf{anchor graph structure alignment}, where sample joint embedding representations with consistent latent space are derived from anchor point relationships for initial view alignment; \textbf{structure-enhanced feature learning}, where the model learns view structure information through pretraining and combines multi-view graph convolutional networks to further extract deep latent features from the aligned graph structure to improve the discriminative power of representations; and \textbf{a dual alignment strategy}, where initial alignment is performed through the anchor graph in the pretraining phase, and contrastive learning loss and the Hungarian algorithm are introduced in the training phase to further optimize the alignment of latent features. Experimental results on various datasets demonstrate that the DAS-PMVC framework outperforms existing state-of-the-art methods in clustering performance, showcasing its effectiveness and superiority.

## Metadata
- **Published**: 2026-07-30T07:01:35Z
- **Authors**: Shubin Ma, Liang Zhao, Chuanye He, Zhenjiao Liu, Liang Zou, Lin Yuanbo Wu, Yu Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27761v1)