---
title: Rotation-Invariant Multi-IMU Activity Recognition under Independent Per-Location Orientation Shifts
url: http://arxiv.org/abs/2608.15621v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_08-39-41Z_Rotation_InvariantMulti_IMUActivityRecognitionunde.md
generated_at: 2026-08-17 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Truly Rotation‑Invariant HAR (TRI‑HAR), a framework that treats independent per‑location IMU orientation offsets as an inherent property of the model rather than an external problem. By reshaping sensor streams into triaxial vectors and applying a shared SO(3)-equivariant backbone, TRI‑HAR fuses invariant features across all IMUs to classify activities while preserving macro‑F1 scores under arbitrary rotations.

## Key Takeaways
- The framework explicitly models independent per‑location orientation shifts as part of the model architecture, eliminating the need for rotation augmentation or calibration pipelines. 
- It reshapes accelerometer and gyroscope streams into triaxial vectors before processing, enabling a shared equivariant backbone that treats each IMU location symmetrically. 
- Across four multi‑IMU benchmarks, TRI‑HAR maintains macro‑F1 under fixed independent SO(3) rotations while outperforming rotation‑augmented baselines.

## Context
In wearable HAR systems, orientation drift between body locations often leads to performance degradation because conventional models assume a single global reference frame. This work addresses the gap by decoupling sensor calibration from model training, allowing robust classification without requiring additional sensors or manual alignment procedures.

## Implications
For researchers and engineers developing at‑home rehabilitation monitors, TRI‑HAR offers a scalable solution that can be deployed across multiple IMU sites with minimal user effort. The approach may inspire future systems that handle heterogeneous sensor setups while preserving privacy by avoiding explicit rotation calibration steps.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15621v1)
