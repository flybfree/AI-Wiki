---
title: Accuracy and Order Sensitivity Diverge Under Label-Free Strategies
url: http://arxiv.org/abs/2608.11947v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_11-34-45Z_AccuracyandOrderSensitivityDivergeUnderLabel_FreeS.md
generated_at: 2026-08-12 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how removing label information from multiple‑choice questions affects large language model performance and whether this debiasing improves accuracy. It tests two strategies that eliminate option labels: a generation‑then‑matching method and an isolated scoring approach, both of which fail to boost scores. The analysis shows the bottleneck lies in withholding options rather than the matching step.

## Key Takeaways
- Removing label information does not reliably increase model accuracy across tested configurations.
- Only the configuration that presents all options paired with an LLM matcher matches the baseline performance.
- Cyclic permutation of option order sometimes yields modest gains, indicating residual positional sensitivity remains.

## Context
Multiple‑choice benchmarks are standard for evaluating language models but often conflate knowledge with answer order bias. Recent work seeks to isolate this bias, yet empirical results suggest that simple label removal is insufficient to correct it.

## Implications
Practitioners should consider more nuanced debiasing techniques beyond mere label omission when assessing model knowledge. The findings highlight the need for rigorous evaluation methods that account for both content and order effects in MCQ tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11947v1)
