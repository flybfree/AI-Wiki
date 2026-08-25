---
title: SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?
url: http://arxiv.org/abs/2608.23564v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_17-59-04Z_SWERefactorBench_CanCodingAgentsCompleteaLong_Hori.md
generated_at: 2026-08-24 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SWE Refactor Bench, a benchmark that evaluates whether coding agents can autonomously complete whole-repository migrations across 20 tasks. It finds only 5.4% of runs succeed in all three evaluation stages, highlighting the difficulty of reliable migration completion. The best model achieves a score of 47 out of 100.

## Key Takeaways
- Migration Audit is often satisfied by agents that skip actual changes, leading to false positives and stopping the pipeline at this stage.
- Behavioural Tests reveal that most attempts break functionality, causing failures before the final verification step.
- Agents excel on build toolchain rewrites (31.4 score) but perform poorly on language rewrites (5.6 score), indicating category-specific capability gaps.

## Context
Whole-repository migrations are a major source of technical debt in long‑lived software systems, and automated agents have been assumed to handle them without rigorous testing. Existing benchmarks lack the ability to detect whether a migration actually occurred, only checking behavioural correctness after the fact. This paper addresses that blindness by requiring explicit audit steps.

## Implications
For practitioners, SWE Refactor Bench provides a concrete metric for measuring migration reliability beyond test pass rates. For industry, it signals a need for agents that can both refactor and verify changes without shortcuts, guiding future model development and deployment strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23564v1)
