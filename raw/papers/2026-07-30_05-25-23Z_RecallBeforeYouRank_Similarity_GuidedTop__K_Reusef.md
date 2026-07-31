---
title: Recall Before You Rank: Similarity-Guided Top-$K$ Reuse for Efficient Long-Context Attention
published: 2026-07-30T05:25:23Z
authors: Wenshuai Yao, Wenyong Zhou, Hanyong Shao, Yizhe Chen, Zhiyuan Ning, Yuannuo Feng, Ru Huang, Kechao Tang
url: http://arxiv.org/abs/2607.27692v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recall Before You Rank: Similarity-Guided Top-$K$ Reuse for Efficient Long-Context Attention

## Abstract
Top-$K$ sparse attention reduces the cost of Softmax and value aggregation by attending to only a small subset of key--value (KV) entries. However, identifying this subset still requires scoring the current query against the full KV cache and performing global Top-$K$ selection, leaving selector cost linear in context length and limiting the practical efficiency of sparse attention for long-context decoding. In this paper, we introduce ReTopK, a training-free method that accelerates dynamic Top-$K$ attention by reusing historical retrieval decisions. ReTopK builds on the observation that similar queries often attend to overlapping supports and that partially overlapping supports can still preserve most of the Exact Top-$K$ attention mass. For each attention head, it maintains a bounded cache of historical query--support pairs, retrieves the most similar cached queries for each new query, unions their stored supports with a recent window, and reranks only the resulting compact candidate set using exact current-query scores. A similarity-based fallback invokes full-history Exact Top-$K$ when reuse is unreliable, while periodic exact refreshes limit cache drift. ReTopK retains the complete KV cache and reuses only selected indices, rather than historical scores, attention weights, or outputs. Across 16K--128K contexts, ReTopK achieves the lowest PG19 perplexity and the highest NIAH and LongBench scores among the evaluated approximate methods. At 128K with $K=512$, ReTopK incurs only a 0.50\% perplexity increase over Exact Top-$K$ while accelerating attention computation by $3.07\times$.

## Metadata
- **Published**: 2026-07-30T05:25:23Z
- **Authors**: Wenshuai Yao, Wenyong Zhou, Hanyong Shao, Yizhe Chen, Zhiyuan Ning, Yuannuo Feng, Ru Huang, Kechao Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27692v1)