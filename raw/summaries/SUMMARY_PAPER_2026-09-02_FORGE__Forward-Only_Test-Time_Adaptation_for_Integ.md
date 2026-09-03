---
title: FORGE: Forward-Only Test-Time Adaptation for Integer-Only Vision Models on Microcontrollers
url: http://arxiv.org/abs/2609.01683v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_13-59-28Z_FORGE_Forward_OnlyTest_TimeAdaptationforInteger_On.md
generated_at: 2026-09-02 20:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FORGE, a forward‑only test‑time adaptation method that works on integer‑only convolutional networks deployed to microcontrollers. By re‑normalizing each folded convolution’s per‑channel output using only forward‑pass estimates, FORGE restores the benefits of gradient‑based TENT while staying compatible with the inference‑only runtime. Experiments show a 20.9‑point accuracy gain versus standard adaptation and match BN‑free forward‑only methods, all on a real ESP32‑S3.

## Key Takeaways
- FORGE recovers most of TENT’s accuracy improvement (+20.9 points) while operating only with forward passes and integer convolutions that have been fused to remove batch normalization.  
- The method adapts just three out of twenty‑one layers, selected without knowledge of test corruptions, achieving 93% of the benefit and surviving single‑sample streaming via a batch‑size‑scaled momentum.  
- On an ESP32‑S3, forward‑only adaptation adds only 8.3 mJ (6.8 % of inference energy) and takes 21.9 ms, demonstrating that recalibration is cheap on microcontrollers.

## Context
Vision models for edge devices are often quantized to integer arithmetic, eliminating the need for backpropagation during deployment. Traditional test‑time adaptation relies on gradient updates or batch normalization, both of which cannot be used in a pure inference pipeline. This creates a gap between server‑side training and real‑world microcontroller execution.

## Implications
FORGE shows that adaptive inference can be achieved without sacrificing the integer‑only constraints, opening the door to continuous improvement of deployed models on resource‑constrained hardware. Practitioners can integrate lightweight recalibration into existing MCU pipelines, reducing power impact while maintaining high accuracy across diverse sensor conditions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01683v1)
