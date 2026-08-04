---
title: MANGO-Grasp: Mahalanobis Fields over Geometry-Oriented 3D Gaussians for Cross-Embodiment Dexterous Grasping
published: 2026-08-03T10:12:15Z
authors: Heng Zhang, Kevin Yuchen Ma, Mike Zheng Shou, Weisi Lin, Yan Wu
url: http://arxiv.org/abs/2608.02014v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MANGO-Grasp: Mahalanobis Fields over Geometry-Oriented 3D Gaussians for Cross-Embodiment Dexterous Grasping

## Abstract
Cross-embodiment dexterous grasping aims to synthesize stable grasps across heterogeneous multi-fingered hands with little or no embodiment-specific tuning. Existing interaction-centric methods achieve promising results, but their object representations often underrepresent local surface geometry, while their robot descriptors do not explicitly encode both robot morphology and kinematics. We propose MANGO-Grasp, an anisotropic interaction framework that represents objects as geometry-oriented 3D Gaussian primitives and robot hands as surface keypoints encoded into morpho-kinematic descriptors. The object primitives are adaptively allocated by geometric complexity and shaped as surface-aligned plates with outward normals, encoding local geometry. Mahalanobis fields over keypoint--primitive pairs serve as interaction prediction targets during training and as optimization guidance for grasp realization at inference. These fields rise sharply for displacement along the surface normal but only gently within the tangent plane, matching the directional structure of contact. Grasps are realized with one shared optimization formulation and hyperparameter setting across all embodiments. On the CMAP and MultiGripperGrasp benchmarks, MANGO-Grasp outperforms the strongest seen-hand baseline by up to 8.24 percentage points in simulation. It also transfers zero-shot to the unseen SharpaWave hand, improving over the strongest zero-shot baseline by up to 16.57 percentage points, and achieves 86% success in real-world experiments. The code and additional materials will be made available upon publication at https://connor-zh.github.io/MANGO-Grasp/.

## Metadata
- **Published**: 2026-08-03T10:12:15Z
- **Authors**: Heng Zhang, Kevin Yuchen Ma, Mike Zheng Shou, Weisi Lin, Yan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02014v1)