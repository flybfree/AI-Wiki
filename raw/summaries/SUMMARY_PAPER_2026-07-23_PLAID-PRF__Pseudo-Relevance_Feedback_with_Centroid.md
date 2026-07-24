---
title: PLAID-PRF: Pseudo-Relevance Feedback with Centroid-like Tokens in PLAID
url: http://arxiv.org/abs/2607.18626v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_01-50-11Z_PLAID_PRF_Pseudo_RelevanceFeedbackwithCentroid_lik.md
generated_at: 2026-07-23 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PLAID-PRF, which adds Pseudo‑Relevance Feedback to the centroid‑based index of PLAID without recomputing full query vectors. By using only high‑utility expansion tokens derived from top retrieved results, it refines candidate generation and final scores while keeping computation cheap. Experiments on MSMARCO and BEIR show up to 7.3% MRR improvement with minimal overhead.

## Key Takeaways
- PLAID-PRF leverages existing centroid vectors as PRF tokens, avoiding costly query‑time clustering.
- The method appends a small set of diverse expansion vectors to the original query, then reruns PLAID for refinement.
- Results achieve up to 4.3% nDCG@10 gain over plain PLAID while using less than twice the runtime.

## Context
Modern dense retrieval systems rely on token‑level interactions captured by multi‑vector models like ColBERT. Efficient indexing is essential, yet feedback mechanisms often require full re‑indexing or heavy computation. This work demonstrates that centroid‑aware PRF can be integrated cheaply into such pipelines.

## Implications
Practitioners can boost retrieval quality on existing indexes with minimal infrastructure changes. The lightweight nature of PLAID-PRF makes it suitable for real‑time applications where latency and cost matter, encouraging adoption in search engines and recommendation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18626v1)
