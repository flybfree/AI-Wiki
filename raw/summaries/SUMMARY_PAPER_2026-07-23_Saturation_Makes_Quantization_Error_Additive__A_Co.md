---
title: Saturation Makes Quantization Error Additive: A Coverage Model with a Certificate
url: http://arxiv.org/abs/2607.12266v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-14_02-08-33Z_SaturationMakesQuantizationErrorAdditive_ACoverage.md
generated_at: 2026-07-23 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how quantization error behaves when different layers are quantized to low precision, showing that the loss change can be modeled as an additive function of per‑layer contributions. It finds that most variance in loss is explained by individual layer effects and proposes a coverage model that captures this structure with few parameters.

## Key Takeaways
- 85–93 % of the variance of the loss from quantizing a set of layers comes from per‑layer effects alone, indicating that pairwise or global sensitivities capture only a small fraction.  
- A monotone transformation of a sum of per‑layer terms reproduces the ranking of configurations with at most 2 % misordering, showing additive models are nearly optimal for ordering.  
- The coverage model f(S)=c(1−∏_{i∈S}(1−a_i)) matches the measured variance profile to within a few percent and its mean‑squared error equals the unexplained variance, providing a certificate of performance.

## Context
Mixed‑precision quantization is essential for deploying large language models on limited hardware. Current sensitivity‑based methods assume that per‑layer sensitivities are sufficient to predict loss, but this assumption breaks down at 4‑bit precision where memory constraints force aggressive allocation decisions.

## Implications
The additive model offers a simpler and more accurate predictor than sensitivity‑based approaches, reducing KL divergence in resource allocation across models of varying size. Practitioners can rely on this coverage framework to allocate bits where they matter most, improving both code generation and reasoning performance at low bit depths.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.12266v1)
