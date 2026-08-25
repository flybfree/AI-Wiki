---
title: The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory
published: 2026-08-24T03:42:03Z
authors: Qi Feng, Chris Ding, Jicong Fan
url: http://arxiv.org/abs/2608.22767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory

## Abstract
Long-term language-model agents accumulate memories across interactions, but their retrievers typically do not accumulate retrieval experience. Semantic retrieval is efficient, but embedding similarity does not always reflect whether a memory contains evidence relevant to the current query. Large language model (LLM) rerankers provide stronger query-conditioned relevance scores, yet stateless reranking repeatedly scores a large candidate pool and discards these scores after each query. We introduce EARM, an experience-amortized reranking framework that treats previously acquired LLM relevance scores as reusable retrieval experience. EARM stores sparse query--memory relevance scores in an online matrix, learns their shared structure through causal matrix completion, and combines a small set of newly observed scores with estimated scores to rerank the remaining candidates. The scoring budget decreases as experience accumulates, changing LLM reranking from a repeated per-query expense into a retrieval capability learned over an agent's lifetime. Experiments on long-term conversational memory show that mixed observed-and-estimated reranking improves answer accuracy over semantic retrieval by up to 6.62% and remains effective when only 17.5% of candidates receive direct LLM relevance scores, thereby substantially reducing the inference overhead of LLM reranking. These results motivate a broader view of agent memory: a long-lived agent should remember not only past content, but also how that content has proved useful for retrieval.

## Metadata
- **Published**: 2026-08-24T03:42:03Z
- **Authors**: Qi Feng, Chris Ding, Jicong Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22767v1)