---
title: Explanation-Based Runtime Verification for Trustworthy ML-driven Optical Networks
published: 2026-07-22T19:22:41Z
authors: Omran Ayoub, Carlos Natalino, Ali Al Housseini, Felix Foschum, Philipp Morger, Tiziano Leidi, David Hock, Paolo Monti
url: http://arxiv.org/abs/2607.20675v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explanation-Based Runtime Verification for Trustworthy ML-driven Optical Networks

## Abstract
Machine learning (ML) models are increasingly integrated into optical network automation frameworks to support tasks such as failure management, performance monitoring and resource allocation. In these environments, ML-driven predictions may be directly coupled with control-plane actions where incorrect decisions can immediately impact service quality, resource efficiency, and network stability. As automation levels increase, ensuring the reliability of individual decisions at deployment time becomes a critical requirement. Explainable artificial intelligence (XAI) techniques have emerged to improve transparency by highlighting the factors influencing ML predictions. In addition to identifying influential features, they provide insights into the underlying reasoning process of the model, revealing how different input variables contribute to the final outcome and how feature interactions shape the decision boundary. In this work, we introduce explanation-based runtime verification, an approach that exploits model explanations to assess the soundness of individual ML decisions before they are executed in the network control loop. The proposed approach evaluates explanation coherence and physics grounding consistency at runtime, enabling the system to defer or reject decisions flagged as uncertain. We demonstrate the effectiveness of our approach on a representative use case of lightpath quality of transmission classification. Experimental results show that explanation-based verification can intercept a significant fraction of erroneous decisions while preserving high automation rate.

## Metadata
- **Published**: 2026-07-22T19:22:41Z
- **Authors**: Omran Ayoub, Carlos Natalino, Ali Al Housseini, Felix Foschum, Philipp Morger, Tiziano Leidi, David Hock, Paolo Monti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20675v1)