---
title: Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation
url: http://arxiv.org/abs/2608.22757v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_03-27-22Z_Object_Uni_AUnifiedModelforObject_CentricSpatialUn.md
generated_at: 2026-08-24 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Object-Uni, a unified model that integrates object-centric spatial understanding with controllable generation. By treating the pose of an object as an explicit geometric variable rather than just a label or control signal, the model can simultaneously perceive and synthesize consistent 3D poses across different viewpoints.

## Key Takeaways
- The model defines object pose as a shared geometric variable that is explicitly passed from perception to synthesis, enabling precise continuous representation of orientation.
- It introduces a viewpoint-based orientation abstraction that converts continuous pose data into structured textual descriptions while maintaining geometric fidelity for multimodal language models.
- A new benchmark UniSpatial-80K and an object-token-grounded pose anchor are created to ground each instance with its pose state, improving both understanding and generation tasks.

## Context
Current unified vision-language models excel at describing objects but often fail to handle continuous spatial relationships. This limitation hampers applications that require accurate pose manipulation or novel view synthesis. The paper addresses this gap by unifying perception and generation under a single geometric variable.

## Implications
For researchers, Object-Uni provides a template for integrating explicit geometry into multimodal systems, opening doors to real-time pose control in robotics and AR. Industry practitioners can leverage the model’s pose abstraction to generate realistic images from textual or sensor inputs without sacrificing geometric consistency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22757v1)
