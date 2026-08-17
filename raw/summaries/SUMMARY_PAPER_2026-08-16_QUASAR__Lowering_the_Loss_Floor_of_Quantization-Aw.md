---
title: QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction
url: http://arxiv.org/abs/2608.13966v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_05-29-58Z_QUASAR_LoweringtheLossFloorofQuantization_AwareTra.md
generated_at: 2026-08-16 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
QUASAR addresses the problem that quantization-aware training often ends with a higher loss floor because it uses lossy reconstruction to compute gradients. The authors show that continuous, lightweight reconstruction lowers this error and improves low-bit model performance across Qwen3 and Llama‑3.1 at 2‑4 bits.

## Key Takeaways
- Continuous loss‑aware reconstruction in the training loop reduces the reconstruction‑dependent term that limits convergence, directly lowering the final quantized model’s loss.
- The method uses exponential moving averages of squared gradients to estimate saliency and solves an affine dequantizer via least squares each step without freezing the model.
- QUASAR achieves the lowest held‑out KL divergence among QAT baselines at 2‑4 bits, improving accuracy by 3.5‑4.3 points on eight tasks compared with strong QAT or PTQ.

## Context
Quantization is critical as inference moves to lower precision where standard post‑training quantization fails, and quantization‑aware training remains computationally expensive due to repeated heavy reconstructions. QUASAR’s approach makes this process tractable by embedding lightweight reconstruction within the normal forward pass.

## Implications
For practitioners deploying large language models at 2‑4 bits, QUASAR offers a practical way to retain high quality without extra inference overhead or model changes. This could accelerate adoption of low‑bit inference in edge devices and cloud services where latency and power are constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13966v1)
