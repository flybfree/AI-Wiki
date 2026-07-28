---
title: Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline
url: http://arxiv.org/abs/2607.22997v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_02-23-34Z_Real2Sim2RealforVision_Language_ActionManipulation.md
generated_at: 2026-07-27 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Real2Sim2Real, an AMD‑accelerated pipeline that trains vision‑language‑action models and deploys them on physical robots without CUDA. It shows end‑to‑end simulation to real manipulation using SmolVLA, object selection, synthetic data generation with 3D Gaussian Splatting and Genesis physics, and large‑scale locomotion RL across AMD hardware.

## Key Takeaways
- The pipeline is fully ROCm based, enabling training and deployment on Radeon PRO GPUs and Ryzen AI edge without CUDA lock.  
- It integrates Sim2Real data generation using 3D Gaussian Splatting fused with Genesis physics to create realistic synthetic scenes for training.  
- Large‑scale reinforcement learning for quadruped and humanoid locomotion is demonstrated across multiple AMD hardware platforms.

## Context
Physical AI aims to embed large multimodal models in embodied agents that interact with the physical world, a trend highlighted by industry leaders in 2025‑2026. This work provides a concrete, open‑source stack that bridges data‑center training and edge inference on AMD silicon.

## Implications
The results show that AMD hardware can replace NVIDIA‑centric ecosystems for multimodal manipulation, lowering cost and increasing accessibility. Practitioners can adopt ROCm‑based pipelines to develop real‑world AI agents without proprietary CUDA dependencies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22997v1)
