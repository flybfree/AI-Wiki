---
title: How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account
published: 2026-08-30T22:21:16Z
authors: Ruize Xu, Xiao Yu, Yujin Tang, Chenming Shang, Nikhil Singh
url: http://arxiv.org/abs/2608.30067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account

## Abstract
How do LLM agents come to both understand environments they act in and master tasks set within them? Through controlled experiments combining world-model training (next-state prediction) and policy training (reward maximization), we investigate this question. We dissect the resulting models through their additive parameter updates. Geometrically, we find effective world-model updates are low-rank and share an input-feature subspace with policy updates while writing to nearly orthogonal output directions, whether trained separately or sequentially. However, we find that, in projection interventions, the sequential update induces more robustness than separate policy RL when removing the world model's leading input directions, suggesting that it has learned alternative input pathways. Behaviorally, we find the sequentially trained agent explores a wider range of states and actions. Based on this, we ask: does policy training preserve world knowledge as well as it could? We probe this with training-free merging built on the geometrically motivated input basis plus an online world-model loss during policy RL, and show both improve over the untreated baseline. Our findings suggest world knowledge and task-directed ability can be learned in geometrically complementary forms, and that future post-training pipelines should consider how best to engineer the interface between them.

## Metadata
- **Published**: 2026-08-30T22:21:16Z
- **Authors**: Ruize Xu, Xiao Yu, Yujin Tang, Chenming Shang, Nikhil Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30067v1)