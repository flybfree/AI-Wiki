---
title: What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial LLM API Migrations
url: http://arxiv.org/abs/2608.17719v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_12-44-54Z_WhatAggregateScoresMiss_MeasuringItem_LevelRegress.md
generated_at: 2026-08-18 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how aggregate benchmark scores obscure item‑level performance changes during commercial LLM API migrations, using three successive GPT‑5.4 to GPT‑5.6 upgrades and a set of 900 public items tested repeatedly under controlled false‑discovery rates.

## Key Takeaways
- Across all migration‑benchmark cells reliable improvements and reliable regressions appear together, showing that a single net gain can hide up to 8.3 % of items that actually worsened.
- Aggregate losses contain up to 10.7 % reliably improved items, indicating that a negative score may be driven by a minority of worsening cases.
- On the instruction‑following benchmark the strict and loose scoring gap widens by 3.9 points on the latest migration, reducing a 3.9‑point regression to only 0.04 points under loose scoring.

## Context
In AI research and industry practice, model migrations are often judged by overall score improvements that aggregate heterogeneous test results into a single metric. This approach can mask important trade‑offs between different domains of knowledge or task types, leading to suboptimal deployment decisions.

## Implications
Practitioners relying solely on aggregate scores risk deploying models that perform poorly for specific tasks while reporting higher overall metrics. The paper calls for item‑level regression analysis to provide a more nuanced view and mitigate the risks associated with blind reliance on compressed performance numbers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17719v1)
