---
title: ASR-Roundtrip Evaluation Can Mask Context- and Convention-Dependent Reading Errors in Chinese News TTS
url: http://arxiv.org/abs/2608.10606v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_07-49-37Z_ASR_RoundtripEvaluationCanMaskContext_andConventio.md
generated_at: 2026-08-11 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the limitations of ASR-roundtrip evaluation for Chinese news text‑to‑speech (TTS) by highlighting false negatives that arise from context‑ and convention‑dependent reading errors. The study identifies 46 masked cases where raw TTS produced a plausible but incorrect transcription while ASR captured the intended surface text, demonstrating that roundtrip methods can mask these subtle issues.

## Key Takeaways
- Raw TTS may select a plausible yet wrong reading for high‑risk spans such as sports scores or aircraft models, leading to false negatives in ASR-roundtrip audits.  
- A targeted audit of 110 MiMo TTS cases reveals 46 previously masked errors that are re‑exposed when using span‑isolation diagnostics.  
- Qwen3‑ASR surface‑recovers 40 out of the 97 confirmed masked cases, whereas Paraformer succeeds in only 2, showing a significant gap between models.

## Context
The rapid adoption of ASR-roundtrip as a scalable proxy for TTS intelligibility overlooks nuanced linguistic phenomena prevalent in Chinese news media. This work contributes to the broader AI field by emphasizing that surface‑level correctness does not guarantee semantic or conventional accuracy, prompting researchers to reconsider evaluation benchmarks and diagnostic tools.

## Implications
For industry practitioners, relying solely on ASR-roundtrip may result in undetected reading errors that affect listener comprehension and brand perception. Practitioners should integrate additional audits such as span‑isolation diagnostics and model‑specific recovery checks to ensure robust TTS quality assurance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10606v1)
