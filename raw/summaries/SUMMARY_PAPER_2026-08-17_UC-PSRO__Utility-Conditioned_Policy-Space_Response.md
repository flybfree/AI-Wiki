---
title: UC-PSRO: Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum for Game-Theoretic Course-of-Action Generation in Adversarial Swarms
url: http://arxiv.org/abs/2608.15372v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_18-52-50Z_UC_PSRO_Utility_ConditionedPolicy_SpaceResponseOra.md
generated_at: 2026-08-17 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces UC-PSRO, a framework for generating game‑theoretically optimized courses of action for a blue UAS swarm against an adaptive red adversary in a communication‑degraded setting. It combines policy‑space response oracles with self‑play, fine‑tuned intent weighting and curriculum dropout to study trade‑offs between robustness and convergence speed.

## Key Takeaways
- The communication‑dropout curriculum alone yields the highest mission‑completion rates, rising from 35% to 62% as dropout probability increases from 0 to 0.75, showing that loss of connectivity can be mitigated by learning decentralized fallback strategies.
- Adding utility‑conditioning and self‑play slows convergence within a fixed training budget, indicating a non‑trivial cost for incorporating these mechanisms without clear robustness gains.
- The results show no statistically significant advantage over a fixed opponent policy in exploitability, with gaps near zero, suggesting that the added complexity does not provide exploitable superiority.

## Context
This work addresses challenges faced by autonomous swarms where communication loss is common and adversarial behavior must be anticipated. By modeling the training environment as a game‑theoretic setting, it contributes to understanding how decentralized learning can improve resilience without relying on full network connectivity.

## Implications
For industry practitioners developing swarm robotics or UAV coordination systems, the findings suggest that curriculum‑driven robustness is valuable but should not be pursued at the expense of training efficiency. The methodology offers a template for balancing performance and resource constraints in real‑world deployment scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15372v1)
