---
title: RING: Retrieval-Internalized Generation for Continual Large-Scale Knowledge Injection
published: 2026-08-03T03:00:43Z
authors: Shicheng Xu, Liang Pang, Liyi Chen, Zihao Wei, Jingcheng Deng, Yan Gao, Yi Wu, Yao Hu, Huawei Shen, Xueqi Cheng
url: http://arxiv.org/abs/2608.01630v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RING: Retrieval-Internalized Generation for Continual Large-Scale Knowledge Injection

## Abstract
Retrieval-augmented generation (RAG) improves factuality but adds latency and engineering overhead at serving time. We propose RING (Retrieval-Internalized Generation), a holistic paradigm spanning both architecture and training that injects large-scale external knowledge into a \textit{Mixture-of-Memory Experts} and learns parametric search over this internal memory via reinforcement learning, removing the external retriever entirely. Training proceeds in three stages: continued pre-training injects new corpora into a Knowledge Expert via our novel \textit{Dual Causal Attention}; supervised fine-tuning teaches a ``search-then-answer'' pattern; and reinforcement learning with hierarchical rewards optimizes the routing-and-search policy over the parametric memory. Unlike prior parametric injection methods that pair internal memory with a fixed or rule-based retriever, RING {learns} its retrieval policy directly from task signals. We further frame RING theoretically as a search-free approximation to the classical RAG objective. To evaluate large-scale injection of genuinely {new} knowledge without test-time leakage, we further construct News-2025, a benchmark built from news strictly post-dating the base LLM's pretraining cutoff. RING matches or surpasses both search-based RAG and parametric injection baselines in accuracy and efficiency.

## Metadata
- **Published**: 2026-08-03T03:00:43Z
- **Authors**: Shicheng Xu, Liang Pang, Liyi Chen, Zihao Wei, Jingcheng Deng, Yan Gao, Yi Wu, Yao Hu, Huawei Shen, Xueqi Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01630v1)