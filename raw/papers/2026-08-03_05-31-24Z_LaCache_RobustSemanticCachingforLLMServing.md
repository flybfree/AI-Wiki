---
title: LaCache: Robust Semantic Caching for LLM Serving
published: 2026-08-03T05:31:24Z
authors: Jiacheng Liang, Yuhui Wang, Tanqiu Jiang, Ting Wang
url: http://arxiv.org/abs/2608.01718v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LaCache: Robust Semantic Caching for LLM Serving

## Abstract
Semantic caching, which reuses responses to semantically similar requests via their embeddings, has seen growing adoption in LLM serving, offering faster responses and reduced costs. Yet existing schemes are fundamentally vulnerable to cache-collision attacks, wherein an adversary pollutes the cache by injecting crafted queries, corrupting responses to subsequent legitimate requests. We present LaCache, a novel semantic caching scheme that addresses this vulnerability through a conceptually simple yet principled redesign. The key insight is that while the adversary has full control over the adversarial query, it has far less control over its response, which must simultaneously satisfy multiple semantic constraints. Rather than checking only the cache hit of a query, LaCache additionally checks the cache hit of its first k (speculatively) decoded tokens. This design yields two concrete benefits. First, it provides formally guaranteed resilience against cache-collision attacks: we prove that it is impossible to craft adversarial queries that simultaneously elicit malicious responses and collide with benign queries. Second, the enriched index supplies additional semantic context for cache retrieval, improving response relevance. Empirical evaluation across diverse LLMs and benchmarks validates both LaCache's security guarantees and efficiency gains, pointing to a promising direction for robust semantic caching.

## Metadata
- **Published**: 2026-08-03T05:31:24Z
- **Authors**: Jiacheng Liang, Yuhui Wang, Tanqiu Jiang, Ting Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01718v1)