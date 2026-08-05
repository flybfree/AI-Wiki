---
title: Quantization Effects on Biomedical LLM Reliability
url: http://arxiv.org/abs/2608.03854v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_15-57-21Z_QuantizationEffectsonBiomedicalLLMReliability.md
generated_at: 2026-08-05 01:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates three Mistral‑7B variants (Base, BioMistral, Instruct) on PubMed RCT sentence classification using FP16, INT8, and INT4 quantization under four answer‑text prompt templates. The study shows that the probability extraction protocol—specifically whether summed or mean token log‑likelihood scoring is used—dominates apparent calibration, with accuracy changes varying from less than one percentage point for specialized models to up to six points for the base model.

## Key Takeaways
- Switching from summed to mean token log‑likelihood scoring reverses the calibration ranking between BioMistral and Instruct: BioMistral’s average expected calibration error rises from 0.097 to 0.289, while Instruct drops from 0.237 to 0.096.  
- Prompt template choice produces accuracy differences of 7–24 percentage points, comparable or larger than model‑level effects.  
- INT8 quantization changes accuracy and F1 by only 1–2 percentage points for BioMistral and Instruct but can increase the base model’s performance by up to +4.2 percentage points on some templates; INT4 yields heterogeneous but non‑catastrophic effects. Temperature scaling reduces expected calibration error under summed scoring for both models, but only when that scoring rule is used.

## Context
The results highlight that experimental design choices such as scoring rules and prompt templates have outsized influence on the reliability of decoder language models in medical classification tasks. This matters because current benchmarks often ignore these factors, leading to misleading comparisons between model variants.

## Implications
For practitioners deploying LLMs in healthcare applications, selecting appropriate prompt templates and normalization methods is essential to ensure calibrated outputs; otherwise apparent improvements may be artifacts rather than genuine gains. The study underscores the need for systematic evaluation protocols that treat these experimental variables as first‑order considerations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03854v1)
