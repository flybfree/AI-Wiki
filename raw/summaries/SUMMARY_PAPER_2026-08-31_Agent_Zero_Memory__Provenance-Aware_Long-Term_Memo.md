---
title: Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents
url: http://arxiv.org/abs/2608.29606v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_06-55-59Z_AgentZeroMemory_Provenance_AwareLong_TermMemoryfor.md
generated_at: 2026-08-31 20:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Agent Zero Memory, a provenance‑aware long‑term memory system for LLM agents that stores user data in three parallel structures: an episodic timeline, an associative knowledge graph, and a citation‑locked documentary hierarchy. Retrieval uses an intent gate, source router, and three concurrent searches to produce grounded answers with high confidence.

## Key Takeaways
- The episodic Memory Events timeline records when and what changed as first‑class events, enabling precise temporal retrieval.
- The associative entity‑event knowledge graph links people and projects across sessions, preserving relational context without a single store.
- Every answer is read under a citation lock that only cites evidence the reader actually opened, preventing fabrication.

## Context
Long‑term memory for LLM agents remains fragmented because most systems rely on one organizing structure, leading to blind spots. This work shows that integrating multiple provenance‑aware structures can improve factual accuracy while keeping costs low.

## Implications
Practitioners can adopt Agent Zero Memory to reduce hallucinations and latency in agent workflows. The approach sets a new benchmark for memory‑driven quality over model‑driven scaling, encouraging industry adoption of provenance‑centric design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29606v1)
