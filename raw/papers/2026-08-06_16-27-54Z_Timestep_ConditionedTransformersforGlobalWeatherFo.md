---
title: Timestep-Conditioned Transformers for Global Weather Forecasting
published: 2026-08-06T16:27:54Z
authors: Sam Levang, Fran Bartolic, Ty Dickinson, Chase Dwelle, Paulius Rauba, Viktor Cikojevic
url: http://arxiv.org/abs/2608.06241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Timestep-Conditioned Transformers for Global Weather Forecasting

## Abstract
Existing machine-learning weather forecasting models rely on predetermined and fixed autoregressive timesteps. The choice of model timestep involves a fundamental trade-off: shorter timesteps (e.g. 1 to 6 hours) finely resolve atmospheric dynamics within the diurnal cycle but increase error accumulation for a given forecast horizon, while longer timesteps (e.g. 24 hours) reduce error accumulation but limit the usability of short-range forecasts where sub-daily predictability is high. In this work, we present GEM-3, a probabilistic global weather model that addresses this trade-off through explicit multi-timestep inference. With a single set of trained weights, the model timestep can be configured at inference time to balance predictability and usability across a broad forecast horizon. Additionally, we find that mixed-timestep training consistently improves rollout stability relative to timestep-specialist models. Under the hood, GEM-3 is a lightweight neighborhood-attention transformer with ~134M parameters on an equirectangular grid with a number of architectural advancements beyond its predecessor GEM-2. The result is a practical forecasting system that couples near-SOTA medium-range probabilistic skill, stable extended-range rollouts, efficient training and inference, and decision-relevant diagnostics.

## Metadata
- **Published**: 2026-08-06T16:27:54Z
- **Authors**: Sam Levang, Fran Bartolic, Ty Dickinson, Chase Dwelle, Paulius Rauba, Viktor Cikojevic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06241v1)