---
title: Quantization Damage Is Multiplicative, Not Additive
url: http://arxiv.org/abs/2608.06564v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_20-22-21Z_QuantizationDamageIsMultiplicative_NotAdditive.md
generated_at: 2026-08-09 22:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how quantization affects the confidence margins of large language model decisions, showing that damage is multiplicative rather than additive. The authors measure decision margins across many models and bit-widths and find that quantization multiplies these margins by a factor that drops sharply with fewer bits. This contraction leads to specific failures in tool‑calling and safety refusals without changing benchmark scores.

## Key Takeaways
- Quantization does not add constant noise; instead it scales the margin of each decision, causing it to shrink multiplicatively which reduces model confidence.
- The shrinkage is severe at low bit-widths: median margins drop to 0.86 at four bits and near zero at two bits, leading to tool‑call failures while tool selection remains unchanged.
- Statistical comparison shows additive‑noise models cannot explain the observed damage; the fitted multiplicative relation predicts flip probabilities with high calibration accuracy.

## Context
Quantization is essential for deploying large language models on limited hardware, yet prior assumptions treat quantization as a simple noise addition that does not affect model logic. This study reveals that the internal decision margins are vulnerable, suggesting that safety and reliability cannot be assumed to remain intact under aggressive compression.

## Implications
For practitioners, this means that adding more bits is often the most cost‑effective way to preserve decision quality. It also highlights a need for new evaluation metrics that capture margin preservation rather than only benchmark scores.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06564v1)
