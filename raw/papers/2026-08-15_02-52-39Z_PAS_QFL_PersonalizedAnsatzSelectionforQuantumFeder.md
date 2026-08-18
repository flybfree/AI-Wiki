---
title: PAS-QFL: Personalized Ansatz Selection for Quantum Federated Learning under Client Data Heterogeneity
published: 2026-08-15T02:52:39Z
authors: Jindi Wu, Qun Li
url: http://arxiv.org/abs/2608.14995v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PAS-QFL: Personalized Ansatz Selection for Quantum Federated Learning under Client Data Heterogeneity

## Abstract
Quantum federated learning (QFL) lets multiple quantum clients collaboratively train quantum neural networks (QNNs) without sharing private local data. However, existing QFL methods commonly assume that all clients use the same ansatz, overlooking how heterogeneous client data affects ansatz suitability. Under class-imbalanced non-IID data, different clients may favor different ansatz structures, so a fixed ansatz can lead to unstable and unfair performance across clients. In this paper, we propose PAS-QFL, a Personalized Ansatz Selection framework for QFL under client data heterogeneity. Rather than treating the ansatz as a monolithic structure, PAS-QFL decomposes each client QNN into a globally shared ansatz and a client-specific private ansatz, and personalizes the structure of the private ansatz rather than only its parameters. The shared ansatz is placed first and selected by a stability-aware cross-client criterion so that its parameters can be reliably aggregated, while the private ansatz serves as a personalized decision head, selected per client by local Macro-F1 to adapt the shared representation to its local data. During training, each client updates both its shared and private parameters locally but uploads only the shared parameters, so federated aggregation stays well-defined while each client keeps its own private structure. PAS-QFL uses Macro-F1 as the primary selection metric to avoid misleading accuracy under class imbalance. Experiments on heterogeneous QFL tasks show that PAS-QFL improves average Macro-F1 over the existing fixed-ansatz QFL baselines, demonstrating the value of personalizing the ansatz structure for practical QFL.

## Metadata
- **Published**: 2026-08-15T02:52:39Z
- **Authors**: Jindi Wu, Qun Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14995v1)