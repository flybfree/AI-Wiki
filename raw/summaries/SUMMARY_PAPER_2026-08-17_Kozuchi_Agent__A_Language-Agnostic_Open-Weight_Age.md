---
title: Kozuchi Agent: A Language-Agnostic Open-Weight Agent for Software Repair
url: http://arxiv.org/abs/2608.15579v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_07-06-37Z_KozuchiAgent_ALanguage_AgnosticOpen_WeightAgentfor.md
generated_at: 2026-08-17 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Kozuchi Agent, a language‑agnostic open‑weight repair agent that turns bug reports into correct patches without fine‑tuning. It achieves 374/500 SWE‑bench Verified fixes using locally hosted Qwen3.5‑27B and scores highly across Java, Python, and Multi‑SWE‑bench.

## Key Takeaways
- The agent resolves 374 out of 500 SWE‑bench Verified instances on the official evaluator, demonstrating strong performance without proprietary models.
- It maintains consistent per‑phase behavior within ±5 percentage points across Java, Python, and Multi‑SWE‑bench, showing language‑agnostic reliability.
- The CI pipeline reduces operator touch‑points from five to one, enabling reproducible runs on heterogeneous clusters.

## Context
LLM‑based software repair is a growing research area where agents must generate accurate patches while being open‑weight and auditable. Existing solutions often rely on fine‑tuned proprietary models or complex tool‑use pipelines that limit reproducibility.

## Implications
Kozuchi shows that open‑weight, deterministic agents can rival closed systems in SWE benchmarks, encouraging industry adoption of transparent repair tools. Its CI integration lowers operational overhead, making large‑scale bug fixing more feasible for teams with limited resources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15579v1)
