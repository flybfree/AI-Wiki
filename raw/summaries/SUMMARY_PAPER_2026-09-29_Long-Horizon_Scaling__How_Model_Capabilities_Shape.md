---
title: Long-Horizon Scaling: How Model Capabilities Shape the Returns to Computation
url: http://arxiv.org/abs/2609.35236v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_14-11-57Z_Long_HorizonScaling_HowModelCapabilitiesShapetheRe.md
generated_at: 2026-09-29 02:08
model: qwen3.6-35b-a3b
---

## Summary
This study examines how model capabilities influence the returns to computation for long-horizon agents by analyzing performance on AutoLab and EdgeBench benchmarks. The authors reveal that starting scores and subsequent growth stem from different capability profiles, meaning similar early results can lead to divergent future gains. By modeling these dynamics with category-specific logistic power laws, they derive a continuation policy that optimizes resource usage, saving significant time while incurring minimal score loss compared to full execution runs.

## Key Takeaways
- Early performance metrics are decoupled from long-horizon growth trajectories; models with comparable initial scores can exhibit vastly different improvement patterns based on distinct capability profiles, necessitating category-specific logistic power laws fitted to early data to accurately extrapolate future score distributions and identify the fraction of tasks likely to improve.
- Aggregate improvements often obscure a narrowing distribution of gains where continued progress concentrates among fewer models rather than spreading uniformly across the population, highlighting that rising average scores mask diminishing improvement opportunities for the majority of runs.
- The proposed continuation policy dynamically evaluates whether to extend agent interactions by weighing predicted growth against computation costs, achieving approximately one-third savings in time and resources with relative score losses of only 2.4% on AutoLab individual runs and 3.3% on EdgeBench published mean curves.

## Context
Long-horizon agents are

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35236v1)
