---
title: KING: Embodiment-Aware Kinematic Graph Neural Network for Unified Motion Representation of Legged and Wheeled Robots
url: http://arxiv.org/abs/2608.01015v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_05-42-58Z_KING_Embodiment_AwareKinematicGraphNeuralNetworkfo.md
generated_at: 2026-08-03 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KING, a Graph Neural Network that unifies kinematic models for both wheeled and legged robots by representing each robot as a common graph. The model learns accurate odometry from proprioceptive inputs such as encoders and an IMU using only an embodiment description like a URDF file. Experiments demonstrate high‑accuracy estimation in real environments and the ability to adapt to new robots with just one minute of data.

## Key Takeaways
- KING encodes robot embodiments as graphs, allowing wheel kinematics and leg joint dynamics to share a single representation.
- The unified model eliminates the need for separate training pipelines per embodiment, reducing computational overhead.
- Transfer learning with minimal data (one minute) enables rapid adaptation to new robots without full retraining.

## Context
Current odometry systems rely heavily on external sensors that can be unreliable in featureless settings. Learning‑based kinematic models improve accuracy but often fail when applied to different robot bodies because they ignore the structural differences between wheels and legs. KING addresses this limitation by treating embodiment as a graph, providing a more flexible and generalizable solution.

## Implications
For robotics engineers, KING simplifies deployment across diverse platforms, lowering development time and cost. In industry, it supports rapid prototyping of wheeled and legged robots without costly retraining cycles. Practitioners can rely on a single model to deliver robust odometry, enhancing autonomy in challenging environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01015v1)
