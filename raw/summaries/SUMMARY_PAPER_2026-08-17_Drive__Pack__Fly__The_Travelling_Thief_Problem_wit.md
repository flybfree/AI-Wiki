---
title: Drive, Pack, Fly: The Travelling Thief Problem with Drone
url: http://arxiv.org/abs/2608.16435v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_11-34-15Z_Drive_Pack_Fly_TheTravellingThiefProblemwithDrone.md
generated_at: 2026-08-17 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces the Travelling Thief Problem with Drone which seeks to maximize profit by selecting items, routing a ground vehicle and synchronising drone flights while accounting for time‑based rental costs. The formulation captures both the trade‑off between collection speed and drone rental expense.

## Key Takeaways
- The mixed‑integer linear program solves small instances optimally, providing exact profit maximisation under given constraints.
- A hybrid DRL‑metaheuristic solver recovers most of the baseline quality at lower computational cost, though large instances still need full budget.
- Sensitivity analysis shows rental ratio is primary driver of profitability while fleet parameters have marginal effect.

## Context
In AI and operations research, integrating reinforcement learning with combinatorial optimisation enables scalable solutions for resource‑intensive logistics problems. This work extends the DRL paradigm to a real‑world operational model that balances multiple conflicting objectives.

## Implications
For industry practitioners, the hybrid approach offers a practical trade‑off between speed and accuracy, allowing real‑time adaptation to changing rental rates. The finding that rental cost dominates profitability highlights the need for dynamic pricing strategies in drone‑assisted collection services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16435v1)
