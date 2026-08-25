---
title: Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning
published: 2026-08-22T07:17:14Z
authors: Qiqian Fu
url: http://arxiv.org/abs/2608.21811v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning

## Abstract
Reinforcement learning for vision-language math reasoning starves under sparse reward: on a pool of 20,830 visual-math problems where Qwen2-VL-2B answers 3.6% of rollouts correctly, 85-97% of GRPO rollout groups are entirely wrong and contribute zero gradient. We train eleven methods under identical conditions in this regime, each injecting a different prior: text (reference-solution hints), distribution (on-policy distillation from a 7B teacher), and value (a value-pretrained critic with an MSE or HL-Gauss categorical loss). A prior helps exactly when it is delivered: the six arms whose prior effectively reaches the policy separate with no overlap from the remaining five -- the no-prior baseline and four arms whose prior is teacher-capped, gated away, or lost to a mis-parameterized critic -- both on the pooled in-domain metric and on cross-domain transfer (DynaMath). The central finding, however, concerns evaluation: one slice of the in-domain pool -- long used as this project's general-distribution check -- anti-correlates with genuine cross-domain transfer (Spearman rho = -0.74, n = 11 arms, permutation p = 0.011), while the hardest in-domain slice predicts it closely (rho = +0.89, p < 0.001). We attribute the inversion to a near-chance multiple-choice subset that rewards models for not having changed; read through it, the best cross-domain method looked mediocre and the worst looked like the champion. Among the methods, hint-guided exploration -- not UFT's auxiliary loss -- drives hint gains, and replacing the critic's MSE loss with HL-Gauss cross-entropy is worth +14.4 points in-domain. All accuracies are blind-judged, with paired exact tests.

## Metadata
- **Published**: 2026-08-22T07:17:14Z
- **Authors**: Qiqian Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21811v1)