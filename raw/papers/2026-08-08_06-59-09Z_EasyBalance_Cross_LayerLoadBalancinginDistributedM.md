---
title: EasyBalance: Cross-Layer Load Balancing in Distributed MoE Inference
published: 2026-08-08T06:59:09Z
authors: Yize Wu, Ke Gao, Ling Li, Yanjun Wu
url: http://arxiv.org/abs/2608.07964v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EasyBalance: Cross-Layer Load Balancing in Distributed MoE Inference

## Abstract
Load Balancing has emerged as a critical problem in expert-parallel distributed inference of Mixture-of-Experts (MoE) models. As routing distributions are typically skewed across experts, devices hosting lighter-loaded experts must idle to wait for the heaviest during expert computing, leading to inefficiency. Existing load-balancing approaches primarily rely on expert replication or migration within each layer, which introduce additional overhead and limit their flexibility and scalability. To address this problem, we propose EasyBalance, a cross-layer load balancing strategy that requires no modifications to the expert-device mapping, enabling instant adaptability and incurring essentially no additional overhead. Our key insights are that (1) experts of other layers can be viewed as naturally redundant for the current layer, and (2) cross-layer MoE workloads can be jointly executed to mitigate their individual imbalance. Based on these observations, EasyBalance greedily schedules a subset of cross-layer workloads to run at each MoE step and defers the remaining workloads for future balancing opportunities, effectively leveraging cross-layer imbalance mitigation. Extensive experiments across models, tasks, and configurations demonstrate that EasyBalance consistently accelerates distributed MoE inference, reducing GPU idling by mostly over 40%. Code is available at https://github.com/yize-wu/EasyInfra.

## Metadata
- **Published**: 2026-08-08T06:59:09Z
- **Authors**: Yize Wu, Ke Gao, Ling Li, Yanjun Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07964v1)