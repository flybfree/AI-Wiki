---
title: Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents
published: 2026-10-26T01:05:20Z
authors: Xinyu Zhang, Weiwei Sun
url: http://arxiv.org/abs/2610.34673v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents

## Abstract
Large language model (LLM) agents that serve users across many sessions must choose, for every request, the few stored memories that enter a limited context window. This choice largely decides whether the agent answers correctly, and it runs on every request at Web scale. This selection faces three challenges: a large and growing store, a per-request cost budget, and multi-session questions that need all of their evidence. Many memory systems build notes or graphs with hundreds to thousands of LLM calls per history, and each is designed on its own, so it is unclear which component yields the accuracy. These challenges mirror the properties of recommendation, so we formalize agent memory as budgeted slate recommendation, with the request as the user, stored memories as items and the context window as a slate. The formalization places memory systems in one design space of recommender cascades and factorizes accuracy into the completeness that each stage controls. Guided by it, we propose AgentMemRec, which adapts candidate generation, learning to rank and slate construction from recommender systems and selects memories without any LLM call. On multi-session questions of LongMemEval, AgentMemRec outperforms memory and context-selection methods, including A-Mem, HippoRAG 2, DynamicRAG and T-Mem, by 10 to 31 points of accuracy. It matches an LLM reranker that makes 64 calls per query at 3.2 times lower serving cost, and on LoCoMo it outperforms Mem0 and Zep without any LLM call at write time. The factorization attributes the gains to slates that more often hold all of the evidence, so recommender-system design offers an effective and efficient foundation for the long-term memory of LLM agents.

## Metadata
- **Published**: 2026-10-26T01:05:20Z
- **Authors**: Xinyu Zhang, Weiwei Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34673v1)