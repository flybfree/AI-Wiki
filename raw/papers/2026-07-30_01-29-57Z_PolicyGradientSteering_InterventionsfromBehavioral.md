---
title: Policy Gradient Steering: Interventions from Behavioral Objectives
published: 2026-07-30T01:29:57Z
authors: Yoann Poupart, Aurélie Beynier, Nicolas Maudet
url: http://arxiv.org/abs/2607.27574v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Policy Gradient Steering: Interventions from Behavioral Objectives

## Abstract
Activation steering has emerged in large language models as a lightweight alternative for dynamically changing a model's behavior at inference time. However, we show that existing steering methods fail to steer even a simple policy in a two-route gridworld environment. To address this limitation, we propose Policy Gradient Steering (PGS), which formulates steering as a reinforcement learning problem. PGS accumulates gradients of a temporary behavioral objective over a small set of rollouts or demonstrations to construct a removable task vector. We first demonstrate the calibration and reversibility of PGS in a two-route gridworld environment. Using chess puzzles, we then evaluate independently fitted PGS vectors both in isolation and in combination, finding that compatible tactical objectives accumulate constructively. Finally, in competitive football, we show that PGS can alter specific team behaviors and that its effects transfer across opponents. Together, these results show that policy gradients provide a natural interface for constructing temporary and composable behavioral adaptations across diverse decision-making domains.

## Metadata
- **Published**: 2026-07-30T01:29:57Z
- **Authors**: Yoann Poupart, Aurélie Beynier, Nicolas Maudet
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27574v1)