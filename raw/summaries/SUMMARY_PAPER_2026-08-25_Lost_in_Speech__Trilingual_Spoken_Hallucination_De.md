---
title: Lost in Speech: Trilingual Spoken Hallucination Detection Across Audio and Transcripts
url: http://arxiv.org/abs/2608.24707v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_15-24-48Z_LostinSpeech_TrilingualSpokenHallucinationDetectio.md
generated_at: 2026-08-25 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a multilingual benchmark for detecting hallucinations in spoken news content across English, Russian, and Kazakh. It compares transcript‑based detection with direct audio processing and shows that synthetic‑trained detectors transfer well to real fakes.

## Key Takeaways
- The benchmark includes 12,013 news samples with controlled hallucinations of three types and severity levels across three languages, providing a comprehensive resource for evaluating spoken hallucination detection.  
- Transcript‑based detection outperforms direct audio processing, but binary‑task degradation is observed in strong encoders that track per‑language ASR error.  
- Synthetic‑trained detectors achieve macro‑F1 scores of 0.82–0.88 on original text and Russian provenance analysis uncovers both veracity‑related signals and model‑dependent machine‑style artifacts.

## Context
Spoken hallucination detection remains a niche area compared to its text counterpart, limiting research in low‑resource languages where ASR systems are less reliable. This work fills that gap by providing a multilingual dataset that can be used for both synthetic training and real‑world evaluation.

## Implications
For practitioners developing news verification tools, the findings suggest prioritizing transcript pipelines over raw audio when hallucination risk is high. The identified confounders also guide future benchmark design to isolate veracity from model artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24707v1)
