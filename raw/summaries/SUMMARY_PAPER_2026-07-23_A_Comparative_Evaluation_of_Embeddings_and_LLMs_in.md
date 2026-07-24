---
title: A Comparative Evaluation of Embeddings and LLMs in a Greek Book Publisher Setting - The CUP Dataset
url: http://arxiv.org/abs/2607.21274v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_12-51-55Z_AComparativeEvaluationofEmbeddingsandLLMsinaGreekB.md
generated_at: 2026-07-23 22:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CUP, a Greek book retrieval benchmark consisting of 868 catalog records and 104 expert‑annotated queries with graded relevance judgments. It evaluates sparse BM25, dense sentence‑transformer embeddings, hybrid methods, and LLM‑assisted retrieval in this setting. Dense multilingual embeddings outperform Greek‑specific models, while hybrid retrieval achieves the best overall performance.

## Key Takeaways
- Multilingual sentence‑transformer embeddings outperform Greek‑specific models on the CUP benchmark.  
- Hybrid retrieval methods combine the strengths of BM25 and dense embeddings to achieve the highest overall relevance scores.  
- LLM post‑filtering improves early‑stage retrieval but at a high computational cost, while TOC summarization is effective for TOC‑only queries.

## Context
This work contributes to the ongoing effort to benchmark multilingual book search systems where domain specificity and query diversity are crucial. By providing a Greek‑focused dataset with graded relevance judgments, it helps researchers compare embedding quality across languages and assess the practical impact of hybrid or LLM augmentations beyond standard retrieval pipelines.

## Implications
For publishers and developers, CUP demonstrates that multilingual embeddings can serve as a reliable baseline for Greek book catalogs, while hybrid approaches offer a pragmatic solution to balance speed and relevance. The findings suggest that deploying LLMs for TOC summarization may be worthwhile only when high‑precision retrieval is required despite the cost.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21274v1)
