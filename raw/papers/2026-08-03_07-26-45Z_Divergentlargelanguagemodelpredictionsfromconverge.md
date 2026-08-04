---
title: Divergent large language model predictions from convergent representations in ambiguous word pairs
published: 2026-08-03T07:26:45Z
authors: K. Jack Scott, Narun Pat, Veronica Liesaputra
url: http://arxiv.org/abs/2608.01816v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Divergent large language model predictions from convergent representations in ambiguous word pairs

## Abstract
In this work we investigate how decoder-only transformers resolve lexical ambiguity through layer-by-layer analysis of three models spanning three parameter sizes (GPT-2-Small-117M, Llama-3.2-3B, Qwen2.5-32B). For both homonyms and polysemes, we find that representations become maximally distinct in middle layers, then partially reconverge in late layers, while the KL divergence between their next-token predictions reaches its maximum in the final layers. The activation patching experiment provides causal evidence that late-layer representational differences directly determine outputs despite apparent increased similarity in embedding space. Our single-layer ablation experiment indicates that models achieve equivalent disambiguation despite qualitatively different layer-wise vulnerabilities. These findings offer a mechanism for recent observations where models' internal embedding similarities show low correlation with their behavioural outputs despite strong performance. The semantic distinctions therefore remain present but become increasingly invisible to similarity measures over the embeddings, with implications for embedding-based methods such as semantic search, retrieval, and clustering that rely on late-layer cosine similarity.

## Metadata
- **Published**: 2026-08-03T07:26:45Z
- **Authors**: K. Jack Scott, Narun Pat, Veronica Liesaputra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01816v1)