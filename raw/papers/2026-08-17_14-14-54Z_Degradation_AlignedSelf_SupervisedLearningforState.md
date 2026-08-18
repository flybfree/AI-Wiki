---
title: Degradation-Aligned Self-Supervised Learning for State of Health Estimation of Lithium-Ion Batteries under Label Sparsity
published: 2026-08-17T14:14:54Z
authors: Jiaqi Yao, Julia Kowal
url: http://arxiv.org/abs/2608.16612v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Degradation-Aligned Self-Supervised Learning for State of Health Estimation of Lithium-Ion Batteries under Label Sparsity

## Abstract
An accurate estimation of the state of health (SOH) underpins a safe and optimized use of the battery system. Although compelling, data-driven SOH estimation models typically require large amounts of high-quality labeled cycling data, while in practice such labels are often sparse in both quantity and coverage. Therefore, in this work, we propose a degradation-aligned self-supervised learning (SSL) framework based on a convolutional neural network-gated recurrent unit (CNN-GRU) model, which learns aging-consistent representations from unlabeled data through a cycle-order ranking objective as the pretext task for pretraining, thereby enabling robust SOH estimation after fine-tuning on sparsely labeled data. Test results showcase that the proposed ranking-based SSL approach proves to endow the pretrained model with degradation-aligned information from unlabeled data, and after fine-tuning the model can carry out accurate, robust SOH estimation, even when only an extremely limited amount of 1% of unevenly distributed labeled training data is available, where the MAE of 1.718% and RMSE of 2.329% can be achieved on the test cell. In addition, in-depth analyses are presented regarding the influences of label distribution of battery degradation data. We believe this work could shed new light on SOH estimation of lithium-ion batteries under label sparsity in real-world applications.

## Metadata
- **Published**: 2026-08-17T14:14:54Z
- **Authors**: Jiaqi Yao, Julia Kowal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16612v1)