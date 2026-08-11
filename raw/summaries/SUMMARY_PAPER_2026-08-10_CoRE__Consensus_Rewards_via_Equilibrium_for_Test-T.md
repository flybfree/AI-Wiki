---
title: CoRE: Consensus Rewards via Equilibrium for Test-Time Reinforcement Learning
url: http://arxiv.org/abs/2608.09324v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_09-06-03Z_CoRE_ConsensusRewardsviaEquilibriumforTest_TimeRei.md
generated_at: 2026-08-10 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoRE (Consensus Rewards via Equilibrium) as a method for generating reliable pseudo‑rewards in test‑time reinforcement learning without relying on external labels. By modeling the N roll‑outs as a graph and applying replicator dynamics, CoRE produces graded rewards that correctly identify minority correct answers while preserving majority alignment. The approach improves average performance by 21.7 points compared with simple voting and reaches voting baselines with fewer steps.

## Key Takeaways
- Consensus rewards replace the binary majority vote with a calibrated reward derived from answer agreement, reasoning similarity, and generation confidence using graph‑based replicator dynamics.
- A block‑value analysis shows that consensus can recover correct minority answers when they outperform a larger wrong plurality by up to 7.5 points, with confidence calibration lowering this threshold multiplicatively.
- The method recovers simple majority voting as a special case, improves average test‑time RL scores across seven backbones and five benchmarks, and reduces the number of steps needed to reach plateau accuracy.

## Context
Test‑time reinforcement learning struggles because it lacks ground‑truth rewards on unseen data. Traditional solutions rely on noisy majority voting which can mislabel minority correct actions. CoRE addresses this by creating a self‑supervised reward signal that balances consensus across multiple roll‑outs, offering a more stable and informative feedback loop.

## Implications
CoRE provides practitioners with a lightweight way to enhance test‑time RL without extra data collection or model retraining. By turning roll‑out groups into a calibrated consensus graph, it can be integrated directly into existing pipelines, potentially leading to faster convergence and higher accuracy in real‑world applications where label efficiency is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09324v1)
