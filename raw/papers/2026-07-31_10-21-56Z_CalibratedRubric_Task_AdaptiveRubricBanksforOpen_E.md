---
title: CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation
published: 2026-07-31T10:21:56Z
authors: Mengting Chen, Yanshu Sun, Wanting Liang, Beidi Luan, Rui Sun, Dezhi Chen, Jing Li, Zuo Bai
url: http://arxiv.org/abs/2607.29252v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation

## Abstract
Reliable evaluation of open-ended LLM outputs requires fine-grained rubrics, yet expert curation is costly and difficult to scale. Existing automated pipelines rely on strict judge unanimity and binary variance filters, which cannot distinguish measurable rubrics from informative ones. We introduce CalibratedRubric, a task-adaptive framework that combines type-specific scoring, Bayesian rubric-measurability filtering, and item response theory (IRT)-based bank assembly. CalibratedRubric estimates each rubric's measurability with a Beta--Bernoulli agreement posterior and uses a submodular information-coverage objective to construct compact rubric banks over the observed capability range. Across financial, healthcare, general, and legal benchmarks, measurability filtering improves human-gold agreement on JudgmentBench from $κ=0.604$ to $0.743$. IRT-based greedy selection improves cross-fitted rank fidelity over random selection across all six evaluated response blocks and requires only 49 rather than 131 rubrics to reach the target correlation on FinResearchBench decision-support tasks. Task-label perturbations further reduce system separation, confirming the practical relevance of task-adaptive scoring. These results support CalibratedRubric as an efficient, uncertainty-aware approach to open-ended LLM evaluation, with calibration gains depending on sufficient judge redundancy.

## Metadata
- **Published**: 2026-07-31T10:21:56Z
- **Authors**: Mengting Chen, Yanshu Sun, Wanting Liang, Beidi Luan, Rui Sun, Dezhi Chen, Jing Li, Zuo Bai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29252v1)