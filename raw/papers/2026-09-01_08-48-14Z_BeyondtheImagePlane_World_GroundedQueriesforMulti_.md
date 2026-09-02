---
title: Beyond the Image Plane: World-Grounded Queries for Multi-Object Tracking
published: 2026-09-01T08:48:14Z
authors: Orcun Cetintas, Guillem Brasó, Tim Meinhardt, Laura Leal-Taixé
url: http://arxiv.org/abs/2609.00924v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Image Plane: World-Grounded Queries for Multi-Object Tracking

## Abstract
Monocular videos record 3D scenes as sequences of 2D image-plane projections, obscuring depth and spatial relationships. Multi-object trackers localize and associate objects primarily using appearance and geometry observed only in the image plane, inheriting these ambiguities. To address this limitation, we introduce PLANET, an end-to-end multi-object tracker designed to move beyond the image plane. As an enabling step, we lift existing 2D tracking datasets into 3D. We then form world-grounded queries by embedding reconstructed 3D scene geometry into the features and positional encodings used during query formation. An auxiliary 3D location prediction task further encourages the queries to encode object positions during training. A complementary dual-resolution temporal memory preserves this evidence across longer temporal gaps. As a result, PLANET achieves state-of-the-art performance across three diverse benchmarks.

## Metadata
- **Published**: 2026-09-01T08:48:14Z
- **Authors**: Orcun Cetintas, Guillem Brasó, Tim Meinhardt, Laura Leal-Taixé
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00924v1)