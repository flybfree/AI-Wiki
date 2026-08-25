---
title: Cross-Subject Generalization in Decoding Perceived Speech from Non-Invasive Brain Recordings
published: 2026-08-23T13:50:32Z
authors: Aoke Zhang, Bo Wang, Xihong Wu, Heping Cheng, Jing Chen
url: http://arxiv.org/abs/2608.22420v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Subject Generalization in Decoding Perceived Speech from Non-Invasive Brain Recordings

## Abstract
Decoding perceived speech from non-invasive brain recordings has garnered significant attention in recent years due to its wide range of potential applications. However, existing methods face considerable challenges in cross-subject decoding, primarily due to limited generalizability and the absence of explicit mechanisms for extracting subject-consistent information. These limitations result in high training costs and suboptimal decoding performance. To address these challenges, we propose an innovative Cross-Subject Perceived Speech Decoding (CPSD) framework, which comprises two training stages: source model pre-training and personal specialization. In the source model pre-training stage, contrastive learning is employed to capture shared representations across multiple source subjects. Subsequently, personal specialization initializes the model for the target subject by extracting consistent components from the source model and fine-tuning it using target subject data. Additionally, we introduce the Positional Encoding-based Spatial Attention (PESA) module, which remaps MEG/EEG data into a standardized reference space, thereby enhancing cross-subject consistency and facilitating model training. We evaluate the proposed CPSD framework on three perceived speech neural datasets encompassing different modalities and languages. The results demonstrate that our framework outperforms baseline methods by more than 6.8%, 15.4%, and 15.8% in Top-10 accuracy on the Armeni 2022, PKUEEG 2025, and Broderick 2018 datasets, respectively. Further analyses confirm the effectiveness, efficiency, and robustness of the proposed approach.

## Metadata
- **Published**: 2026-08-23T13:50:32Z
- **Authors**: Aoke Zhang, Bo Wang, Xihong Wu, Heping Cheng, Jing Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22420v1)