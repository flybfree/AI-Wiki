---
title: FinPerMA: A Theory-Informed, Event-Grounded Personalized-Memory Benchmark for LLM Agents
url: http://arxiv.org/abs/2608.04095v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_18-00-04Z_FinPerMA_ATheory_Informed_Event_GroundedPersonaliz.md
generated_at: 2026-08-05 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FinPerMA, an event‑grounded benchmark that tests whether LLM agents can retain and adapt a personalized user model over long horizons in high‑stakes domains such as finance. The study shows that seven frontier models remain far from saturated on 2,994 questions across 276 personas, achieving only about 0.47 overall accuracy or 39% on multiple‑choice items after shocks.

## Key Takeaways
- FinPerMA evaluates personalized memory using frozen longitudinal investor trajectories and deterministic impact rules, isolating whether an agent integrates material events into its persistent user model.
- The benchmark reveals that no full‑context configuration exceeds roughly 0.47 overall accuracy or 39% on multiple‑choice questions, indicating significant performance gaps after shocks.
- Simple retrieval outperforms summary‑based memory systems, and the advantage widens as new events are incorporated.

## Context
The paper addresses a longstanding challenge in LLM personalization: maintaining individualized knowledge over time without forgetting. By grounding evaluation in real investor trajectories, FinPerMA provides a more realistic test of event‑driven adaptation than static factual recall benchmarks. This approach aligns with the trend toward dynamic, context‑aware agents that must respond to changing user preferences.

## Implications
For industry practitioners, FinPerMA highlights the limitations of current memory architectures in high‑stakes advisory roles where personalization is critical. The findings suggest a shift toward lightweight retrieval methods or hybrid systems that balance factual accuracy with preference adaptation. Researchers should prioritize event‑grounded evaluation to guide future model design and deployment strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04095v1)
