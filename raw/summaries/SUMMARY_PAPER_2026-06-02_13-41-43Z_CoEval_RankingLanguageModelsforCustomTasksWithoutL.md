---
title: CoEval: Ranking Language Models for Custom Tasks Without Labeled Data or Trustworthy Benchmarks
url: http://arxiv.org/abs/2606.03650v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-02_13-41-43Z_CoEval_RankingLanguageModelsforCustomTasksWithoutL.md
generated_at: 2026-06-11 10:51
model: nvidia/nemotron-3-nano-4b
---

## Summary
CoEval is an open‑source framework that lets researchers rank language models using only a textual task description and without relying on human‑labeled data or standard benchmark scores. It creates a fresh attribute‑controlled benchmark each run, judges the rankings automatically with a cross‑family ensemble of models, and recovers the true model ordering with high accuracy. The system generates items that show no verbatim overlap with existing public benchmarks.

## Key Takeaways
- CoEval synthesizes an entirely new benchmark from a task description, eliminating human labels and preventing contamination from memorized benchmark items.
- It uses a small, diverse cross‑family judge ensemble to rank models; the reliability comes from panel composition rather than size, avoiding single‑judge bias.
- The framework produces zero verbatim 13‑gram overlap with five major public benchmarks, ensuring clean evaluation and removing verbosity bias.

## Context
Model selection for language applications remains a bottleneck when labeled data is scarce or public benchmarks are suspect. Current solutions often depend on human‑rated scores that may reflect memorization rather than genuine performance, limiting reproducibility and fairness across domains.

## Implications
For practitioners, CoEval offers a cheap, automated way to generate reliable leaderboards, enabling rapid iteration with each model release. This democratizes model evaluation and supports fair competition without costly human annotation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.03650v1)
