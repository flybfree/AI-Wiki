---
title: Cortex: Compact Behavior Cloning for Quake with Frozen Visual Features
published: 2026-07-22T18:34:30Z
authors: Dzmitry Malyshau
url: http://arxiv.org/abs/2607.22739v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cortex: Compact Behavior Cloning for Quake with Frozen Visual Features

## Abstract
We study how far a deliberately simple behavioral-cloning policy can progress in a visually rich first-person game before adding reinforcement learning or explicit memory. Cortex is a compact Quake policy with 10.98 million trainable parameters in a six-layer transformer over a frozen DINOv3 encoder. It is trained on the Quake subset of the public Pixels2Play corpus: 6,849 recordings (about 474.7 hours), represented as 17.09 million cached decision frames with keyboard and mouse actions. One sampled training epoch uses 517,048 four-frame windows and takes 3.3 minutes of policy-head optimization on one RTX 5080, excluding one-time feature extraction. We evaluate two independent batches of 20 stochastic, 120-second episodes on Quake E1M1. Cortex does not complete the level, but every episode reaches the opening door, button room, and gate descent; 19 of 20 episodes in each batch record at least one kill. Under the same time-controlled harness, released P2P-150M and NitroGen checkpoints remain shallower in five matched-duration episodes each. These comparisons are limited by small reference samples and different native interfaces. Ablations show that denser visual tokens improve combat and survival, while longer optimization and naive action history improve offline metrics without consistently improving play. The remaining failures are consistent with covariate shift and motivate targeted corrective data. We release the policy implementation, checkpoint, and a representative rollout.

## Metadata
- **Published**: 2026-07-22T18:34:30Z
- **Authors**: Dzmitry Malyshau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22739v1)