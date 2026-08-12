---
title: SeFoRA: Sketch-Aggregated Federated Low-Rank Adaptation with Heterogeneous Client Ranks
published: 2026-08-10T18:59:25Z
authors: Yue Xia, Tayyebeh Jahani-Nezhad, Mayank Bakshi, Rawad Bitar
url: http://arxiv.org/abs/2608.10144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SeFoRA: Sketch-Aggregated Federated Low-Rank Adaptation with Heterogeneous Client Ranks

## Abstract
We consider federated parameter efficient fine-tuning of large neural networks with low-rank adaptation (LoRA,~Hu et al.\ 2022). Combining LoRA with federated PEFT introduces challenges absent from either setting alone: clients may use different LoRA ranks, making their factor matrices dimension-incompatible, and factor-wise averaging suffers from a bilinear mismatch. We propose SeFoRA, a sketch-aggregated federated LoRA algorithm in which each client transmits a linear sketch of its local updates, enabling direct aggregation at the federator. As a result, SeFoRA alleviates the bilinear mismatch, and allows for aggregation in a small subspace of the full model. We introduce a rank-homogeneous version called SeFoRA-Ho which allows for direct adapter aggregation in this setting. We prove convergence to a neighborhood of the first-order stationary point at rate $\cO(1/T)$ for the rank-homogeneous setting. Numerical experiments on fine-tuning RoBERTa-Large on GLUE datasets show how our algorithms outperform the state-of-the-art.

## Metadata
- **Published**: 2026-08-10T18:59:25Z
- **Authors**: Yue Xia, Tayyebeh Jahani-Nezhad, Mayank Bakshi, Rawad Bitar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10144v1)