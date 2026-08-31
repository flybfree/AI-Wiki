---
title: When Linguistic and Internal Confidence Diverge in Large Language Models
url: http://arxiv.org/abs/2608.28382v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_14-37-31Z_WhenLinguisticandInternalConfidenceDivergeinLargeL.md
generated_at: 2026-08-30 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the confidence that large language models express in their responses matches the uncertainty they actually feel internally across a range of tasks and model types. It finds that linguistic confidence often diverges from internal logit‑based measures, especially on classification and generation benchmarks. The study shows that prompt design and model training affect both the reported confidence and its alignment with true uncertainty.

## Key Takeaways
- Linguistic confidence rarely aligns with internal logits; association is weak except for easier items or stronger models.
- Instruction‑tuned models report higher confidence but also show larger gaps and poorer calibration, indicating a lossy channel between verbal statements and true uncertainty.
- Distributional properties of confidence scores explain most alignment patterns, while model metadata contributes less after controlling for task difficulty.

## Context
Understanding the gap between external confidence reports and internal uncertainty is crucial as LLMs are increasingly used in safety‑critical applications where reliability matters. This work adds to debates on model interpretability and the limits of self‑assessment metrics.

## Implications
Practitioners should treat linguistic confidence as a diagnostic tool rather than a guarantee, using multi‑axis checks before trusting it for downstream decisions. The findings suggest that current pipelines may overestimate model reliability if they rely solely on confidence scores without calibration verification.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28382v1)
