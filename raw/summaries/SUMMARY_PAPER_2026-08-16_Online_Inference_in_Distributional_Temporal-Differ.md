---
title: Online Inference in Distributional Temporal-Difference Learning
url: http://arxiv.org/abs/2608.14408v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_15-51-50Z_OnlineInferenceinDistributionalTemporal_Difference.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates online statistical inference for functionals of the return distribution under a fixed policy, using distributional temporal-difference learning from a single Markov trajectory. It establishes weak Gaussian convergence for the Polyak–Ruppert averaged estimator’s root‑T error and shows bootstrap consistency, while developing a local asymptotic theory for nonsmooth functionals. These results enable inference for both smooth and nonsmooth statistical measures.

## Key Takeaways
- The Polyak–Ruppert averaged estimator’s root‑T error converges weakly to a centered Gaussian random element in Cramér space, justifying its use as an online estimator of variance and CVaR.
- Conditional on the observed trajectory, the bootstrap average differs from the original estimate by a weak limit that is also Gaussian, confirming bootstrap inference for smooth functionals.
- A local asymptotic theory provides $T^{-1/2}$ convergence for the estimated return CDF around thresholds, allowing inference for nonsmooth functionals defined by CDF equations.

## Context
In reinforcement learning and risk analysis, practitioners need reliable online estimates of statistical functionals such as variance or expected shortfall without retraining models. Traditional offline methods assume full data, which is impractical in streaming settings where only a single trajectory is available. This work bridges that gap by providing theoretical guarantees for inference directly from incremental updates.

## Implications
These results give practitioners confidence to use online estimators and bootstrap procedures in real‑time risk assessment, reducing reliance on batch data collection. The framework supports regulatory compliance and decision making in finance, insurance, and autonomous systems where timely inference is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14408v1)
