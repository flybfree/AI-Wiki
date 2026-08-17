---
title: QuaSAR: Quantization Compensation via Stable Activation-Aware Rank Truncation
url: http://arxiv.org/abs/2608.14149v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_10-00-36Z_QuaSAR_QuantizationCompensationviaStableActivation.md
generated_at: 2026-08-16 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a parameter‑free truncated pseudoinverse solver that stabilizes the closed‑form residual compensation used in training‑free post‑training quantization. The method prevents misclassification of poorly predictable layers caused by rank‑deficient Gram matrices, enabling higher accuracy under low‑bit W4A4 settings. On ViT‑B it reaches 81.42 % top‑1 accuracy while maintaining a compact model size.

## Key Takeaways
- Rank‑deficient input activations create singular or ill‑conditioned Gram matrices that make the existing goodness‑of‑fit solver unstable, leading to spuriously negative fit scores and unnecessary layer discarding.
- The proposed truncated pseudoinverse removes collapsed directions before inversion, providing a numerically stable compensation even when the original solver fails.
- The approach yields 81.42 % top‑1 accuracy on ViT‑B with W4A4 quantization, outperforming prior post‑training methods and fine‑tuning baselines.

## Context
Training‑free quantization aims to compress deep neural networks without retraining, balancing storage reduction against performance loss. Recent work relies on closed‑form residual compensation but often discards layers that cause numerical issues, limiting the achievable trade‑off between size and accuracy.

## Implications
Stable low‑bit inference is crucial for edge deployment where both memory and compute are constrained. By eliminating solver failures, this method makes quantization more robust, enabling higher accuracy at lower model sizes without additional fine‑tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14149v1)
