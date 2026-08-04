---
title: PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning
url: http://arxiv.org/abs/2608.01837v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-47-59Z_PCSD_PersistentConsistencyforSelf_DistillationinAg.md
generated_at: 2026-08-03 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Persistent Consistency Self-Distillation (PCSD) to improve on‑policy self‑distillation for large language model agents in reinforcement learning. It learns token‑level distillation weights by measuring how long teacher signals persist and uses adaptive windows with sigmoid gating, achieving higher performance than GRPO and SDAR on ALFWorld.

## Key Takeaways
- PCSD derives token‑level distillation weights from the local persistence of teacher‑favoring signals rather than relying on isolated discrepancies.  
- It combines adaptive windows with exponentially decayed aggregation to capture persistent relative support, applying trend‑aware modulation that attenuates locally declining support.  
- The continuous sigmoid‑gated weights are jointly optimized with GRPO, merging dense teacher guidance with sparse environmental feedback.

## Context
Self‑distillation is a promising way to give agents fine‑grained supervision without requiring extra inference skills, but existing methods often suffer from noisy token scores or fixed step‑level weighting. The ALFWorld benchmark tests multi‑turn dialogue RL where rewards are extremely sparse, highlighting the need for robust teacher signals.

## Implications
For practitioners developing agentic LLMs, PCSD offers a practical framework to boost reward efficiency in long trajectories. By integrating persistent consistency into distillation, researchers can achieve higher overall scores with minimal extra compute, encouraging wider adoption of self‑distillation in real‑world interactive systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01837v1)
