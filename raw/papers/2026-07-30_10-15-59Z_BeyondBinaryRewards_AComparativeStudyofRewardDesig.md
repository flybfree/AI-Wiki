---
title: Beyond Binary Rewards: A Comparative Study of Reward Design for Reinforcement Unlearning
published: 2026-07-30T10:15:59Z
authors: Efstratios Zaradoukas, Davide Gabrielli, Bardh Prenkaj, Gjergji Kasneci
url: http://arxiv.org/abs/2607.27968v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Binary Rewards: A Comparative Study of Reward Design for Reinforcement Unlearning

## Abstract
Machine unlearning seeks to selectively remove specific knowledge from trained language models without full retraining, a growing necessity under privacy regulations such as GDPR and the EU AI Act. Recent work has reformulated unlearning as a Reinforcement Learning with Verifiable Rewards (RLVR) problem, where models are optimized against verifiable rewards computed directly from their outputs. However, existing methods rely on sparse binary rewards that provide minimal learning signal, indicating only whether forbidden content was avoided, and limiting convergence speed. In this paper, we study how reward design affects unlearning efficiency within the Reinforcement Unlearning (RUL) framework. We introduce a principled reward decomposition framework that decouples verifiability from sparsity, and propose two new reward functions: an exponential reward that provides graded penalties based on the count of forbidden-concept occurrences, and a PageRank inspired reward that weights penalties by semantic importance. We conduct experiments on the Real World Knowledge Unlearning (RWKU) benchmark, demonstrating that both rewards consistently outperform the binary setting, while reaching similar forgetting performance up to $3\times$ faster and preserving general model utility. Our results show that reward design is a key driver of unlearning efficiency offering a practical path toward scalable and efficient machine unlearning.

## Metadata
- **Published**: 2026-07-30T10:15:59Z
- **Authors**: Efstratios Zaradoukas, Davide Gabrielli, Bardh Prenkaj, Gjergji Kasneci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27968v1)