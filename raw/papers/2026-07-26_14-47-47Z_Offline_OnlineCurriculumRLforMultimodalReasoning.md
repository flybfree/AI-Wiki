---
title: Offline-Online Curriculum RL for Multimodal Reasoning
published: 2026-07-26T14:47:47Z
authors: Wendi Deng, Hang Du, Guoshun Nan, Haokun Tian, Jiaqi Yu, Xinlei Cao, Jaile Li, Jingfeng Chen, Ling Deng, Ting Li, Hao Yang, Jun Liu, Xudong Jiang, Sicong Leng
url: http://arxiv.org/abs/2607.23700v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Offline-Online Curriculum RL for Multimodal Reasoning

## Abstract
Multimodal large language models exhibit capabilities on reasoning tasks, yet often produce flawed intermediate steps while yielding correct final answers. This behavior undermines interpretability and reliability, suggesting reliance on spurious shortcuts rather than faithful reasoning. Although efforts have explored step-level supervision, distinguishing decisive steps from redundant ones remains challenging. We propose $O^2$-CritiCuRL, a novel curriculum reinforcement learning framework that introduces critical-step awareness through an iterative offline-online paradigm. In the offline stage, $O^2$-CritiCuRL conducts multi-rollout analysis over step-annotated trajectories to estimate step-level importance, allowing the framework to distill critical reasoning steps and filter out redundant ones. In the online stage, we employ a progressive step-level reinforcement learning strategy, where truncated chains guide the model to infer missing steps and refine its reasoning, thereby sharpening its focus on critical steps and overcoming the limitations of static supervision. Extensive experiments on multimodal reasoning benchmarks show that our method achieves state-of-the-art performance while delivering superior training and inference efficiency. Code is available at https://github.com/kk0013/CritiCuRL.

## Metadata
- **Published**: 2026-07-26T14:47:47Z
- **Authors**: Wendi Deng, Hang Du, Guoshun Nan, Haokun Tian, Jiaqi Yu, Xinlei Cao, Jaile Li, Jingfeng Chen, Ling Deng, Ting Li, Hao Yang, Jun Liu, Xudong Jiang, Sicong Leng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23700v1)