---
title: Robo-Dopamine 2.0: History-Conditioned and OOD-Aware Process Reward Modeling for Robotic Manipulation
published: 2026-08-16T11:15:55Z
authors: Yijie Xu, Haopeng Jin, Run Zhou, Shengbang Liu, Sixiang Chen, Hongyang Cheng, Sicheng Hu, Peterson Co, Jinwen Luo, Huajie Tan, Shanghang Zhang
url: http://arxiv.org/abs/2608.15680v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robo-Dopamine 2.0: History-Conditioned and OOD-Aware Process Reward Modeling for Robotic Manipulation

## Abstract
Vision-language-action (VLA) models improve robotic manipulation but remain vulnerable to compounding errors, scene changes, and off-trajectory states. Reinforcement learning can refine pretrained VLA policies, yet sparse success signals hinder exploration, while engineered dense rewards are costly and task-specific. Existing learned visual reward models often rely on static before-after observations, causing temporal ambiguity and weak discrimination between robustness-preserving variations and task-invalid failures under out-of-distribution (OOD) execution. We introduce Robo-Dopamine 2.0, a history- and OOD-aware process reward model with a pairwise prediction interface. It combines (1) history-conditioned pairwise rewards that use source-aligned reference panels for synthetic OOD queries and observed rollout history for online queries, while preserving the queried endpoints, and (2) an OOD-aware signed progress space that represents valid progress, robustness, failure, and recovery. A Signed-Hop Curriculum with transition-aware replay learns coarse execution ordering before fine-grained progress calibration. We also construct an OOD trajectory dataset and a five-family benchmark. Reference panels improve mean visual order consistency (VOC) from 0.967 to 0.986 and OOD-robust VOC from 0.906 to 0.958. With the same 400K pairwise-reward budget, Signed-Hop training with 25% replay reaches 0.9872 mean VOC, compared with 0.9858 for a matched-pool shuffled control. In downstream reinforcement learning, the full model achieves 86.8% mean RoboTwin success and 71/80 successful real-world insertions.

## Metadata
- **Published**: 2026-08-16T11:15:55Z
- **Authors**: Yijie Xu, Haopeng Jin, Run Zhou, Shengbang Liu, Sixiang Chen, Hongyang Cheng, Sicheng Hu, Peterson Co, Jinwen Luo, Huajie Tan, Shanghang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15680v1)