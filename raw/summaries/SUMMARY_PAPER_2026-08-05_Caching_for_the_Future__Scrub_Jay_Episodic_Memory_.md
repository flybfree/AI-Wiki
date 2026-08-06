---
title: Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems
url: http://arxiv.org/abs/2608.04746v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_12-12-44Z_CachingfortheFuture_ScrubJayEpisodicMemoryPrincipl.md
generated_at: 2026-08-05 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes ScrubJay-MEM, an agent memory system that models episodic memory using per-memory type-conditioned decay coefficients π_i and utility horizons τ_i. It demonstrates that this approach improves retrieval performance on benchmark tests compared to existing memory stores. The Temporal Generalization Test shows a positive GenGap of +0.108.

## Key Takeaways
- Each memory is assigned a perishability coefficient π_i derived from the scrub jay’s episodic decay pattern, allowing content to fade over time based on its type and utility horizon τ_i.
- Retrieval uses query‑adaptive scoring that weights recent and relevant memories higher, preventing contamination by stale facts.
- Ablation shows that removing type‑conditioned decay reduces GenGap by 5.7×, proving the necessity of this mechanism.

## Context
Current LLM agents store all retrieved information persistently, leading to outdated context in downstream tasks. This work introduces a biologically inspired memory model that respects temporal decay, aligning AI behavior with animal episodic learning.

## Implications
For practitioners, ScrubJay-MEM offers a lightweight way to manage memory freshness without sacrificing performance. The approach can be integrated into any LLM pipeline to enhance factual consistency and reduce hallucination in long‑running conversations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04746v1)
