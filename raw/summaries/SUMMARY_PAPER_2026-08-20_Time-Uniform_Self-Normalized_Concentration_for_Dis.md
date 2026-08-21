---
title: Time-Uniform Self-Normalized Concentration for Discounted Least Squares: Limits and Corrections
url: http://arxiv.org/abs/2608.19643v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_05-19-11Z_Time_UniformSelf_NormalizedConcentrationforDiscoun.md
generated_at: 2026-08-20 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the validity of a claimed time‑uniform concentration bound for discounted least‑squares estimators in non‑stationary settings and identifies its limitations. It demonstrates that a simple Gaussian counterexample violates the bounded radius, and that deterministic anytime boundaries must be at least order \(R\sqrt{\log(T/\delta)}\) by horizon \(T\). The authors also provide corrected finite‑ and infinite‑horizon bounds for the weighted inequality.

## Key Takeaways
- A fixed scalar Gaussian model with a constant parameter shows that the claimed uniform radius is crossed with probability one, disproving the original claim.  
- For discount \(\delta \leq 1/2\) and large \(T/\delta\), any uniformly valid deterministic anytime boundary must grow at least as \(R\sqrt{\log(T/\delta)}\), which is necessary even for nondecreasing boundaries at time \(T\).  
- The proof error stems from using different terminal times with distinct Gaussian mixing distributions, so fixed‑time mixtures are not a supermartingale and the stopping‑time argument fails to repair it.

## Context
In reinforcement learning and online learning, self‑normalized concentration inequalities provide uniform guarantees across episodes. Discounted least squares is a common estimator for non‑stationary bandit problems, yet existing results often assume stationarity or ignore time‑varying distributions, limiting their applicability in real‑world scenarios where data drift occurs.

## Implications
Practitioners must adopt corrected bounds that respect the true mixing structure of each horizon to avoid overconfidence in performance estimates. Ignoring these limitations can lead to suboptimal decisions and inflated risk assessments in automated decision systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19643v1)
