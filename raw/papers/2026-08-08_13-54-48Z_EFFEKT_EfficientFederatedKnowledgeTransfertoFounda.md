---
title: EFFEKT: Efficient Federated Knowledge Transfer to Foundation Models
published: 2026-08-08T13:54:48Z
authors: Matteo Caligiuri, Francesco Barbato, Pietro Zanuttigh, Francesco Restuccia
url: http://arxiv.org/abs/2608.08138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EFFEKT: Efficient Federated Knowledge Transfer to Foundation Models

## Abstract
Recent data protection laws have accelerated the adoption of Federated Learning (FL) for privacy-preserving decentralized training. Nevertheless, increasing model sizes impose substantial computational demands on client devices, limiting FL applicability in resource-constrained settings. We introduce a novel multi-domain federated learning framework in which lightweight client-side proxy models collaborate with a server-side Foundation Model (FM) to learn new concepts without sharing private data. Our approach, EFFEKT, enables efficient server-side training of domain-specific LoRA adapters while preserving feature-space alignment between the FM and proxy extractors via novel bi-directional cross-distillation strategies. Experiments on multiple real-world datasets and deployments on low-power edge devices demonstrate improvements over state-of-the-art baselines in most considered domains while maintaining lightweight computation at the client side.

## Metadata
- **Published**: 2026-08-08T13:54:48Z
- **Authors**: Matteo Caligiuri, Francesco Barbato, Pietro Zanuttigh, Francesco Restuccia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08138v1)