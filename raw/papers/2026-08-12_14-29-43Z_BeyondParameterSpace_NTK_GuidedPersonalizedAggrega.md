---
title: Beyond Parameter Space: NTK-Guided Personalized Aggregation for Robust Federated Learning
published: 2026-08-12T14:29:43Z
authors: Mirko Konstantin, Stefan Zachow, Anirban Mukhopadhyay
url: http://arxiv.org/abs/2608.12108v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Parameter Space: NTK-Guided Personalized Aggregation for Robust Federated Learning

## Abstract
Federated learning (FL) enables collaborative model training across distributed clients while keeping data local. A central challenge is determining which client updates are beneficial for aggregation with respect to each client's target domain. Existing methods typically address this problem in parameter space by comparing model parameters or gradients. However, parameter-space similarity can be a poor proxy for predictive behavior, especially under heterogeneous, non-IID data. Consequently, updates that are misaligned with a client's target domain, including those caused by heterogeneous data or malfunctioning clients, may degrade local model performance.   We propose Local Inference Guided Aggregation for Heterogeneous Training Environments to Yield Enhancement Through Agreement and Regularization (LIGHTYEAR), a federated learning framework that performs update selection in function space. LIGHTYEAR uses an NTK-based agreement score to characterize predictive behavior and determine a personalized aggregation set for each client. By relating model parameters to local predictive responses, the Neural Tangent Kernel (NTK) provides a more expressive criterion for update selection than parameter-space similarity alone.   Because function-space information is not available before aggregation in conventional centralized FL, LIGHTYEAR uses a peer-to-peer (P2P) topology in which clients exchange updates directly and evaluate incoming models on private validation data. Each client selects only updates that are beneficial for its own target domain and aggregates them using a regularized rule that improves stability under heterogeneity.   Across five datasets and nine baseline methods, LIGHTYEAR consistently outperforms centralized FL baselines and existing P2P approaches.

## Metadata
- **Published**: 2026-08-12T14:29:43Z
- **Authors**: Mirko Konstantin, Stefan Zachow, Anirban Mukhopadhyay
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12108v1)