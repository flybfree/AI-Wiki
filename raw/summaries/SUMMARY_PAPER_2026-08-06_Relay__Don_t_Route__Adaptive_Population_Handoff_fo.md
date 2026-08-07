---
title: Relay, Don't Route: Adaptive Population Handoff for Cost-Efficient LLM-Driven Evolution
url: http://arxiv.org/abs/2608.05651v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_06-48-08Z_Relay_Don_tRoute_AdaptivePopulationHandoffforCost_.md
generated_at: 2026-08-06 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a training‑free framework called model that reduces cost in LLM‑driven evolutionary search by shifting budget allocation from individual queries to evolving populations through adaptive population handoff, achieving higher mean scores across benchmarks and budgets. The framework demonstrates that early progress can be captured efficiently with cheaper models.

## Key Takeaways
- Early trajectory performance is informative but noisy, allowing cheap models to recover much of the early progress achieved by strong models at lower cost.
- The scheduler uses relay gain, a marginal improvement metric from a compact quality‑diverse candidate bank, to decide when to hand off.
- Across four benchmarks and three budgets, model achieves the highest mean score in 11 of 12 settings, outperforming competitive baselines.

## Context
LLM‑driven evolution is gaining traction for program search but suffers from high inference costs as strong models are used throughout long runs. This work addresses the inefficiency by rethinking budget allocation at a population level rather than per query, highlighting that early progress can be captured efficiently with cheaper models.

## Implications
By organizing budgets around evolving populations, practitioners can deploy cheaper models effectively and achieve comparable or better results, reducing operational expenses in large‑scale evolutionary AI projects and enabling broader adoption of LLM‑driven search methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05651v1)
