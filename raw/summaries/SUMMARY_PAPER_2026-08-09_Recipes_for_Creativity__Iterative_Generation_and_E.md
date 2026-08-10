---
title: Recipes for Creativity: Iterative Generation and Evaluation in Large Language Models
url: http://arxiv.org/abs/2608.07243v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_14-02-36Z_RecipesforCreativity_IterativeGenerationandEvaluat.md
generated_at: 2026-08-09 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether iterative generation improves creativity in large language models by adapting FunSearch to recipe generation for the 2024 Pillsbury Bake-Off and evaluating outputs against human benchmarks using TTCT-based LLM evaluation. It finds that iterative generation-selection can match human creativity scores but additional iterations alone do not help. The in‑loop evaluator is identified as a key factor.

## Key Takeaways
- Iterative generation with selection yields creativity scores comparable to human benchmarks, indicating that the process itself matters more than sheer number of steps.
- A smaller selection scorer produces significantly higher TTCT scores across most dimensions, showing that evaluator design outweighs iteration count.
- Temperature influences originality only and has limited effect on other creative metrics.

## Context
Generative models are typically judged by single outputs rather than the creative process that produced them. This study highlights a gap between automated evaluation and human‑like iterative refinement. The findings align with broader efforts to model subjective creativity in AI systems.

## Implications
Designing in‑loop evaluators is crucial for any system aiming to mimic human‑style creativity, suggesting future work should prioritize scorer efficiency over iteration depth. Practitioners can leverage this insight to build more effective creative search pipelines that balance exploration and evaluation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07243v1)
