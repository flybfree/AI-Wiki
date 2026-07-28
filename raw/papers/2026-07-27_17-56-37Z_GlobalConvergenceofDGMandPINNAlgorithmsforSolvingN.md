---
title: Global Convergence of DGM and PINN Algorithms for Solving Nonlinear PDEs
published: 2026-07-27T17:56:37Z
authors: Justin Sirignano, Konstantinos Spiliopoulos, Samuel Cohen
url: http://arxiv.org/abs/2607.24726v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Global Convergence of DGM and PINN Algorithms for Solving Nonlinear PDEs

## Abstract
The Deep Galerkin Method (DGM) and Physics Informed Neural Networks (PINNs) have become widely-used methods for solving partial differential equations (PDEs) in the rapidly growing field of scientific machine learning. In these methods, a neural network is trained to approximate the PDE solution by using (stochastic) gradient descent to minimize the PDE residual of the neural network. Due to the non-convexity of the PDE residual objective function, the trained neural network may, in principle, only converge to a local minimizer of the objective function (which would not be a solution of the PDE). Therefore, there is a longstanding question regarding the mathematical foundations of these algorithms, and it is highly valuable to establish that the trained neural network will converge to the PDE solution. For a class of semi-linear PDEs (nonlinear in the solution and its first derivative), we prove that neural networks trained with gradient descent to minimize the PDE residual objective function will converge to the PDE solution.

## Metadata
- **Published**: 2026-07-27T17:56:37Z
- **Authors**: Justin Sirignano, Konstantinos Spiliopoulos, Samuel Cohen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24726v1)