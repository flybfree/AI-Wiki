---
title: Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in Interactive Narratives
url: http://arxiv.org/abs/2608.08160v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_14-38-18Z_CanLLMAgentsSticktotheScript_ABenchmarkforLong_Hor.md
generated_at: 2026-08-10 22:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the challenge of maintaining long‑horizon logical consistency in interactive narratives when LLMs generate dialogue. It introduces NCP‑Bench, a benchmark with 100 narrative environments, and shows that even top models like GPT‑5.2 fail to preserve commitments after many turns.

## Key Takeaways
- The best model survives only 42% of the 100‑turn limit, indicating persistent logical drift despite high linguistic quality.
- Fact conflict rates reach as high as 68%, showing that adversarial user actions can break narrative integrity quickly.
- NCP‑Bench quantifies commitment preservation across state‑of‑the‑art LLMs, revealing a systematic gap between fluency and consistency.

## Context
This work matters because interactive storytelling increasingly relies on AI agents to generate coherent plots without human oversight. Existing benchmarks focus on short‑term coherence or user satisfaction but ignore sustained logical tracking over many exchanges.

## Implications
For game developers, the findings warn that current LLMs cannot reliably sustain story arcs beyond a few turns, prompting a need for hybrid systems or explicit consistency constraints. Practitioners must design evaluation metrics that capture long‑horizon commitment preservation rather than just surface fluency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08160v1)
