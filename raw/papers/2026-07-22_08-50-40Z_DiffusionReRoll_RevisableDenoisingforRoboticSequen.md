---
title: Diffusion ReRoll: Revisable Denoising for Robotic Sequential Prediction
published: 2026-07-22T08:50:40Z
authors: Seonsoo Kim, Seongil Hong, Jun-Gill Kang
url: http://arxiv.org/abs/2607.19919v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diffusion ReRoll: Revisable Denoising for Robotic Sequential Prediction

## Abstract
We propose Diffusion ReRoll, a diffusion-based framework for robotic sequential prediction that enables revisable denoising over horizons. Existing diffusion-based sequence predictors typically perform a single monotonic denoising process. In contrast, Diffusion ReRoll selectively re-noises regions that have become locally stable while the remaining regions continue denoising, so the re-noised regions can be refined again using context from the rest of the horizon. This structured re-noising enables iterative cross-horizon revision, allowing earlier and later segments to revise one another, while maintaining local consistency. We evaluate Diffusion ReRoll against full-sequence diffusion and causal denoising based on Diffusion Forcing across long-horizon planning, policy learning, and unified video-action modeling. On OGBench PointMaze and AntMaze, Diffusion ReRoll achieves relative gains in average success rate of 21% over Diffusion Forcing in matched guidance-based planning and 23% over Diffuser in matched goal-inpainting. In diffusion-policy-style action prediction, Diffusion ReRoll improves average success by 56.5% relative to Diffusion Policy across different prediction horizons and history lengths on the LIBERO-10 multi-task benchmark. In unified video-action prediction, Diffusion ReRoll improves policy and inverse dynamics performance, especially under out-of-distribution evaluation, and achieves the best action-video consistency. These results support structured re-noising as an effective mechanism for revisable robotic sequence generation.

## Metadata
- **Published**: 2026-07-22T08:50:40Z
- **Authors**: Seonsoo Kim, Seongil Hong, Jun-Gill Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19919v1)