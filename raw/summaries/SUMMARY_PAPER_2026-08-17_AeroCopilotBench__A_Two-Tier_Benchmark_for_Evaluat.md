---
title: AeroCopilotBench: A Two-Tier Benchmark for Evaluating LLM Agents as Aviation Copilots in an Interactive Virtual Cockpit Environment
url: http://arxiv.org/abs/2608.16349v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_09-53-52Z_AeroCopilotBench_ATwo_TierBenchmarkforEvaluatingLL.md
generated_at: 2026-08-17 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AeroCopilotBench, a two‑tier benchmark that tests large language model agents as aviation copilots in an interactive virtual cockpit. The study shows that while static knowledge scores improve across models, procedural execution and safety compliance remain inconsistent, with the best Tier‑2 success rate reaching 72.6 %.

## Key Takeaways
- Tier‑1 evaluates pure aviation knowledge through 1,200 multiple‑choice questions, yet its performance does not reliably predict real‑world task completion in dynamic environments.
- Tier‑2 comprises 73 emergency tasks instantiated in the ACOE environment, and success depends on meeting hard safety constraints without violating trajectory safety, highlighting procedural completeness as a critical failure mode.
- The benchmark uncovers recurring issues such as poor state feedback usage and long‑horizon execution management across 451 failed episodes from representative models.

## Context
Aviation AI research has focused largely on static knowledge retrieval, overlooking the need for dynamic, safety‑critical interaction. This work bridges that gap by providing a reproducible virtual cockpit where agents must translate natural language into executable state transitions and enforce hard constraints.

## Implications
The findings underscore that deploying LLM agents in aviation requires more than knowledge checks; they demand robust procedural execution and continuous safety monitoring. Practitioners can leverage AeroCopilotBench to iteratively improve agent design, ensuring both task completion and operational safety in real‑world cockpits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16349v1)
