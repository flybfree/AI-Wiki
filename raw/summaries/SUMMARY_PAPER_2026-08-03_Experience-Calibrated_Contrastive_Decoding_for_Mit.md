---
title: Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based Text-to-Speech
url: http://arxiv.org/abs/2608.00722v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_15-41-55Z_Experience_CalibratedContrastiveDecodingforMitigat.md
generated_at: 2026-08-03 23:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Experience-Calibrated Contrastive Decoding (ECCD), a training-free decoding-time method that strengthens text-derived alignment information while preserving experience information from acoustic context. Experiments on four models show up to 55.6% reduction in WER/CER across SeedTTS-Eval and CV3-Eval, with a listening gain of +0.644 CMOS. The analysis reveals alignment influence is strongest at correct boundaries and weaker at first-error points.

## Key Takeaways
- ECCD distinguishes text-derived alignment information from experience information supplied by acoustic context and learned speech regularities.
- The method applies only positive alignment enhancement, preserving the original expert distribution of the model.
- Experience compatibility calibration determines the strength of alignment boost, leading to up to 55.6% WER reduction.

## Context
This work addresses a persistent challenge in LM-based text-to-speech systems where hallucinated speech can degrade user experience and system reliability. By introducing a decoding-time control mechanism that does not require retraining, ECCD offers a practical improvement over architectural or training-based solutions.

## Implications
The findings suggest that conditional information control could become a standard technique for mitigating hallucinations in generative TTS pipelines. Practitioners can integrate ECCD into existing systems to boost performance without additional data collection, supporting scalable deployment across multilingual applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00722v1)
