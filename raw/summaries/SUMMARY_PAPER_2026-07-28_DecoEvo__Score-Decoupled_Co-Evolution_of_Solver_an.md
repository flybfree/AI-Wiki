---
title: DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space
url: http://arxiv.org/abs/2607.25675v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_12-53-30Z_DecoEvo_Score_DecoupledCo_EvolutionofSolverandRubr.md
generated_at: 2026-07-28 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DecoEvo, a method that co-evolves a solver skill and a rubric-generator skill in text space without relying on gold rubrics. It separates the feedback loop for the solver from the generation of new rubrics, allowing each to improve independently based on different objectives.

## Key Takeaways
- The solver is updated using criterion-level feedback while the rubric generator is revised through audits that focus on requirement coverage and response discrimination independent of aggregate scores.
- Decoupling prevents the rubric from becoming easier simply because the solver’s score improves, avoiding misleading progress signals.
- Under standard benchmarks, DecoEvo achieves 2.8–5.0% relative gains over SkillOpt across five benchmarks and three LLM backbones.

## Context
Text-space optimization seeks to enhance LLMs by modifying external artifacts rather than model weights, preserving interpretability while improving performance. Existing approaches often treat evaluation as static, limiting adaptation on open-ended tasks where criteria evolve dynamically.

## Implications
Practitioners can adopt DecoEvo’s decoupled design to create more robust and interpretable optimization pipelines that respond to emerging solver weaknesses without overfitting to current rubrics. This could lead to continual improvement of AI systems in a transparent, scalable manner.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25675v1)
