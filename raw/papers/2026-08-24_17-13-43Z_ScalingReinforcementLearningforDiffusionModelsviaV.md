---
title: Scaling Reinforcement Learning for Diffusion Models via Velocity Matching
published: 2026-08-24T17:13:43Z
authors: Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, Yongxin Chen
url: http://arxiv.org/abs/2608.23664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Reinforcement Learning for Diffusion Models via Velocity Matching

## Abstract
Reward fine-tuning is becoming an important tool for adapting diffusion models to human preferences and task-specific objectives, but existing methods largely inherit policy-gradient machinery from large language models. Unlike autoregressive models, diffusion models do not provide tractable likelihoods for generated samples. As a result, current approaches either construct trajectory likelihoods from stochastic denoising transitions or approximate endpoint likelihoods with evidence lower bound, introducing additional computation and algorithmic complexity. We demonstrate that this likelihood-based machinery is not necessary for effective diffusion reward fine-tuning. We propose reward-based velocity matching (RVM), a simple trajectory-free update that acts directly on the velocity field. RVM reinforces directions associated with high-reward generations, suppresses those with low reward, and involves an optional anchor term controlling drift from a reference velocity. Notably, it provides a general framework that recovers recent fine-tuning methods, including RAM and DiffusionNFT, as special cases. Across various large-scale diffusion models reward fine-tuning tasks, RVM is competitive with or outperforms trajectory-based policy-gradient methods under substantially reduced training cost. We further find that, once the velocity update is simplified, the particular loss variant matters less than reward and anchor design. For video generation, standard preference rewards can favor visually clean but nearly static outputs; introducing a new dynamic-tracking reward that substantially improve motions while improving overall VBench performance. These results suggest that scalable reward fine-tuning for diffusion models is better posed in the native velocity representation than as likelihood-based policy optimization.

## Metadata
- **Published**: 2026-08-24T17:13:43Z
- **Authors**: Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, Yongxin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23664v1)