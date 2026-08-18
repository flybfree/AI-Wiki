---
title: MotionGS-SLAM: Event-Modulated Gaussian Splatting for Motion-Blur Robust SLAM
published: 2026-08-15T04:20:51Z
authors: Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa
url: http://arxiv.org/abs/2608.15024v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MotionGS-SLAM: Event-Modulated Gaussian Splatting for Motion-Blur Robust SLAM

## Abstract
Current Vision-based SLAM systems fail catastrophically when motion blur corrupts the visual input, as they attempt the ill-posed inverse problem of recovering sharp content from degraded observations. We present MotionGS-SLAM, which fundamentally reimagines motion blur handling through a paradigm shift: rather than removing blur artifacts, we reformulate the challenge as a well-constrained forward problem that generatively models blur formation within the rendering pipeline. By leveraging event cameras' microsecond temporal resolution and immunity to motion blur, we introduce a novel event-modulated Gaussian kernel that dynamically adapts each Gaussian's rasterization based on precise motion cues. Our dual-modulation mechanism transforms 2D Gaussian projections from isotropic dots into anisotropic, motion-aligned elliptical brush strokes (spatial modulation) while adaptively varying exposure integral sampling density based on local velocity (temporal modulation). This physics-based approach enables joint optimization of intra-exposure camera trajectories and 3D scene geometry through blur-aware photometric and event-based constraints. Extensive experiments demonstrate significant improvements over state-of-the-art methods in trajectory accuracy and map quality under severe high-motion conditions.

## Metadata
- **Published**: 2026-08-15T04:20:51Z
- **Authors**: Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15024v1)