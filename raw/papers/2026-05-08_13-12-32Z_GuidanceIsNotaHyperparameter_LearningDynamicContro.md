---
title: 'Guidance Is Not a Hyperparameter: Learning Dynamic Control in Diffusion Language Models'
published: 2026-05-08T13:12:32Z
authors: Fan Zhou, Tim Van de Cruys
url: http://arxiv.org/abs/2605.07701v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Guidance Is Not a Hyperparameter: Learning Dynamic Control in Diffusion Language Models

## Abstract
Classifier-Free Guidance (CFG) is a widely used mechanism for controlling diffusion-based generative models, yet its guidance scale is typically treated as a fixed hyperparameter throughout generation. This static design yields a suboptimal controllability and quality tradeoff, as the optimal degree of guidance varies across tasks and across different stages of the diffusion process, especially in NLP domain. We recast CFG scale selection as a sequential decision-making problem and propose to learn dynamic guidance trajectories via reinforcement learning. Specifically, we model the guidance scale as a discrete control action selected at each generation step based on the evolving diffusion state, and optimize a policy using Proximal Policy Optimization (PPO) under task-level rewards. Experiments on three controlled NLP generation tasks using discrete diffusion language models demonstrate that adaptive guidance consistently achieves a better balance between controllability and generation quality than fixed-scale strategies. Further analysis of the learned policies reveals distinct and interpretable guidance trajectories across tasks, underscoring the importance of treating guidance as a dynamic control process rather than a static design choice.

## Metadata
- **Published**: 2026-05-08T13:12:32Z
- **Authors**: Fan Zhou, Tim Van de Cruys
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.07701v1)