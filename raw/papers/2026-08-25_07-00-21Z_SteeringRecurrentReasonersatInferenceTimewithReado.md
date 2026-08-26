---
title: Steering Recurrent Reasoners at Inference Time with Readout Feedback
published: 2026-08-25T07:00:21Z
authors: Shunsuke Kamiya, Masanori Koyama, Seongcheol Jeong, Fumiya Uchiyama, Kenji Kubo, Kohei Hayashi, Masahiro Suzuki, Yutaka Matsuo
url: http://arxiv.org/abs/2608.24136v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Steering Recurrent Reasoners at Inference Time with Readout Feedback

## Abstract
Recurrent models, which repeatedly update latent states with shared computation blocks, have emerged as powerful architectures for solving complex reasoning tasks. Existing inference-time methods scale computation by running more steps or sampling more trajectories, but ignore information revealed within each trajectory. Here we show that recurrent models can be improved at inference time by using their own readout probabilities to steer latent dynamics without retraining. We introduce Readout Feedback (RoFB), a test-time intervention that converts intermediate predictions into token-wise pairwise coupling forces injected into the latent dynamics. Across three recurrent models (AKOrN, ItrSA++, TRM) on Sudoku and Maze, RoFB yields clear gains in four of six model-task pairs, achieving performance unattainable by merely running more steps or selecting from multiple trajectories, at comparable or lower computational cost. These results suggest that closed-loop steering of latent dynamics can serve as a complementary inference-time control mechanism for recurrent reasoning models.

## Metadata
- **Published**: 2026-08-25T07:00:21Z
- **Authors**: Shunsuke Kamiya, Masanori Koyama, Seongcheol Jeong, Fumiya Uchiyama, Kenji Kubo, Kohei Hayashi, Masahiro Suzuki, Yutaka Matsuo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24136v1)