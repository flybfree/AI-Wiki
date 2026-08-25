---
title: What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels
url: http://arxiv.org/abs/2608.22960v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_08-27-33Z_WhatProcessEvaluationofCodingAgentsActuallyMeasure.md
generated_at: 2026-08-24 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a framework to clarify what process evaluation of coding agents actually measures. By distinguishing action, task, and step levels, the authors show that current methods often conflate these concepts, leading to misleading assessments of agent behavior.

## Key Takeaways
- Next actions in file‑localization are driven mainly by execution provenance rather than transitions through a code graph, indicating that process evaluation focuses on causal roots.  
- Execution uncertainty is structured at the task level instead of individual steps, revealing that agents experience higher doubt about overall goals than fine‑grained actions.  
- Full‑trace judges suffer from systematic collider bias, suggesting that present evaluations may capture semantic relevance rather than genuine causal contributions.

## Context
AI research increasingly relies on process metrics to gauge how intelligent systems work, but many studies treat action prediction, task uncertainty, and step attribution as interchangeable problems. This conflation obscures the true nature of agent execution and hampers reliable benchmarking.

## Implications
For practitioners, recognizing these levels helps design evaluations that target genuine causal mechanisms rather than superficial correlations. For industry, it enables more trustworthy deployment monitoring where agents’ reasoning steps truly matter.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22960v1)
