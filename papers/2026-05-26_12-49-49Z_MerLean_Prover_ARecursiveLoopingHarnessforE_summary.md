---
title: "Summary: 2026-05-26_12-49-49Z_MerLean_Prover_ARecursiveLoopingHarnessforEnd_to_E.md"
date: 2026-05-26
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-26_12-49-49Z_MerLean_Prover_ARecursiveLoopingHarnessforEnd_to_E.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.26959v1)
Saved: 2026-05-26 20:01
Source: 2026-05-26_12-49-49Z_MerLean_Prover_ARecursiveLoopingHarnessforEnd_to_E.md
Model: None

---


## Summary  
The authors present MerLean‑Prover, an end‑to‑end Lean 4 theorem prover that automatically generates kernel‑checkable proofs instead of relying on “sorry” placeholders. It is built from three agents—Planning, Check, and Lean—wrapped in a recursive outer loop whose unit of revision is the proof plan itself. Crucially, the system requires no fine‑tuning, custom reinforcement‑learning objectives, or problem‑specific scaffolding. The harness demonstrates that simple design choices can yield strong performance across both benchmark suites.

## Key Contributions  
- [Finding 1] MerLean‑Prover solves 10 out of 23 FormalQualBench problems, outperforming the best open‑source baseline (OpenGauss: 8/23).  
- [Finding 2] It closes all 12 Putnam2025 problems with a substantially lower total wall‑clock time than the next‑best system that also solves the full set.  
- [Finding 3] The harness transfers to smaller models, where Sonnet solves all four FormalQualBench tasks and Haiku solves the two short ones.

## Methodology  
The authors approached the problem by constructing a recursive proof‑generation loop: the Planning agent proposes a high‑level plan, the Check agent verifies that each step is kernel‑checkable, and the Lean agent produces the actual Lean code. The outer loop iteratively revises the plan until a complete proof is obtained. This design avoids any model fine‑tuning or problem‑specific objectives, relying instead on a generic harness that can be applied uniformly across theorems.

## Results  
Experimental results show that MerLean‑Prover achieves 10/23 FormalQualBench success rate and 12/12 Putnam2025 closure. When using the same harness with smaller models—Sonnet (a distilled version of GPT‑4) and Haiku—performance remains strong: Sonnet solves all four FormalQualBench problems, while Haiku handles the two short ones. Moreover, MerLean‑Prover’s total wall‑clock time is lower than that of OpenGauss for Putnam2025, indicating both higher success and efficiency.

## Significance  
These findings highlight that harness design is a central factor in end‑to‑end Lean 4 theorem proving, alongside raw model capability. A relatively simple recursive looping structure can already produce state‑of‑the‑art results, suggesting that future work could focus on improving the loop’s logic rather than solely on scaling up models.

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]
