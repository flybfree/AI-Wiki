---
title: Quantum Multi-Armed Bandits and Linear Bandits: Lower Bounds and Algorithms
published: 2026-08-14T14:04:21Z
authors: Maoli Liu, Zhuohua Li, John C. S. Lui
url: http://arxiv.org/abs/2608.14319v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantum Multi-Armed Bandits and Linear Bandits: Lower Bounds and Algorithms

## Abstract
We study quantum multi-armed bandits (QMAB) and quantum linear bandits (QLB) in the model of Wan et al. [2023], where the learner queries each arm or action through a quantum reward oracle or its inverse. Prior work gives algorithms over horizon $T$ with regret $O(K\log T)$ for QMAB with $K$ arms and $O(d^2\operatorname{polylog} T)$ for $d$-dimensional QLB. This leaves open whether the $K\log T$ scale is unavoidable and whether the $d^2$ dependence can be improved. We prove the first minimax lower bounds of $Ω(K\log(T/K))$ for QMAB and $Ω(d\log(T/d))$ for finite-action QLB, resolving the question raised by Wan et al. [2023] of whether regret independent of $T$ is achievable. At the heart of our argument is a high-confidence single-arm quantum testing lower bound for distinguishing a fixed reward mean from an interval of alternatives, proved by the polynomial method and a Remez-type inequality for trigonometric polynomials. A bandit-to-testing reduction then lifts it to the QMAB lower bound, while a linear embedding gives the finite-action QLB lower bound. Complementing the lower bounds, we give a design-based elimination algorithm for finite-action QLB. When the action set has size $\operatorname{poly}(d)$, its regret is linear in $d$, improving the prior $d^2$ dependence and matching our lower bound up to polylogarithmic factors. The algorithm couples a low-bias low-variance quantum mean estimator with a small-support $G$-optimal design through a query allocation matched to the design weights. The design-based elimination reduces the dimension dependence from $d^2$ to $d^{3/2}$ when using Quantum Monte Carlo estimates. The low-variance estimator then makes reconstruction error aggregate through variance rather than worst-case absolute error, removing the remaining $\sqrt d$ factor.

## Metadata
- **Published**: 2026-08-14T14:04:21Z
- **Authors**: Maoli Liu, Zhuohua Li, John C. S. Lui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14319v1)