---
title: Activation Denoising: A Robustness View on Parallel vs Sequential LLM Quantization
url: http://arxiv.org/abs/2610.07522v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_23-41-48Z_ActivationDenoising_ARobustnessViewonParallelvsSeq.md
generated_at: 2026-10-06 21:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper studies post-training quantization for large language models and argues that parallel quantization is efficient but vulnerable to compounding errors through residual streams. It proposes activation denoising, a robustness-based regularization that models upstream quantization error as noise and makes each layer robust to it while preserving a fully parallel quantization schedule. The method recovers much of the accuracy benefit of sequential quantization without its serial bottleneck.

## Key Takeaways
- Parallel quantization is scalable because every layer can be calibrated independently, but it leaves residual-stream errors uncorrected: each layer sees inputs distorted by earlier quantization, and those distortions accumulate across depth.
- Sequential quantization improves accuracy by recalibrating each layer on outputs already affected by previous quantized layers, but it imposes a serial dependency that limits throughput and becomes costly for large models.
- Activation denoising reframes the problem as robustness: a preprocessing step and metric-weighted rounding regularize layers against upstream noise, creating a depth-compounding smoothness penalty that dampens error amplification. Combined with general linear weight transformations, it is complementary to orthogonal rotations and can improve accuracy in a single parallel pass.

## Context
Post-training quantization is central to deploying large language models efficiently, but current methods face a tradeoff between parallel scalability and error-aware calibration. This paper matters because it connects quantization error propagation to robustness and regularization, offering a principled way to bridge accuracy and efficiency in large-scale model compression.

## Implications
For practitioners, the approach suggests that quantization pipelines can achieve near-sequential accuracy without serial layer-by-layer calibration, reducing compression time and enabling more scalable deployment. For the field, it reframes quantization as a robustness problem, potentially guiding future methods that combine error modeling, regularization, and linear transformations to make LLM compression faster and more reliable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07522v1)
