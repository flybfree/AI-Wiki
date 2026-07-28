---
title: When Rates Are Geometric: Rate-Certificate Transfer for Contact Splittings in Optimization
url: http://arxiv.org/abs/2607.23642v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_13-12-58Z_WhenRatesAreGeometric_Rate_CertificateTransferforC.md
generated_at: 2026-07-27 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new framework for providing convergence certificates to discrete optimization algorithms by using contact Hamiltonian systems. It shows that under three checkable hypotheses an order‑r splitting transfers the continuous‑time rate certificate over the horizon set by backward error analysis, with only O(h^r) perturbations and a shadowing defect.

## Key Takeaways
- The augmented energy E built from the intrinsic decay identity dot H = -H ∂_s H controls the objective gap, giving a continuous‑time rate certificate when E dominates the gap.  
- An order‑r contact splitting with step h transfers this certificate over the horizon set by backward error analysis, preserving the conformal factor up to O(h^r) plus a shadowing defect.  
- The quadratic heavy ball case is fully solvable: its projected dissipative‑leapfrog spectrum matches conformal‑symplectic theory and the augmented Hamiltonian yields a sharp objective‑to‑certificate comparison.

## Context
This work bridges discrete algorithm analysis with continuous‑time rate certificates, a longstanding challenge in optimization. By leveraging contact Hamiltonians on J^1(R^n) it provides a principled way to verify convergence without resorting to stochastic approximations or ad‑hoc Lyapunov functions.

## Implications
For practitioners developing fast solvers for ill‑conditioned problems or deep‑learning training, this framework offers a clear diagnostic tool that guarantees convergence rates and can be implemented efficiently. The method also inspires new design templates for contact Hamiltonians with closed‑form sub‑flows, potentially accelerating algorithmic implementations across scientific computing and machine learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23642v1)
