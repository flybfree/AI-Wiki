---
title: Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents
url: http://arxiv.org/abs/2609.04875v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_08-31-40Z_ForgettingWithoutRestarting_Execution_StateUnlearn.md
generated_at: 2026-09-06 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces execution‑state unlearning for stateful LLM agents, showing that naive memory deletion leaves derived artifacts unchanged. It proves a lower bound on recomputed transitions needed and presents Provenance‑Guided Selective Replay achieving it. The method restores counterfactual behavior by repairing provenance graphs and truncating KV caches.

## Key Takeaways
- Execution‑state unlearning requires at least T‑τ+1 recomputed transitions where τ is the injection step, meaning only a small window after forgetting must be fixed.
- Provenance‑Guided Selective Replay creates a cross‑layer contract that locates the target’s injection point and restores the KV cache by cropping it, eliminating leakage from deleted memory.
- Audits show instruction‑based forgetting collapses under elicitation (Leak@probes = 1.00) while source redaction still respects revoked preferences in 80% of episodes.

## Context
Stateful LLM agents accumulate persistent artifacts beyond the transcript, making traditional “forget” operations insufficient for privacy and correctness. This work formalizes execution‑state unlearning to address these hidden side effects.

## Implications
Practitioners can implement selective replay to reduce recomputation costs by up to ninefold, offering a scalable path toward truly forgetful agents without full resets. The approach also clarifies the limits of memory deletion in large language systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04875v1)
