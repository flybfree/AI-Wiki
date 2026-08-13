---
title: Who Thinks Best Depends on How Long You Let Them: Budget-Dependent Rankings in LLM Evaluation
url: http://arxiv.org/abs/2608.12150v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_15-11-35Z_WhoThinksBestDependsonHowLongYouLetThem_Budget_Dep.md
generated_at: 2026-08-12 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper challenges the assumption of stable LLM rankings by varying token budgets across seven levels and evaluates four models on three reasoning benchmarks, finding that model rankings can reverse with budget changes, some items show decreasing accuracy as more tokens are allowed, and a router using budget features reduces oracle gaps but only within domains.

## Key Takeaways
- 3–19% of items display non‑monotone behavior where accuracy drops when more tokens are allowed, even after accounting for truncation.
- Model rankings reverse on all benchmarks with high statistical significance (p < 0.01) according to McNemar tests.
- A budget‑aware router can close about 14% of the oracle gap across domains, improving within‑domain scores by up to +5.7 points but worsening transfer by -1.2 points.

## Context
This work highlights that standard LLM evaluation protocols ignore how computational constraints affect performance, a limitation for reliable model comparison and deployment planning. The findings suggest that evaluation must account for token budget variability to capture true reasoning ability.

## Implications
Practitioners should adopt budget‑aware evaluation frameworks to avoid misleading rankings and allocate resources more efficiently. Researchers need to incorporate context‑specific features into routing strategies to balance domain performance and transferability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12150v1)
