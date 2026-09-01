---
title: Training-Free Hidden-State Refinement for Flow-Matching Image Generators
published: 2026-08-29T09:17:02Z
authors: Yuanyi Yan, Xinzhe Rao, Canyu Shen, Yang Chen, Yunlu Chen, Meng Tang, Teng Long, Vincent Tao Hu
url: http://arxiv.org/abs/2608.29160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training-Free Hidden-State Refinement for Flow-Matching Image Generators

## Abstract
We aim to improve frozen flow-matching image generators by adding inference computation inside the denoiser, without changing model weights or the outer sampler. Existing generators usually spend extra test-time computation by increasing the number of sampling steps, which repeatedly evaluates the entire denoiser and couples quality gains to sampler cost. A key challenge is how to use extra computation inside a frozen transformer denoiser: the method must decide which tokens, layers, and sampling times receive repeated updates while preserving the original generation pipeline. We introduce a training-free looping framework that repeatedly applies selected transformer layers inside each denoising call. Dense and Sparse Token Loop vary the token scope; Sampling-Progress Gating and the loop layer range specify when and where looping is active; loop count and strength control the repeated updates; and Loop Guidance combines ordinary and looped vector-field predictions. Across two Scale-RAE model scales, loop variants improve primary and auxiliary quality metrics with competitive quality--efficiency trade-offs. Loop Guidance further improves both primary metrics across all three tested models; on Scale-RAE DiT2.4B, it raises GenEval from 0.4471 to 0.5691 and DPG-Bench from 0.7656 to 0.8053. Code will be released.

## Metadata
- **Published**: 2026-08-29T09:17:02Z
- **Authors**: Yuanyi Yan, Xinzhe Rao, Canyu Shen, Yang Chen, Yunlu Chen, Meng Tang, Teng Long, Vincent Tao Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29160v1)