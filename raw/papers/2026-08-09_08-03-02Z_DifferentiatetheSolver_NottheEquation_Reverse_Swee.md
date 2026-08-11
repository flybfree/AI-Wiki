---
title: Differentiate the Solver, Not the Equation: Reverse-Sweep Adjoints for Block Implicit Simulation
published: 2026-08-09T08:03:02Z
authors: Lei Shu, Ying Jiang, Kui Wu, Yin Yang, Leonidas Guibas, Chenfanfu Jiang
url: http://arxiv.org/abs/2608.08559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Differentiate the Solver, Not the Equation: Reverse-Sweep Adjoints for Block Implicit Simulation

## Abstract
Differentiable simulation is a key component in learning, control, and inverse problems, where gradients through nonlinear implicit solvers are required. Existing approaches either rely on unrolled automatic differentiation, whose memory grows with solver depth, or on equation-level implicit differentiation, which assembles global Jacobians and solves large sparse adjoint systems, discarding the locality of the forward solver -- and differentiating the converged equation rather than the finite computation that actually ran. We propose solver-level differentiation, which differentiates the executed solver itself. When a solver is composed of block implicit updates, its discrete adjoint is obtained by applying the corresponding adjoint updates in reverse order, yielding a reverse-sweep formulation whose backward pass mirrors the forward solver. From an operator perspective, the forward pass realizes an approximate inverse through ordered local solves, and the backward applies its transpose through reverse local adjoint solves, constructing no global system. We instantiate this idea on Vertex Block Descent, yielding a differentiable solver whose reverse colored Gauss-Seidel sweeps are composed entirely of local $3\times 3$ adjoint solves. The backward matches automatic differentiation through the identical executed forward to machine precision at every solver depth, where the equation-level adjoint is off by 37% after one sweep; in a controlled same-codebase, same-GPU comparison it is 33x faster and uses 71x less memory than unrolled automatic differentiation; and the same construction is exact on projective dynamics and extended position-based dynamics. We scale differentiable elastodynamics to $10^6$ contact-coupled soft bodies (8M vertices) on one GPU. Overall, this work highlights solver structure as a practical organizing principle for efficient differentiable simulation.

## Metadata
- **Published**: 2026-08-09T08:03:02Z
- **Authors**: Lei Shu, Ying Jiang, Kui Wu, Yin Yang, Leonidas Guibas, Chenfanfu Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08559v1)