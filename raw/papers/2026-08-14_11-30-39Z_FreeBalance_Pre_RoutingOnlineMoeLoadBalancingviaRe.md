---
title: FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction
published: 2026-08-14T11:30:39Z
authors: Pengfei Chen, Yize Wu, Shouxu Kuang, Ke Gao, Ling Li
url: http://arxiv.org/abs/2608.14205v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction

## Abstract
Load imbalance poses a major bottleneck to the efficiency of expert parallelism in distributed inference of Mixture-of-Experts (MoE) models. The most heavily loaded rank stalls global execution due to skewed routing distributions, directly increasing latency. While offline expert placement can alleviate persistent imbalance, practical multi-task serving workloads exhibit layer- and batch-dependent routing dynamics, making online load balancing indispensable. Existing approaches rely on routing statistics collected after each MoE router, requiring expert weight load or migration to begin only after routing decisions are available, consequently placing migration overhead on the inference critical path. In this work, we observe that online balancing can instead be largely overlapped with computation before target routing (e.g., attention), if routing distributions can be predicted accurately in advance. Therefore, we propose FreeBalance, a lossless online load-balancing framework that overlaps expert migration with preceding computation stages via residual workload prediction. FreeBalance leverages cross-layer similarities in hidden representations within the residual network to build a lightweight workload predictor. This enables proactive expert migration planning before routing decisions are available, creating substantial overlap between weight transfer and computation-heavy pre-routing stages. Furthermore, a cost model constrains the number of swaps to fully hide the synchronization overhead within the available window. Experiments across models and datasets show that FreeBalance reduces the max-to-mean rank load ratio by 32.8% and end-to-end prefill latency by 13.1%. Specifically, our method hides balancing overhead of an average of 5.1 experts per layer, which would otherwise account for about 8.5% of the critical-path latency.

## Metadata
- **Published**: 2026-08-14T11:30:39Z
- **Authors**: Pengfei Chen, Yize Wu, Shouxu Kuang, Ke Gao, Ling Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14205v1)