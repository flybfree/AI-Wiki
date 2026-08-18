---
title: Pre-training Visual Dexterity in Simulation
published: 2026-08-16T20:21:33Z
authors: Sarthak Kamat, Adam Rashid, Satvik Sharma, Aseem Doriwala, Chelsea Finn, Phillip Isola, C. Karen Liu
url: http://arxiv.org/abs/2608.15917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pre-training Visual Dexterity in Simulation

## Abstract
Large-scale pre-training has made robot policy fine-tuning increasingly data-efficient, but this progress has largely been driven by datasets and embodiments built around simple parallel-jaw grippers. Dexterous, multi-fingered hands remain comparatively data-starved because real teleoperation is costly to scale, while human hand video is off-embodiment and requires lossy pose estimation and retargeting. We introduce Simulation Pre-training for Dexterity (SPD), a pre-training framework for dexterous manipulation that uses data entirely collected in simulation. In SPD, humans manipulate virtual objects inside a VR headset, enabling on-embodiment trajectories and robot-free collection. With the help of five operators, we collect 75 hours of multi-task dexterous manipulation over one week, and use it to pre-train a causal transformer on a sequence modeling objective. We study the benefits of simulation pre-training on real-world tasks by fine-tuning on 1-2 hours of physical demonstrations on a 56-DoF bimanual dexterous setup. We find that our approach outperforms training behavior cloning policies from scratch, showing that simulation teleoperation is a viable pre-training source for real-world dexterous manipulation. We perform ablation studies, measuring the benefits of history conditioning and short action chunks for reactive control.

## Metadata
- **Published**: 2026-08-16T20:21:33Z
- **Authors**: Sarthak Kamat, Adam Rashid, Satvik Sharma, Aseem Doriwala, Chelsea Finn, Phillip Isola, C. Karen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15917v1)