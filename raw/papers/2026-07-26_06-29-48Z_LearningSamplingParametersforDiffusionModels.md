---
title: Learning Sampling Parameters for Diffusion Models
published: 2026-07-26T06:29:48Z
authors: Arisrei Lim, Yossi Gandelsman
url: http://arxiv.org/abs/2607.23488v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Sampling Parameters for Diffusion Models

## Abstract
Text-to-image diffusion models expose many inference-time sampling parameters, including prompts, negative prompts, classifier-free guidance scales, and noise schedules. These parameters are typically manually chosen once and then held fixed across prompts and denoising timesteps, even though different prompts and stages of generation can benefit from different parameter values. We introduce LeSAMP, a framework for learning prompt-conditioned, timestep-varying sampling parameters. We formulate parameter selection as a reinforcement learning problem: Given a user prompt, a large language model is trained to emit schedules for the chosen sampling parameters. We optimize our model using rewards from human preference models and VLM-as-a-judge. We evaluate our model on Flux.1 [dev] and Stable Diffusion 3.5, and find that compared to baselines, LeSAMP has a win rate of up to 68.12% using human preference scores and 73.37% using VLM-as-a-judge. These gains are validated in a user study where we achieve win rates of up to 59.46% over previous baselines. Our results suggest that learned sampling-parameter policies provide a complementary approach to existing post-training methods for improving diffusion model outputs.

## Metadata
- **Published**: 2026-07-26T06:29:48Z
- **Authors**: Arisrei Lim, Yossi Gandelsman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23488v1)