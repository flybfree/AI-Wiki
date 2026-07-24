---
title: Stochastic Reset Pathfinding: Path-Level Regret for Cascading Bandits over Graph Paths
url: http://arxiv.org/abs/2607.15440v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_20-20-18Z_StochasticResetPathfinding_Path_LevelRegretforCasc.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Stochastic Reset Pathfinding (SRP) as an episodic learning problem on a directed graph where any failed edge resets the path to its source, modeling scenarios like quantum repeater networks and Lightning Network routing. It demonstrates that optimal policies are open-loop and places SRP within the combinatorial cascading bandit framework, delivering a path-level regret bound for PathUCB that breaks down regret into per‑path complexity.

## Key Takeaways
- The global-reset structure of SRP makes the optimal policy open-loop, placing it in the combinatorial cascading bandit (CCB) setting.  
- A Log-Dijkstra meta-algorithm with UCB and Thompson Sampling provides path-level regret bounds that depend on prefix and suffix reliability per edge.  
- PathTS achieves best empirical performance across diverse domains but fails to converge on adversarial instances due to exponential obstruction.

## Context
This work extends combinatorial bandit theory to graph‑structured problems where resetting after failures creates a cascading effect, offering insights into online decision making under uncertainty. It bridges classic bandit algorithms with real‑world scenarios such as quantum network routing and unreliable mesh delivery.

## Implications
For practitioners designing robust systems in noisy environments, SRP provides a principled framework for evaluating path selection strategies under edge failure. The results guide algorithm choice: PathTS is recommended but must be aware of adversarial limits that prevent guaranteed convergence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15440v1)
