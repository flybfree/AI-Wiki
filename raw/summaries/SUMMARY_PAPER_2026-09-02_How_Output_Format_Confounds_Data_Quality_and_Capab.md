---
title: How Output Format Confounds Data Quality and Capability in Instruction Tuning
url: http://arxiv.org/abs/2609.02015v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_02-42-36Z_HowOutputFormatConfoundsDataQualityandCapabilityin.md
generated_at: 2026-09-02 20:53
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the output format used to present model answers distorts both data quality assessments and model capability evaluations during instruction tuning. By analyzing gradient signatures across 12 tasks, four equivalent interfaces, three model families, and controlled corruptions, it demonstrates that the surface format confounds these judgments while preserving semantic content.

## Key Takeaways
- The residual signal from interface variation is not noise; it perfectly identifies each unit’s target task across all three model families.  
- A skill that improves accuracy by over 40 points under the training format can become invisible when measured under other formats, showing capability is stored relative to the training interface.  
- Adjusting a single generation budget flips GSM8K fine‑tuning effects from gain to loss, indicating that output formatting directly influences measured outcomes.

## Context
In modern AI research, instruction tuning relies on surface metrics such as accuracy scores and benchmark results, yet these are often evaluated after answers are rendered in specific formats. This paper reveals a hidden layer of influence where the chosen interface can mask or amplify true performance changes, affecting both empirical evaluation and theoretical understanding of model learning.

## Implications
Practitioners must recognize that reporting only the output format without considering its impact on underlying quality may lead to misleading conclusions about model effectiveness. Future work should standardize format‑independent metrics and report interventions that isolate content from presentation artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02015v1)
