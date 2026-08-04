---
title: HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference
published: 2026-08-01T10:30:01Z
authors: Xin Yuan, Ning Li, Wenchao Xu, Athanasios V. Vasilakos, Song Guo, Haijun Zhang
url: http://arxiv.org/abs/2608.00577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference

## Abstract
Mixture-of-Experts (MoE) models have become a dominant architecture for large-scale AI services, yet deploying them over geo-distributed heterogeneous edge servers remains challenging. When the Top-k activated experts of a token are spread across multiple servers, the optimal routing depends jointly on cross-server link bandwidth, heterogeneous GPU computing capability, GPU-CPU expert loading delay, instantaneous queueing backlog, and replica-level quantization quality loss. Existing distributed inference and MoE serving methods address these factors separately and do not provide a unified framework for online multi-server collaborative routing. In this paper, we propose HetRoute, a heterogeneous-cost-aware collaborative routing framework for distributed edge MoE inference. HetRoute introduces a unified per-assignment cost model that explicitly captures four cost components: cross-server transmission, GPU-CPU offloading, GPU computation with queueing, and quantization-induced quality penalty. Guided by this model, the offline stage determines expert server placement, GPU-CPU residency, and replica precision through a routing-cost-coupled deployment algorithm, while the online stage routes the Top-k activated expert set as a whole by minimizing the bottleneck layer cost via exact enumeration or beam search. Theoretical analysis establishes fallback feasibility, a bound on the number of participating servers, per-layer optimality for small candidate domains, and online computational complexity. Trace-driven evaluation on three MoE models over a heterogeneous 10-server edge testbed shows that HetRoute reduces average inference latency by up to 59.0% and P99 latency by up to 58.0%, cuts cross-server traffic by up to 72.1%, and achieves 2.13x throughput improvement compared with representative baselines, while keeping quality degradation within the configured budget.

## Metadata
- **Published**: 2026-08-01T10:30:01Z
- **Authors**: Xin Yuan, Ning Li, Wenchao Xu, Athanasios V. Vasilakos, Song Guo, Haijun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00577v1)