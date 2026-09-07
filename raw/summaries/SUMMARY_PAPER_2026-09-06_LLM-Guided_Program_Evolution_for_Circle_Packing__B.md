---
title: LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28
url: http://arxiv.org/abs/2609.05093v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_12-48-13Z_LLM_GuidedProgramEvolutionforCirclePacking_Breakin.md
generated_at: 2026-09-06 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Discovery Loop, a lightweight system that leverages a large language model to iteratively evolve optimization algorithms for the circle‑packing problem. Applied to Packomania’s benchmark, the method achieved 2.4%–5.4% improvements over existing records for ten values of N (101–114) within fifteen iterations at a total LLM cost of $27.72, and these results have been independently accepted by the competition.

## Key Takeaways
- The system uses an LLM to propose algorithmic improvements guided by a scoreboard of past results and a history of prior ideas, discarding failures after verification.  
- Applied to Packomania’s circle‑packing benchmark, it raised the best known solutions for ten values of N in the range 101–114, delivering gains between 2.4% and 5.4% over previous records.  
- The entire process required only fifteen iterations and cost $27.72, showing a highly efficient use of LLM resources.

## Context
This work highlights how large language models can act as automated research assistants, providing real‑time feedback on algorithmic proposals without the need for extensive human oversight. By integrating an independent verifier and adaptive plateau detection, Discovery Loop demonstrates that LLMs can be employed cost‑effectively to push the boundaries of combinatorial optimization problems.

## Implications
For researchers, this approach offers a scalable pathway to discover novel solutions in complex scientific challenges at minimal expense. Practitioners may adopt similar LLM‑guided pipelines to accelerate algorithmic development and reduce reliance on manual trial‑and‑error methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05093v1)
