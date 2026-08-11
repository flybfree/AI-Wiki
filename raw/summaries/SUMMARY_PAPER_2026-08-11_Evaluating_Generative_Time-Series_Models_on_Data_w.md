---
title: Evaluating Generative Time-Series Models on Data with Point Masses
url: http://arxiv.org/abs/2608.09692v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_14-57-36Z_EvaluatingGenerativeTime_SeriesModelsonDatawithPoi.md
generated_at: 2026-08-11 12:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how generative time‑series models perform when evaluated on data that concentrate probability mass on a single value, such as zeros or rare events. The authors show that standard evaluation protocols can mislead by comparing windows with different atom structures and that certain metrics become invariant only because of artificial constraints. Benchmarking seven models reveals an autoregressive hurdle outperforming a conditional flow model by up to 153× on several datasets, while the flow’s performance varies widely across seeds.

## Key Takeaways
- The rolling‑origin protocol can produce misleading scores when evaluation windows contain far fewer non‑zero atoms than the dataset, as seen with 42 % zeros versus 13 % in one benchmark.  
- A control experiment demonstrates that CRPS invariance is achieved by construction and isolates how much temporal coupling contributes to the statistic.  
- The autoregressive hurdle model consistently beats the conditional flow model across five of six datasets, with performance differences up to a factor of 153, whereas the flow’s occurrence statistics fluctuate by up to 62 % with training seeds.

## Context
Generative time‑series models are widely used for forecasting and simulation tasks, yet most benchmark datasets feature sparse non‑zero events. Traditional evaluation methods assume comparable atom structures between data and windows, which may not hold in real‑world scenarios where rare events dominate. This paper addresses the gap by introducing more realistic evaluation protocols that respect the underlying probability mass distribution.

## Implications
For practitioners selecting or deploying generative models, it is essential to evaluate them under conditions that mirror actual data sparsity rather than relying on synthetic benchmarks with balanced atom structures. The findings suggest that model ordering and performance can be highly sensitive to occurrence statistics, guiding more robust experimental design in AI research and industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09692v1)
