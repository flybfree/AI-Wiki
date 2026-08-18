---
title: UniFed-VLM: Federated Instruction Tuning for Vision-Language Models with Multiple Heterogeneity
published: 2026-08-16T04:01:04Z
authors: Pengyu Wang, Baochen Xiong, Xiaoshan Yang, Yifan Xu, Zhang Qimeng, Haifeng Chen, Changsheng Xu
url: http://arxiv.org/abs/2608.15516v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UniFed-VLM: Federated Instruction Tuning for Vision-Language Models with Multiple Heterogeneity

## Abstract
Vision-Language Models (VLMs) have demonstrated strong performance in multimodal understanding and generation. However, fine-tuning of VLMs typically relies on centralized data, which raises privacy concerns in certain domains (e.g. healthcare). Federated Learning (FL) provides a natural solution by enabling model training without sharing raw data. However, applying FL to VLM instruction tuning is highly challenging. VLMs have substantial parameter scales, and in real-world scenarios, clients exhibit significant heterogeneity in tasks, modalities, and model architectures.   Existing methods mainly focus on simplified settings and are unable to handle such multi-dimensional heterogeneous scenarios. In this work, we study federated instruction tuning under joint heterogeneity in tasks, modalities, and model architectures.   We propose UniFed-VLM, a unified federated instruction tuning framework for VLMs that addresses multiple types of heterogeneity. It consists of two key components: 1) Federated Compensated Subspace Aggregation (FedCSA), which performs subspace-aligned aggregation of parameter-efficient adapters with dynamic weighting and compensation to mitigate heterogeneity-induced conflicts; 2) Two-stage Collaborative Distillation (TCoD), which enables effective knowledge transfer across heterogeneous models via a Mutual Distillation Adapter (MDA) and a mixture-of-experts-based distillation strategy. We conduct experiments on multiple benchmark datasets, and the results show that UniFed-VLM achieves stronger average performance across diverse tasks compared with existing FL methods. The source code is available at: https://github.com/wangpengyu2004/UniFed-VLM.

## Metadata
- **Published**: 2026-08-16T04:01:04Z
- **Authors**: Pengyu Wang, Baochen Xiong, Xiaoshan Yang, Yifan Xu, Zhang Qimeng, Haifeng Chen, Changsheng Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15516v1)