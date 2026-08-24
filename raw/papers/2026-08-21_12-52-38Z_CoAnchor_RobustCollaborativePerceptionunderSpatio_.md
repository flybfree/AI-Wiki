---
title: CoAnchor: Robust Collaborative Perception under Spatio-Temporal Misalignment via Object-Level Anchors
published: 2026-08-21T12:52:38Z
authors: Chi Li, Rui Lin, Aobo Ji, Dongzhu Xu
url: http://arxiv.org/abs/2608.21055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoAnchor: Robust Collaborative Perception under Spatio-Temporal Misalignment via Object-Level Anchors

## Abstract
Collaborative perception extends the sensing range of a single vehicle by fusing observations from nearby agents, which improves the robustness of autonomous driving. In realistic deployments, however, the received collaborator messages are often affected by both communication delay and relative-pose noise, which jointly cause stale observations, spatial misalignment, and unstable feature fusion. Existing methods usually address these issues from either the spatial or temporal side, but handling them jointly in a unified and efficient manner remains challenging. In this paper, we propose CoAnchor, an anchor-centric spatio-temporal alignment framework for asynchronous collaborative perception. Instead of directly reasoning on dense BEV features, CoAnchor builds sparse object-level spatio-temporal anchors as a shared interface for pose correction and tightly connects spatial refinement, temporal propagation, and current-time verification within one unified loop, while keeping the overall correction process lightweight. Extensive experiments on both simulated and real-world datasets illustrate that CoAnchor remains competitive under clean settings and improves the robustness under joint delay and pose perturbations with a favorable practical accuracy-efficiency trade-off.

## Metadata
- **Published**: 2026-08-21T12:52:38Z
- **Authors**: Chi Li, Rui Lin, Aobo Ji, Dongzhu Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21055v1)