---
title: Finite-Time Analysis of Discounted Exponential-Utility Reinforcement Learning
published: 2026-08-03T08:50:07Z
authors: Ankur Naskar, Vivek T A, Aditya Kumar, Gugan Thoppe, Prashanth L. A
url: http://arxiv.org/abs/2608.01917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Finite-Time Analysis of Discounted Exponential-Utility Reinforcement Learning

## Abstract
Discounted exponential utility provides a principled criterion for risk-sensitive sequential decision-making, but its nonlinear structure complicates reinforcement learning. A recent work \citep{thoppe2026reinforcement} addressed this difficulty by introducing a Bellman-compatible surrogate and two model-free fixed-point algorithms for optimizing it over stationary policies. However, their main convergence results are asymptotic. In this work, we establish finite-time rates of $\tilde{O} (1/\sqrt{n})$ for the aforementioned two algorithms under asynchronous Markovian sampling, where $n$ is the iteration index and $\tilde{O}$ hides logarithmic expressions. Importantly, we employ parameter-free choices for the stepsize parameter to derive these rate results. For the algorithmically simpler one-timescale method, the main challenge is that its update equation is not directly aligned with the contraction geometry of its underlying power-law operator. We overcome this mismatch by exploiting the boundedness, monotonicity, and homogeneity of the operator to obtain a local pseudo-contraction property for the relative-error dynamics. We then use a Moreau-envelope-based Lyapunov function and Polyak--Ruppert averaging to obtain the stated convergence rate with parameter-free stepsizes. For the two-timescale method, the main challenge is to control a tracking error on the faster timescale. These results provide the first finite-time guarantees for model-free discounted exponential-utility reinforcement learning.

## Metadata
- **Published**: 2026-08-03T08:50:07Z
- **Authors**: Ankur Naskar, Vivek T A, Aditya Kumar, Gugan Thoppe, Prashanth L. A
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01917v1)