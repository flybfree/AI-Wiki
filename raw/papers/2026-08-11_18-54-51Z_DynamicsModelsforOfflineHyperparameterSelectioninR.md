---
title: Dynamics Models for Offline Hyperparameter Selection in Real-World RL
published: 2026-08-11T18:54:51Z
authors: Jordan Coblin, Han Wang, Martha White, Adam White
url: http://arxiv.org/abs/2608.11349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamics Models for Offline Hyperparameter Selection in Real-World RL

## Abstract
A key obstacle to deploying reinforcement learning in real-world systems is hyperparameter selection, particularly when simulators are unavailable and online experimentation is costly. Prior work has proposed calibration models trained on offline data to approximate environment dynamics and enable offline hyperparameter selection, but these methods have so far been evaluated only in simple simulated settings. In this paper, we present the first application of calibration models in a real-world industrial setting: a municipal water treatment plant. We evaluate several calibration model approaches, including a k-nearest neighbors model with a Laplacian distance metric, on high-dimensional, non-stationary sensor data for nexting prediction tasks. Our results show that these models can generate realistic long-horizon rollouts and recover meaningful hyperparameter sensitivity trends. We further examine how calibration models scale to year-long datasets, how they support the selection of fine-tuning learning rates for pre-trained agents, and how robust they are under distribution shift. Overall, our findings provide a proof of concept for using offline dynamics models to support RL deployment in real-world environments, while highlighting important practical challenges for future work.

## Metadata
- **Published**: 2026-08-11T18:54:51Z
- **Authors**: Jordan Coblin, Han Wang, Martha White, Adam White
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11349v1)