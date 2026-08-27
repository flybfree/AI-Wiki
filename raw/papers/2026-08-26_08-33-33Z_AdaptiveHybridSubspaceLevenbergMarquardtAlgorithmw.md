---
title: Adaptive Hybrid Subspace Levenberg Marquardt Algorithm with Adequacy Monitor for Large Scale Least Squares Problems
published: 2026-08-26T08:33:33Z
authors: M. Duc Hoang, Timothy J. Lewis
url: http://arxiv.org/abs/2608.25524v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Hybrid Subspace Levenberg Marquardt Algorithm with Adequacy Monitor for Large Scale Least Squares Problems

## Abstract
The Levenberg-Marquardt (LM) algorithm is the most widely used method for solving nonlinear least-squares problems, as it combines the robustness of steepest descent with the fast local convergence of the Gauss-Newton method. However, its computational cost can become prohibitive for large-scale problems because each iteration requires solving a large damped linear system, and conventional step acceptance strategies may require repeated solves as the damping parameter is adjusted. Despite this computational challenge, many large-scale least-squares problems exhibit effective low-dimensional structure, with only a small number of parameter-space directions strongly informed by the data. We propose an adaptive hybrid subspace Levenberg-Marquardt (HSLM) algorithm that constructs a low-dimensional subspace from complementary sources of gradient, memory, Krylov-subspace, and randomized curvature information and computes a spectrally damped LM step within this subspace. A distinguishing feature of the method is a deterministic adequacy monitor that quantifies how much descent information is captured by the reduced space and adaptively enriches the subspace when necessary. Step acceptance is decoupled from damping adjustment: Armijo backtracking determines the accepted step length, while the ratio of actual to predicted reduction is used solely to update the damping parameter, thereby avoiding repeated damped-system solves during step acceptance. For the HSLM algorithm, we establish global convergence to stationarity and prove local linear and superlinear convergence. Numerical experiments on neural-network training problems show that HSLM achieves convergence behavior comparable to classical and Krylov subspace LM (KSLM) while substantially reducing per-iteration computational cost, with increasing advantages observed as the parameter dimension grows.

## Metadata
- **Published**: 2026-08-26T08:33:33Z
- **Authors**: M. Duc Hoang, Timothy J. Lewis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25524v1)