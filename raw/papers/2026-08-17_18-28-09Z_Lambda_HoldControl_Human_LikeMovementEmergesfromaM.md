---
title: Lambda-Hold Control: Human-Like Movement Emerges from a Minimal Task Reward in Predictive Musculoskeletal Simulation
published: 2026-08-17T18:28:09Z
authors: Jun Hyuk Lee, Chihyeong Lee, Jooeun Ahn
url: http://arxiv.org/abs/2608.17030v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lambda-Hold Control: Human-Like Movement Emerges from a Minimal Task Reward in Predictive Musculoskeletal Simulation

## Abstract
The massive overactuation in the human musculoskeletal system makes it challenging to train musculoskeletal models to generate human-like motion via reinforcement learning, primarily because exploration in the resulting high-dimensional and redundant action space is extremely inefficient. To address this problem, we propose the $λ$-hold controller, inspired by the equilibrium-point (EP) hypothesis, which has been widely supported by extensive evidence from human motor control studies. The policy's control variable is the per-muscle EP threshold length $λ$, from which a stretch-reflex recruitment law computes the muscle excitations automatically. Holding each $λ$ over an interval of the gait phase also sharply reduces the frequency at which the policy must be queried. Consequently, the controller, to our knowledge for the first time, enables a muscle-actuated skeletal model to learn human-like sprinting using only a minimal reward within an hour of training. The efficient exploration through the proposed $λ$-hold controller is not merely an engineering trick but an approach grounded in physiology, bringing together the EP hypothesis, intermittent control, and optimal feedback control. Beyond encapsulating human-like behavior in predictive simulation, this achievement contributes to developing a learnable model of the human motor controller.

## Metadata
- **Published**: 2026-08-17T18:28:09Z
- **Authors**: Jun Hyuk Lee, Chihyeong Lee, Jooeun Ahn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17030v1)