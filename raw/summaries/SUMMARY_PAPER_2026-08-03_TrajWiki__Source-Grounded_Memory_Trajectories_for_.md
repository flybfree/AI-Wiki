---
title: TrajWiki: Source-Grounded Memory Trajectories for Long-Horizon Dialogue Agents
url: http://arxiv.org/abs/2608.00967v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_03-36-03Z_TrajWiki_Source_GroundedMemoryTrajectoriesforLong_.md
generated_at: 2026-08-03 20:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TrajWiki, a trajectory‑based memory framework that stores conversational information as immutable snapshots linked by source‑grounded operations such as ADD, REVISE, and DEPRECATE. Experiments on LoCoMo and MedMT demonstrate that TrajWiki boosts long‑horizon dialogue performance for both open‑source and closed‑source LLMs while offering clear diagnostic visibility into memory evolution.

## Key Takeaways
- The framework treats each memory as a source‑grounded evolution trajectory, preserving how information originates, evolves, conflicts, or becomes obsolete over time.
- Memory Wiki acts as a persistent intermediate layer that compiles dialogue history into structured wiki pages linking entities, events, quantities, topics, and conflicts to reduce fragmentation and retrieval cost.
- The hierarchical query routing from wiki pages to memory snapshots yields evidence‑grounded answer synthesis and improves performance across diverse LLM backbones.

## Context
Current AI research focuses on augmenting language models with external memory to sustain dialogue over many turns. Most approaches store memories as static or overwritable states, which obscures provenance and makes debugging difficult. TrajWiki addresses these limitations by providing a traceable, updatable representation of conversational knowledge.

## Implications
For practitioners, TrajWiki offers a transparent way to monitor memory integrity and retrieve relevant evidence during inference, reducing hallucinations and improving reliability. The approach could be adopted in enterprise chatbots where accountability and explainability are critical, fostering trust in AI‑driven conversations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00967v1)
