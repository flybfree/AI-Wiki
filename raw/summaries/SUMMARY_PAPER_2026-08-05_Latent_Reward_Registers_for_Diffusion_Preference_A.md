---
title: Latent Reward Registers for Diffusion Preference Alignment
url: http://arxiv.org/abs/2608.03929v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_17-00-52Z_LatentRewardRegistersforDiffusionPreferenceAlignme.md
generated_at: 2026-08-05 01:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Latent Reward Registers to estimate terminal preference directly from intermediate noisy latents in diffusion models, avoiding reliance on final outputs. It proposes a mechanism that prepends learnable register tokens to the input sequence of a frozen Diffusion Transformer, extracting latent reward evidence without changing hidden states or velocity fields. The approach enables two alignment strategies: Reward-Gradient On-Policy Distillation for training and Reward-Guided Sampling for inference.

## Key Takeaways
- Latent Reward Registers estimate terminal preference from intermediate noisy latents rather than final generated samples, solving the temporal credit‑assignment problem across multi‑step denoising.  
- The register mechanism uses position‑free learnable tokens that read out latent reward evidence while leaving the generator’s hidden states and velocity field unchanged, providing a dense differentiable signal throughout the process.  
- Reward‑Gradient On‑Policy Distillation (RG‑OPD) leverages this signal to train alignment updates without costly rollouts, achieving up to 33× fewer GPU hours compared with standard policy‑gradient baselines.

## Context
Diffusion preference alignment has traditionally depended on evaluating only the final output, which creates a bottleneck for aligning models with human judgments across many denoising steps. This limitation hampers efficient training and inference pipelines that require continuous feedback. The proposed latent reward registers address this by providing an internal signal that can be used throughout generation.

## Implications
For practitioners, Latent Reward Registers enable more scalable preference‑alignment training and sampling without expensive rollouts or parameter updates. In industry, the reduction in GPU usage and improved alignment metrics could accelerate deployment of high‑quality diffusion models while maintaining perceptual fidelity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03929v1)
