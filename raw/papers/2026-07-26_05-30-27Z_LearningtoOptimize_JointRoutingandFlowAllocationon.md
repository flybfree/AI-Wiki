---
title: Learning to Optimize: Joint Routing and Flow Allocation on Sparse Non-Euclidean Networks
published: 2026-07-26T05:30:27Z
authors: Haomiao Sun, Fang He, Congyuan Ji, Xindi Tang
url: http://arxiv.org/abs/2607.23467v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Optimize: Joint Routing and Flow Allocation on Sparse Non-Euclidean Networks

## Abstract
We study an integrated pickup-and-delivery problem on sparse, non-Euclidean networks that jointly optimizes cyclic routing, cargo flow allocation, and cross-cycle service. The tight coupling of these operational constraints creates a complex discrete-continuous decision space with highly restricted feasible regions. To overcome these computational challenges, we propose Double-Channel Graph Attention (DCGA), an end-to-end reinforcement learning framework. DCGA isolates network reachability and demand-service logic into separate graph channels and constructs valid routes using a simulator-coupled, constraint-informed decoder. Experiments on LinerLib benchmarks demonstrate that DCGA achieves seconds-level inference and delivers state-of-the-art solution quality on instances beyond a specific scale, with its advantage over existing baselines widening significantly as problem size increases. Supported by extensive stability and ablation analyses, our results demonstrate that this structure-aware learning approach provides an effective, low-latency engine for realistic routing-and-flow optimization.

## Metadata
- **Published**: 2026-07-26T05:30:27Z
- **Authors**: Haomiao Sun, Fang He, Congyuan Ji, Xindi Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23467v1)