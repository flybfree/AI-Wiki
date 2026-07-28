---
title: Learning Sampling Parameters for Diffusion Models
url: http://arxiv.org/abs/2607.23488v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_06-29-48Z_LearningSamplingParametersforDiffusionModels.md
generated_at: 2026-07-27 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes LeSAMP, a framework that learns prompt‑conditioned and timestep‑varying sampling parameters for text‑to‑image diffusion models instead of fixing them manually. By treating parameter selection as a reinforcement learning task the authors train a model to emit schedules using rewards from human preference scores and a vision language model judge. On Flux.1 and Stable Diffusion 3.5 LeSAMP outperforms baselines with win rates up to 68.12% (human) and 73.37% (VLM), validated by user studies showing gains of about 59.46%.

## Key Takeaways
- The framework treats sampling‑parameter selection as a reinforcement learning problem where the model learns schedules from prompts using rewards from human preference models and VLM‑as‑a‑judge.
- Human preference scores provide up to a 68.12% win rate improvement over previous baselines, indicating strong alignment with user taste.
- The approach yields a 73.37% win rate when judged by a vision language model judge, demonstrating robust performance across different evaluation methods.

## Context
Diffusion models rely heavily on inference‑time parameters that are often set once and never adapted to the specific prompt or denoising stage. Manual tuning limits personalization, while existing post‑training methods do not address dynamic parameter optimization. LeSAMP bridges this gap by learning policies that adjust guidance scales, noise schedules, and negative prompts in real time.

## Implications
For practitioners, LeSAMP offers a scalable way to improve diffusion outputs without retraining the model, reducing reliance on trial‑and‑error tuning. In industry, integrating such learned policies could enable more consistent user experiences across diverse content, potentially boosting adoption of generative AI tools. The method also highlights the value of reinforcement learning and preference modeling in shaping multimodal generation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23488v1)
