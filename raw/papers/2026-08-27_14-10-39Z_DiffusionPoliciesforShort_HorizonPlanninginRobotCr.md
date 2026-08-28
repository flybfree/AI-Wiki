---
title: Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation
published: 2026-08-27T14:10:39Z
authors: Wendong Li, Jochen Garcke
url: http://arxiv.org/abs/2608.27158v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation

## Abstract
Robot crowd navigation requires safe and efficient decision-making under dense, dynamic, and multimodal human--robot interactions. Existing reinforcement-learning methods typically output a single reactive action at each timestep, which limits their ability to represent diverse short-term avoidance strategies. We propose Planning Diffusion Policy Optimization (PDPO), an offline-to-online reinforcement-learning framework that uses a diffusion policy to generate short-horizon action chunks for crowd navigation. PDPO is first pretrained on collision-avoidance demonstrations and then fine-tuned online with PPO by treating the denoising process as an internal decision process. During execution, the policy generates a five-step action chunk and applies it in a receding-horizon manner. Furthermore, we observe an evaluation artifact in common crowd-navigation benchmarks: without explicit boundary constraints, learned agents may leave the valid domain and bypass dense crowds. To address this, we introduce a setting in which boundary violations are treated as collisions. Experiments show that PDPO obtains an improved success rate over strong baselines, and ablations demonstrate that action chunks are especially important for the modified bounded benchmark.

## Metadata
- **Published**: 2026-08-27T14:10:39Z
- **Authors**: Wendong Li, Jochen Garcke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27158v1)