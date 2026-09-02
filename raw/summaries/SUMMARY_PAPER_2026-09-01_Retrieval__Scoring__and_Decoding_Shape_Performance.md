---
title: Retrieval, Scoring, and Decoding Shape Performance and Stability in LLM-based Conversational Recommendation
url: http://arxiv.org/abs/2609.00086v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_10-54-20Z_Retrieval_Scoring_andDecodingShapePerformanceandSt.md
generated_at: 2026-09-01 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates large language model rerankers within the ReDial conversational movie recommendation benchmark, comparing proprietary, open‑weight, and fine‑tuned models against non‑LLM baselines across variations in candidate pool size, first‑stage retriever type, and decoding temperature. It finds that a proprietary LLM reaches NDCG@10 of 0.1497 with a shared semantic top‑250 pool and strict candidate‑aware scoring, while zero‑shot generation yields a higher apparent advantage due to unconstrained scoring.

## Key Takeaways
- The best proprietary reranker achieves NDCG@10 of 0.1497 with a shared semantic top‑250 pool and strict candidate‑aware scoring, outperforming non‑LLM baselines by more than 60%.
- Switching from semantic to collaborative‑filtering candidates can increase NDCG@10 by over 50%, indicating that candidate generation is a major driver of performance.
- Raising decoding temperature from 0 to 1.0 raises top‑10 Jaccard distance but only slightly degrades mean NDCG@10, whereas weaker LLMs suffer larger degradation.

## Context
Large language models are being adopted as rerankers in recommender systems, yet their effectiveness is often hidden behind opaque evaluation protocols that ignore candidate generation and decoding choices. This study reveals how these factors critically shape measured outcomes.

## Implications
Researchers and practitioners should report candidate‑generation methods, pool size, scoring policies, and temperature settings as separate metrics rather than implementation details. Ignoring them leads to misleading comparisons of LLM performance in recommender systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00086v1)
