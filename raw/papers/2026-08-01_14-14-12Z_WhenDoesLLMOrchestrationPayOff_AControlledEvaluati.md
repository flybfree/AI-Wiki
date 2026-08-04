---
title: When Does LLM Orchestration Pay Off? A Controlled Evaluation of Accuracy, Cost, and Task Difficulty
published: 2026-08-01T14:14:12Z
authors: Nicolas Leins, Nico Pelleriti, Jana Gonnermann-Müller, Sebastian Pokutta
url: http://arxiv.org/abs/2608.00685v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Does LLM Orchestration Pay Off? A Controlled Evaluation of Accuracy, Cost, and Task Difficulty

## Abstract
LLM orchestration is often assumed to improve reasoning by allocating additional inference-time computation, yet its gains may not justify its cost. Existing comparisons also frequently overlook differences in optimization effort, making it difficult to isolate the value of orchestration itself. We conduct a controlled evaluation of Self-Refine, Best-of-$N$, and Debate against task-only and chain-of-thought (CoT) single-call baselines across five LLM backbones and three domains: competitive programming, chess puzzles, and mathematics. For comparability, we optimize each method with GEPA under the same optimization budget and evaluate all methods on the same difficulty-stratified benchmark items. Orchestration yields moderate but benchmark-dependent gains: averaged across backbones within each benchmark, the largest improvement is 4.6 percentage points over optimized CoT inference and 4.5 points over task-only inference, while requiring approximately 2 to 4 times the mean total tokens of task-only inference. Human-derived difficulty is associated with lower absolute accuracy in all three benchmarks, but within-benchmark analyses do not indicate that orchestration effects increase with task difficulty. By contrast, exploratory mixed-effects analyses reveal strong interactions between orchestration method and backbone model across all three benchmarks, showing that orchestration effectiveness depends substantially on the underlying model. Our results suggest that orchestration decisions should be model-specific and account for whether moderate accuracy gains justify the additional inference cost. More broadly, evaluations of LLM orchestrations should control optimization effort and report model-specific accuracy--cost trade-offs rather than treating additional inference-time structure as uniformly beneficial.

## Metadata
- **Published**: 2026-08-01T14:14:12Z
- **Authors**: Nicolas Leins, Nico Pelleriti, Jana Gonnermann-Müller, Sebastian Pokutta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00685v1)