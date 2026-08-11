---
title: FedA2L: Adaptive layer-wise learning rate adjustment in decentralized federated learning
published: 2026-08-10T07:27:21Z
authors: Van Truong Vo, Khoa Nguyen, Taehong Kim
url: http://arxiv.org/abs/2608.09208v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedA2L: Adaptive layer-wise learning rate adjustment in decentralized federated learning

## Abstract
Decentralized intelligence systems with heterogeneous devices and limited coordination increasingly rely on decentralized federated learning (DFL). However, DFL suffers from convergence inefficiency under data heterogeneity due to the use of a uniform learning rate (LR) that ignores layer-specific optimization needs. Foundational layers are responsible for maintaining network consensus, while specialized layers adapt to local data characteristics, leading to conflicting gradients and degraded performance under non-IID conditions. To address this fundamental tension, this work introduces FedA2L, a method that dynamically adjusts layer-wise LRs based on model divergence signals. By leveraging local update intensity and network consensus constraints, FedA2L seamlessly integrates into existing DFL protocols without additional communication or coordination. Extensive evaluations across DFL algorithms, various model architectures, and datasets demonstrate that FedA2L achieves up to 4.94 times faster convergence than vanilla DFL and reduces communication rounds by up to 59% compared to scheduler-based baselines. Furthermore, FedA2L exhibits resilience to severe data heterogeneity, larger network sizes, and sparse topologies, reducing communication overhead and establishing it as a versatile optimization tool for resource-constrained or large-scale distributed learning in edge and IoT deployments. The code is released at https://github.com/nclabteam/FedA2L.

## Metadata
- **Published**: 2026-08-10T07:27:21Z
- **Authors**: Van Truong Vo, Khoa Nguyen, Taehong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09208v1)