---
title: From Fixed Grids to Moving Particles:A Transferable Latent Operator for Fluid Dynamics
published: 2026-08-14T09:26:02Z
authors: Meng Li, Chuqi Chen, Zhengqing Gao, Xi Zhou, Xiao Sun, Yang Xiang, Huaxi Huang
url: http://arxiv.org/abs/2608.14120v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Fixed Grids to Moving Particles:A Transferable Latent Operator for Fluid Dynamics

## Abstract
Lagrangian modeling is vital to fluid dynamics, as it characterizes particle transport and complements the Eulerian description.However, Lagrangian trajectories are less commonly available than Eulerian fields, while most neural operators are trained and evaluated primarily in the Eulerian representation. This mismatch motivates a new learning problem: can a model trained solely on Eulerian observations generalize zero-shot from Eulerian field prediction to Lagrangian particle rollout, without Lagrangian supervision or task-specific adaptation? To address this problem, we propose the Transferable Latent Operator (TLO), which learns a unified flow representation shared by Eulerian field prediction and Lagrangian particle rollout. TLO decouples latent flow evolution from coordinate-dependent decoding: querying the evolving latent representation at fixed spatial coordinates yields Eulerian fields, whereas querying velocities at particle positions and recursively updating these positions enables Lagrangian rollout. Across five fluid-dynamics benchmarks, TLO consistently outperforms existing neural operators in both Eulerian field prediction and zero-shot Lagrangian rollout, with further gains from limited Lagrangian fine-tuning.

## Metadata
- **Published**: 2026-08-14T09:26:02Z
- **Authors**: Meng Li, Chuqi Chen, Zhengqing Gao, Xi Zhou, Xiao Sun, Yang Xiang, Huaxi Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14120v1)