---
title: Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning
published: 2026-07-26T11:16:59Z
authors: Wenxuan Zhang, Yuhui Wang, Donggang Jia, Xiaoqian Shen, Jian Ding, Ivan Viola, Jürgen Schmidhuber, Mohamed Elhoseiny
url: http://arxiv.org/abs/2607.23605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning

## Abstract
Large Vision-Language Models (VLMs) now act as agents in interactive environments, where success requires coherent reasoning and decision-making across turns. Although end-to-end training in agentic environments can improve such multi-turn decision-making abilities, current methods mainly rely on either token-wise optimization over concatenated token trajectories or turn-wise optimization with uniform within-turn credit. In this work, we establish theoretical formulations for the two levels of optimization and derive a hybrid advantage that serves both objectives. Furthermore, with an appropriate choice of discount factor and learning target, we prove that a unified critic model can estimate values for both turn-wise and token-wise. As such, we propose HyGAE, an actor-critic framework that jointly optimizes token- and turn-level objectives with the hybrid advantage and unified critic. We conduct extensive evaluations of HyGAE across five multi-turn decision-making environments, where it achieves an average success rate of 91% and a significant improvement of 10% over other methods. Furthermore, we provide an in-depth analysis showing that the exact analytic form of the hybrid advantage and return is crucial for optimization. Project Page: https://wx-zhang.github.io/hygae-web/.

## Metadata
- **Published**: 2026-07-26T11:16:59Z
- **Authors**: Wenxuan Zhang, Yuhui Wang, Donggang Jia, Xiaoqian Shen, Jian Ding, Ivan Viola, Jürgen Schmidhuber, Mohamed Elhoseiny
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23605v1)