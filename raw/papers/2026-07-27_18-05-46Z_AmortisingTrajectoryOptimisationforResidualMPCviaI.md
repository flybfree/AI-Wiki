---
title: Amortising Trajectory Optimisation for Residual MPC via Implicit Contact Differentiation
published: 2026-07-27T18:05:46Z
authors: Daniel Layeghi, Thomas Corbères, Calum Arnott, Aditya Kamireddypalli, Hashim Al-Obaidi, Steve Tonneau, Michael Mistry
url: http://arxiv.org/abs/2607.24959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Amortising Trajectory Optimisation for Residual MPC via Implicit Contact Differentiation

## Abstract
Differentiable simulation can accelerate contact-rich trajectory optimisation by exposing local sensitivities of task outcomes to controls. Existing approaches either use finite differences, which are expensive and step-size sensitive; differentiate iterative contact solvers by unrolling automatic differentiation (AD), which stores a growing computation trace; or require intricate, solver-specific KKT sensitivity derivations. We introduce an AD-assisted implicit derivative for regularised smooth contacts and apply it to Mujoco MJX, based on the Implicit Function Theorem (IFT). The method differentiates the stationarity residual at the tolerance-converged solution, avoiding both solver unrolling and hand-assembled KKT systems. IFT keeps compiled temporary memory nearly constant with solver effort, changing by less than 4$\%$ from one to ten iterations versus 10.6$\times$ growth for unrolled AD. IFT memory grows slower with active contacts and model dimension, using 20$\times$ less memory at 256 contacts and 6$\times$ less at 16 contacts and 96 DoF. We further introduce optimiser distillation for residual MPC, amortising batched full-horizon iLQR into a policy that guides short-horizon residual iLQR. Across Finger, Franka, and Unitree, this raises six-step success by 28-98 percentage points over standard iLQR.

## Metadata
- **Published**: 2026-07-27T18:05:46Z
- **Authors**: Daniel Layeghi, Thomas Corbères, Calum Arnott, Aditya Kamireddypalli, Hashim Al-Obaidi, Steve Tonneau, Michael Mistry
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24959v1)