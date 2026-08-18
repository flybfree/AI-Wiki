---
title: MoE Router-Guided Clustering for Heterogeneous Federated Instruction Tuning
published: 2026-08-15T16:35:12Z
authors: Ankita Sharma, Bahar Farahani, Sanaz Rahimi Moosavi, Amir Rrahmani, Farshad Firouzi, Krishnendu Chakrabarty
url: http://arxiv.org/abs/2608.15311v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoE Router-Guided Clustering for Heterogeneous Federated Instruction Tuning

## Abstract
Federated instruction fine-tuning enables Large Language Models (LLMs) to adapt to decentralized, privacy-sensitive data without requiring data sharing. Recent Mixture-of-Experts (MoE) LLMs are particularly attractive for federated learning because their sparse activation reduces computation and communication while scaling model capacity. However, existing federated MoE methods primarily focus on parameter aggregation and personalization, overlooking the routing behavior of MoE models as a source of information for client collaboration. Under heterogeneous instruction distributions, indiscriminate aggregation can lead to negative transfer, highlighting the need to identify which clients should collaborate during federated optimization. We propose ClientMorpher, a routing-aware, personalized federated instruction fine-tuning framework that leverages routing signatures from pretrained MoE models to organize client collaboration prior to aggregation. We investigate two complementary clustering strategies: ClientMorpher-C, which directly clusters clients using expert activation profiles, and ClientMorpher-E, which first clusters experts based on their cross-client usage signatures and then derives client collaboration groups. We evaluate ClientMorpher for federated instruction fine-tuning on the Databricks Dolly-15K dataset, using pathological and Dirichlet-based heterogeneous client distributions across multiple instruction-following tasks. Experimental results show that routing-aware collaboration consistently improves personalized performance compared to conventional federated averaging and local training, while maintaining the same communication cost. Furthermore, our study shows that client-centric and expert-centric clustering provides an effective and scalable approach for personalized federated instruction fine-tuning of sparse MoE LLMs.

## Metadata
- **Published**: 2026-08-15T16:35:12Z
- **Authors**: Ankita Sharma, Bahar Farahani, Sanaz Rahimi Moosavi, Amir Rrahmani, Farshad Firouzi, Krishnendu Chakrabarty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15311v1)