---
title: FedTaste: Topology-Aware Structural Transfer for Multimodal Federated Learning with Missing Modalities
published: 2026-07-25T15:11:58Z
authors: Haochen Liang, Jie Zhang, Hideya Ochiai
url: http://arxiv.org/abs/2607.23245v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedTaste: Topology-Aware Structural Transfer for Multimodal Federated Learning with Missing Modalities

## Abstract
Multimodal Federated Learning is often challenged by arbitrary modality missingness and Non-IID data distributions, which lead to severe representation drift and hinder effective collaboration across clients. Existing methods typically rely on generative imputation, external auxiliary data, or isolated unimodal training to bridge modality gaps, often incurring substantial communication and computational costs as well as potential privacy risks. To address these limitations, we propose FedTaste, a parameter-efficient framework for topology-aware structural transfer in Multimodal Federated Learning with missing modalities. Instead of aligning fragile first-order features, FedTaste focuses on more stable group-level semantic relations. Specifically, FedTaste leverages frozen foundation models to extract a joint multimodal topology from full-modality clients, which is then consolidated by the server into a global structural blueprint. To adapt clients with missing modalities, we introduce Modality-Adaptive Structural Prompts together with spectral consistency regularization, enabling lightweight branch-specific adaptation that aligns local partial representations with the shared blueprint. In this way, FedTaste avoids explicit modality imputation while preserving shared semantic structure across clients. Extensive experiments demonstrate that FedTaste consistently achieves superior performance across multiple datasets and challenging Non-IID settings, while substantially reducing communication overhead compared with existing methods.

## Metadata
- **Published**: 2026-07-25T15:11:58Z
- **Authors**: Haochen Liang, Jie Zhang, Hideya Ochiai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23245v1)