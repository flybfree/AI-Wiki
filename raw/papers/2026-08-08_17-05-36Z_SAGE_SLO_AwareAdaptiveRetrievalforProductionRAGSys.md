---
title: SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems
published: 2026-08-08T17:05:36Z
authors: Muhammad Faizan Raza,  Shuo,  Yang, Satish Mahadevan Srinivasan
url: http://arxiv.org/abs/2608.08237v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems

## Abstract
Retrieval-Augmented Generation (RAG) systems in production operate under strict service level objectives (SLOs) on tail latency and infrastructure cost. However, standard retrieval pipelines rely on fixed retrieval budgets that ignore query difficulty, over-retrieving for easy queries and under-serving hard ones, forcing operators to trade answer quality against SLO compliance. This paper proposes SAGE, a learned SLO-aware adaptive retrieval policy that dynamically selects the number of passages k per query. SAGE uses lightweight features derived from initial retrieval (e.g., score distributions, rank gaps, lexical signals) and is trained offline via imitation learning from an oracle that approximates optimal latency-quality trade-offs. At inference, it adds no LLM calls and minimal overhead. On Natural Questions, under a 5s P95 latency SLO, SAGE achieves 95% SLO compliance versus 30% for the best static baseline (k=20), reduces P95 latency by 36% and retrieval cost by 51% with only 2 percentage points Exact Match (EM) loss. A single policy trained on Natural Questions generalizes across HotpotQA, UnSeenTimeQA, and four LLM families (Llama, Qwen, Mistral, Gemma), consistently yielding +45-52 point SLO improvements without quality degradation.

## Metadata
- **Published**: 2026-08-08T17:05:36Z
- **Authors**: Muhammad Faizan Raza,  Shuo,  Yang, Satish Mahadevan Srinivasan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08237v1)