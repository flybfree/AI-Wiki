---
title: From Relevant Memories to Sufficient Evidence: Rethinking Memory Utilization in LLM Agents
url: http://arxiv.org/abs/2610.22668v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_21-34-17Z_FromRelevantMemoriestoSufficientEvidence_Rethinkin.md
generated_at: 2026-10-18 20:44
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a critical gap in LLM agent memory systems: retrieving memories that are relevant to a query does not guarantee that the retrieved information constitutes sufficient evidence to answer the query correctly. The authors propose QEMem, a framework that reframes memory utilization as the construction of query-specific evidence sets rather than relying on individual retrieval relevance. QEMem demonstrates substantial improvements over existing baselines, achieving 91.43% accuracy on the LoCoMo benchmark while operating on existing memory stores without modifying how memories are formed.

## Key Takeaways
- The paper identifies the "relevance-sufficiency gap" as a fundamental problem in LLM agent memory systems. Even when memories are retrieved that appear relevant to a query, essential information may remain fragmented across multiple memory records, obscured by abstraction layers, or disconnected from the relational reasoning chains needed to produce a correct answer. This means high retrieval relevance scores do not translate into answer accuracy.
- QEMem introduces three complementary mechanisms to close this gap: query-guided discovery that searches across multiple memory granularities to find evidence fragments, source-grounded reification that organizes retrieved fragments into structured "ViewCards" with explicit evidential roles and source references, and sufficiency-guided refinement that selectively recovers missing information when the current evidence set is incomplete. This shifts the paradigm from "find the most relevant single memory" to "build a complete evidence set for this specific query."
- QEMem achieves 91.43% LLM-judge accuracy on LoCoMo using Claude Opus 4.5, outperforming the strongest baseline MemR3 by 7.6 percentage points and NEMORI by 10.7 points under a shared memory store. Critically, QEMem operates on existing memory stores without modifying memory formation processes, making it a plug-in improvement rather than requiring a redesign of the entire memory pipeline. Further analyses confirm improved evidence coverage and strong performance specifically on questions requiring cross-session evidence integration.

## Context
LLM agents increasingly rely on long-term memory systems to maintain coherence across extended interactions, multi-session conversations, and complex task sequences. The field has largely focused on improving retrieval mechanisms—embedding quality, similarity scoring, and ranking algorithms—to surface relevant memories. However, this paper reveals that the retrieval-centric paradigm is insufficient because real-world queries often require synthesizing information scattered across multiple memory entries, connecting entities across sessions, and reasoning over relationships that no single memory record captures. This work sits at the intersection of retrieval-augmented generation, agent memory architectures, and evidence-based reasoning, addressing a bottleneck that limits the practical reliability of deployed LLM agents in long-horizon tasks.

## Implications
For practitioners building LLM agent systems, this work suggests that improving retrieval relevance alone will not solve memory-grounded question answering; instead, evidence assembly and sufficiency checking must be explicitly designed into the agent pipeline. The plug-in nature of QEMem—requiring no changes to memory formation—makes it immediately applicable to existing agent deployments, potentially improving accuracy on benchmarks like LoCoMo without costly retraining or architectural redesign. For the broader field, the relevance-sufficiency gap reframes how researchers should evaluate memory systems: metrics should measure whether agents can construct complete, grounded evidence chains rather than merely retrieving topically similar memories, which has direct consequences for safety, reliability, and trustworthiness in autonomous agent applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22668v1)
