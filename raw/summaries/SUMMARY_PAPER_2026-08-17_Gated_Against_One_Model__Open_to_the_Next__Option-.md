---
title: Gated Against One Model, Open to the Next: Option-Only Solvability in Legal Multiple-Choice Benchmarks
url: http://arxiv.org/abs/2608.15428v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_22-11-00Z_GatedAgainstOneModel_OpentotheNext_Option_OnlySolv.md
generated_at: 2026-08-17 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a novel gating mechanism that isolates model behavior on legal multiple‑choice items by removing the question while keeping the correct answer option hidden. Applied to the UA-JudgeExam benchmark, it reveals that many models exhibit answer‑position bias, scoring only marginally above chance when the key is at A and performing poorly otherwise. The study shows that two models—GPT‑5.6 and Sonnet 4.6—maintain a small excess over chance after gating, while most others collapse to near‑chance performance.

## Key Takeaways
- Models can be “gated” against one model’s answer position, producing scores that are indistinguishable from random guessing on the majority of items.
- The gating effect is not transferable: the same model’s high confidence on rejected items does not improve its overall score beyond what it achieves when the question is present.
- Small sample sizes (e.g., 400 items) mask these biases, indicating that the phenomenon may be more pronounced in larger datasets.

## Context
Legal multiple‑choice benchmarks are a standard for evaluating AI reasoning under time pressure. This work highlights how answer‑position artifacts can masquerade as genuine competence, challenging current benchmark interpretations and prompting rethinking of model performance metrics.

## Implications
Researchers must incorporate gating analyses to separate true knowledge from superficial guessing in future evaluations. Practitioners should consider these biases when deploying models for high‑stakes legal or exam settings where accuracy is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15428v1)
