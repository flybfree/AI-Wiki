---
title: Provably Efficient Federated Reinforcement Learning with Linear Function Approximation and Logarithmic Communication Cost
url: http://arxiv.org/abs/2609.00193v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-11-54Z_ProvablyEfficientFederatedReinforcementLearningwit.md
generated_at: 2026-09-01 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Fed‑LSVI, a provably efficient federated algorithm for online reinforcement learning using linear function approximation. It achieves the optimal regret bound of \(\widetilde{\mathcal O}(\sqrt{Md^3H^4T})\) while limiting communication to logarithmic dependence on the number of episodes per agent. The method replaces raw trajectory sharing with compressed sufficient statistics via event‑triggered synchronization and stepwise backward updates.

## Key Takeaways
- Fed‑LSVI reduces communication cost to \(\log T\) instead of linear in \(T\), making it suitable for privacy‑sensitive federated settings.
- The algorithm matches the best known regret bound for multi‑agent online RL with linear function approximation, guaranteeing strong performance.
- It relies on determinant‑based event triggering and stepwise backward updates to exchange only sufficient statistics.

## Context
Federated reinforcement learning aims to train agents locally while preserving data privacy and minimizing communication. Recent approaches often sacrifice efficiency by requiring extensive raw data exchange, which is impractical at scale. This work bridges that gap by delivering strong theoretical guarantees with minimal interaction.

## Implications
The logarithmic communication requirement opens the door for large‑scale deployment where bandwidth is limited. Practitioners can implement Fed‑LSVI in real‑world federated environments such as multi‑user robotics or distributed gaming, achieving both privacy and optimal learning efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00193v1)
