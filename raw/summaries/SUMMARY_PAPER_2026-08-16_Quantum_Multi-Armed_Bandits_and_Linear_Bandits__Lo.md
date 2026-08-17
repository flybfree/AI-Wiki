---
title: Quantum Multi-Armed Bandits and Linear Bandits: Lower Bounds and Algorithms
url: http://arxiv.org/abs/2608.14319v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_14-04-21Z_QuantumMulti_ArmedBanditsandLinearBandits_LowerBou.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates quantum multi‑armed bandits (QMAB) and quantum linear bandits (QLB) under the Wan model, establishing tight minimax lower bounds of Ω(K log(T/K)) for QMAB and Ω(d log(T/d)) for finite‑action QLB. It also presents a design‑based elimination algorithm that reduces the dimension dependence from d² to d^{3/2} when using quantum Monte Carlo estimators, matching the lower bound up to polylogarithmic factors.

## Key Takeaways
- The Ω(K log(T/K)) lower bound shows that any QMAB strategy cannot achieve regret independent of T for K arms.  
- The Ω(d log(T/d)) bound proves that finite‑action QLB also suffers a d factor in the optimal regret, improving on the prior d² dependence.  
- A design‑based elimination algorithm achieves O(d^{3/2}) regret by coupling low‑bias quantum mean estimators with G‑optimal designs and using variance aggregation to eliminate the remaining √d factor.

## Context
Quantum bandits extend classical multi‑armed bandit problems to quantum reward oracles, where queries involve quantum states. Understanding optimal query complexity is crucial for designing efficient quantum algorithms that leverage entanglement and interference. This work bridges theoretical lower bounds with practical design strategies in this emerging field.

## Implications
For practitioners developing quantum machine learning systems, the d^{3/2} regret bound suggests that algorithmic improvements are possible beyond simple scaling laws. In industry, these results guide hardware selection and query scheduling to minimize experimental overhead while maintaining performance guarantees.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14319v1)
