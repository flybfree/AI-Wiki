---
title: OceanLight: Efficient Global Ocean Forecasting via Geometry-Adaptive Unstructured Mesh Representation
published: 2026-08-17T04:03:30Z
authors: Wei Wu, Xiang Wang, Hongze Leng, Qingye Min, Junxing Zhu, Junqiang Song
url: http://arxiv.org/abs/2608.16070v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OceanLight: Efficient Global Ocean Forecasting via Geometry-Adaptive Unstructured Mesh Representation

## Abstract
Reliable global ocean forecasting is critical for climate monitoring, marine navigation, and extreme event early warning. Physics-based ocean forecasting models impose prohibitive computational costs, while existing deep learning approaches predominantly rely on structured-grid architectures, incurring unnecessary computation on masked land cells and enforcing uniform resolution across dynamically heterogeneous ocean regions regardless of local flow complexity. Here we present OceanLight, an efficient global ocean forecasting framework innovatively combining geometry-adaptive unstructured mesh tokenization with a graph neural network (GNN) backbone. OceanLight achieves pointwise forecast accuracy and kinetic energy spectral fidelity exceeding both operational numerical analyses and state-of-the-art AI-based models, while surpassing all AI-based ocean models in geostrophic balance consistency. Furthermore, OceanLight demonstrates reliable mesoscale eddy representation, capturing coherent ocean structures beyond pointwise statistical optimization. These capabilities are delivered with a 62% reduction in GPU memory consumption and 70\% reduction in FLOPs relative to structured-grid baselines. Our unstructured mesh representation establishes a generalizable paradigm for scalable data-driven oceanography.

## Metadata
- **Published**: 2026-08-17T04:03:30Z
- **Authors**: Wei Wu, Xiang Wang, Hongze Leng, Qingye Min, Junxing Zhu, Junqiang Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16070v1)