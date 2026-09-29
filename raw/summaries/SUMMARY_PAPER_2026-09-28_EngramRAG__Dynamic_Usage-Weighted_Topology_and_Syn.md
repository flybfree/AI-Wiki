---
title: EngramRAG: Dynamic Usage-Weighted Topology and Synaptic Consolidation for Multi-Hop Agentic Memory
url: http://arxiv.org/abs/2609.32049v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-25_22-28-53Z_EngramRAG_DynamicUsage_WeightedTopologyandSynaptic.md
generated_at: 2026-09-28 20:52
model: qwen3.6-35b-a3b
---

## Summary
EngramRAG introduces an adaptive memory architecture for autonomous LLM agents that addresses associative blindness, temporal decay, and static topology stagnation by coupling a low-latency Waking State with an asynchronous Dreaming State consolidation cycle. The system leverages usage-weighted topological updates and hybrid retrieval mechanisms to significantly enhance multi-hop reasoning and long-term retention compared to conventional RAG approaches. Evaluations on the LoCoMo benchmark demonstrate substantial improvements in recall, mean reciprocal rank, and hallucination suppression over dense vector baselines.

## Key Takeaways
- EngramRAG employs Usage-Modulated Personalized PageRank to adapt transition probabilities via Hebbian plasticity, promoting persistent entities into high-centrality Epistemic Macro-Hubs, while Consolidation-Activated Topology Decay scales retention half-life based on topological load-bearing weight rather than simple recency, protected by a cold-start grace period.
- The architecture implements Directed SUPERSEDES DAG filtering to suppress obsolete states during

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32049v1)
