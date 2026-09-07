---
title: PLUME: Parameter-Efficient Personalization of Large Language Models via Low-Rank User Modulation in Shared Subspaces
published: 2026-09-04T04:38:50Z
authors: Xinyu Li, Hao Zhou, Jianfeng Zhu, Julina Maharjan, Ruixin Guo, Feodor Dragan, Ruoming Jin
url: http://arxiv.org/abs/2609.04715v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PLUME: Parameter-Efficient Personalization of Large Language Models via Low-Rank User Modulation in Shared Subspaces

## Abstract
Personalizing large language models (LLMs) is essential for delivering AI assistance that aligns with individual users' styles, intents, and preferences. While per-user fine-tuning can substantially enhance personalization quality, it introduces significant parameter and storage overhead, limiting scalability to large user populations. We propose PLUME (Personalized Low-Rank Adaptation through User Modulation and Shared Subspace), a lightweight framework that achieves efficient and expressive per-user adaptation by leveraging a shared task-specific subspace. Specifically, PLUME first learns a global task subspace from aggregated user data. Personalization is then achieved by training only a lightweight small square matrix within this subspace, enabling each user to obtain a tailored model while keeping shared components fixed. Cross-layer shared parameters and rank-1 residual terms are further introduced to significantly reduce redundancy while maintaining expressiveness. Experiments on multiple personalized text generation benchmarks demonstrate that PLUME achieves comparable or superior performance to strong baselines, while reducing per-user parameters by over 95%. These results establish shared-subspace modulation with minimal residuals as a scalable and semantically grounded approach to LLM personalization.

## Metadata
- **Published**: 2026-09-04T04:38:50Z
- **Authors**: Xinyu Li, Hao Zhou, Jianfeng Zhu, Julina Maharjan, Ruixin Guo, Feodor Dragan, Ruoming Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04715v1)