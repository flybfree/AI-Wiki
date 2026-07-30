---
title: Minimal Markovization via Stable Quotients in Holonomy-Cover Decision Processes
published: 2026-07-29T17:03:35Z
authors: Zuyuan Zhang, Yongshan Chen, Mahdi Imani, Tian Lan
url: http://arxiv.org/abs/2607.27132v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Minimal Markovization via Stable Quotients in Holonomy-Cover Decision Processes

## Abstract
An agent acting under partial observability must retain a recursively updateable statistic of history that restores the Markov property, but the smallest such statistic is generally unknown. We characterize this minimal Markov sufficient statistic for holonomy-cover decision processes, a structured POMDP class in which the visible dynamics are Markov and every realized visible transition applies a fixed permutation to a hidden mode. In particular, we construct the stable quotient, the coarsest observation-wise abstraction preserving one-step rewards and quotient successors, and prove that the pair of the current observation and stable class forms an exact finite Markov state. When the current class is correctly initialized, exact class tracking requires exactly the minimal memory symbols, in the sense that under reachability and pairwise decision separation at a maximizing observation, no arbitrary finite-memory controller can use fewer. Under resettable diagnostics, nearest-prototype class inference has exponentially decaying error, and a calibrate-then-restart reduction transfers finite-MDP guarantees to the recovered state. The results enable \emph{Holonomy Memory Reinforcement Learning}. It represents memory by the current stable class, updates it through ordered edge transports, identifies local class coordinates when diagnostics are available, and applies a standard finite-MDP RL backbone after synchronization. Experiments recover an exact compression from raw states to quotient states and achieve perfect paired-order accuracy with three decision-time memory states, matching the quotient oracle and outperforming the non-oracle baselines.

## Metadata
- **Published**: 2026-07-29T17:03:35Z
- **Authors**: Zuyuan Zhang, Yongshan Chen, Mahdi Imani, Tian Lan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27132v1)