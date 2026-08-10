---
title: SoRoMoX: Fast, Differentiable, and Parallelizable Soft Robot Models
published: 2026-08-06T23:31:47Z
authors: Maximilian Stölzle, Solange Gribonval, Daniel Feliu-Talegon, Vito Daniele Perfetta, Michele Martini, Chuhan Zhang, Kiwan Wong, Mohammed Tarnini, Anup Teejo Mathew, Federico Renda, Daniela Rus, Cosimo Della Santina
url: http://arxiv.org/abs/2608.06650v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SoRoMoX: Fast, Differentiable, and Parallelizable Soft Robot Models

## Abstract
Reduced-order models based on Cosserat-rod theory are now well established, and modeling theory is no longer the primary bottleneck in soft-robot control. Their implementations, however, do not support the differentiable, GPU-parallel, and control-oriented workflows that underpin advanced rigid-robotics applications. Here, we fill this gap with SoRoMoX (Soft Robot Models in JAX), a fully numerical, JIT-compilable Python/JAX framework. SoRoMoX implements articulated, Piecewise Constant Strain, and Variable Strain models through a unified, control-ready interface that provides inertia matrices, gravitational and elastic forces, Jacobians, and their derivatives. To our knowledge, it is the first rod/strain-based soft-robot modeling framework that runs directly on GPUs and is end-to-end differentiable with respect to states, inputs, and parameters. Sequential CPU rollouts are up to 18.1x faster than state-of-the-art alternatives, while GPU-parallel rollouts increase throughput by up to 234.6x. This performance enables workflows that were previously impractical or impossible: static-equilibrium system identification with 66% lower marker RMSE; residual-force learning with a further 64% reduction; computed-torque tracking with RMSE reduced by a factor of approximately 500 relative to model-free PD; control-gain optimization with up to 62% lower loss than untuned gains; safety-constrained control using high-order control barrier functions to keep the peak contact force within a prescribed 5 N bound, compared with 33.5 N without the safety constraint; and reinforcement-learning policy training up to 7x faster than a CPU PyElastica discrete-rod baseline through massively parallel rollouts.

## Metadata
- **Published**: 2026-08-06T23:31:47Z
- **Authors**: Maximilian Stölzle, Solange Gribonval, Daniel Feliu-Talegon, Vito Daniele Perfetta, Michele Martini, Chuhan Zhang, Kiwan Wong, Mohammed Tarnini, Anup Teejo Mathew, Federico Renda, Daniela Rus, Cosimo Della Santina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06650v1)