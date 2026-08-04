---
title: MANGO-Grasp: Mahalanobis Fields over Geometry-Oriented 3D Gaussians for Cross-Embodiment Dexterous Grasping
url: http://arxiv.org/abs/2608.02014v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_10-12-15Z_MANGO_Grasp_MahalanobisFieldsoverGeometry_Oriented.md
generated_at: 2026-08-03 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MANGO-Grasp, a framework that uses geometry‑oriented 3D Gaussians and morpho‑kinematic descriptors to predict stable grasps across different hands without per‑hand tuning. On benchmark tasks it improves over previous methods by up to 8.24% in simulation and 16.57% zero‑shot transfer, achieving 86% success in real experiments.

## Key Takeaways
- MANGO-Grasp represents objects as geometry‑oriented 3D Gaussian primitives with surface‑aligned plates whose outward normals encode local curvature.
- Interaction prediction uses Mahalanobis fields over keypoint–primitive pairs that rise sharply along the surface normal but only gently in the tangent plane, guiding grasp optimization.
- The framework employs a single shared optimization formulation and hyperparameter set across all hands, enabling cross‑embodiment performance.

## Context
Cross‑embodiment dexterous grasping remains challenging because each hand’s morphology and kinematics differ, yet current methods often treat them separately. This work advances the field by unifying object geometry representation with robot descriptors in a single anisotropic interaction model.

## Implications
The unified approach reduces engineering effort for new hands and can be deployed in real‑world robotic systems where rapid deployment is critical. It also demonstrates that geometric priors improve zero‑shot transfer, offering practical benefits for assistive robotics and industrial automation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02014v1)
