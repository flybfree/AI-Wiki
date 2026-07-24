---
title: TAPAS: Throughput-adaptive Perception for Autonomous Systems
url: http://arxiv.org/abs/2607.17317v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_16-01-11Z_TAPAS_Throughput_adaptivePerceptionforAutonomousSy.md
generated_at: 2026-07-23 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TAPAS, a throughput‑adaptive perception framework that dynamically adjusts frame‑per‑second targets and model‑to‑cluster mappings to meet real‑time requirements while minimizing energy use on mobile and edge hardware. Evaluated on Jetson Orin NX with KITTI and nuScenes data, TAPAS achieves 93–100 % throughput met rates across test sequences and reduces energy consumption by up to 76 % compared with state‑of‑the‑art methods.

## Key Takeaways
- TAPAS couples scene complexity awareness to estimate a suitable FPS target, eliminating over‑ or under‑provisioning of computational resources.  
- It employs dynamic model‑to‑cluster mapping that reallocates workloads across heterogeneous platforms in real time, ensuring the required throughput is delivered with minimal energy.  
- The reinforcement learning agent using RRM and GRU learns to balance FPS targets and energy usage, resulting in up to 64 % lower energy than SOTA on unseen nuScenes while maintaining high throughput.

## Context
Autonomous systems must continuously adapt their perception pipelines as scene complexity fluctuates, yet most existing solutions operate under static assumptions that lead to inefficiencies. This work addresses the gap by integrating real‑time awareness and adaptive resource allocation within a reinforcement learning framework, aligning closely with trends toward edge AI and energy‑aware robotics.

## Implications
For industry practitioners, TAPAS offers a practical solution for deploying perception systems on constrained hardware without sacrificing performance or battery life. The methodology can be extended to other autonomous platforms, fostering more sustainable and responsive autonomous navigation in diverse environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17317v1)
