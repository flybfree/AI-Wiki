---
title: The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks
url: http://arxiv.org/abs/2608.16630v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_14-30-41Z_TheWorkingSetofaCodingAgent_CoherenceDebtinReposit.md
generated_at: 2026-08-17 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how coding agents manage consistency across large repositories by modeling the problem as a coupled-fact graph where facts are either retrieved from recent context or stored in parametric memory, and coherence debt arises when required facts are missing. Experiments show that without any fact channel models fail on unseen APIs, while supplying facts restores success; availability of facts determines outcomes more than their proximity to edits.

## Key Takeaways
- No model completes a task with both channels empty because it cannot reconstruct the coupled-fact graph, leading to coherence debt.
- Providing facts in the prompt resolves failures by restoring successful execution across all models and harnesses.
- Missing facts cause agents to fabricate content rather than remain silent, making read-based instruments unreliable.

## Context
This work addresses a core challenge in repository-scale AI: maintaining consistency when context windows are limited. It highlights how memory strategies affect task completion and introduces the concept of coherence debt as a quantitative measure of missing information.

## Implications
For practitioners, the findings suggest that prompt engineering must prioritize making required facts available to agents rather than relying on reading them from code. Industry systems should design harnesses that track fact availability and compare it with generated output to ensure correctness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16630v1)
