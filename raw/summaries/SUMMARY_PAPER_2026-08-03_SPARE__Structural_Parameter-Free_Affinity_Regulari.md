---
title: SPARE: Structural Parameter-Free Affinity Regularization for Flow Matching
url: http://arxiv.org/abs/2608.01990v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_09-50-51Z_SPARE_StructuralParameter_FreeAffinityRegularizati.md
generated_at: 2026-08-03 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SPARE, a parameter‑free regularizer that aligns the pairwise affinities of tokens in diffusion transformer latent spaces without using external encoders or projection heads. It matches token similarity across images and recovers REPA’s FID reduction while adding only 0.08 GB memory overhead.

## Key Takeaways
- SPARE eliminates the need for an encoder and a learnable head, relying solely on the intrinsic similarity between tokens as a scalar affinity metric.
- The regularizer extends token‑pair matching to cross‑image pairs, addressing the limitation of prior target‑free methods that only repel within a single image.
- On ImageNet 256×256 with SiT backbones SPARE achieves the lowest FID among parameter‑free regularizers and improves REPA’s performance by 37–54 % in FID reduction.

## Context
Diffusion transformer models benefit from internal representation regularization to speed convergence, yet most methods either require costly external encoders or discard data‑driven structure. SPARE demonstrates that latent token affinities can serve as a direct target, offering a lightweight alternative that preserves the model’s ability to learn spatial structure.

## Implications
For practitioners seeking faster training without extra hardware costs, SPARE provides a scalable solution that integrates seamlessly into existing pipelines. Its success suggests that exploiting fine‑grained relational patterns in data can replace expensive external supervision, influencing future research on efficient diffusion regularization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01990v1)
