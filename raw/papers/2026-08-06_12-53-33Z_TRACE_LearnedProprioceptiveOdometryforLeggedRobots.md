---
title: TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions
published: 2026-08-06T12:53:33Z
authors: Taehyeon Kong, Woojin Kim, Jemin Hwangbo
url: http://arxiv.org/abs/2608.05975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions

## Abstract
In this paper, we present TRACE (Tokenized Robust Attention for Contact-Aware Estimation), an end-to-end learned proprioceptive odometry estimator for legged robots under unreliable contact conditions. The proposed estimator directly predicts relative displacement, relative rotation, and body-frame velocity from a recent history of onboard inertial and joint measurements. To improve robustness under unreliable contact conditions, we introduce a foot-aware cross-attention module that adaptively weights IMU and leg-wise kinematic tokens without relying on manually defined contact or slip thresholds. The estimator is trained with direct supervision and two physics-inspired auxiliary losses that promote kinematic consistency and reliable use of leg information. To reduce policy-specific overfitting and consequently improve sim-to-real transfer, simulation training incorporates policy randomization, followed by partial real-world fine-tuning of the temporal encoder and prediction head. Experiments across diverse indoor and outdoor terrains demonstrate consistent reductions in position drift compared with classical filtering-based, hybrid, and purely learning-based baselines. Ablation studies further validate the contributions of the proposed training objectives, policy randomization, and real-world fine-tuning, particularly under unreliable contacts and sim-to-real mismatch.

## Metadata
- **Published**: 2026-08-06T12:53:33Z
- **Authors**: Taehyeon Kong, Woojin Kim, Jemin Hwangbo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05975v1)