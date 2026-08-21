---
title: StreamSoccer: Event-Driven Memory for Streaming Soccer Commentary
url: http://arxiv.org/abs/2608.19723v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_07-19-29Z_StreamSoccer_Event_DrivenMemoryforStreamingSoccerC.md
generated_at: 2026-08-20 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces StreamSoccer, an event-driven architecture for generating live soccer commentary that maintains a causal memory of completed events while producing three modes: current-event, recent-window, and historical-memory. Experiments on 174 raw‑video runs across 58 matches show per‑minute RTF p95 between 0.10 and 0.22 without long‑term growth, confirming that event memory enables streaming commentary with bounded computation.

## Key Takeaways
- StreamSoccer uses a fixed‑budget active memory to retain completed events locally and consolidate them into retrievable records, allowing the system to describe past actions only when appropriate.
- The unified generator combines current, recent, and historical context to produce three distinct commentary modes, with a rule‑assisted scheduler choosing among them or silence based on temporal cues.
- Ablations demonstrate that local retained events improve all evaluation tracks, indicating that event memory is essential for both short‑term and long‑term performance.

## Context
Streaming video understanding remains challenging because models must update state continuously while managing unbounded history. Traditional approaches rely on frame‑level caches or fixed output windows, which cannot capture the dynamic nature of live events such as soccer goals and fouls. StreamSoccer’s event memory model offers a principled way to handle long‑term dependencies in real time.

## Implications
For sports broadcasting platforms, this work shows that event‑based memory can reduce latency and computational load without sacrificing recall accuracy. Practitioners may adopt similar architectures for any live commentary where temporal context matters, such as news or gaming streams.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19723v1)
