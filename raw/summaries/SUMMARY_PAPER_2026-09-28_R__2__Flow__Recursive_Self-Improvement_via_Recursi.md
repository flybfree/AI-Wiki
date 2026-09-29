---
title: R$^2$ Flow: Recursive Self-Improvement via Recursive Skill Evolution
url: http://arxiv.org/abs/2609.33867v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_19-43-15Z_R__2_Flow_RecursiveSelf_ImprovementviaRecursiveSki.md
generated_at: 2026-09-28 21:38
model: qwen3.6-35b-a3b
---

## Summary
R$^2$ Flow is a recursive self-improvement framework designed to enable LLM-based agents to reliably enhance their capabilities by reusing and revising skills within executable procedures. The method addresses critical failures in flow-based training, such as strategy collapse and misaligned credit assignment, by employing a shared-state orchestration graph that pools evidence across equivalent executions and incorporates independent verification for skill library updates. Experimental results demonstrate significant gains in task accuracy and edit precision across diverse domains compared to existing baselines.

## Key Takeaways
- R$^2$ Flow mitigates strategy collapse and erroneous credit assignment by constructing a shared-state orchestration graph that merges execution histories differing only in the order of independent steps, allowing flow training to aggregate evidence efficiently while using a flow-share readout invariant to the backward policy.
- The framework implements a rigorous update cycle alternating policy learning, verification, and versioned library edits; skill changes are determined by a signed utility rank and verifier evidence, with updates triggered only when residual-variance plateaus indicate genuine improvement potential.
- Empirical evaluations across question answering, mathematical reasoning, interactive decision making, and code generation confirm that R$^2$ Flow surpasses heuristic orchestration, reinforcement learning, and skill-evolution baselines in both accuracy and library-edit precision, while demonstrating robust transfer capabilities across different execution environments.

## Context
As autonomous agents become more complex, ensuring stable self-improvement mechanisms is paramount to prevent degradation or instability during iterative refinement. This work advances the state of recursive self-improvement by introducing structural innovations in flow-based training that resolve fundamental obstacles in credit assignment and strategy stability within tree-structured agent histories.

## Implications
The proposed framework offers a scalable pathway for developing robust, self-evolving AI systems capable of continuous skill refinement without relying on external supervision or heuristic rules

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33867v1)
