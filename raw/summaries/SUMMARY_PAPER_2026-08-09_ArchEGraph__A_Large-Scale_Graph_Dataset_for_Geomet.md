---
title: ArchEGraph: A Large-Scale Graph Dataset for Geometry-Topology-Physics Aligned Building Energy Modeling
url: http://arxiv.org/abs/2608.06772v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_03-45-41Z_ArchEGraph_ALarge_ScaleGraphDatasetforGeometry_Top.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ArchEGraph, a large-scale benchmark dataset that maps building geometry to energy performance through graph representation. It contains 5,481 buildings and 49,326 validated weather cases with over 133,000 space nodes and 1.44 million face nodes. The authors define two tasks: reconstructing topology from meshes and predicting zone-level loads using topology and weather.

## Key Takeaways
- ArchEGraph provides a heterogeneous graph dataset linking geometry, topology, weather, and thermal loads for building energy modeling.
- It enables reconstruction of topological structure directly from polygonal mesh representations.
- The dataset supports forecasting zone-level response time series by integrating temporal weather conditions with graph topology.

## Context
This work addresses the need for large-scale, physically grounded datasets in AI-driven design feedback. By aligning geometry and physics, it creates a testbed that can evaluate how machine learning models capture real-world building behavior across climates and designs.

## Implications
Architects and engineers can use ArchEGraph to calibrate surrogate models that offer rapid energy predictions. The dataset’s cross-building and cross-climate experiments demonstrate model robustness, supporting scalable solutions for sustainable design and carbon‑neutral buildings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06772v1)
