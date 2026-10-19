---
title: Harness-Delta Attribution: Dissecting Gains From Harness Evolution
url: http://arxiv.org/abs/2610.22466v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_17-39-38Z_Harness_DeltaAttribution_DissectingGainsFromHarnes.md
generated_at: 2026-10-18 20:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Harness-Delta Attribution (HDA), an evaluation protocol designed to dissect performance gains from harness evolution—where prompts, tools, and orchestration code are iteratively optimized around a fixed-weight model—into three components: benchmark-specific overfitting, gains attributable to test-time scaling, and residual generalizable improvement. Applied across 11 executor models and three harness-evolution frameworks spanning math, coding, creativity, and agentic tasks, the study finds that in 21 statistically significant settings, overfitting and test-time scaling together account for a majority of observed gains, while search-set improvements frequently fail to transfer to held-out tasks.

## Key Takeaways
- Overfitting and test-time scaling dominate reported gains: across 21 settings showing statistically significant search-set improvements, overfitting accounts for 54% of the gain on average and test-time scaling accounts for 14%, with their combined share exceeding 50% in 14 out of 21 settings. This means that much of what appears to be harness-evolution progress is actually memorization of the search set or simply spending more inference-time compute, not genuine generalizable capability improvement.
- Search-set gains do not reliably transfer to held-out tasks: the residual generalizable improvement and held-out transfer vary substantially across tasks, models, and frameworks, and the paper provides limited evidence that search-set gains persist under practical distribution shifts. Validation-based signals used during harness evolution are insufficient to prevent overfitting, undermining a common assumption that held-out validation during optimization guards against benchmark-specific memorization.
- Attribution-aware evaluation is necessary for meaningful progress: the HDA protocol provides an upper bound on residual generalizable improvement, enabling researchers to separate genuine harness improvements from artifacts of overfitting or compute scaling, and the authors argue future harness-evolution research must adopt such attribution-aware evaluation to avoid overstating progress.

## Context
Harness evolution represents a growing paradigm in agentic AI where model weights remain frozen while surrounding scaffolding—prompts, tool configurations, orchestration logic—is iteratively refined to boost task performance. This approach has gained traction because it sidesteps expensive model retraining, but the field has lacked rigorous methods to determine whether reported gains reflect true generalizable improvement or merely exploitation of the optimization target. This paper addresses that gap by formalizing an attribution framework that decomposes gains into interpretable components, bringing methodological rigor to a rapidly evolving subfield.

## Implications
For practitioners deploying agentic systems, this work serves as a caution that harness-evolution benchmarks may overstate real-world transferability, and organizations should not assume that search-set improvements will hold under distribution shifts encountered in production. For the research community, the findings motivate a shift toward attribution-aware evaluation protocols that explicitly separate overfitting, compute scaling, and genuine generalization, which could reshape how harness-evolution frameworks are designed, validated, and reported in future publications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22466v1)
