---
title: Rethinking On-Policy Distillation of Large Language Models II: One Training Example
url: http://arxiv.org/abs/2609.04172v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-54-38Z_RethinkingOn_PolicyDistillationofLargeLanguageMode.md
generated_at: 2026-09-03 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the impact of training data on on‑policy distillation (OPD) by training a student model with only one query, demonstrating that performance improves dramatically over many steps and approaches results from full‑data OPD. The authors introduce state coverage as a metric to explain how well rollouts explore teacher states and why single‑query training can match multi‑query setups.

## Key Takeaways
- A single query reaches about 71.5 % of the states visited by full‑data OPD within the first 100 steps, showing that data volume is not the limiting factor for coverage.
- Adding more semantically distinct queries increases both state coverage and validation accuracy until 16 queries achieve near‑full‑data performance, indicating diminishing returns beyond a certain point.
- The student’s alignment with the teacher slows regardless of whether training uses one query or many, revealing that OPD is data‑overfed but algorithm‑starved.

## Context
On‑policy distillation has become a popular method for improving large language models without retraining from scratch. Recent successes suggest that efficient rollout generation can capture rich supervision, yet the underlying role of data remains unclear in minimal settings.

## Implications
For practitioners, this study highlights that step efficiency may be more critical than dataset size in OPD pipelines. Researchers should focus on designing queries that maximize state coverage and consider algorithmic bottlenecks when scaling distillation to frontier models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04172v1)
