---
title: Trajectory Design and Budgeted Querying for Digital Twin Calibration
published: 2026-08-09T10:36:24Z
authors: Vladyslava Spitkovska, Dmytro Kuzmenko
url: http://arxiv.org/abs/2608.08631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory Design and Budgeted Querying for Digital Twin Calibration

## Abstract
Digital-twin calibration requires interaction data that is expensive to collect. We study two acquisition decisions: which trajectories to generate, and when to spend a limited budget on privileged parameter measurements. Our framework couples an excitation-oriented reinforcement learning controller, a recurrent parameter estimator with predictive uncertainty, and a budgeted query policy. In Pendulum, a Random Forest diagnostic recovers gravity only weakly from task-oriented trajectories and does not recover mass or length, while a GRU trained on excitation-oriented trajectories reaches a mean absolute error of 0.0066 with no queries. We then withdraw continuous oracle access partway through an episode, so that the twin must run on the estimator's output for the remainder. The estimator-plus-policy pipeline achieves a terminal error of 0.0092 under a three-query budget, against 0.2031 for an uncalibrated twin. In partially observable Waterworld, five controllers produce different observed error profiles across three hidden parameters, and an estimator trained on a five-controller mixture reaches online normalized errors of roughly 4-5%. These exploratory case studies are not controlled ablations, but they motivate treating trajectory design and query allocation as explicit design variables in data-scarce calibration.

## Metadata
- **Published**: 2026-08-09T10:36:24Z
- **Authors**: Vladyslava Spitkovska, Dmytro Kuzmenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08631v1)