---
title: xPress: Parallel Refinement for Diffusion Drafters in Speculative Decoding
url: http://arxiv.org/abs/2608.02438v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_16-18-22Z_xPress_ParallelRefinementforDiffusionDraftersinSpe.md
generated_at: 2026-08-03 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces xPress, a lightweight causal refiner for block-diffusion drafters that restores token dependencies without sequential loops. On Qwen3-8B across multiple benchmarks it improves acceptance length by ~30% and decoding throughput by up to 1.7x.

## Key Takeaways
- The original dFlash draft uses independent marginals per position, causing early rejection due to lack of joint probability.
- xPress reconcilies the whole diffusion block in parallel, propagating causal dependencies across tokens simultaneously.
- This leads to higher acceptance length and faster end-to-end decoding compared to baseline.

## Context
Block-diffusion models generate drafts efficiently but suffer from incoherent token generation because each token is sampled independently. Restoring causality is a known challenge that limits the practical use of speculative decoding in long sequences.

## Implications
The improvement enables longer, more coherent outputs for applications like code and math generation where sequence length matters. Practitioners can adopt xPress to boost model throughput without sacrificing quality, accelerating deployment in real-time systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02438v1)
