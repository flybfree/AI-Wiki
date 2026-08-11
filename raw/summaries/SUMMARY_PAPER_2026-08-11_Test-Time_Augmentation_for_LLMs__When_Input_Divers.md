---
title: Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute
url: http://arxiv.org/abs/2608.09351v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_09-31-48Z_Test_TimeAugmentationforLLMs_WhenInputDiversityBea.md
generated_at: 2026-08-11 12:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates test-time augmentation (TTA) for large language models and compares input-side diversity with output-side self-consistency under matched compute budgets. It finds that varying the input yields higher accuracy per dollar spent than repeating reasoning paths alone, especially for mid-tier models where stronger models are costly.

## Key Takeaways
- Semantic rephrasing provides consistent and statistically significant accuracy gains across tasks while Pareto-dominating self-consistency on cost-effectiveness. - TTA delivers roughly 1.8 times more accuracy per dollar than self-consistency, outperforming it on five of six evaluated datasets. - The approach is most effective for mid-tier models where a stronger model is unavailable or too expensive.

## Context
Test-time scaling has become a key focus in LLM deployment as compute budgets are limited. Prior methods concentrate on output diversity through repeated reasoning, but input perturbations offer an alternative way to improve accuracy without sacrificing speed.

## Implications
For practitioners, TTA suggests that diversifying inputs can be a cost-effective strategy for improving model performance when upgrading hardware is impractical. This insight may guide resource allocation in AI services where compute efficiency directly impacts profitability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09351v1)
