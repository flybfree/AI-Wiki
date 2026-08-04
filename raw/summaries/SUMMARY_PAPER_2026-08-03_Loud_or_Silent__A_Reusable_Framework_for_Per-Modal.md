---
title: Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis in Multimodal Clinical AI
url: http://arxiv.org/abs/2608.01462v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_19-38-56Z_LoudorSilent_AReusableFrameworkforPer_ModalityFail.md
generated_at: 2026-08-03 23:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PRIMED‑AI, a model‑agnostic framework that analyses how dropping individual modalities affects multimodal clinical AI performance. It distinguishes between failures that are loud (large accuracy drop) and silent (small drop), providing per‑example and per‑modality failure taxonomies. On EchoJEPA and HuBERT‑ECG models, the framework correctly identifies echo as the dominant modality and shows its absence nearly doubles error.

## Key Takeaways
- The framework returns a per‑example failure taxonomy that pinpoints which modality caused an error.
- It produces a per‑modality complementarity matrix showing how modalities jointly support predictions.
- Loud vs silent dropout rates are computed using only deployment‑observable signals, revealing echo’s critical role when missing.

## Context
Multimodal clinical AI systems often rely on multiple data streams such as imaging and ECG. When one modality is unavailable in real‑world settings, the impact on model performance can be severe yet difficult to diagnose. This work provides a systematic method to quantify that impact without relying on post‑hoc attribution methods.

## Implications
Practitioners can now monitor which modalities are essential for their models and prepare fallback strategies when data gaps occur. The framework scales to three modalities, making it applicable across diverse clinical pipelines and supporting more robust deployment of AI in healthcare.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01462v1)
