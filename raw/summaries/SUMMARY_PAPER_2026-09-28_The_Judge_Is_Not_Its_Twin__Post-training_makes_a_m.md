---
title: The Judge Is Not Its Twin: Post-training makes a model's writing more predictable but barely moves its taste, as a judge, toward predictable writing
url: http://arxiv.org/abs/2609.32196v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_03-46-50Z_TheJudgeIsNotItsTwin_Post_trainingmakesamodel_swri.md
generated_at: 2026-09-28 20:52
model: qwen3.6-35b-a3b
---

## Summary
This study examines whether post-training language models to produce more predictable text inadvertently biases their capacity to evaluate other texts as judges. By tracking OLMo-2 and Zephyr models through base, supervised fine-tuning, and direct preference optimization stages, the authors demonstrate that while generative predictability consistently increases, evaluative preferences remain largely stable. The research highlights a significant decoupling between how training shapes writing style versus how it shapes judgment criteria in automated evaluation pipelines.

## Key Takeaways
- Post-training progressively increases the predictability of generated narratives across all tested prompts, with fully trained models showing substantial reductions in token surprise compared to their base versions.
- Despite this generational shift toward familiarity, trained models acting as judges exhibit negligible preference for predictable writing, with probability tilts remaining under one point and falling within untrained baseline variance.
- When evaluating creativity, training actually reinforces a bias toward longer narratives rather than predictability, and ultimately degrades the reliability of the "more creative" metric by breaking its ability to distinguish original stories from scrambled text.

## Context
As automated LLM-based evaluators become standard in AI development pipelines, understanding how alignment techniques shape both generation and evaluation capabilities is critical. This work addresses a growing concern that optimization for coherence or human preference might systematically penalize novelty, potentially creating blind spots in creativity assessment. By empirically testing the same models as both creators and critics across multiple training stages, the study provides rare empirical insight into how post-training alters internal representational biases across different functional roles.

## Implications
Practitioners relying on automated judges to measure creative progress should recognize that standard alignment techniques may not inherently skew evaluations toward formulaic outputs, though they do fundamentally alter generation styles. The findings suggest that evaluation benchmarks require explicit controls for narrative length and structural predictability to avoid conflating quantity with quality or novelty. Ultimately, developers must carefully decouple generative training objectives from evaluative metrics to ensure that automated grading accurately captures genuine creative advancement rather than mere stylistic conformity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32196v1)
