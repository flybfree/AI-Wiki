---
title: Anticipatory Risk-Guided Reinforcement Learning for Safe Flight Through Dynamic Clutter
published: 2026-07-26T09:31:49Z
authors: Yuchao Mei, Guohao Zhang, Luxia Ai, Haopeng Chen, Wenbing Tao
url: http://arxiv.org/abs/2607.23565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Anticipatory Risk-Guided Reinforcement Learning for Safe Flight Through Dynamic Clutter

## Abstract
Safe quadrotor navigation in cluttered and dynamic environments depends not only on instantaneous geometric perception, but more critically on anticipating collision risks induced by relative motion. Conventional modular pipelines frequently suffer from perception latency, while end-to-end learning methods relying on implicit scalar rewards often struggle to extract reliable spatio-temporal features without physics-grounded supervision. To address this, we propose an anticipatory risk-guided reinforcement learning framework. Leveraging privileged simulator states, we construct a directionally aligned future collision risk map based on the Closest Point of Approach (CPA). Through an asymmetric actor-critic architecture, the network is trained to self-predict this structured risk, which explicitly guides the visual policy during deployment. A lightweight spatio-temporal encoder extracts motion cues directly from onboard depth sequences, bypassing explicit object tracking or optical flow estimation. Extensive simulated and real-world experiments demonstrate that our method effectively improves safety margins and flight efficiency in dense dynamic clutters compared to existing baselines. Furthermore, the learned policy achieves robust zero-shot Sim-to-Real transfer on a physical quadrotor, relying purely on abstracted spatio-temporal depth sequences and its self-predicted risk priors, validating the effectiveness of our approach and its robust generalization from simulation to reality.

## Metadata
- **Published**: 2026-07-26T09:31:49Z
- **Authors**: Yuchao Mei, Guohao Zhang, Luxia Ai, Haopeng Chen, Wenbing Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23565v1)