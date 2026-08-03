---
title: MBDiff: Multi-view Behavior-aware Diffusion Model for Probabilistic Utility Data Imputation
published: 2026-07-31T08:58:54Z
authors: Rongchao Xu, Lin Jiang, Dahai Yu, Ximiao Li, Guang Wang
url: http://arxiv.org/abs/2607.29177v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MBDiff: Multi-view Behavior-aware Diffusion Model for Probabilistic Utility Data Imputation

## Abstract
Utility data (e.g., electricity, water, and gas consumption), collected by ubiquitous sensors and embedded devices, often contains substantial missing values due to various factors such as device failures and data transmission issues. The data missingness can severely impact utility billing accuracy, hinder demand forecasting, and disrupt efficient utility supply management. As a result, utility data imputation has attracted much interest from both industry and academia. While many studies have attempted to address this issue, most of them rely on aggregated datasets for training, overlooking rich user behavior information, which could provide valuable insights for more accurate imputation. However, learning comprehensive user behavior from long-term, diverse, and incomplete utility data remains a significant challenge. Moreover, leveraging user behavior information to guide imputation is nontrivial due to the indirect nature of the correlations. To address these challenges, we propose MBDiff, a Multi-view Behavior-aware Diffusion Model for Probabilistic Utility Data Imputation. MBDiff incorporates two key technical components: (i) a multi-view User Behavior Extraction module that learns comprehensive user behavior from multiple perspectives, including global, local, and instance-level views; and (ii) a behavior-aware conditional diffusion model consisting of a reference selection module and a conditional attentional denoising network to impute utility data in a computationally efficient manner. We implement and evaluate MBDiff by collaborating with one of the largest municipal utility providers in Florida. Experimental results demonstrate our proposed MBDiff effectively outperforms state-of-the-art baselines, e.g., it improves 7.04% and 29.1% on the electricity and water usage datasets for block missingness imputation, respectively.

## Metadata
- **Published**: 2026-07-31T08:58:54Z
- **Authors**: Rongchao Xu, Lin Jiang, Dahai Yu, Ximiao Li, Guang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29177v1)