---
title: Poisson-Gamma Dynamical Systems with Time-varying Transition Dynamics
url: http://arxiv.org/abs/2609.00896v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_08-22-58Z_Poisson_GammaDynamicalSystemswithTime_varyingTrans.md
generated_at: 2026-09-01 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a time-varying transition kernel Poisson-Gamma Dynamical System (TV-PGDS) to model count series where the underlying Markov kernels evolve over time. It demonstrates that this extension improves predictive accuracy compared with static PGDS models by allowing heterogeneous structural mutations in dependencies.

## Key Takeaways
- The TV-PGDS replaces fixed transition matrices with time-varying ones, enabling the system to capture evolving dependency structures in count data.
- Three Dirichlet Markov chains—Dir-Dir, Dir-Gam-Dir, and PR-Gam-Dir—are designed to handle different types of structural mutations within the Poisson-Gamma framework.
- A fully-conjugate Gibbs sampler using Dirichlet-Multinomial-Beta augmentation provides efficient posterior simulation for the time-varying model.

## Context
Count-valued time series are common in applications such as epidemiology, finance, and network science. Traditional Bayesian models like PGDS assume static transition dynamics, which can limit performance when real-world processes change over time. This work addresses that gap by introducing a principled method to learn evolving kernels.

## Implications
For practitioners, TV-PGDS offers a flexible tool to improve forecasts in domains where latent structures drift, such as customer churn or disease spread. The efficient Gibbs sampler reduces computational burden, making the model scalable for large datasets and real-time inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00896v1)
