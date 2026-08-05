---
title: Can Training Logs Make Model Comparisons More Precise?
published: 2026-08-03T16:08:14Z
authors: Wei-Jung Huang
url: http://arxiv.org/abs/2608.02705v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Training Logs Make Model Comparisons More Precise?

## Abstract
Comparing stochastically trained models requires estimating both a performance difference and its uncertainty from repeated runs. We study whether training logs from those same runs can make such comparisons more precise. Because training-log covariates are produced during training rather than measured before it, we use arm-specific covariate adjustment: each model is adjusted only with statistics from its own runs, and the raw mean difference remains the reported effect. In a vision study spanning three architectures and three datasets, simple adjustments based on early training logs often reduce uncertainty in model comparisons. The main limitation is covariate selection. Broadly searching the log pool for the most correlated statistic often adds more noise than it removes, even when useful statistics exist in hindsight. Training logs therefore appear useful for more precise model comparisons, but only when the adjustment avoids large selection noise.

## Metadata
- **Published**: 2026-08-03T16:08:14Z
- **Authors**: Wei-Jung Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02705v1)