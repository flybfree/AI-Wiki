---
title: Mitigating Performance Discrepancy in Cross-Domain 3D Class-Incremental Learning
url: http://arxiv.org/abs/2609.04860v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_08-20-00Z_MitigatingPerformanceDiscrepancyinCross_Domain3DCl.md
generated_at: 2026-09-06 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper tackles performance discrepancy in cross‑domain 3D class‑incremental learning, where heterogeneous point clouds from different acquisition sources cause uneven degradation. By introducing PolyMem, an exemplar‑free method that implicitly captures high‑order feature statistics, the authors show that this discrepancy can be mitigated while also boosting overall accuracy across domains.

## Key Takeaways
- The heterogeneity of 3D point clouds—originating from CAD, RGB‑D scans, video reconstructions, or corrupted observations—leads to a variable degree of performance loss known as performance discrepancy.  
- A domain‑specific CIL protocol (Domain3D‑CIL) is established that includes categories from multiple heterogeneous domains to expose this problem across standard baselines.  
- PolyMem’s high‑order statistical modeling reduces the impact of this discrepancy, yielding both improved robustness and higher accuracy on diverse 3D datasets.

## Context
In autonomous driving and robotics, 3D perception must continuously adapt to new object categories without forgetting prior knowledge. Unlike 2D vision where data is often homogeneous, 3D point clouds suffer from domain‑specific noise and quality variations, making incremental learning more challenging than catastrophic forgetting alone.

## Implications
Maintaining consistent performance across diverse acquisition sources is critical for real‑world deployment of 3D perception systems. PolyMem’s approach offers a practical solution that can be integrated into existing CIL pipelines, enabling more reliable autonomous navigation and augmented reality experiences in heterogeneous environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04860v1)
