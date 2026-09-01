---
title: Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation and Model Contributions
published: 2026-08-31T13:49:00Z
authors: Rodrigo Almeida, Noelia Otero, Jost Arndt, Simon Baur, Wojciech Samek, Jackie Ma
url: http://arxiv.org/abs/2608.30795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation and Model Contributions

## Abstract
End-to-end weather forecasting systems produce skillful global gridded and station forecasts directly from raw Earth observations, replacing the numerical weather prediction pipeline, including data assimilation, at a fraction of its cost. These systems are deterministic and issue no uncertainty. Here we render the Aardvark Weather model probabilistic by attaching one stochastic mechanism to each component: learned, input-dependent noise at the observation encoder, capturing aleatoric uncertainty inherited from the observing system, and Monte Carlo dropout in the processor, capturing epistemic uncertainty in the learned dynamics. The resulting nested ensemble attributes forecast spread to the two sources through a law-of-total-variance decomposition, cross-checked by withholding observation streams. Probabilistic finetuning significantly improves the mean forecast, by 4.2% on average across variables and lead times. The ensemble is calibrated against ERA5 through the medium range (spread-skill ratio 0.98), keeps station RMSE within 2.4% of the deterministic model while beating it in CRPS at every lead time, and trails the operational ECMWF ensemble. The encoder branch behaves as observation-driven uncertainty. Component-attributed uncertainty makes end-to-end forecasts more transparent, a step toward observation-driven digital twins of the atmosphere.

## Metadata
- **Published**: 2026-08-31T13:49:00Z
- **Authors**: Rodrigo Almeida, Noelia Otero, Jost Arndt, Simon Baur, Wojciech Samek, Jackie Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30795v1)