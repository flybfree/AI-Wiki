---
title: Expert-Guided Forecast Editing for Time-Series Foundation Models
published: 2026-07-22T01:49:23Z
authors: Hung Le, Minh Hoang Nguyen, Manh Nguyen, Huu Hiep Nguyen, Dai Do
url: http://arxiv.org/abs/2607.19659v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Expert-Guided Forecast Editing for Time-Series Foundation Models

## Abstract
Time-series foundation models can forecast across heterogeneous domains without task-specific training, but their forecasts are fixed once produced and cannot directly incorporate task-specific expert feedback. We study expert-guided forecast editing: a frozen foundation model generates candidate future trajectories, and an expensive expert evaluator scores them to guide forecast revision. Under a tight query budget, two natural strategies sit at opposite ends: best-of-$N$ purely exploits the foundation model's predictive distribution, while optimization approaches mostly explore the forecast horizon as an unstructured high-dimensional vector. Each extreme is individually sub-optimal. We introduce \textbf{DEFT}, an expert-guided forecast editing framework that balances the two by first exploiting the foundation model's predictive samples in a decomposed trend--seasonal space, then exploring around them via component-wise refinement. DEFT queries the expert only on complete trajectories, then reuses scores for the trend and seasonal components that appeared in the queried recombinations. This lets each expert query provide structured component-level feedback while keeping the foundation model frozen. We compare DEFT against direct search approaches, including best-of-$N$, cross-entropy methods, and Bayesian optimization, under matched expert-query budgets. Across two forecasting benchmarks consisting of 78 datasets, three time-series foundation models, four feedback types, and seven query budgets, DEFT consistently improves the effectiveness of expert guidance. A molecular-dynamics case study further suggests that the same principle extends to more physically grounded feedback, supporting the hypothesis that sparse test-time guidance should be spent balancing prior exploitation with structured exploration.

## Metadata
- **Published**: 2026-07-22T01:49:23Z
- **Authors**: Hung Le, Minh Hoang Nguyen, Manh Nguyen, Huu Hiep Nguyen, Dai Do
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19659v1)