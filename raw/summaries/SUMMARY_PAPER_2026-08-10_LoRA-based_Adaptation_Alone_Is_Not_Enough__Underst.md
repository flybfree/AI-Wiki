---
title: LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection
url: http://arxiv.org/abs/2608.09633v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_14-13-23Z_LoRA_basedAdaptationAloneIsNotEnough_Understanding.md
generated_at: 2026-08-10 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates why LoRA-based adaptation alone is insufficient for face presentation attack detection across datasets, showing that zero‑shot prompting yields performance close to random while LoRA fine‑tuning improves only within‑dataset ACER to below 2% and cross‑dataset ACER rises. It evaluates 32 foundation models with various architectures.

## Key Takeaways  
- Zero‑shot prompting on FMs produces performance close to random across all model families, indicating that the base model’s representation dominates.  
- LoRA adaptations with under one percent trainable weights achieve sub‑2% intra‑dataset ACER but cross‑dataset ACER is much higher, revealing limited generalization.  
- The study finds that pretrained representations and adaptation datasets matter more than lightweight LoRA fine‑tuning for cross‑dataset performance.

## Context  
Foundation models are widely used as zero‑shot detectors in security tasks, yet their utility varies with dataset characteristics. This work highlights a gap between intra‑dataset adaptation and real‑world deployment where diverse conditions appear.

## Implications  
Practitioners should consider larger adaptation datasets or alternative fine‑tuning strategies rather than relying solely on low‑rank LoRA for robust PAD systems. The findings encourage more holistic evaluation of foundation model adaptability beyond single‑dataset benchmarks. Future research should explore hybrid approaches that combine LoRA with richer adaptation data to improve cross‑dataset robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09633v1)
