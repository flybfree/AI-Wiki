---
title: SelfOp: An Optimization Algorithm for Self-Improving Security Agents
url: http://arxiv.org/abs/2609.22792v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-19_05-51-27Z_SelfOp_AnOptimizationAlgorithmforSelf_ImprovingSec.md
generated_at: 2026-09-28 14:26
model: qwen3.6-35b-a3b
---

## Summary
SelfOp introduces an algorithm to automatically optimize the task context of frozen security LLM agents without modifying model weights or execution harnesses, addressing the scarcity of expert demonstrations and rewards in security tasks. By employing chain-rule-inspired textual gradient descent, the method propagates error signals backward through agent trajectories to generate per-instance gradients that are accumulated via consensus-based filtering. Evaluated on real-world vulnerability reproduction tasks, SelfOp achieves significant self-improvements with minimal training data, enabling smaller models to outperform larger baselines and demonstrating strong cross-model transferability of optimized skills.

## Key Takeaways
- SelfOp optimizes instructions, skills, and reference documents using textual gradient descent derived from backward error propagation through the agent

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.22792v1)
