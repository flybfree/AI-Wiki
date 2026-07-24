---
title: GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries
url: http://arxiv.org/abs/2607.20757v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_22-14-23Z_GaugeQuant_OnlineLearningofQuantization_OptimalBas.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GaugeQuant, a method that learns quantization‑optimal bases during training by exploiting continuous symmetries of transformer outputs. By adding a LogSumExp term to the loss and using a stop‑gradient operator, it breaks these symmetries without changing the language modeling objective, resulting in lower perplexity compared with post‑training calibration methods.

## Key Takeaways
- The LogSumExp loss forces the model to select a basis that minimizes activation outliers while preserving the original LM objective. 
- Only rotation matrices are updated thanks to the stop‑gradient operator, leaving the rest of the network frozen and unchanged. 
- No external calibration data or quantization simulation is required; training overhead remains negligible.

## Context
Transformer models often exhibit continuous symmetries that affect downstream tasks such as quantization. Conventional post‑training quantization relies on freezing weights and calibrating with representative data, which can be costly and limited to specific hardware configurations. GaugeQuant addresses these bottlenecks by integrating symmetry breaking directly into the training loop.

## Implications
This approach enables more efficient inference with reduced perplexity across multiple quantization levels without sacrificing model flexibility. Practitioners can adopt it in production pipelines where online learning is feasible, offering a path toward scalable quantization that complements existing post‑training techniques.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20757v1)
