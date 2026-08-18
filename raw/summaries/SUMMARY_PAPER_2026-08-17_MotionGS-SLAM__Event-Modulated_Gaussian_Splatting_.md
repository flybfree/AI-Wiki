---
title: MotionGS-SLAM: Event-Modulated Gaussian Splatting for Motion-Blur Robust SLAM
url: http://arxiv.org/abs/2608.15024v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_04-20-51Z_MotionGS_SLAM_Event_ModulatedGaussianSplattingforM.md
generated_at: 2026-08-17 21:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
MotionGS‑SLAM tackles the problem of motion blur in vision‑based SLAM by treating blur as a generative process rather than an artifact to be removed. The authors demonstrate that their event‑modulated Gaussian splatting framework recovers accurate camera trajectories and 3D maps even under severe high‑motion conditions, outperforming existing state‑of‑the‑art methods.

## Key Takeaways
- Motion blur is modeled as a forward process where each Gaussian’s rasterization adapts to precise motion cues, turning isotropic dots into anisotropic elliptical brush strokes that follow the camera’s velocity.  
- The dual modulation mechanism also adjusts exposure integral sampling density according to local speed, ensuring temporal consistency with event‑camera data.  
- Joint optimization of intra‑exposure trajectories and 3D geometry is achieved through blur‑aware photometric and event constraints, yielding significant gains in trajectory accuracy and map quality.

## Context
Vision‑based SLAM has long struggled with motion blur because it corrupts the observed image and makes the inverse problem ill‑posed. Event cameras offer a natural solution with microsecond temporal resolution that resists blur, yet integrating them into existing pipelines remains challenging. MotionGS‑SLAM bridges this gap by providing a principled, physics‑based representation of blur within a splatting framework.

## Implications
This work opens a path for robust SLAM in real‑world scenarios where cameras experience high speeds, such as autonomous vehicles and aerial drones. By decoupling blur modeling from denoising, the approach can be extended to other modalities like LiDAR or radar, fostering unified perception systems that handle dynamic environments reliably.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15024v1)
