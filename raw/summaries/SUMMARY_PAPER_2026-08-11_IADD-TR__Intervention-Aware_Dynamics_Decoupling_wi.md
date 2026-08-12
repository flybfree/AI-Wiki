---
title: IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning
url: http://arxiv.org/abs/2608.10634v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_08-20-02Z_IADD_TR_Intervention_AwareDynamicsDecouplingwithTa.md
generated_at: 2026-08-11 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces IADD‑TR, a framework that separates the dynamics prediction from policy learning in model‑based reinforcement learning by factoring transitions into an action‑intervention stage and a natural evolution stage. The method combines Intervention‑Aware Dynamics Decoupling (IADD) with Targeted Regularization (TR), achieving doubly robust policy‑gradient estimation and demonstrating competitive returns on MuJoCo tasks with better sample efficiency.

## Key Takeaways
- IADD factorizes transitions into an action‑intervention stage and a natural evolution stage using a zero‑action anchor to resolve the non‑uniqueness of this two‑stage factorization for robust generalization.  
- TR augments the critic with an action‑density‑scaled residual correction derived from the efficient influence function of a replay‑state policy‑gradient functional, providing doubly robust estimation when either the critic or the replay action density is consistently specified.  
- Extensive experiments on five MuJoCo tasks show that IADD‑TR achieves competitive returns with improved sample efficiency.

## Context
Model‑based reinforcement learning offers sample‑efficient decision making by learning environment dynamics for synthetic experience, yet many approaches treat transition models and value functions as monolithic predictors, ignoring policy‑induced data bias. This limitation can entangle actions with environmental evolution and distort counterfactual value estimates used for policy improvement.

## Implications
The decoupling of dynamics from policy enables more reliable training under non‑uniform action coverage, which is crucial for industry applications where sample budgets are limited. Practitioners can leverage IADD‑TR to build robust model‑based agents that generalize well despite sparse or biased data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10634v1)
