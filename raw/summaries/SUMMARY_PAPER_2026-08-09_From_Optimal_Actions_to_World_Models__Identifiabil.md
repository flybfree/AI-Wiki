---
title: From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs
url: http://arxiv.org/abs/2608.07301v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_14-56-11Z_FromOptimalActionstoWorldModels_IdentifiabilityofT.md
generated_at: 2026-08-09 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how much information about the transition probabilities of a discounted Markov decision process can be recovered from optimal actions alone, highlighting that optimal actions do not uniquely determine the dynamics. It shows that two different transition kernels produce identical optimal actions for every reward only under specific algebraic conditions involving an invertible matrix L with row sums one. Near kernels with positive entries there exists an n(n-1)-dimensional family of such kernels, and this result holds even when rewards have a unique optimal action per state.

## Key Takeaways
- Two kernels give the same optimal actions for every reward exactly when Q_{s,a} equals (P_{s,a}+1/γ e_s^T(L-I))L^{-1} for an invertible matrix L satisfying L\mathbf 1 = \mathbf 1, indicating a high-dimensional family of equivalent dynamics. - Near any kernel with strictly positive entries there are n(n-1) distinct kernels sharing this property, showing non-uniqueness despite identical optimal actions. - When rewards depend on the next state (r(s,a,s')) the transition kernel is fully recoverable except possibly rows where only one action exists.

## Context
The study addresses a classic inverse problem in reinforcement learning: reconstructing environment dynamics from observed policy information. Understanding this limit helps design reward structures that provide informative feedback without requiring direct observation of transitions, which is crucial for scalable and safe AI systems.

## Implications
For practitioners, the findings suggest that relying solely on optimal action data may lead to ambiguous interpretations of system behavior, necessitating richer reward specifications or additional observations to disambiguate dynamics. This insight guides the design of learning environments where reward signals are carefully crafted to avoid hidden transition ambiguities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07301v1)
