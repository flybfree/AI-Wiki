---
title: Bigger or Cheaper? Scale and Quantization Effects on Uncertainty Signals in Vision-Language Models Under Image Degradation
url: http://arxiv.org/abs/2607.24440v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_13-47-44Z_BiggerorCheaper_ScaleandQuantizationEffectsonUncer.md
generated_at: 2026-07-27 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how model scale and 4‑bit quantization influence the internal uncertainty signals of vision‑language models when operating under image degradation. Across a large dataset, it finds that larger models provide stronger error‑detection performance while their verbalized confidence remains weak; conversely, quantizing a smaller full‑precision model yields better accuracy but poorer uncertainty signaling.

## Key Takeaways
- Scale improves the internal AUROC of mean token probability from 0.80 to 0.98, yet the model’s self‑reported confidence stays near chance (0.61–0.69).  
- 4‑bit quantization preserves accuracy with only a 1.6‑point loss but drops internal AUROC to 0.80 and reduces verbalized confidence parse rate from 99 % to 64 %.  
- For a fixed memory budget, the best configuration is a larger quantized model (7B‑4bit), which yields the highest accuracy and the strongest uncertainty signal.

## Context
Vision‑language models must balance computational constraints with reliable decision making under noisy inputs. The study highlights that confidence signals are not automatically aligned with internal error detection, a gap that affects real‑world deployment where users rely on model statements rather than raw metrics.

## Implications
Practitioners should prioritize larger quantized models over smaller full‑precision ones to maintain both performance and trustworthy uncertainty cues. This recommendation can guide resource allocation in edge AI systems where memory is limited but user confidence must be preserved.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24440v1)
