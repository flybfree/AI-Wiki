---
title: SIGMA-Lane: Scale-pyramId Gated MAmba for Temporally Consistent Video Lane Detection
published: 2026-08-17T09:44:27Z
authors: Tiancheng Zhang, Mengmeng Wang, Yan Gao, Xiangjie Kong, Guojiang Shen, Jiaxin Du
url: http://arxiv.org/abs/2608.16338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SIGMA-Lane: Scale-pyramId Gated MAmba for Temporally Consistent Video Lane Detection

## Abstract
Video lane detection requires predictions that remain stable across frames, yet severe vehicle occlusions can break temporal cues. In streaming recurrent models, corrupted observations may enter the hidden state and produce errors that persist into later frames. Existing occlusion-aware refinements usually provide obstacle masks as auxiliary inputs, so the state-update path is only indirectly protected. We propose SIGMA-Lane, which treats this failure mode as state contamination in State Space Model (SSM)-based temporal modeling. SIGMA-Lane places occlusion-aware gates on the SSM write and residual-fusion paths, controlling how current observations enter temporal memory and are fused back after temporal propagation. After coordinate-consistent affine alignment, the model combines two complementary paths: SSM-consistent dual-gating for temporal filtering and Structural Spatial Retrieval (SSR) for recovering missing lane structure from aligned historical priors. Experiments on VIL-100 and OpenLane-V show improved temporal stability under heavy occlusion, with competitive F1 and mIoU scores.

## Metadata
- **Published**: 2026-08-17T09:44:27Z
- **Authors**: Tiancheng Zhang, Mengmeng Wang, Yan Gao, Xiangjie Kong, Guojiang Shen, Jiaxin Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16338v1)