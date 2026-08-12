---
title: Fisher8: Stabilizing Neural Heteroscedastic Regression via Output-Layer Fisher Geometry
published: 2026-08-11T02:10:51Z
authors: Sumedh Vemuganti, Nickvash Kani
url: http://arxiv.org/abs/2608.10374v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fisher8: Stabilizing Neural Heteroscedastic Regression via Output-Layer Fisher Geometry

## Abstract
Training neural networks to jointly predict mean and uncertainty estimates from noisy observations can be unstable, prompting a series of independent stabilization efforts. We argue that these interventions highlight a common underlying issue where gradient steps are poorly aligned with the geometry of the loss landscape. To better align updates with local curvature, we derive Fisher8, an output-layer gradient correction that reorients and rescales updates using Fisher geometry rather than Euclidean geometry. Unlike past stabilizers, Fisher8 introduces no data-dependent hyperparameters beyond learning rate and admits an approximate KL trust radius between successive predictive distributions. We show that prior stabilizers converge on overlapping components of this geometric correction. Across multidimensional regression and representation-learning tasks, Fisher8 obtains superior likelihood--error tradeoffs, predicts calibrated uncertainty estimates, and learns rich uncertainty-aware feature spaces.

## Metadata
- **Published**: 2026-08-11T02:10:51Z
- **Authors**: Sumedh Vemuganti, Nickvash Kani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10374v1)