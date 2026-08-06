---
title: Cost-Aware Multi-Objective Bandits: Theory and Application to Budgeted LLM Configuration Evaluation
url: http://arxiv.org/abs/2608.04333v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_01-21-02Z_Cost_AwareMulti_ObjectiveBandits_TheoryandApplicat.md
generated_at: 2026-08-05 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper treats LLM configuration evaluation as a cost‑aware multi‑objective bandit problem, introducing an online selection algorithm and a fixed‑budget Pareto identification method that account for varying evaluation costs. The proposed hypervolume‑based UCB optimizes an efficiency index, yielding a budgeted regret bound, while the empirical gap elimination algorithm achieves exponential error decay with budget. Experiments show efficient decision making and accurate cost‑aware Pareto sets under limited resources.

## Key Takeaways  
- The framework models each configuration evaluation as a noisy vector outcome with a configuration‑dependent cost, enabling a unified view of trade‑offs between hypervolume gain and expense.  
- A budgeted regret bound of order O(∑_{i≠i*} log B / Δ_i) is established, preserving the classic logarithmic dependence while incorporating efficiency gaps for non‑optimal configurations.  
- The cost‑aware empirical gap elimination algorithm yields an error probability of O(exp(-B/H_{μ,c})), which decays exponentially with budget and reduces to the standard guarantee when all costs are equal.

## Context  
LLM configuration evaluation is a critical but resource‑constrained task where hypervolume, latency, and cost compete. Traditional bandit methods ignore these real‑world constraints, leading to suboptimal use of limited budgets. This work bridges that gap by integrating cost awareness into classic multi‑objective bandit theory.

## Implications  
Practitioners can now select configurations online while respecting budget limits, improving both performance and financial efficiency. The results offer a scalable benchmark for evaluating LLM deployment strategies in settings where every evaluation dollar matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04333v1)
