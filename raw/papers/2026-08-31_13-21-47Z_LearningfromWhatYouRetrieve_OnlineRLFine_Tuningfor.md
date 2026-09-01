---
title: Learning from What You Retrieve: Online RL Fine-Tuning for Semantic Retrieval
published: 2026-08-31T13:21:47Z
authors: Shaowei Wei, Chong Huang, Songtao Fang, Jin Zhang, Zhuojun Wang, Chengfu Huo
url: http://arxiv.org/abs/2608.30753v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from What You Retrieve: Online RL Fine-Tuning for Semantic Retrieval

## Abstract
In large-scale e-commerce retrieval, dual-encoder retrievers are op- timized for contrastive similarity, whereas downstream rerankers capture finer-grained relevance preferences; this objective mis- match limits end-to-end retrieval quality. Reinforcement Learning offers a way to use reward-model feedback for retriever adaptation, but we observe that standard policy-gradient updates can degrade embedding geometry, especially when the document index must remain frozen due to industrial constraints. To address this, we propose PAO (Positive-Advantage-Only), a selective RL optimization method. Our analysis reveals that in- discriminate penalization of negative samples (pushing away) in a frozen high-dimensional space disrupts pre-trained semantic man- ifolds. PAO selectively applies gradient updates only to retrieved items with positive advantages, effectively pulling query embed- dings toward high-reward regions while preserving global topo- logical stability. Experiments on both a massive industrial dataset and public benchmarks demonstrate that PAO significantly outper- forms standard RL and distillation baselines.

## Metadata
- **Published**: 2026-08-31T13:21:47Z
- **Authors**: Shaowei Wei, Chong Huang, Songtao Fang, Jin Zhang, Zhuojun Wang, Chengfu Huo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30753v1)