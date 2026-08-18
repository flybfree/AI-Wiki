---
title: Bridging the Gap between Labeled and Unlabeled Data via Unified Flow with Feature Memory Bank
published: 2026-08-17T15:04:25Z
authors: Shanwen Wang, Xin Sun, Danfeng Hong, Junyu Dong, Patrick Le Callet
url: http://arxiv.org/abs/2608.16681v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bridging the Gap between Labeled and Unlabeled Data via Unified Flow with Feature Memory Bank

## Abstract
Although semi-supervised semantic segmentation ($\text{S}^4$) utilizes abundant unlabeled data to reduce manual labeling burdens, independent training of labeled and unlabeled data causes the former to dominate, which severely degrades pseudo-label quality. To address this challenges, we propose a novel remote sensing (RS) $\text{S}^4$ method via unified flow with feature memory bank (UFFM). Specifically, UFFM comprises two key innovations: unified flow (UF) and feature memory bank (FMB). The UF is a new training flow that generates less biased pseudo-labels by combining an external visual foundation model (VFM) with an RS domain teacher, and jointly optimizes labeled and pseudo-labeled data under a unified training objective. The FMB is a novel memory module for $\text{S}^4$ that dynamically updates class-specific features during training and reduces the feature discrepancy between labeled and unlabeled data through class-feature alignment. To verify the effectiveness of our model, we conduct extensive experiments on RS datasets. The experimental results show the superiority of our method over SOTA $\text{S}^4$ methods. Moreover, the results demonstrate the effectiveness of our contributions in bridging the optimization and feature representation gap between labeled and unlabeled data. Our code is released at \href{https://github.com/wangshanwen001/RS-UFFM}{https://github.com/wangshanwen001/RS-UFFM}.

## Metadata
- **Published**: 2026-08-17T15:04:25Z
- **Authors**: Shanwen Wang, Xin Sun, Danfeng Hong, Junyu Dong, Patrick Le Callet
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16681v1)