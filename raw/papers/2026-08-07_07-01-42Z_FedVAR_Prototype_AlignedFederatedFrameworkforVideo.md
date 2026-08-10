---
title: FedVAR: Prototype-Aligned Federated Framework for Video Anomaly Recognition
published: 2026-08-07T07:01:42Z
authors: Ghani Haider, Majid Kundroo, Boyun Eom, Dong Hwan Park, Chen Chen, Taehong Kim
url: http://arxiv.org/abs/2608.06876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedVAR: Prototype-Aligned Federated Framework for Video Anomaly Recognition

## Abstract
In the era of Industrial Internet of Things (IIoT) and Cyber-Physical Systems (CPS), Federated Learning (FL) offers a promising decentralized intelligence paradigm for Video Anomaly Recognition (VAR). This task is vital for maintaining high-fidelity Digital Twins and ensuring safety in mission-critical environments. However, the inherent data heterogeneity across distributed edge clients leads to a fundamental challenge known as semantic misalignment, where clients learn divergent feature representations of "normal" and "abnormal" events. The problem becomes particularly pronounced in VAR, where the presence of diverse and fine-grained anomaly categories leads each client to develop distinct semantic interpretations of abnormality. Existing federated methods primarily focus on binary anomaly detection and fail to address this misalignment, preventing effective fine-grained recognition. In this paper, we introduce FedVAR, a weakly-supervised FL framework explicitly designed for VAR. Leveraging the rich representations of Vision-Language Models (VLMs), FedVAR employs a prototype-based alignment mechanism that creates a shared semantic anchor for all clients to re-center and align their visual and textual feature spaces. This process enforces a consistent representation of "normality" across the decentralized network, directly mitigating semantic misalignment and enabling robust prompt-learning of anomaly direction vectors with minimal communication overhead. We conduct extensive experiments on challenging benchmarks under various non-IID data partitioning schemes, unseen domains, and novel anomaly classes. The results demonstrate that FedVAR consistently outperforms state-of-the-art federated baselines, establishing a robust framework for distributed intelligence in video-based CPS.

## Metadata
- **Published**: 2026-08-07T07:01:42Z
- **Authors**: Ghani Haider, Majid Kundroo, Boyun Eom, Dong Hwan Park, Chen Chen, Taehong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06876v1)