---
title: The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory
url: http://arxiv.org/abs/2608.22767v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_03-42-03Z_TheRetrieverShouldRemember_Experience_AmortizedRer.md
generated_at: 2026-08-24 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EARM, an experience‑amortized reranking framework that reuses LLM relevance scores across interactions to reduce per‑query inference cost. Experiments on long‑term conversational memory show mixed observed‑and‑estimated reranking improves answer accuracy by up to 6.62% compared with semantic retrieval.

## Key Takeaways
- EARM stores sparse query‑memory relevance scores in an online matrix and learns their structure via causal matrix completion, allowing previously acquired LLM scores to be reused.
- The framework combines newly observed scores with estimated scores for reranking remaining candidates, decreasing the scoring budget as experience accumulates.
- Even when only 17.5% of candidates receive direct LLM relevance scores, mixed retrieval yields significant accuracy gains and reduces inference overhead.

## Context
Long‑term language agents face a bottleneck where each query triggers expensive LLM rerankings on large candidate sets. Traditional approaches treat each reranking as independent, ignoring the accumulated knowledge that past queries have found useful memories. This paper addresses that inefficiency by treating retrieval experience as learnable and reusable.

## Implications
EARM demonstrates that agent memory should include not only content but also its proven utility for future retrieval. By amortizing LLM scoring costs over time, this approach can enable scalable long‑term agents with lower latency and higher accuracy in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22767v1)
