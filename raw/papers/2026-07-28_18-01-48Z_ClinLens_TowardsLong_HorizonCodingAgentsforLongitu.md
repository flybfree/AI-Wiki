---
title: ClinLens: Towards Long-Horizon Coding Agents for Longitudinal Multimodal Clinical Data Science
published: 2026-07-28T18:01:48Z
authors: Yuan Zhu, Ethan B. Liu, Frank Nie, Jindong Han
url: http://arxiv.org/abs/2607.26155v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ClinLens: Towards Long-Horizon Coding Agents for Longitudinal Multimodal Clinical Data Science

## Abstract
Clinical data-science agents must transform heterogeneous longitudinal records into auditable analyses, yet existing benchmarks largely isolate medical question answering, structured-table reasoning, or generic scientific repositories. We introduce CLINLENS, a benchmark of 200 executable tasks over five linked MIMIC resources spanning structured electronic health records, notes, electrocardiograms, chest radiographs, and echocardiograms. A 4 x 5 taxonomy crosses four patient-time scopes with five analysis capabilities. Program-first reverse synthesis pairs each bounded semi-raw package with an evaluator-private reference workflow and checks required artifacts, cohort and temporal semantics, and the final answer. On a fixed 126-task suite, the strongest of 24 standardized model-scaffold configurations achieves 56.3% scope-macro STRICTPASS despite 100% EXECSUCCESS. For reference, a separately configured coding agent solves 83 of 126 tasks, while five biomedical systems adapted to GPT-4o-mini reach at most 2.9% scope-macro STRICTPASS. These results expose a substantial gap between runnable submissions and correct clinical analyses.

## Metadata
- **Published**: 2026-07-28T18:01:48Z
- **Authors**: Yuan Zhu, Ethan B. Liu, Frank Nie, Jindong Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26155v1)