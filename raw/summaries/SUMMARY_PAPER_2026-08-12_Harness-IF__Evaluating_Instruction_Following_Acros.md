---
title: Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents
url: http://arxiv.org/abs/2608.11727v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_07-07-57Z_Harness_IF_EvaluatingInstructionFollowingAcrossIns.md
generated_at: 2026-08-12 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Harness‑IF, a method to evaluate how coding agents follow operational rules by analyzing execution evidence across multiple rule surfaces. It demonstrates that models score higher on rule compliance than on detecting rule violations, revealing systematic overestimation of instruction following.

## Key Takeaways
- The benchmark scores 60 multi‑turn coding tasks with 256 rules placed on five configurable agent surfaces, showing accuracy ranges from 72.1% to 85.9% across models.
- Against‑Prior Accuracy (AP‑Acc) measures rule violations by re‑running tasks with the rule held back, yielding AP‑Acc scores of 66.1–78.6%, indicating a clear gap between compliance and actual rule adherence.
- Every model performs worse on against‑prior rules than on prior‑control rules, with mean difference of about 5.8 points, confirming that prior control inflates apparent compliance.

## Context
Current instruction‑following benchmarks for coding agents focus either on final task success or on user‑turn rules, leaving the intermediate operational rule adherence unexplored. This work bridges that gap by providing a fine‑grained metric that isolates rule execution from overall success, which is crucial as agents grow more complex and multi‑modal.

## Implications
For developers, Harness‑IF offers a reliable way to detect when an agent’s apparent compliance masks hidden rule violations, guiding safer deployment. For researchers, the method highlights the need for benchmarks that probe rule surfaces rather than just final outcomes, informing future model evaluation practices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11727v1)
