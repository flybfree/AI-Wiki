---
title: Graph-Guided Repository Environment Construction
published: 2026-09-27T10:22:46Z
authors: Jianying Pan, John Zhang, Hongyu Zhang
url: http://arxiv.org/abs/2609.33429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Graph-Guided Repository Environment Construction

## Abstract
Coding agents now increasingly rely on execution to validate their solutions, making the construction of reliable execution environments a critical enabling capability. However, repository environment construction is challenging because execution requirements are fragmented across repository artifacts and may only become apparent during execution. Existing agent-based approaches address this problem through iterative interaction, but information about the current construction state, including discovered requirements, satisfied and unresolved prerequisites, and their dependencies, can remain distributed across the interaction history. We present Graph2Env, an agent-based approach centered on DepGraph, a typed dependency graph that explicitly represents the environment requirements needed for repository execution, their dependency relations, and their states. Graph2Env uses DepGraph to guide environment construction and continuously refines it with execution feedback, while persisting successful repairs into a replayable construction procedure. The resulting artifacts are then applied in a fresh environment to verify that the constructed environment can be reproduced. We evaluate Graph2Env on a benchmark of 200 Python repositories drawn from RATBench and EnvBench, against a static dependency-inference baseline (pipreqs), three specialized environment-construction systems (Repo2Run, RAT, and SetupX), and two general-purpose coding agents (SWE-agent and Claude Code). Graph2Env achieves an 81.0% Environment Build Success Rate (EBSR) and a 59.3% Environment Setup Success Rate (ESSR), outperforming the strongest baseline by 9.5 and 9.0 percentage points, respectively.

## Metadata
- **Published**: 2026-09-27T10:22:46Z
- **Authors**: Jianying Pan, John Zhang, Hongyu Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33429v1)