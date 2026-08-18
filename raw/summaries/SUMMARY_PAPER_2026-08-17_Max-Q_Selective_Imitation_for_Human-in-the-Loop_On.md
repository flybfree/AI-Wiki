---
title: Max-Q Selective Imitation for Human-in-the-Loop Online Robot Learning
url: http://arxiv.org/abs/2608.15088v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_07-13-59Z_Max_QSelectiveImitationforHuman_in_the_LoopOnlineR.md
generated_at: 2026-08-17 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Max-Q selective imitation for human‑in‑the‑loop online robot learning, combining a Monte Carlo Q‑chunk critic with max‑Q updates to quickly learn from human interventions while improving beyond them. The method achieves 99 % success in only 30 minutes on real tasks, far outperforming existing approaches.

## Key Takeaways
- The method uses a Monte Carlo Q‑chunk critic that evaluates intervention trajectories directly, avoiding dilution by current‑policy TD backups.
- It applies max‑Q selective imitation with a hard winner‑take‑all rule to update the actor, automatically switching between learning from humans and self‑improvement.
- On real tasks it achieves 99 % success in 30 minutes, versus ~5 hours for HIL‑SERL.

## Context
This work addresses a key challenge in human‑in‑the‑loop reinforcement learning where rapid adaptation is needed while preserving progress beyond the human baseline. It demonstrates that integrating MC evaluation with selective imitation can close the policy–target gap efficiently.

## Implications
These results suggest that HIL systems can be deployed in real robots without lengthy offline training cycles, enabling faster iteration and higher reliability. Practitioners may adopt similar chunk‑based critics and max‑Q rules to balance human guidance with autonomous improvement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15088v1)
