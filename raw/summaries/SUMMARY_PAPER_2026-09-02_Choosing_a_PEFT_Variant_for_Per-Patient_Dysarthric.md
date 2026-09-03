---
title: Choosing a PEFT Variant for Per-Patient Dysarthric ASR: A Single-Speaker Case Study on Two ASR Bases
url: http://arxiv.org/abs/2609.02735v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_15-42-48Z_ChoosingaPEFTVariantforPer_PatientDysarthricASR_AS.md
generated_at: 2026-09-02 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper compares seven parameter‑efficient fine‑tuning (PEFT) variants within the LoRA family on a single post‑stroke Hungarian speaker using two production ASR checkpoints. It finds that attention‑projection adapters raise CER, while the simplest LoRA method is preferred for its cost and storage efficiency.

## Key Takeaways
- Attention‑projection adapters substantially improve CER on both Whisper‑large‑v3 (Hungarian fine‑tuning) and Qwen3‑ASR‑1.7B, reducing errors by roughly 14 pp.
- Real 4‑bit QLoRA yields higher CER than LoRA despite claiming memory savings, with no actual reduction in storage at the model scale.
- A lightweight 115 MB LoRA that also adapts feed‑forward blocks reaches within 0.66 percentage points of full fine‑tuning while using only about 3.7 % of the per‑patient storage.

## Context
The study addresses a growing need for patient‑specific ASR solutions where memory and compute resources are limited, especially in clinical settings with severe dysarthria. It highlights how PEFT strategies can balance accuracy and deployment cost without full model retraining.

## Implications
For researchers, the findings guide the selection of lightweight adapters that preserve performance while minimizing storage overhead. For industry practitioners, they suggest adopting simple LoRA variants for per‑patient deployments, reserving more complex methods for research or high‑resource environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02735v1)
