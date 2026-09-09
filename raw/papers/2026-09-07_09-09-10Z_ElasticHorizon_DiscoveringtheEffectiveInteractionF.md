---
title: Elastic Horizon: Discovering the Effective Interaction Frontier in Agentic Reinforcement Learning
published: 2026-09-07T09:09:10Z
authors: Gangyi Zhang, Junjie Meng, Letian Zhang, Wei Wu, Yang Zheng, Dong Wang, Yang Liu, Guanjun Jiang, Chongming Gao
url: http://arxiv.org/abs/2609.07247v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Elastic Horizon: Discovering the Effective Interaction Frontier in Agentic Reinforcement Learning

## Abstract
Scaling the interaction horizon-the maximum number of environment interactions per episode-improves LLM agents on long-horizon tasks, and curriculum-based methods that progressively expand the horizon outperform fixed-horizon alternatives. However, existing schedules are open-loop: they monotonically increase the horizon until a manually specified maximum, with no mechanism to detect when further expansion stops helping. We propose the effective interaction frontier hypothesis: a dynamic boundary beyond which additional interactions yield diminishing returns while cost grows linearly. We then introduce Elastic Horizon, a closed-loop controller that tracks this boundary via the 90th percentile of successful trajectory lengths. On AppWorld and BFCL, fixed-horizon sweeps reveal clear saturation plateaus; Elastic Horizon stabilizes the horizon inside the saturation band from both under- and over-capacity initializations, attains the best success rates across 7B and 14B backbones, and saves up to 25% of per-step trajectory tokens. Our work shifts the paradigm from how to scale interaction horizons to when to stop scaling.

## Metadata
- **Published**: 2026-09-07T09:09:10Z
- **Authors**: Gangyi Zhang, Junjie Meng, Letian Zhang, Wei Wu, Yang Zheng, Dong Wang, Yang Liu, Guanjun Jiang, Chongming Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07247v1)