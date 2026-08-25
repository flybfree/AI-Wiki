---
title: Federated Continual Learning as a Distributed Drift-Plus-Penalty Control Problem
published: 2026-08-21T18:21:19Z
authors: Nazreen Shah, Naveen Kumar Reddy Somireddy, Zubair Shaban, Ranjitha Prasad, B. N. Bharath
url: http://arxiv.org/abs/2608.21539v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Federated Continual Learning as a Distributed Drift-Plus-Penalty Control Problem

## Abstract
Federated Continual Learning (FCL) is fundamental to real-world distributed learning systems, requiring models to adapt to sequential, non-IID data across clients while mitigating catastrophic forgetting and client drift. Existing approaches formulate continual learning (CL) as a sequence of per-task optimization problems, applied locally at each client and coupled through aggregation, using heuristic mechanisms such as replay, regularization, or projection-based constraints. However, forgetting in FCL is inherently a long-term, distributed phenomenon, arising from the interaction of temporal task evolution and cross-client heterogeneity, which is not explicitly regulated. In this work, we cast FCL as a stochastic control problem and propose Federated Queue-regulated Continual Learning (FedQCL), a framework based on Lyapunov drift-plus-penalty (DPP) optimization. FedQCL introduces virtual queues to track the accumulation of forgetting across tasks and clients, enabling explicit control of the stability-plasticity trade-off. By optimizing a DPP objective, the method jointly improves current-task performance while the queue-based formulation provides an interpretable and tunable mechanism to balance adaptation and retention through a single parameter, without requiring gradient projection or additional communication overhead. Empirical evaluations on standard benchmarks, including Split-CIFAR-10, Split-CIFAR-100, and Split-TinyImageNet, demonstrate that FedQCL outperforms state-of-the-art baselines with respect to accuracy while significantly reducing forgetting under heterogeneous data distributions.

## Metadata
- **Published**: 2026-08-21T18:21:19Z
- **Authors**: Nazreen Shah, Naveen Kumar Reddy Somireddy, Zubair Shaban, Ranjitha Prasad, B. N. Bharath
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21539v1)