---
title: From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue
url: http://arxiv.org/abs/2610.11314v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_06-21-45Z_FromRetrievaltoReconstruction_ConstructingEvolvabl.md
generated_at: 2026-10-08 21:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces CogMem, a cognitive memory architecture designed to enable large language models to maintain reliable reasoning over extended, multi-session dialogues. By structuring memory as a PEC²F (Person-Event-Concept-Claim-Fact) graph, CogMem separates subjective beliefs from objective facts and supports temporal reconciliation of conflicting updates. Experiments on the LoCoMo and LongMemEval benchmarks demonstrate strong performance, particularly on multi-hop reasoning, temporal tracking, and knowledge-update tasks, with ablation studies confirming that epistemic separation, consolidation, and agentic retrieval each contribute complementary gains.

## Key Takeaways
- CogMem addresses a fundamental weakness in existing RAG frameworks by treating memory as an active, structured cognitive system rather than passive storage. The PEC²F graph schema explicitly separates Claim nodes (which preserve the source and target of subjective statements) from Fact and Event nodes (which represent semantic and episodic knowledge), enabling the system to distinguish who said what from what is objectively true. This epistemic separation is critical for long-term dialogue where a user's evolving opinions must be tracked alongside stable factual knowledge.
- The retrieval mechanism replaces probabilistic or embedding-based search with a rule-based controller driven by LLM intent parsing that composes four deterministic graph operators: anchoring, traversal, intersection, and evidence grounding. This agentic retrieval approach allows the system to reconstruct query-relevant context across sessions by traversing the graph structure, making multi-hop and temporal queries tractable in ways that flat vector retrieval cannot achieve.
- Dialogue turns are incrementally converted into provenance-aware graph records, consolidated into higher-level facts, and reconciled into temporally scoped Claim views when the same source provides conflicting updates. This consolidation pipeline ensures that outdated beliefs are superseded while preserving the history of how knowledge evolved, which is essential for maintaining coherent long-term conversational agents.

## Context
Long-term dialogue agents represent a frontier challenge in conversational AI, where systems must maintain coherent understanding across hundreds or thousands of turns spanning days or weeks. Current RAG-based memory systems treat retrieved chunks as undifferentiated text, conflating a user's personal opinions with general world knowledge and failing to track how beliefs change over time. CogMem sits at the intersection of knowledge graph construction, cognitive science-inspired memory modeling, and agentic retrieval, offering a structured alternative that aligns with how humans actually organize episodic and semantic memory.

## Implications
For practitioners building customer-service bots, personal assistants, or therapeutic dialogue systems, CogMem provides a blueprint for memory architectures that can track user-specific beliefs, resolve contradictions over time, and answer complex multi-hop questions without hallucinating from flat retrieval. The open-source code release lowers the barrier for adoption, while the benchmark results on LoCoMo and LongMemEval suggest that structured graph-based memory can outperform embedding-based retrieval on the hardest long-context reasoning tasks. This work signals a shift in the field from treating memory as a retrieval problem to treating it as a reconstruction and reconciliation problem, which will likely influence the design of next-generation conversational agents and their evaluation standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11314v1)
