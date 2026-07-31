---
title: A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models
url: http://arxiv.org/abs/2607.27910v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_09-24-27Z_ACross_ArchitectureAuditofDirection_BasedInference.md
generated_at: 2026-07-30 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates five direction‑based inference‑time defenses against jailbreaks in vision‑language models across diverse architectures. The study finds that no single defense excels on both recovery and utility, with the image conditioning shift performing best for LLaVA 1.5 and Pixtral 12B while the prompt instruction works well for Qwen2.5 VL.

## Key Takeaways
- The image conditioning shift leads on LLaVA 1.5 and Pixtral 12B and shows utility loss at measurement noise level, indicating strong effectiveness without harming performance.
- Prompt instructions to ignore the image succeed as refusals in Qwen2.5 VL, highlighting that textual cues can also guide defenses.
- The CMRM direction aligns positively with the image conditioning shift across all cells (mean cosine 0.35), suggesting shared geometry but limited transferability between architectures.

## Context
Defences that modify model outputs at inference time are a growing concern as jailbreak attacks become more sophisticated. Understanding which techniques work where is essential for building robust multimodal systems that balance safety and functionality.

## Implications
Practitioners must treat direction‑based defenses as architecture‑specific rather than one‑size‑fits‑all solutions, allocating resources to calibrate each family of language decoders separately. This insight can guide more targeted research into unified yet adaptable safety mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27910v1)
