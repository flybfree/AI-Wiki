---
title: FedADB: Class Anchor-Driven Dual-Branch Federated Learning for Mitigating Forgetting
published: 2026-08-15T16:28:23Z
authors: Zhenyan Liu, Hua Zhang, Haoran Gao, Qi Li, Hongliang Zhu, Huiyu Zhou, Zongliang Shen, Yanxin Xu, Jiahui Wang
url: http://arxiv.org/abs/2608.15310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedADB: Class Anchor-Driven Dual-Branch Federated Learning for Mitigating Forgetting

## Abstract
Multimodal data collected by heterogeneous devices are used for collaborative training, where federated learning (FL) serves as a key paradigm for effective distributed modeling with data privacy preservation. However, local training suffers from the forgetting of previously learned global knowledge under cross-client data heterogeneity, which leads to significant declines in both performance and convergence speed. Most previous studies rely on global alignment strategies to retain global knowledge, which hinder local optimization and lead to inadequate supervision of missing classes. Some studies introduce proxy datasets to supplement supervision for missing classes. However, it remains a challenge to balance class-wise global consistency and local optimization objectives without proxy datasets. In this work, we propose FedADB, a Class Anchor-Driven Dual-Branch FL framework. Specifically, the server generates class anchors optimized in a differentiable input space, which are shared across clients. These class anchors serve as global references that provide supervision for missing classes during local training. A dual-branch collaborative training mechanism is designed for clients. In this mechanism, the anchor-based global branch focuses on learning with global consistency, achieving global knowledge alignment by class-anchor balanced sampling. The local calibration branch focuses on learning discriminative local features, mitigating the degradation of local representations caused by excessive global alignment. Extensive experiments across multiple medical and natural datasets demonstrate that FedADB achieves significant improvements in both accuracy and convergence speed.

## Metadata
- **Published**: 2026-08-15T16:28:23Z
- **Authors**: Zhenyan Liu, Hua Zhang, Haoran Gao, Qi Li, Hongliang Zhu, Huiyu Zhou, Zongliang Shen, Yanxin Xu, Jiahui Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15310v1)