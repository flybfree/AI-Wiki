---
title: Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control
url: http://arxiv.org/abs/2609.15803v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_16-12-41Z_DelegatingAuthorizationtoMisalignedAgents_Coalitio.md
generated_at: 2026-09-15 00:28
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper addresses the control problem inherent in long-running AI agents by proposing a framework for delegating authorization to panels of potentially misaligned reviewer agents. The authors establish a novel condition called k-robust coalitional alignment, which guarantees that a principal's expected utility meets or exceeds a designated baseline even when individual reviewers lack full alignment. Through theoretical analysis and empirical experiments, the study demonstrates how threshold-based approval rules can maintain safety in both static decision-making environments and sequential discounted Markov decision processes.

## Key Takeaways
- The authors introduce k-robust coalitional alignment, a condition weaker than individual agent alignment that guarantees safe delegation when a reviewing panel tolerates up to k disapprovals under a threshold rule.
- In sequential control settings modeled as discounted MDPs, the paper proves that safety at every state is both necessary and sufficient for an induced policy to match or improve upon a baseline policy, regardless of the proposer agent's alignment.
- When reviewer agents vote strategically, unanimous approval combined with full panel coverage in reward-function space ensures all Nash equilibria remain safe, whereas more permissive thresholds may inadvertently permit unsafe outcomes even among individually aligned reviewers.

## Context
As AI systems become increasingly autonomous and operate over extended horizons, ensuring their actions remain safely aligned with human objectives has emerged as a critical challenge.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15803v1)
