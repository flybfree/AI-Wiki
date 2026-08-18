---
title: Where Does Retrieval Fail? Evaluating RAG Architectures for Agricultural Advisory
url: http://arxiv.org/abs/2608.14886v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_20-50-24Z_WhereDoesRetrievalFail_EvaluatingRAGArchitecturesf.md
generated_at: 2026-08-17 21:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why retrieval quality varies in Retrieval-Augmented Generation (RAG) systems for Bengali agricultural advisory, showing that aggregate scores mask important differences across query types and language conditions. It evaluates five retrieval architectures and six embedding models on a dataset of 1,000 farmer queries and 2,882 knowledge nodes.

## Key Takeaways
- BM25 performs best for native Bengali queries with R@10 = 0.506 but collapses to R@10 = 0.004 when English queries are matched against the Bengali corpus.
- Dense retrieval scores drop only slightly from 0.464 to 0.425 across language conditions, indicating more stability than BM25.
- Embedding task configuration and passage length can each change reported R@10 by a factor of seven, showing that evaluation metrics are highly sensitive to these factors.

## Context
This study highlights a common limitation in AI research where single aggregate performance numbers obscure the heterogeneous behavior of models under real-world conditions. By focusing on specific language and query types, researchers can better understand model robustness and applicability.

## Implications
For agricultural advisory systems that must serve multilingual and colloquial users, relying solely on overall R@10 scores is misleading; practitioners should report results stratified by language condition and query type to guide design choices. The findings also suggest that embedding configuration and passage length are critical hyperparameters worth optimizing for low-resource settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14886v1)
