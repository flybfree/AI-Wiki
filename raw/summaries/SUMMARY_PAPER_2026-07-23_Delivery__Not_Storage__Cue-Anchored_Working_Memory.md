---
title: Delivery, Not Storage: Cue-Anchored Working Memory as a Harness Property for Coding Agents
url: http://arxiv.org/abs/2607.20972v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_06-50-04Z_Delivery_NotStorage_Cue_AnchoredWorkingMemoryasaHa.md
generated_at: 2026-07-23 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a two-tier memory design for coding agents where long-term storage is minimal and the primary load-bearing memory is cue-anchored, enabling automatic retrieval without agent choice. Experiments show voluntary memory use is negligible and deterministic harness injection restores lost facts across compactions. These findings demonstrate that the harness can act as a reliable memory channel without requiring agent‑level storage decisions.

## Key Takeaways
- Voluntary memory operations are zero in 114 turns despite a pre-seeded store.
- Deterministic injection via the harness ensures facts survive all 138 compact-resumes with no false alarms.
- The deprived agent rebuilds missing facts by grepping session files, while harness‑owned stored facts persist.

## Context
This work aligns with cognitive memory offloading research and challenges the assumption that agents must manage their own long-term storage. By treating cue‑anchored memory as a harness property, it mirrors human procedural knowledge that is not explicitly written but triggered automatically.

## Implications
For AI developers, this suggests building memory systems that are transparent to the agent rather than requiring explicit encoding decisions. It could lead to more reliable agents with less operational overhead and better persistence across restarts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20972v1)
