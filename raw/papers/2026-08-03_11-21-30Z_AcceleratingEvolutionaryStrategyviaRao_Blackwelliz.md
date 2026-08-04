---
title: Accelerating Evolutionary Strategy via Rao-Blackwellizing Realization of Uncertain Input
published: 2026-08-03T11:21:30Z
authors: So Nakashima, Tetsuya J. Kobayashi
url: http://arxiv.org/abs/2608.02073v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Accelerating Evolutionary Strategy via Rao-Blackwellizing Realization of Uncertain Input

## Abstract
We investigate Optimization under Input Uncertainty (OIU), in which the input to the objective function, rather than the objective function itself, is subject to uncertainty. OIU appears in manufacturing processes with production tolerance, control of physical systems with actuation noise, Mixture of Experts, and Reinforcement Learning (RL). Most of the existing approaches solve OIU by using the value of the objective function but discard the information of the realized input, even though the realized input is observable in various applications. The question here is whether the discarded information of the realized input is useful to accelerate the optimization process. We affirmatively answer this question for Evolutionary Strategy (ES) by theoretically showing that the information of the realized input can reduce the variance of the gradient estimator via Rao-Blackwellization. Using the Rao-Blackwellized gradient estimator, we propose Phenotype-Accelerated Evolutionary Strategy (PAES), which is a refinement of ES for OIU. Numerical experiments show that PAES converges faster than the usual ES from simple continuous optimization problems to RL benchmarks.

## Metadata
- **Published**: 2026-08-03T11:21:30Z
- **Authors**: So Nakashima, Tetsuya J. Kobayashi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02073v1)