---
title: TangPoetryBench: A Multi-Dimensional Benchmark and Rubric-Conditioned Evaluator for Poetry-to-Image Generation
url: http://arxiv.org/abs/2608.11452v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_21-30-53Z_TangPoetryBench_AMulti_DimensionalBenchmarkandRubr.md
generated_at: 2026-08-12 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TangPoetryBench, a multi‑dimensional benchmark that evaluates how well text‑to‑image models render classical Chinese Tang poems by measuring ten quality dimensions such as visual soundness, faithfulness to imagery, cultural and stylistic appropriateness, absence of spurious text, emotional fidelity, and the evocation of implicit emotion. The study finds that current T2I models vary across these dimensions and that a rubric‑conditioned evaluator can match the performance of a strong proprietary judge while generalizing to unseen generators and additional poetic traditions.

## Key Takeaways
- The benchmark reveals both shared strengths and model‑specific weaknesses among state‑of‑the‑art T2I systems when illustrating poetry.  
- Models are especially challenged in evoking a poem’s implicit emotion, which is rarely explicit in the text.  
- PoemAutoEvaluator (PAE) achieves parity with Claude, generalizes to unseen generators and Song Ci poems, and scales without additional human annotation.

## Context
The rapid advancement of generative models has placed them at the forefront of creative AI, yet existing evaluation tools focus on literal text‑image correspondence rather than holistic artistic fidelity. TangPoetryBench addresses this gap by providing a nuanced assessment framework that aligns with human judgments across multiple dimensions.

## Implications
For researchers and practitioners, TangPoetryBench offers a reproducible benchmark to guide model improvement beyond surface metrics. It also demonstrates the viability of rubric‑based evaluation for creative AI, potentially reshaping industry standards for assessing artistic output in generative systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11452v1)
