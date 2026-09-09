---
title: NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness
url: http://arxiv.org/abs/2609.08183v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_03-14-54Z_NeoHorse_1_TowardsRecursiveSelf_ImprovementviaAgen.md
generated_at: 2026-09-08 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces NeoHorse‑1, a set of agent‑native models that enable recursive self‑improvement by turning evaluation feedback into the next training mixture. The approach uses intelligent routing to collect capability demand records and converts them into structured training examples across three curriculum stages.

## Key Takeaways
- The system records predicted capability demand, selected service tier, and interaction for each user turn, preserving interleaved reasoning, tool calls, and harness context as training data.
- Routing signals organize fine‑tuning into a three‑stage curriculum and extend to routing‑guided on‑policy distillation where a teacher supervises student responses under the same progression.
- The evaluation‑selection‑update loop closes by converting feedback into the next training mixture, improving macro‑averages from 58.94 to 64.87 at 4B and from 65.60 to 69.04 at 9B.

## Context
Neuro‑recursive self‑improvement is a central goal in AI safety research, aiming for systems that can iteratively enhance their own capabilities. NeoHorse‑1 demonstrates a concrete harness‑mediated mechanism that bridges evaluation and learning without requiring external supervision.

## Implications
This work offers a prototype framework for harness‑driven RSI that could be adapted to various model sizes and domains. Practitioners may leverage it to reduce the gap between smaller post‑trained models and larger baselines, accelerating progress toward more capable agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08183v1)
