---
title: VQ-VAD: Vector-quantized Motion Representation Learning for Human-centric Video Anomaly Detection
url: http://arxiv.org/abs/2608.05069v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-12-39Z_VQ_VAD_Vector_quantizedMotionRepresentationLearnin.md
generated_at: 2026-08-05 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VQ-VAD, a human‑centric video anomaly detection system that learns discrete motion representations by adapting the vector‑quantized GAN to keypoint sequences. The framework builds a motion codebook from normal behavior and flags anomalies as high‑error reconstructions, achieving 81.83 % in‑domain accuracy on HR‑SHT while enabling cross‑dataset transfer without retraining.

## Key Takeaways
- VQ-VAD adapts the vector‑quantized GAN to operate on keypoint sequences, constructing a motion codebook that encodes normal behavior.
- It detects anomalies by measuring reconstruction errors when an observed motion sequence cannot be mapped to any codebook entry.
- The method attains 81.83 % accuracy on HR‑SHT and transfers effectively from CMU Panoptic to HR‑SHT with only 76.69 % performance, showing robust cross‑dataset generalization.

## Context
Pose‑based video anomaly detection has moved away from raw frames toward motion dynamics, yet most models operate in continuous latent spaces that cannot capture compact, discrete patterns essential for reliable behavior analysis. VQ-VAD addresses this limitation by introducing a quantization step that creates a finite set of motion codes, enabling more efficient and interpretable representation learning.

## Implications
The discrete motion codebook reduces reliance on labeled anomalies, lowering annotation costs while preserving high detection performance across diverse surveillance scenarios. Practitioners can leverage VQ‑VAD to build privacy‑preserving systems that generalize well without extensive retraining, offering a scalable solution for real‑world anomaly monitoring.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05069v1)
