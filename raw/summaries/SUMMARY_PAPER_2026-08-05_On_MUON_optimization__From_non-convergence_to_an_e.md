---
title: On MUON optimization: From non-convergence to an error analysis with Polar Express and the Newton-Schulz polynomial from implementations
url: http://arxiv.org/abs/2608.04607v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_09-14-22Z_OnMUONoptimization_Fromnon_convergencetoanerrorana.md
generated_at: 2026-08-05 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates convergence behavior of a generalized MUON optimizer that uses arbitrary‑degree Newton‑Schulz polynomials and includes Polar Express as a special case. It demonstrates that for most mini‑batch sizes the method does not converge to the optimum of stochastic optimization problems, and it provides an error analysis linking convergence rates to both number of gradient steps and batch size.

## Key Takeaways
- The generalized MUON optimizer fails to converge for almost every mini‑batch size as the number of gradient steps tends to infinity.  
- An error analysis is introduced that quantifies how the optimization error behaves with respect to the step count and the mini‑batch dimension.  
- The analysis applies to both quadratic stochastic problems and ℓ2 regularized logistic regression, showing concrete failure modes.

## Context
Accelerated SGD variants such as MUON are widely used in training large language models where standard SGD is too slow. Understanding their theoretical limits helps practitioners choose more reliable methods or adjust hyper‑parameters effectively.

## Implications
For AI researchers and engineers, this work clarifies why certain accelerated optimizers may appear effective only on small batches, guiding future algorithm design. It also suggests that error analysis tools are essential for evaluating real‑world performance beyond idealized settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04607v1)
