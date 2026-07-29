---
title: Quotient Dynamics, Effective Curvature, and Implicit Bias in Positive Quadratic Networks
url: http://arxiv.org/abs/2607.25624v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_12-04-46Z_QuotientDynamics_EffectiveCurvature_andImplicitBia.md
generated_at: 2026-07-28 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the quotient structure of positive quadratic networks influences training dynamics, curvature, recovery, and interpolation bias for low-rank PSD matrices. It shows that factor gradient flow aligns with Riemannian gradient flow on a quotient manifold and derives explicit curvature formulas under Gaussian measurements.  

## Key Takeaways
- The Euclidean factor gradient is horizontal on the full‑column‑rank stratum, yielding an exact congruence recursion for finite‑step descent.  
- Effective Hessian at interpolators equals the empirical Gram form restricted to the tangent space of the quotient metric, providing uniform deviation bounds for the normal operator.  
- Under isotropic initialization, predictors converge to the minimum‑trace solution set via weighted entropy in the invariant joint spectral algebra.  

## Context
Positive quadratic networks are a theoretical framework for low‑rank matrix factorization where the rank is not uniquely identifiable due to right orthogonal transformations. Understanding their dynamics is crucial for designing robust learning algorithms that handle non‑uniqueness and measurement noise.  

## Implications
These results offer principled guidance for gradient flow methods in underdetermined settings, enabling practitioners to predict convergence rates and recovery behavior without relying on full‑space second‑moment assumptions. The insights also support the use of entropy‑based selection rules to resolve non‑uniqueness in practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25624v1)
