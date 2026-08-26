---
title: Preference Data Selection for Mitigating the Alignment Tax in Large Language Models
url: http://arxiv.org/abs/2608.24192v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_07-58-42Z_PreferenceDataSelectionforMitigatingtheAlignmentTa.md
generated_at: 2026-08-25 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BALIGN, a balanced data selection strategy that mitigates catastrophic forgetting while optimizing alignment efficacy for large language models. It identifies three key features in the preference optimization gradient that drive parameter drift and proposes a unified composite risk score to filter high‑risk samples. Experiments show that BALIGN preserves foundational capabilities without sacrificing alignment gains.

## Key Takeaways
- The reference model's log-probability margin influences parameter drift by indicating how far the chosen response deviates from the baseline.
- Token length difference between chosen and rejected responses matters because longer differences can destabilize learned representations.
- TF-IDF similarity to general capability corpora is another factor, as high similarity may indicate that a preference does not contribute new alignment utility.

## Context
Large language models must be aligned with human preferences for real‑world use yet often suffer from an alignment tax that erodes pre‑trained capabilities. This work shifts focus from architectural or optimization challenges to the data‑centric aspects of preference selection, highlighting which samples are most likely to cause forgetting.

## Implications
Practitioners can reduce the alignment tax by applying BALIGN's risk scoring, ensuring that only high‑utility preferences are retained. This approach maintains model robustness and efficiency, supporting scalable deployment where preserving general capabilities is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24192v1)
