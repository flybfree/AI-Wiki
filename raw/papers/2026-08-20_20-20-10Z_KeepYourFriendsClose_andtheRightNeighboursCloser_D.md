---
title: Keep Your Friends Close, and the Right Neighbours Closer: Disaster-Conditioned Kernel-Regularized Graph Attention for Building Damage Classification
published: 2026-08-20T20:20:10Z
authors: Fuad Hasan, Chul Min Yeum
url: http://arxiv.org/abs/2608.20548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Keep Your Friends Close, and the Right Neighbours Closer: Disaster-Conditioned Kernel-Regularized Graph Attention for Building Damage Classification

## Abstract
Disaster damage is spatial: buildings rarely fail in isolation. Yet using spatial context for damage classification remains surprisingly underexplored, and many pipelines still rely primarily on per-building appearance cues even when the dominant uncertainty is spatially structured. Complicating matters, the right neighbourhood is not the same across events. Floods, hurricanes, and wildfires can exhibit very different clustering behaviour, making spatial reasoning valuable but easy to misuse - naive context aggregation can improve visual coherence while oversmoothing boundaries or propagating structured errors. We study this tension on xBD (the dataset used in the xView2 challenge) in a controlled post-localization, classification-only setup: each building is represented by a pre/post combined (PPC) patch cropped from the provided polygons, and spatial context is modelled with GPS-derived building graphs. Our approach keeps local evidence "close" by preserving strong spatial relationships in disaster damage patterns, while bringing only the right neighbours "closer" through a disaster-type-conditioned graph model that injects a learnable multi-scale spatial kernel prior into attention, allowing the effective neighbourhood scale to adapt across disaster types rather than being learned as a single global smoothing rule. To discourage coherence-by-smoothing, we add a residual de-correlation loss that penalizes positive Moran's~I in prediction residuals. We evaluate the method under event and dataset shift with a leave-one-event-out (LOEO) protocol on xBD and cross-dataset transfer from xBD to Ida-BD. The model improves macro-F1 and substantially reduces residual spatial autocorrelation under zero-shot event shift, indicating better use of spatial context rather than naive smoothing and enabling more reliable transfer to unseen events within known disaster types.

## Metadata
- **Published**: 2026-08-20T20:20:10Z
- **Authors**: Fuad Hasan, Chul Min Yeum
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20548v1)