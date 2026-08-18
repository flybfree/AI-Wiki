---
title: $R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets
url: http://arxiv.org/abs/2608.16033v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_02-59-58Z_R_3__Bench_LLMsStrugglewithResource_RationalReason.md
generated_at: 2026-08-17 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces R³‑Bench, a benchmark that tests six problem suites — mathematics, competitive programming, and abstract reasoning — under shared computational budgets across tool‑free and agentic settings. The results show that the offline empirical oracle derived from single‑problem response curves matches or exceeds contest performance in all cells, highlighting a persistent gap between demonstrated competence and resource‑rational execution.

## Key Takeaways
- The offline oracle outperforms contest averages in every main‑table cell, indicating that shared budgets do not fully capture model capabilities.  
- Under moderate tool‑free pressure, equal‑allocation replay exceeds contest performance for four of the six models, suggesting that simple strategies can be effective when resources are limited.  
- Diagnostic analysis reveals limited strategy updating and failure patterns that depend on pressure, with no single scheduler dominating across all domains.

## Context
R³‑Bench addresses a gap in AI evaluation where most benchmarks allocate independent budgets per task, ignoring how models share computational resources. This misalignment can lead to unrealistic performance estimates and hinder fair comparison of resource‑rational agents.

## Implications
For researchers, the findings underscore the need for shared‑budget testing as a standard metric alongside single‑task scores. Practitioners should consider how budget constraints affect real‑world deployment and may design adaptive strategies that update allocation policies under pressure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16033v1)
