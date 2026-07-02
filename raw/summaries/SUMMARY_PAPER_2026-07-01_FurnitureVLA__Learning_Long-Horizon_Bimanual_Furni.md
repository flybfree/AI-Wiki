---
title: FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model
url: http://arxiv.org/abs/2607.01212v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_17-51-21Z_FurnitureVLA_LearningLong_HorizonBimanualFurniture.md
generated_at: 2026-07-01 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FurnitureVLA, a vision-language-action model designed to assemble real‑scale furniture using two arms in a single operator setting. It achieves an 80% success rate in simulation and validates on a Kinova Gen3 robot with only a modest 16% drop on the hardest task.

## Key Takeaways
- The system learns up to seven subtasks across 1550 control steps by jointly predicting actions and a continuous progress signal, which reduces compounding errors during inference.
- It uses expert‑generated simulations and a VR teleoperation pipeline to collect high‑quality real‑world demonstrations for scalable training.
- Real‑scale assembly is limited by perception and control design factors that the study identifies as critical for precision.

## Context
Current robotics research often treats furniture assembly as toy‑scale or single‑arm tasks, overlooking the complexity of coordinated bimanual motion at human scale. This work bridges that gap by applying language‑driven planning to long‑horizon manipulation, showcasing how multimodal models can handle real‑world precision.

## Implications
The results demonstrate that progress‑enhanced VLAs can significantly boost assembly success without sacrificing performance on the most difficult subtasks. For industry practitioners, this approach offers a scalable framework for deploying human‑in‑the‑loop robotics in complex assembly workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01212v1)
