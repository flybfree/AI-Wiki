---
title: Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV
url: http://arxiv.org/abs/2607.23693v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_14-37-53Z_ComputeGlobally_MaterializeLocally_TheMemoryContra.md
generated_at: 2026-07-27 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how long‑term agents can reuse a KV cache as memory, focusing on the effect of evicting earlier observations and whether retained events still contain useful information. Experiments show that when an observation is omitted, certain cached rows retain their original value with high accuracy, indicating that the model can materialize computation locally even without the source event. The authors introduce “semantic materialization” as a memory contract governing what is written, where it lands, and what survives after eviction.

## Key Takeaways
- A retained KV row can act as an independent view of earlier computation, preserving its value despite the original observation being dropped.
- Deliberately phrasing answer‑free events improves donor‑aligned recovery from 6% to 51%, while passively harvesting natural mentions yields no benefit.
- The durability of a memory entry depends on phrasing; two equally understood phrases can produce divergent outcomes, showing that meaning alone does not guarantee survival.

## Context
Long‑horizon agents often rely on KV caches to store intermediate states, but the field rarely tests whether evicted entries still influence later performance. This work bridges theory and practice by empirically measuring the resilience of sparse event‑KV serving under real model behavior.

## Implications
For practitioners managing long conversations, this suggests that carefully crafted memory contracts can boost efficiency without sacrificing accuracy. It also warns against assuming that dropping a source event is harmless if downstream metrics remain stable, highlighting the need for explicit materialization strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23693v1)
