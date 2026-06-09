---
title: GRIP-VLM: Group-Relative Importance Pruning for Efficient Vision-Language Models
published: 2026-05-13T11:32:03Z
authors: Mingzhe Huang, Weijun Wang, Xin Ding, Liang Mi, Hao Wen, Yuanchun Li, Lichen Pang, Shansong Yang, Yunxin Liu, Ting Cao
url: http://arxiv.org/abs/2605.13375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GRIP-VLM: Group-Relative Importance Pruning for Efficient Vision-Language Models

## Abstract
In Vision-Language Models (VLMs), processing a massive number of visual tokens incurs prohibitive computational overhead. While recent training-aware pruning methods attempt to selectively discard redundant tokens, they largely rely on continuous-gradient relaxations. However, visual token pruning is inherently a discrete, non-convex combinatorial problem; consequently, these continuous approximations frequently trap the optimization in sub-optimal local minima, especially under aggressive compression budgets. To overcome this fundamental bottleneck, we propose GRIP-VLM, a Group-Relative Importance Pruning framework driven by Reinforcement Learning. Rather than relying on smooth-gradient assumptions, GRIP-VLM formulates pruning as a Markov Decision Process, employing a Group Relative Policy Optimization (GRPO) paradigm anchored by supervised warm-up to directly explore the discrete selection space. Integrated with a budget-aware scorer, our lightweight agent dynamically evaluates per-token importance and adapts to arbitrary compression ratios without retraining. Extensive experiments across diverse multimodal benchmarks demonstrate that GRIP-VLM consistently outperforms heuristic and supervised-learning baselines, achieving a superior Pareto frontier and delivering up to a 15\% inference speedup at equal accuracy.

## Metadata
- **Published**: 2026-05-13T11:32:03Z
- **Authors**: Mingzhe Huang, Weijun Wang, Xin Ding, Liang Mi, Hao Wen, Yuanchun Li, Lichen Pang, Shansong Yang, Yunxin Liu, Ting Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.13375v1)