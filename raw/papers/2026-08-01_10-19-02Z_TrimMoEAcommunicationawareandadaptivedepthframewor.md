---
title: TrimMoE A communication aware and adaptive depth framework for distributed edge inference
published: 2026-08-01T10:19:02Z
authors: Ning Li, Shuting Bai, Xin Yuan, Wenchao Xu, Athanasios V. Vasilakos, Song Guo, Haijun Zhang
url: http://arxiv.org/abs/2608.00573v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrimMoE A communication aware and adaptive depth framework for distributed edge inference

## Abstract
Serving Mixture-of-Experts (MoE) large language models across distributed edge servers is bottlenecked by the cross-server expert transmission. The existing approaches mainly focus on how to reach a remote expert faster. However, in this paper, we instead consider whether a given layer, and the layers after it, need to be executed at all. To this end, a communication-aware adaptive-depth framework is proposed in this paper, termed TrimMoE, which couples layer skipping and confidence-based early exit with substitute execution and server-expert selection under a unified quality budget. Specifically, in the offline stage, TrimMoE freezes the backbone, trains the lightweight per-layer exit heads, calibrates the per-layer importance thresholds, and allocates the expert replicas by a skip/exit-aware redundancy benefit. In the online stage, a transition-aware look-ahead anticipates the token movement, so that the depth reduction targets the costliest transmissions, and besides, two feedback rules adapt the delay-quality weights and the exit threshold. Moreover, we prove that the substitution-and-skipping proxy degradation never exceeds the configured budget, and that the early exit is admitted only under a calibrated confidence gate. On a heterogeneous 10-server testbed with Switch-Base-8E, Qwen-MoE-A2.7B, and Mixtral-8x7B, TrimMoE reduces the average latency by up to 62.8%, lowers the cross-server traffic and the remote-execution ratio, and sustains high throughput under load, while keeping the task-quality degradation within a 2% bound.

## Metadata
- **Published**: 2026-08-01T10:19:02Z
- **Authors**: Ning Li, Shuting Bai, Xin Yuan, Wenchao Xu, Athanasios V. Vasilakos, Song Guo, Haijun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00573v1)