---
title: Learning Where and What to Lift for Bi-planar X-ray-to-CT Reconstruction
published: 2026-08-18T01:23:36Z
authors: Yifei Wu, Yicheng Wu, Qiang Ma, Qi Chen, Renyang Gu, Xinyu Liu, Yongsheng Pan, Yong Xia
url: http://arxiv.org/abs/2608.17255v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Where and What to Lift for Bi-planar X-ray-to-CT Reconstruction

## Abstract
X-ray imaging can be approximately modeled as the projection of an underlying volumetric attenuation field, with each measurement recording the accumulated attenuation along a corresponding ray path. Reconstructing a CT volume from only a few X-ray views is therefore severely ill-posed, as the projections collapse depth information and leave 3D locations of anatomical regions and their corresponding intensity distributions highly entangled and ambiguous. We observe that once the spatial organization of anatomical regions is established, estimating their CT intensities becomes substantially more tractable. Motivated by this, we propose LiftXR, an interleaved, geometry-guided framework that explicitly incorporates spatial layout recovery into CT reconstruction. Specifically, a layout lifter first generates a 3D anatomical layout from bi-planar X-rays, providing spatial guidance for an intensity renderer to reconstruct a CT volume. An anatomical parser then performs volumetric perception on the reconstruction, exploiting its spatially resolved boundary and intensity cues to recover a refined anatomical layout. This transition from projection-conditioned layout generation to reconstruction-conditioned anatomical perception allows the parsed layout to provide feedback for region-specific intensity calibration. Extensive experiments on two public datasets demonstrate that LiftXR consistently outperforms recent X-ray-to-CT reconstruction methods, establishing a new state of the art. Moreover, the reconstructed CT achieves superior performance in external downstream segmentation, indicating improved anatomical fidelity. Code will be released.

## Metadata
- **Published**: 2026-08-18T01:23:36Z
- **Authors**: Yifei Wu, Yicheng Wu, Qiang Ma, Qi Chen, Renyang Gu, Xinyu Liu, Yongsheng Pan, Yong Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17255v1)