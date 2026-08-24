---
title: Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents
url: http://arxiv.org/abs/2608.20563v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-20_20-55-22Z_BeyondEnd_to_EndSuccess_DiagnosingFailuresinLong_H.md
generated_at: 2026-08-23 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a diagnostic methodology for long-horizon security LLM agents that isolates failures occurring before the model can use discovered information or state. Experiments reveal that failure rates differ between Gemini 2.5 Flash and Gemini 3.7 Flash, especially in tasks involving observed‑state reuse.

## Key Takeaways
- Many Gemini 2.5 Flash failures occur before the model observes the state it is later expected to reuse.
- Targeted protocol‑disambiguation guidance raises state observation from 65.5 % under a matched non‑guidance control message to 95.4 %, indicating that missing state is a bottleneck.
- With Gemini 3.7 Flash, adding the same guidance reduces state observation and further diminishes task completion reliability, suggesting that failure mechanisms shift across model generations.

## Context
Long‑horizon security LLM agents must retain information and decisions across many dependent interactions, making it difficult to attribute final success or failure. This work provides a systematic way to pinpoint upstream bottlenecks rather than relying on aggregate task outcomes.

## Implications
Practitioners can use checkpoint diagnostics to improve agent design and deployment reliability. Researchers should evaluate model‑specific failure patterns because the dominant source of failure may vary across generations, guiding responsible AI development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20563v1)
