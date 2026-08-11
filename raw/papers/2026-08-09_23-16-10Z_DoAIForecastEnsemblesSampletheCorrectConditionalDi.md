---
title: Do AI Forecast Ensembles Sample the Correct Conditional Distribution?
published: 2026-08-09T23:16:10Z
authors: Lucas J. Howard, Elizabeth A. Barnes
url: http://arxiv.org/abs/2608.08954v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do AI Forecast Ensembles Sample the Correct Conditional Distribution?

## Abstract
Ensemble forecasting aims to sample the conditional distribution of outcomes; whether AI forecast ensembles do this correctly in a joint sense remains largely untested. We train a diffusion model for probabilistic subseasonal coastal sea level forecasts at eight US East Coast tide gauge stations, with sea level derived from reanalysis, and find that marginal and joint forecast quality decouple: positive skill at every station and lead time marginally, while joint spatial structure is worse than climatological draws. A shuffle-based permutation decomposition reveals this failure is invisible to the energy score but detected by the variogram score. Lorenz-96 experiments across 0.7-170 equivalent years show the gap persists regardless of training volume and is reproduced by a linear baseline, indicating structural inadequacy of the learned distribution. A dynamical ensemble does not replicate the failure while a deterministic emulator does, suggesting it is specific to learned emulators rather than ensemble forecasting generally.

## Metadata
- **Published**: 2026-08-09T23:16:10Z
- **Authors**: Lucas J. Howard, Elizabeth A. Barnes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08954v1)