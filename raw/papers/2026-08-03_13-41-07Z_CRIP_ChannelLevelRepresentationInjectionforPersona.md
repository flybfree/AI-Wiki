---
title: CRIP: Channel Level Representation Injection for Personalized One-Shot Federated Learning
published: 2026-08-03T13:41:07Z
authors: Zijian Jiang, Chaoli Sun, Handing Wang, Xilu Wang
url: http://arxiv.org/abs/2608.02222v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRIP: Channel Level Representation Injection for Personalized One-Shot Federated Learning

## Abstract
One-shot federated learning (OSFL) has emerged as a promising collaborative model learning framework with only a single round of communication, offering significant advantages in communication efficiency and privacy preservation. However, OSFL often faces inherent limitations under severe domain heterogeneity across clients due to the lack of iterative knowledge exchange. Most existing OSFL methods require an auxiliary public dataset for knowledge distillation or leverage statistical information for parameter-level aggregation, overlooking feature shift caused by domain heterogeneity. To address these challenges, we propose CRIP, a personalized OSFL framework that operates in the representation space via channel-level feature alignment. To achieve this, each client uploads its feature extractor to the server, which broadcasts all extractors back to every client. Since not all source clients share compatible feature distributions with the target client, indiscriminate fusion of cross-client features would introduce domain-specific noise. Therefore, CRIP effectively measures the channel-wise representational similarity between the target client and each source client on a small local mini-batch, and selectively fuses only the most compatible features. Extensive experiments on domain-heterogeneous benchmarks such as DomainNet, PACS, and Office-Home demonstrate that CRIP consistently outperforms local models and state-of-the-art baselines, validating the effectiveness of representation-space personalization under extreme domain heterogeneity.

## Metadata
- **Published**: 2026-08-03T13:41:07Z
- **Authors**: Zijian Jiang, Chaoli Sun, Handing Wang, Xilu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02222v1)