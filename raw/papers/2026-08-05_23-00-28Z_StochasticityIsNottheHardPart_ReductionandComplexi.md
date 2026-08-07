---
title: Stochasticity Is Not the Hard Part: Reduction and Complexity in Instructional Sequencing over Prerequisite DAGs
published: 2026-08-05T23:00:28Z
authors: Zonglin Han, Yichen Chen, Jiawen Jiang, Tongan Shi, Kristian A. Stevens
url: http://arxiv.org/abs/2608.05455v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stochasticity Is Not the Hard Part: Reduction and Complexity in Instructional Sequencing over Prerequisite DAGs

## Abstract
When a student must learn concepts connected by prerequisite dependencies, when does the order of instruction matter, and what does it cost to find the best one? We study instructional sequencing as a stochastic shortest-path problem in which attempting a concept succeeds with a state-dependent probability and failure leaves the learner state unchanged. We first prove that this stochasticity can be eliminated exactly: the problem collapses to a deterministic shortest-path problem on the lattice of prerequisite order ideals, preserving optimal values and actions. The collapse removes stochastic complexity but not combinatorial complexity: optimal sequencing remains NP-hard -- via reduction from feedback arc set in tournaments -- even with no prerequisite edges, unit costs, uniform binary nonnegative transfer, and success probabilities at least $1/2$. Hardness is not uniform: when realizable transfer preferences remain jointly acyclic with the prerequisites, any topological order of the residual joint graph is optimal, and fixed prerequisite width yields polynomial-time exact dynamic programming. A computable diagnostic, $mΔ$, bounds the value of sequencing before optimization. On 70,893 interactions from an introductory CS course, the diagnostic certifies a doubly easy regime -- little value to optimize and little space to search -- while constructed transfer instances realize the challenging regime, where myopic sequencing suffers large regret yet exact A* with a consistent heuristic expands only linearly many states on that family.

## Metadata
- **Published**: 2026-08-05T23:00:28Z
- **Authors**: Zonglin Han, Yichen Chen, Jiawen Jiang, Tongan Shi, Kristian A. Stevens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05455v1)