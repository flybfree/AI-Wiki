---
title: Rethinking Reservoir Pruning: A Dynamical Perspective for Echo State Networks
published: 2026-08-05T08:56:17Z
authors: Sudip Laudari, Puspa Raj Adhikari
url: http://arxiv.org/abs/2608.04593v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Reservoir Pruning: A Dynamical Perspective for Echo State Networks

## Abstract
Echo State Networks (ESNs) offer an efficient framework for temporal prediction, but their randomly initialized reservoirs are often over-parameterized and dynamically redundant. Existing pruning methods largely rely on static connectivity or activation statistics, which may overlook neurons that shape input-driven state transitions. We propose Dynamical Mode Pruning (DMP), a reservoir pruning method that ranks neurons by their contribution to dominant transition modes obtained from a trajectory-averaged Jacobian Gramian. DMP removes low-impact units and retrains only the readout. Experiments on chaotic and real-world time-series benchmarks show that DMP improves or preserves forecasting accuracy while reducing redundant reservoir components. Our results suggest that dynamical influence is a useful criterion for reservoir refinement beyond static structural importance alone.

## Metadata
- **Published**: 2026-08-05T08:56:17Z
- **Authors**: Sudip Laudari, Puspa Raj Adhikari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04593v1)