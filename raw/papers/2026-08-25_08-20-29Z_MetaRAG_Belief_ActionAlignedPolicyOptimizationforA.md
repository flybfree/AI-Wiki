---
title: MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG
published: 2026-08-25T08:20:29Z
authors: Qiuyi Qi, Tian Liang, Jiamu Wang, Jinjian Zhang, Wei Zhou, Pengcheng Zhu, Linjian Mo, Ming Kong, Jie Liu, Qiang Zhu
url: http://arxiv.org/abs/2608.24214v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG

## Abstract
Agentic retrieval-augmented generation (RAG) requires language models to decide when to continue searching and when to answer. Existing RL-based methods rely on external supervision and overlook the agent's internal belief about whether the current evidence is sufficient. To address this problem, we reformulate the search decision quality as belief-action alignment and propose MetaRAG, a belief-action aligned policy optimization framework for agentic RAG. MetaRAG uses Verify-first Action Generation to elicit an explicit verification process before each actual action, and Internal Belief Probing to estimate the policy model's own answerability belief from the same question-history context. Based on these, MetaRAG derives a consistency reward that is further gated by answer correctness, avoiding reinforcement of internally consistent but incorrect trajectories. The belief probe is used only during training and introduces no inference-time overhead. Experiments on seven public QA benchmarks show that MetaRAG consistently improves the accuracy-efficiency trade-off over strong RL-based agentic RAG baselines, with gains that transfer to deep research settings, different optimizers, and multiple model backbones.

## Metadata
- **Published**: 2026-08-25T08:20:29Z
- **Authors**: Qiuyi Qi, Tian Liang, Jiamu Wang, Jinjian Zhang, Wei Zhou, Pengcheng Zhu, Linjian Mo, Ming Kong, Jie Liu, Qiang Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24214v1)