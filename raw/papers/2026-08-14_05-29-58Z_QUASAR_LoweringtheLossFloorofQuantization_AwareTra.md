---
title: QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction
published: 2026-08-14T05:29:58Z
authors: Vincent Counathe, Ben Athiwaratkun, Christopher De Sa, Tianyi Zhang
url: http://arxiv.org/abs/2608.13966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction

## Abstract
As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality. However, QAT computes the loss and surrogate gradients using a lossy reconstruction of latent full-precision weights, while applying updates to the latent weights themselves. This mismatch can lead to suboptimal training trajectories and a higher loss floor. Second-order PTQ methods mitigate a similar gap by minimizing loss-aware reconstruction error, but doing it once for a frozen model can take hours; repeating this process throughout QAT as the weights evolve is impractical. We introduce QUASAR, a QAT method that continuously performs lightweight, loss-aware reconstruction in the training loop to lower the loss floor and improve the resulting low-bit model. At each training step, QUASAR uses the exponential moving average of squared gradients as online saliency estimates, searches over a small set of clipping ranges, and fits affine dequantizers via saliency-weighted least squares. Our analysis shows that the loss-aware reconstruction error is the only reconstruction-dependent term in the QAT convergence bound and controls the loss of the final quantized model, establishing QUASAR's objective as a principled optimization target. QUASAR modifies only the training procedure and supports standard deployment formats, including integer quantization and NVFP4, with no inference-time changes or overhead. Across Qwen3 and Llama-3.1, QUASAR achieves the lowest held-out KL divergence among competitive QAT methods at 2, 3, and 4 bits, reducing KL by at least 10% at 3 and 4 bits and by 29% at 2 bits. At 2 bits, it improves average accuracy across eight tasks by 3.5-4.3 percentage points over strong QAT and PTQ baselines.

## Metadata
- **Published**: 2026-08-14T05:29:58Z
- **Authors**: Vincent Counathe, Ben Athiwaratkun, Christopher De Sa, Tianyi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13966v1)