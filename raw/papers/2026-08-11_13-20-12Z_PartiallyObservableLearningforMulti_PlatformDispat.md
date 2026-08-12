---
title: Partially Observable Learning for Multi-Platform Dispatch Optimization
published: 2026-08-11T13:20:12Z
authors: Fengming Yao, Man Luo
url: http://arxiv.org/abs/2608.10897v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Partially Observable Learning for Multi-Platform Dispatch Optimization

## Abstract
Instant delivery platforms have become a critical component of urban logistics, increasingly relying on crowdsourced couriers to fulfill highly dynamic orders. In real-world systems, couriers are not exclusive to a single platform and may concurrently serve multiple platforms, while each platform can only observe its own orders and couriers' interactions due to privacy and operational constraints. This results in a multi-platform dispatch environment with inherent partial observability. However, most existing works on dispatch optimization assume full courier observability and mandatory assignment acceptance, causing substantial performance degradation when deployed in realistic multi-platform settings. In this paper, we propose POLO, a partially observable multi-agent reinforcement learning framework for dispatching optimization in multi-platform instant delivery systems. POLO firstly models each platform-grid pair as an independent agent that learns dispatch policies solely from platform-local observations, aligning the learning process with real-world privacy and operational constraints. To support effective decision-making under incomplete and heterogeneous courier information, POLO introduces a novel attention-based policy representation that selectively aggregates inter-courier information. Moreover, we design a counterfactual reward shaping mechanism to mitigate the non-stationarity induced by joint actions across grids, leading to more stable and scalable learning. We develop a high-fidelity simulator to evaluate dispatch performance under varying numbers of platforms and system scales. Extensive experiments demonstrate that POLO consistently outperforms strong baselines in terms of platform revenue and courier travel efficiency, highlighting its robustness and effectiveness in realistic multi-platform settings.

## Metadata
- **Published**: 2026-08-11T13:20:12Z
- **Authors**: Fengming Yao, Man Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10897v1)