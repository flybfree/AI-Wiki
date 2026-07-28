---
title: Maximum Satisfiability of Simple Temporal Problems
url: http://arxiv.org/abs/2607.23785v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_18-00-56Z_MaximumSatisfiabilityofSimpleTemporalProblems.md
generated_at: 2026-07-27 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the MAXSTP problem which seeks a maximum‑cardinality consistent subset of Simple Temporal Problems constraints. It proves NP‑hardness and analyses parameterized complexity using variables n, coefficient magnitude k, treewidth tw and vertex cover size vc. The authors show W[1]‑hardness for n and combined parameters but provide an O*(k^n) algorithm for fixed k.

## Key Takeaways
- MAXSTP is W[1]-hard when parameterized only by the number of variables n, indicating that n alone cannot yield fixed‑parameter tractability. - The algorithmic bound O*(k^n) gives single‑exponential time for fixed coefficient magnitude k, showing practical solvability under small numeric ranges. - When combined parameters such as treewidth tw or vertex cover size vc are used, the problem remains W[1]-hard but admits XP algorithms with runtime O*((n·k)^tw).

## Context
Simple Temporal Problems form a foundational model for temporal reasoning in AI and constraint satisfaction systems. Understanding their optimization limits informs algorithm design for real‑world applications where constraints may be noisy or incomplete.

## Implications
For practitioners, the results clarify when MAXSTP can be tackled efficiently using parameterized techniques versus needing exponential methods. This guidance helps prioritize problem instances that benefit from FPT algorithms based on structural parameters like treewidth or coefficient magnitude.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23785v1)
