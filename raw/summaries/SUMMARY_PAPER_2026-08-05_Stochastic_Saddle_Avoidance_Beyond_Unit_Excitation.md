---
title: Stochastic Saddle Avoidance Beyond Unit Excitation and Smoothness: A Pathwise Lyapunov-Perron Framework
url: http://arxiv.org/abs/2608.03001v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_01-34-36Z_StochasticSaddleAvoidanceBeyondUnitExcitationandSm.md
generated_at: 2026-08-05 01:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a pathwise Lyapunov-Perron framework that avoids the unit excitation assumption in stochastic saddle avoidance. It proves an almost sure avoidance theorem for stochastic recursions without requiring uniform positive noise components, using verifiable pathwise conditions derived from smoothness and sampling structure.

## Key Takeaways
- The abstract assumes no need for unit excitation; instead it uses path-dependent change of variables to verify local stability along trajectories.
- Local smoothness together with finite-moment assumptions under i.i.d. sampling yields verifiable conditions that guarantee stochastic saddle avoidance.
- In finite-sum problems without replacement, the low-dimensional noise subspace leads to similar verification criteria that bypass UE.

## Context
Overparameterized models often exhibit vanishing noise near convergence, violating unit excitation yet still converging to a local minimum. This work provides theoretical justification for such behavior by replacing global assumptions with local pathwise checks.

## Implications
Practitioners can rely on these conditions when designing stochastic optimization algorithms, especially in settings where UE is unrealistic. The results support confidence that standard SGD and related methods converge without needing additional noise guarantees.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03001v1)
