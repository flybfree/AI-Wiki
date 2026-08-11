---
title: Which Decisions Low-Bit Quantization Breaks, and How to Predict Them
url: http://arxiv.org/abs/2608.06564v2
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-06_20-22-21Z_WhichDecisionsLow_BitQuantizationBreaks_andHowtoPr.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how low-bit quantization (down to two bits) affects the binary decisions of large language models, especially tool calls and safety refusals. It finds that decision margins shrink in a proportional way rather than collapsing at fixed thresholds, causing specific tools to be abandoned while others remain unaffected. The study quantifies these changes across 16 models using three quantization methods from two to eight bits.

## Key Takeaways
- At three bits the model’s tool‑call decision collapses toward inaction while the choice of which tool remains unchanged, indicating a proportional margin loss rather than a binary switch.
- Quantization reduces the effective decision margin by a factor that drops sharply: 0.86 at four bits, 0.33 at three bits, and zero at two bits, showing damage scales with bit‑width.
- The fitted additive noise model cannot explain the observed damage; instead, per‑model margins measured directly are required to predict flip rates with high calibration.

## Context
Quantization is essential for deploying large language models on limited hardware, yet most prior work assumes a fixed amount of added noise. This assumption can mask how specific decision pathways degrade as bit‑width decreases, leading to safety and functionality regressions that are invisible in benchmark scores.

## Implications
Practitioners must treat low‑bit quantization not just as a performance trade‑off but as a risk to model reliability, especially for safety‑critical tool usage. The paper suggests that adding one more bit is the most cost‑effective fix, highlighting the need for fine‑grained margin monitoring in quantization pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06564v2)
