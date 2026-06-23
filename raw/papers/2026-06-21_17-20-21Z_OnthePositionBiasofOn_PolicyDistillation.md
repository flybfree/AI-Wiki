---
title: On the Position Bias of On-Policy Distillation
published: 2026-06-21T17:20:21Z
authors: Yan Xie, Sijie Zhu, Tiansheng Wen, Bo Chen, Yifei Wang
url: http://arxiv.org/abs/2606.22600v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Position Bias of On-Policy Distillation

## Abstract
On-Policy Distillation (OPD) improves the learning efficiency of standard reinforcement learning through dense, token-level supervision from teachers. In the standard KL objective of OPD, token-level losses are uniformly averaged, implying equal weights for all tokens. However, we discover that not all tokens are created equal: as student rollouts grow longer, they deviate further from the teacher's distribution, leading to degraded supervision quality at later positions. As a result, OPD using only the first 30% of tokens can perform comparably to using all tokens, whereas OPD using only the last 30% of tokens barely learns anything. In this work, we provide a principled understanding of this issue through the lens of constrained optimization. Based on these insights, we derive Importance-Weighted On-Policy Distillation (IW-OPD), in which the weight assigned to each token depends on the accumulated discrepancy between the student's and teacher's distributions, naturally upweighting earlier tokens and downweighting later ones with larger deviations. We show that IW-OPD converges significantly faster than OPD, with better learning efficiency, and achieves better final performance than standard OPD in both same-size and cross-scale settings, improving performance up to 6.9 points on AIME-2025.

## Metadata
- **Published**: 2026-06-21T17:20:21Z
- **Authors**: Yan Xie, Sijie Zhu, Tiansheng Wen, Bo Chen, Yifei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.22600v1)