---
title: Decentralized Federated Learning for Heterogeneous Multi-Task Semantic Communication
published: 2026-08-15T14:22:58Z
authors: Lin Yin, Tiejun Lv, Weicai Li, Xi Yu, Xiaoyu He
url: http://arxiv.org/abs/2608.15256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decentralized Federated Learning for Heterogeneous Multi-Task Semantic Communication

## Abstract
Collaborative training in distributed semantic communication (DSC) networks typically relies on decentralized federated learning (DFL). However, pushing topology-agnostic aggregation into heterogeneous, multi-task environments creates a fundamental bottleneck: it drives negative transfer and overconsensus bias (OCB). This paper introduces a personalized DSC framework that cuts off this cross-task interference. At the node level, a policy-driven multi-path routing mechanism separates task-specific features from shared representations to preserve local fidelity. Across the network, we deploy a "communicationwhile- aggregation" protocol. It calibrates a column-stochastic consensus matrix using task affinities. This limits the system to absorbing complementary knowledge while actively blocking mismatched parameter updates. To bound the convergence, we derive a unified Lyapunov drift analysis. We reveal a strict Ushaped trade-off: deeper topological mixing reduces variance but amplifies structural OCB. Resolving this tension yields a closed-form expression for the optimal aggregation depth. We evaluate the proposed framework on NYU-v2, where the results reveal a clear trade-off between insufficient aggregation and excessive topological mixing. At the analytically derived optimal aggregation depth, our method achieves a 4.77% global relative improvement over the no-aggregation baseline and outperforms decentralized FedAvg, FedAMP, and heuristic max aggregation. We further evaluate the framework on Taskonomy and imperfect wireless links to examine the effects of network-size variation and wireless-link reliability.

## Metadata
- **Published**: 2026-08-15T14:22:58Z
- **Authors**: Lin Yin, Tiejun Lv, Weicai Li, Xi Yu, Xiaoyu He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15256v1)