---
title: FedWeave: Rethinking the Unit of Specialization in Heterogeneous Federated MoE-LoRA
published: 2026-07-29T08:47:58Z
authors: Donghang Duan, Xu Zheng, Lizong Zhang, Chong Mu, Meng Han
url: http://arxiv.org/abs/2607.26618v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedWeave: Rethinking the Unit of Specialization in Heterogeneous Federated MoE-LoRA

## Abstract
Federated PEFT enables LLMs to collaboratively adapt to decentralized private data without sharing raw examples. However, task heterogeneity across clients can cause cross-task interference and gradient conflicts during aggregation. Federated MoE-LoRA addresses this challenge through specialized LoRA experts and conditional routing. Yet existing methods typically specialize at client granularity, implicitly assuming task-coherent clients. Our core insight is that experts need purity, namely pattern-coherent updates that preserve specialization, whereas routers need contrast, namely mixed-task observations that support expert comparison. We propose FedWeave, a framework that adopts asymmetric aggregation, separating expert aggregation from router optimization to meet these two requirements. FedWeave uses unsupervised prototype discovery to form local buckets and align them across clients, enabling prototype-level expert aggregation while retaining mixed-task client trajectories for router training. At inference, FedWeave performs sparse inference with one active expert while preserving nearly all soft-routing performance. Our theoretical analysis explains why asymmetric aggregation is advantageous: it controls expert convergence in stationarity through off-pattern contamination, identifies the consensus error induced by fragmented router trajectories, and bounds sparse-inference risk. On a heterogeneous multi-task benchmark with mainstream LLM backbones, FedWeave consistently outperforms strong baselines, while ablations verify the effectiveness of our design.

## Metadata
- **Published**: 2026-07-29T08:47:58Z
- **Authors**: Donghang Duan, Xu Zheng, Lizong Zhang, Chong Mu, Meng Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26618v1)