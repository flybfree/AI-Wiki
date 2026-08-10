---
title: Synthetic LiDAR Data Generation and Deterministic Downsampling for Point Cloud Classification on the Edge
published: 2026-08-07T11:02:55Z
authors: Niclas Meyer, Stefan Reitmann
url: http://arxiv.org/abs/2608.07106v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Synthetic LiDAR Data Generation and Deterministic Downsampling for Point Cloud Classification on the Edge

## Abstract
Deploying three-dimensional deep learning frameworks to low-power embedded processors is bottlenecked by the unstructured nature of spatial data and the resource-intensive distance sorting algorithms often used before neural network inference. To address this gap, this paper presents a hardware-constrained workflow optimized for native execution on the Raspberry Pi 5. To account for the reality gap between noiseless, clean computer-aided design (CAD) datasets and real-world sensor data, we use physics-based simulation to construct a synthetic LiDAR dataset. Cross-dataset evaluations demonstrate a substantial drop in classification accuracy when networks trained on clean CAD data are evaluated on synthetic LiDAR sensor data, highlighting the critical need for sensor-aware training. To address the latency bottleneck of traditional geometric preprocessing on edge CPUs, we integrate an isolated, feature-driven Critical Points Layer (CPL) as a frontend filter. Our results show that the pretrained CPL deterministically compresses raw 1024-point clouds to a subset of 40 to 60 unique coordinates. When profiled on the ARM Cortex-A76 processor, the complete pipeline achieves an inference throughput of approximately 50 FPS while maintaining an instance classification accuracy of 88.36%, demonstrating the viability of deterministic real-time 3D perception at the edge.

## Metadata
- **Published**: 2026-08-07T11:02:55Z
- **Authors**: Niclas Meyer, Stefan Reitmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07106v1)