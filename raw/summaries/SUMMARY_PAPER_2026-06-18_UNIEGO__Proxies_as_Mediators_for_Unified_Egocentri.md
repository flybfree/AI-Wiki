---
title: UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning
url: http://arxiv.org/abs/2606.20559v1
type: paper-summary
date: 2026-06-18
source_paper: 2026-06-18_17-59-45Z_UNIEGO_ProxiesasMediatorsforUnifiedEgocentricVideo.md
generated_at: 2026-06-18 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces UNIEGO, a unified egocentric encoder that leverages nine heterogeneous teachers across viewpoints, modalities, and foundation models to generate richer video representations. By employing representation-specific proxy models and selective distillation, UNIEGO achieves state-of-the-art results on action recognition, video retrieval, and action segmentation benchmarks.

## Key Takeaways
- The framework uses a hierarchical multi-teacher distillation with nine teachers spanning ego‑exo viewpoints, RGB, depth, and skeleton modalities.  
- A proxy layer translates incompatible teacher features into a homogeneous egocentric space before the second distillation stage.  
- Selective Proxy Distillation (SPD) adaptively selects correct and confident proxies per sample, improving robustness.

## Context
Current egocentric video understanding suffers from limited perspective due to single‑camera constraints, prompting research toward models that integrate complementary knowledge without sacrificing deployment simplicity. This work advances the state of the art by showing how structured proxy mediation can overcome architectural mismatches in multi‑teacher learning.

## Implications
Practitioners can adopt UNIEGO’s proxy‑mediated distillation to build more expressive yet lightweight egocentric video models, reducing reliance on expensive multimodal sensors and enabling broader deployment. The approach also offers a blueprint for integrating diverse foundation model knowledge into single‑camera systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.20559v1)
