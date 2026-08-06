---
title: Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems
published: 2026-08-05T12:12:44Z
authors: Kartikey Singh Bhandari, Aarya Wadhwani, Dhruv Kumar, Pratik Narang
url: http://arxiv.org/abs/2608.04746v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems

## Abstract
LLM agents that persist across sessions accumulate stored memories whose validity varies enormously by content type, yet existing memory architectures treat all memories as equally persistent and systematically contaminate retrieved context with outdated facts. We show that per-memory, type-conditioned temporal decay, a property of western scrub jay episodic memory, can be operationalized as an auto-classified coefficient $π_i$ in an external LLM-agent memory store, yielding ScrubJay-MEM: each memory is encoded as a jointly-bound What--Where--When tuple with an estimated perishability $π_i$ and utility horizon $τ_i$, retrieved by query-adaptive scoring, and revised retroactively at $O(1)$ LLM calls per update. We introduce the Temporal Generalization Test (TGT), a benchmark with held-out retention intervals and a Generalization Gap (GenGap) metric. On TGT, ScrubJay-MEM is the only retrieval-based system with substantially positive GenGap ($+0.108$); on MemoryAgentBench EventQA-64k it improves F1 by $+2.66$ over Mem0 and $+3.09$ over Qwen3-Embedding-4B under a llm backbone. A decay ablation collapses GenGap by $5.7\times$, establishing type-conditioned decay as necessary for the result. Gains narrow under stronger backbones and reverse on fact-consolidation tasks, scoping the contribution to temporal reasoning over perishable facts.

## Metadata
- **Published**: 2026-08-05T12:12:44Z
- **Authors**: Kartikey Singh Bhandari, Aarya Wadhwani, Dhruv Kumar, Pratik Narang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04746v1)