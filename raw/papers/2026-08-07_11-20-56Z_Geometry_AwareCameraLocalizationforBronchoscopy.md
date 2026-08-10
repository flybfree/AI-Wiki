---
title: Geometry-Aware Camera Localization for Bronchoscopy
published: 2026-08-07T11:20:56Z
authors: Lumin Chen, Qingyao Tian, Jinpeng Li, Haoyu Jiang, Huai Liao, Xinyan Huang, Hongbin Liu, Dong Yi
url: http://arxiv.org/abs/2608.07116v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Geometry-Aware Camera Localization for Bronchoscopy

## Abstract
Camera localization in bronchoscopy remains a challenging problem due to stringent accuracy requirements, real-time constraints, and limited training data. Compared to natural scenes, the confined anatomical structures demand millimeter-level precision, while intraoperative guidance necessitates low-latency inference. However, existing methods often fail to effectively exploit preoperative geometric priors, limiting their robustness and accuracy. To address these limitations, we propose a unified geometry-aware bronchoscope localization framework (GABL) that effectively fuses preoperative structural priors with paired intraoperative video to estimate 6-DoF camera poses. Specifically, to address visual ambiguity in complex airways, we propose a graph-guided coarse-to-fine localization scheme that effectively leverages structural priors for precise pose estimation. Furthermore, to mitigate pose jitter and bridge the visual-structural gap, we integrate a Transformer-based tracking model with a novel RGB-depth matching objective, jointly enforcing spatio-temporal and geometric consistency. Extensive experiments demonstrate that our method yields remarkable reductions of 8.37% and 31.76% in translation and rotation errors over the prior state-of-the-art, alongside 4 times inference speedup (33.6 FPS) for robust real-time bronchoscope localization. Project website: https://paulili08.github.io/GABL/.

## Metadata
- **Published**: 2026-08-07T11:20:56Z
- **Authors**: Lumin Chen, Qingyao Tian, Jinpeng Li, Haoyu Jiang, Huai Liao, Xinyan Huang, Hongbin Liu, Dong Yi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07116v1)