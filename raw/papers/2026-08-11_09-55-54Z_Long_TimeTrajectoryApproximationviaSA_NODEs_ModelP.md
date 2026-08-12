---
title: Long-Time Trajectory Approximation via SA-NODEs: Model Predictive and Floquet Strategies
published: 2026-08-11T09:55:54Z
authors: Ziqian Li, Nikolaos M. Matzakos
url: http://arxiv.org/abs/2608.10738v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Long-Time Trajectory Approximation via SA-NODEs: Model Predictive and Floquet Strategies

## Abstract
We study the approximation of dynamical systems by semi-autonomous neural ordinary differential equations (SA-NODEs) over long time horizons. For a single network trained on the whole horizon, the available error bound deteriorates double exponentially in the horizon length. We develop two training strategies that avoid this barrier, each built on a reset of the state. The model predictive strategy partitions the horizon adaptively and restarts every window from observed data: when training meets a prescribed tolerance on every window, the composite model meets it uniformly in time, with a parameter budget linear in the horizon for targets with a bounded, uniformly regular reachable tube. The Floquet strategy addresses autonomous targets with a stable limit cycle and uses no data at deployment: a certified contraction of the learned return map confines the error to linear growth in the number of elapsed periods. For the time-periodic architecture we deploy, the scalar certificate degenerates; we prove instead a uniform-in-time orbital guarantee whose hypotheses are measured on the trained model, and an obstruction showing that, for an exactly periodic learned field, small one-period error and a contracting stroboscopic map cannot hold at once. Numerical experiments on four benchmarks confirm the predicted error laws and measure the hypotheses of every guarantee.

## Metadata
- **Published**: 2026-08-11T09:55:54Z
- **Authors**: Ziqian Li, Nikolaos M. Matzakos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10738v1)