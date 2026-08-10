---
title: From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL
url: http://arxiv.org/abs/2608.07213v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_13-28-27Z_FromTest_TimeScalingtoReusableMemory_MeasuringCrys.md
generated_at: 2026-08-09 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the crystallization problem in text-to-SQL systems by measuring the future value of stored memory beyond immediate test-time scaling. On the BIRD benchmark, storing verified corrected queries boosts held-out first-attempt accuracy by 4.34 percentage points, which represents 44.4% of the accuracy headroom that on‑demand repair alone provides.

## Key Takeaways
- Storing verified corrected queries improves held-out first-attempt accuracy by 4.34 percentage points.
- This gain captures 44.4% of the accuracy headroom provided by on-demand repair on the same questions.
- Controlled interventions identify database‑specific content as the main operating ingredient.

## Context
Text-to-SQL models increasingly rely on external memory to handle complex queries, yet current evaluations treat each answer in isolation and ignore long‑term benefits. This work introduces a controlled methodology that isolates the effect of memory choices, offering a clearer picture of when and how memory reuse adds value.

## Implications
For researchers, this study highlights the need for evaluation protocols that capture sustained performance gains rather than transient test‑time fixes. Practitioners can leverage verified memory to improve real‑world system robustness while avoiding unnecessary computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07213v1)
