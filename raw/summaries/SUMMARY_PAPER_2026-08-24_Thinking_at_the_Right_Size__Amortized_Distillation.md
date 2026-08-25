---
title: Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs
url: http://arxiv.org/abs/2608.22854v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_06-36-32Z_ThinkingattheRightSize_AmortizedDistillationAcross.md
generated_at: 2026-08-24 21:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ADAPT, a framework that amortizes the cost of creating multiple model variants and sizes by using a single distillation run to generate a continuum of interpolated models across both axes. By combining two-phase distillation with weight‑delta initialization, it produces L × K models for L intermediate sizes and K post‑trained variants without extra training.

## Key Takeaways
- ADAPT builds post‑trained students through pre‑training alignment and supervised fine‑tuning distillation, enabling smooth interpolation between size and performance on generation and reasoning tasks.  
- The framework approximates this construction across different post‑trained variants by transferring the weight changes induced by distillation using a delta initialization that starts from distinct variant bases.  
- The resulting continuum allows adaptive model‑size selection at inference time, improving the compute–accuracy trade‑off for long‑form reasoning.

## Context
Current LLM deployment often requires generating separate models for each combination of size and training variant, which is computationally expensive. This paper addresses that inefficiency by showing how distillation can be reused to span both dimensions, a concept that aligns with broader efforts to make large language models more resource‑efficient and scalable.

## Implications
For practitioners, ADAPT reduces development time and hardware costs while maintaining performance across model sizes and variants. It opens the door to dynamic inference pipelines where users can choose optimal size based on latency constraints without retraining, fostering wider adoption of high‑quality LLMs in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22854v1)
