---
title: A Two-Stage Learning PINN Approach for Solving the Inverse Problem of the 1D Porous Medium Equation
published: 2026-08-17T12:13:22Z
authors: Noura Al Helwani, Sophie Moufawad, Nabil Nassif
url: http://arxiv.org/abs/2608.16475v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Two-Stage Learning PINN Approach for Solving the Inverse Problem of the 1D Porous Medium Equation

## Abstract
The Porous Medium Equation (PME), given by $u_t = Δ(u^m)$ for $m > 1$, is a degenerate nonlinear parabolic partial differential equation that arises in various physical applications such as fluid flow in porous media, heat transfer in plasmas, and population dynamics. It is known for its nonlinear diffusion and finite propagation speed. In this paper, we study numerical solutions of the one-dimensional direct and inverse PME using Physics-Informed Neural Networks (PINNs), and compare them with classical numerical methods and available analytical and manufactured solutions. While PINNs provide a flexible framework for solving both forward and inverse problems, we show that the standard inverse formulation suffers from a strong sensitivity to the initial guess, leading to only local convergence. To address this issue, we propose a novel two-stage PINN training framework for the inverse problem, which significantly improves convergence stability and allows reliable recovery of the unknown parameter even for poor initial guesses. Overall, the proposed approach demonstrates that PINNs are a flexible and accurate alternative to classical methods for the 1D PME, and the introduced two-stage training strategy substantially improves their robustness in inverse problems, providing a solid basis for extensions to more complex geometries and higher-dimensional cases.

## Metadata
- **Published**: 2026-08-17T12:13:22Z
- **Authors**: Noura Al Helwani, Sophie Moufawad, Nabil Nassif
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16475v1)