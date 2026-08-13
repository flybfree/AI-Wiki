---
title: Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL
published: 2026-08-12T13:48:56Z
authors: Martin Schuck, Maks Sorokin, Simone Manni, Duy Ta, Angela P. Schoellig, Marco Hutter, Simon Le Cleac'H, Jan Brüdigam
url: http://arxiv.org/abs/2608.12063v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL

## Abstract
Integrating locomotion and manipulation is essential for robot autonomy, but scaling standard Reinforcement Learning (RL) to complex tasks is severely bottlenecked by the slow, manual process of dense reward shaping. To bypass this limitation, we leverage Sample-based Model Predictive Control (SMPC) entirely in simulation as an automated, rapidly tunable expert to generate massive offline datasets. Because this data solves the fundamental exploration problem, we can train an off-policy RL agent using purely sparse task rewards, drastically reducing the time required to learn new skills and eliminating the need for manual tuning. Integrating this high-level agent with a low-level dynamic stability controller yields more optimal behaviors that strictly align with true task objectives, ultimately allowing the learned policies to surpass the original optimal control teacher. We validate the robustness of this sim-to-real framework by successfully deploying complex loco-manipulation skills across different morphologies, including an arm-equipped Spot quadruped and a G1 humanoid.

## Metadata
- **Published**: 2026-08-12T13:48:56Z
- **Authors**: Martin Schuck, Maks Sorokin, Simone Manni, Duy Ta, Angela P. Schoellig, Marco Hutter, Simon Le Cleac'H, Jan Brüdigam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12063v1)