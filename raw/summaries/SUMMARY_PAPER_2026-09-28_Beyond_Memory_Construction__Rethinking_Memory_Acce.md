---
title: Beyond Memory Construction: Rethinking Memory Access for LLM-based Conversational Agents
url: http://arxiv.org/abs/2609.33226v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_05-07-21Z_BeyondMemoryConstruction_RethinkingMemoryAccessfor.md
generated_at: 2026-09-28 23:20
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Threader, a novel memory system for LLM-based conversational agents that replaces traditional LLM-driven memory construction with efficient access to raw interaction data. The authors demonstrate that existing approaches suffer from information loss and high costs in long-horizon conversations, whereas Threader preserves raw interactions as first-class memories organized via lightweight incremental segmentation. Experimental results show Threader achieves superior answer accuracy and evidence recall while drastically reducing computational overhead compared to standard RAG-based memory pipelines.

## Key Takeaways
- Current LLM-based memory construction paradigms degrade significantly in long-horizon, high-entropy conversations due to increasing information loss, instability as context grows, and prohibitive costs from repeated large language model invocations required for rewriting raw interactions into structured units.
- Threader fundamentally shifts the paradigm by treating raw interactions as first-class memory components, employing lightweight incremental segmentation to organize data into topic-coherent segments without rewriting, and utilizing multi-view representations to maintain fidelity while enabling efficient structure-aware access.
- The system implements a multi-signal retrieval mechanism at query time that combines segment-level access with localized evidence matching to ensure both completeness and coherence, resulting in consistent improvements in answer accuracy and evidence recall alongside a significant reduction in memory construction overhead.

## Context
As conversational agents increasingly operate over extended sessions with complex information density, the reliance on generative models for memory summarization has become a bottleneck that limits scalability and fidelity. This

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33226v1)
