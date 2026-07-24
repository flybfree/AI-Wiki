---
title: NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework
published: 2026-07-21T09:15:06Z
authors: Yuan Gui, Hongchen Luo, Liqi Qu, Longyue Fu, Jiao Wang
url: http://arxiv.org/abs/2607.18887v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework

## Abstract
Vessel trajectory prediction in complex maritime environments is essential for traffic management, collision warning, route planning, and autonomous navigation. Although AIS-based learning methods have progressed rapidly, existing datasets are often released as raw message streams or irregular time series, with inconsistent sampling rates, noisy observations, heterogeneous coordinate systems, and non-unified scenario protocols. Most public AIS resources also lack structured representations of navigational lanes, waterway geometry, and navigable-region constraints, limiting reproducible, environment-aware forecasting. To address this, we introduce NaviAIS, a standardized scenario-level AIS dataset for vessel trajectory prediction. It organizes multi-vessel historical-future trajectories within unified temporal windows and local coordinate systems, and provides rasterized navigable maps, vectorized lane priors, lane graphs, and structured map representations. Compared with existing datasets, it jointly supports vectorized lanes, multi-scenario coverage, vectorized maps, open accessibility, and processed trajectories. Built on this dataset, we propose NaviLane, a hierarchical macro-action framework for map-aware prediction. NaviLane first performs trajectory-map joint encoding for a unified scene representation, then uses a discrete macro-action codebook to generate multimodal candidates coarse-to-refined. A residual refinement module improves local geometric and dynamical consistency, and a world-model-based consequence-aware evaluator ranks candidates by interaction risk and environmental feasibility. Experiments show NaviLane outperforms representative baselines in both single-modal and multimodal settings, confirming the value of structured navigational priors, hierarchical multimodal generation, and consequence-aware evaluation.

## Metadata
- **Published**: 2026-07-21T09:15:06Z
- **Authors**: Yuan Gui, Hongchen Luo, Liqi Qu, Longyue Fu, Jiao Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18887v1)