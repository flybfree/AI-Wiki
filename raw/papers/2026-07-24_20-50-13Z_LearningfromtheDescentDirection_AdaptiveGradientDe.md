---
title: Learning from the Descent Direction: Adaptive Gradient Descent under One-Sided Hölder Regularity
published: 2026-07-24T20:50:13Z
authors: Arzu Ahmadova, Ismail Huseynov
url: http://arxiv.org/abs/2607.22906v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from the Descent Direction: Adaptive Gradient Descent under One-Sided Hölder Regularity

## Abstract
We study adaptive gradient descent for continuously differentiable, possibly nonconvex objectives under one-sided Hölder regularity. Unlike classical Hölder- or Lipschitz-gradient assumptions, which control the full gradient variation, our condition bounds only the directional term appearing in the descent inequality. This can allow less conservative step sizes when large gradient changes are orthogonal to, or favorable along, the update direction. We propose an adaptive scalar-step method based on an estimate of positive one-sided Hölder curvature, combined with a simple sufficient-decrease safeguard. For nonconvex objectives on a convex region containing the accepted update segments, we prove an explicit best-iterate stationarity bound with a rate determined by the Hölder exponent. Unlike predetermined diminishing step-size schemes, the method adapts to the local descent geometry. We evaluate the approach on two full-batch benchmarks designed to separate directional curvature from full gradient variation. On a binary classification problem, the method achieves the lowest final cross-entropy, objective value, and gradient norm, together with the largest classification margin among the compared scalar gradient methods. On a nonconvex Hölder regression problem, it attains the lowest final objective gap and gradient norm. These results indicate that one-sided Hölder curvature is an effective adaptive step-size signal when full-gradient variation is inflated by directions that do not hinder descent.

## Metadata
- **Published**: 2026-07-24T20:50:13Z
- **Authors**: Arzu Ahmadova, Ismail Huseynov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22906v1)