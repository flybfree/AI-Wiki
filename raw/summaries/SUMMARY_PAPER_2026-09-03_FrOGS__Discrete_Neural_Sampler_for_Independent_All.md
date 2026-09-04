---
title: FrOGS: Discrete Neural Sampler for Independent Alloy Configurations Across Chemical Conditions
url: http://arxiv.org/abs/2609.02948v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-01_21-38-36Z_FrOGS_DiscreteNeuralSamplerforIndependentAlloyConf.md
generated_at: 2026-09-03 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FrOGS, a hybrid discrete neural sampler that jointly trains an autoregressive model with a continuous-time Markov chain to predict alloy configurations across chemical conditions. It achieves unbiased partition function estimates and consistent thermodynamic observables without mode collapse, matching exact finite-size results on the 2D Ising model and reference phase diagrams for AgPd and CuAu.

## Key Takeaways
- FrOGS uses a single shared loss to train an autoregressive model coupled to a CTMC, enabling sampling across many chemical conditions in one simulation. - The sampler returns i.i.d. configurations and unbiased partition function estimates on a common absolute free-energy scale. - It matches exact finite-size results for the 2D Ising model and reference phase diagrams of AgPd and CuAu without mode collapse.

## Context
Discrete neural samplers have advanced in AI-driven physics, but most rely on reverse KL divergence and suffer from mode bias or require separate simulations per condition. FrOGS addresses these limitations by integrating continuous dynamics with a shared loss function, offering a unified approach for complex thermodynamic sampling.

## Implications
For materials scientists, FrOGS reduces computational cost by eliminating multiple independent runs and auxiliary free-energy calculations. Practitioners can obtain reliable phase diagrams and thermodynamic properties directly from the model, accelerating design of new alloys under varying conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02948v1)
