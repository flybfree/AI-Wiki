---
title: MathDuels: Evaluating LLMs as Problem Posers and Solvers
url: http://arxiv.org/abs/2604.21916v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-23_17-57-46Z_MathDuels_EvaluatingLLMsasProblemPosersandSolvers.md
generated_at: 2026-06-11 10:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MathDuels, a self‑play benchmark that forces frontier language models to both create and solve mathematical problems under adversarial prompting. Experiments across 19 state‑of‑the‑art models show that authoring and solving capabilities are not perfectly correlated, exposing skill gaps invisible in single‑role evaluations.

## Key Takeaways
- The three‑stage generation pipeline (meta‑prompting, problem creation, difficulty amplification) produces valid problems that a verifier can confirm, allowing the Rasch model to estimate both solver ability and problem difficulty.  
- Dual‑role evaluation reveals partial decoupling between how well models solve problems and how difficult problems they generate, indicating distinct competencies.  
- As newer models enter the arena their authored problems defeat older solvers, causing the benchmark’s difficulty to co‑evolve rather than plateau at a fixed ceiling.

## Context
Current AI research often evaluates language models solely as problem solvers on static benchmarks that cannot capture the creative or strategic aspects of generating tasks. This limitation hampers our understanding of model versatility and progress over time.

## Implications
MathDuels provides a dynamic metric for tracking both generation and reasoning strengths, guiding developers to balance model capabilities across different AI applications. Practitioners can use the public leaderboard to monitor improvements and allocate resources where skill gaps persist.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.21916v1)
