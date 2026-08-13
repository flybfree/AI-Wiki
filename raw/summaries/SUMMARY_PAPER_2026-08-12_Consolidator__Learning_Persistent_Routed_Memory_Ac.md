---
title: Consolidator: Learning Persistent Routed Memory Across Context Boundaries
url: http://arxiv.org/abs/2608.11701v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_06-26-53Z_Consolidator_LearningPersistentRoutedMemoryAcrossC.md
generated_at: 2026-08-12 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Consolidator, a lightweight operator that moves short‑term memory into long‑term storage while preserving routing information. On a modulo‑10 mapping task it raises recall by over forty points without affecting immediate STM performance. The approach demonstrates that LTM can influence subsequent slot selection, bridging the gap between storage and retrieval.

## Key Takeaways
- Consolidator transfers STM content to LTM without replaying source tokens, keeping KV caches empty after each step.
- The retained LTM is read later and also feeds the hierarchical router, shaping which explicit‑memory slots are accessed next.
- Training only 12.35K parameters yields a 42‑point recall boost compared with forced identity accumulation.

## Context
In modern transformer architectures, memory is often treated as static, limiting the ability to condition later outputs on earlier states. This work shows that dynamic consolidation can provide both storage and routing capabilities within existing models.

## Implications
This modular design can be integrated into any encoder‑decoder pipeline, allowing efficient long‑term state management across context boundaries. For practitioners, it offers a way to reduce trainable parameters while enabling adaptive memory access in large language systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11701v1)
