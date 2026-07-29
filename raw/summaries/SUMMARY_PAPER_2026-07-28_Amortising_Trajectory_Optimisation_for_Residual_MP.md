---
title: Amortising Trajectory Optimisation for Residual MPC via Implicit Contact Differentiation
url: http://arxiv.org/abs/2607.24959v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_18-05-46Z_AmortisingTrajectoryOptimisationforResidualMPCviaI.md
generated_at: 2026-07-28 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes an AD‑assisted implicit derivative for regularised smooth contacts, enabling efficient residual MPC in contact‑rich environments. By applying the Implicit Function Theorem to unroll automatic differentiation, the method avoids costly finite differences and solver unrolling while keeping memory growth minimal. The approach also introduces optimiser distillation that amortises full‑horizon iLQR into short‑horizon residuals, improving six‑step success rates by 28–98 % across several robots.

## Key Takeaways
- IFT‑based differentiation reduces temporary memory growth to less than 4 % per iteration versus a 10.6× increase with unrolled AD.
- The method scales well: it uses 20× less memory at 256 contacts and 6× less at 16 contacts and 96 DoF, limiting solver‑specific KKT derivations.
- Optimiser distillation yields a policy that guides residual iLQR, raising six‑step success by up to 98 % over standard iLQR.

## Context
Contact‑rich trajectory optimisation remains a bottleneck in real‑time robotics because traditional finite‑difference methods are computationally expensive and sensitive to step size. Differentiable simulation offers a promising path but suffers from high memory demands when unrolling AD across many iterations. This work bridges that gap with an implicit, low‑memory derivative framework.

## Implications
Practitioners can implement residual MPC on contact‑heavy robots without sacrificing performance or real‑time constraints. The technique’s scalability supports future integration into autonomous systems where safety and efficiency are paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24959v1)
