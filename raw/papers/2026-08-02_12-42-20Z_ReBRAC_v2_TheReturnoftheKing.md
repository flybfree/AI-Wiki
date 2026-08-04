---
title: ReBRAC-v2: The Return of the King
published: 2026-08-02T12:42:20Z
authors: Denis Tarasov, Robert K. Katzschmann
url: http://arxiv.org/abs/2608.01205v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReBRAC-v2: The Return of the King

## Abstract
Recent offline reinforcement learning methods increasingly rely on expressive generative policies and specialized value-guidance mechanisms. We ask whether comparable progress can instead come from systematically modernizing a conventional behavior-regularized actor-critic while preserving its algorithmic simplicity. We introduce ReBRAC-v2, which directly trains an exact-likelihood normalizing flow as the RL actor, combines likelihood, MSE, and MAE behavior regularization, and integrates a classification-based residual critic, staged optimization, and multi-sample test-time action selection. Rather than tuning this recipe separately for every task, we develop a single shared configuration via roughly 600 Bayesian proposals on six challenging OGBench tasks, freeze all structural and optimization choices, and adapt only two behavior-regularization coefficients over a 16-point grid. Across ten common state-based OGBench categories, ReBRAC-v2 averages 74.8 compared to 52.3 for the next-best aggregate result and ranks first in eight categories. The same recipe, without structural changes, obtains the strongest averages in our comparisons on D4RL AntMaze (90.2) and Adroit (33.6). Fixed-recipe ablations show the largest sensitivity to the selected mixed cloning objective, staged training, sufficient flow capacity, and multi-sample inference, while showing that several smaller choices depend on the values of other hyperparameters. These results show that disciplined, transferable engineering can achieve state-of-the-art aggregate performance without abandoning a minimalist offline RL foundation.

## Metadata
- **Published**: 2026-08-02T12:42:20Z
- **Authors**: Denis Tarasov, Robert K. Katzschmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01205v1)