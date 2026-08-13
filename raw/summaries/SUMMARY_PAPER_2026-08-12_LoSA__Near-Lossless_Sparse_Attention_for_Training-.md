---
title: LoSA: Near-Lossless Sparse Attention for Training-Free Video Diffusion Acceleration
url: http://arxiv.org/abs/2608.12032v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_13-13-56Z_LoSA_Near_LosslessSparseAttentionforTraining_FreeV.md
generated_at: 2026-08-12 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
LoSA introduces a training‑free sparse attention method that preserves near‑lossless fidelity of video diffusion transformers while cutting computational cost. By fixing a retained attention mass threshold at 99 % and reusing frozen block indices across denoising steps, LoSA achieves up to a 3.2× speedup on HunyuanVideo with only a negligible 0.02‑point VBench drop.

## Key Takeaways
- LoSA fixes a retained‑mass threshold of 99 % rather than a sparsity ratio, ensuring that the majority of attention mass is kept while still allowing removal of roughly 40 % of block interactions.
- The method reuses frozen block indices for all denoising steps after determining the minimal key/value set per head and query block that meets the threshold, eliminating recomputation.
- On Wan2.1‑1.3B models LoSA provides a 1.36× speedup with a 0.06‑point VBench Overall drop, and when combined with feature caching it yields a 3.2× speedup on HunyuanVideo at only 0.02 points.

## Context
Video diffusion transformers dominate training‑free video generation because they process long 3D token sequences with quadratic self‑attention cost. Existing sparse attention techniques often sacrifice accuracy for speed, making them impractical for high‑resolution or long videos. LoSA’s near‑lossless approach addresses this gap by maintaining fidelity while dramatically reducing compute.

## Implications
For practitioners developing video diffusion models, LoSA offers a practical path to faster inference without retraining, lowering latency and hardware costs. The method’s compatibility with existing pipelines means it can be adopted immediately across diverse video generation systems, accelerating deployment in real‑time applications such as content creation and editing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12032v1)
