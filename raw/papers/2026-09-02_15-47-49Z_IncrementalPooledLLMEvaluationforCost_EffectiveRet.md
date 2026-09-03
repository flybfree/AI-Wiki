---
title: Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection
published: 2026-09-02T15:47:49Z
authors: Max Nelson, Hanoz Bhathena, Aviral Joshi, Saket Sharma
url: http://arxiv.org/abs/2609.02745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection

## Abstract
Selecting a retrieval model for a production RAG system requires reliable comparative evaluation, but obtaining relevance judgments at scale is expensive and difficult to repeat as new candidate systems arrive. We study pooled LLM evaluation, in which an LLM judges the union of documents retrieved by the current set of candidate systems, and the pool is then expanded incrementally as new systems are introduced by judging only the new documents they contribute. These judgments are reused to evaluate all systems on a common basis. We validate this approach on four retrieval benchmarks with 11 systems spanning dense, sparse, and hybrid configurations, and deploy it to compare 62 retrieval configurations for a financial news QA system. Pooled LLM rankings correlate strongly with gold-standard evaluation across datasets, and 97% of pairwise system orderings are preserved once bootstrap uncertainty in the qrels is taken into account. In production, document overlap yields 65-80% judgment reuse and up to 4.9x lower evaluation cost, allowing teams to benchmark new retrieval candidates without re-judging previously assessed documents. These results suggest pooled LLM evaluation is a practical and cost-effective workflow for incremental retrieval model selection in deployed systems.

## Metadata
- **Published**: 2026-09-02T15:47:49Z
- **Authors**: Max Nelson, Hanoz Bhathena, Aviral Joshi, Saket Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02745v1)