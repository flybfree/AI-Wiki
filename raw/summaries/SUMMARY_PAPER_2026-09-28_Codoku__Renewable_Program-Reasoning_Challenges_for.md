---
title: Codoku: Renewable Program-Reasoning Challenges for Frontier Coding Agents
url: http://arxiv.org/abs/2609.34661v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_09-01-56Z_Codoku_RenewableProgram_ReasoningChallengesforFron.md
generated_at: 2026-09-28 22:51
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces Codoku, a renewable benchmark designed to test program reasoning capabilities of coding agents by addressing limitations in existing benchmarks where agents can bypass reasoning through code execution or benefit from data contamination. Codoku requires solvers to fill typed cells in partial programs while satisfying global static and dynamic constraints, ensuring that tool use or enumeration cannot substitute for genuine reasoning. Evaluation of five frontier models reveals that even proprietary systems struggle significantly with larger puzzles, highlighting the benchmark's effectiveness as a challenging testbed.

## Key Takeaways
- Existing program-reasoning benchmarks rely on assumptions that coding agents violate; specifically, agents can recover answers by executing programs rather than reasoning, and fixed task sets suffer from data contamination while being expensive to update. Codoku overcomes these issues by generating fresh puzzles on demand via semantic reification, ensuring each puzzle has a solvability witness and controllable complexity without exposure risks.
- The benchmark presents partial programs where agents must fill typed cells to satisfy prescribed control-flow graphs and execution paths; because the space of interdependent choices is exponentially large and valid solutions are sparse, neither tool use nor simple enumeration can solve the puzzles, forcing reliance on deep program reasoning.
- Experimental evaluation across five frontier models and 300 puzzles demonstrates that Codoku poses significant challenges; while small instances already test open-weight models, even top-tier proprietary models solve only approximately half of the larger puzzles when allowed to use tools within a fixed budget, confirming the benchmark's rigor.

## Context
As coding agents become more capable and tool-augmented, traditional benchmarks that measure static prediction or allow code execution no longer provide reliable signals of reasoning ability. This work addresses a critical gap in the evaluation landscape by creating a dynamic assessment framework that remains robust against agent capabilities like self-correction via execution and dataset memorization.

## Implications
The introduction of

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34661v1)
