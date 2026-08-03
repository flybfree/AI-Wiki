---
title: Cross-Resolution Semantic Learning for Graph Domain Adaptation
published: 2026-07-31T12:52:10Z
authors: Yingxu Wang, Haoze Huang, Zhongkai Zheng, Shangsong Liang
url: http://arxiv.org/abs/2607.29365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Resolution Semantic Learning for Graph Domain Adaptation

## Abstract
Graph Domain Adaptation (GDA) transfers predictive knowledge from labeled source graphs to unlabeled target graphs under distribution shift. Existing methods align representations or regularize graph structures, but do not explicitly model how class-discriminative knowledge learned at different source neighborhood ranges should be routed across target ranges. We call the neighborhood range encoded by a graph representation its propagation resolution and define semantic resolution shift as a cross-domain change in the propagation resolutions at which class-discriminative evidence is strongest. Such shifts can make fixed same-resolution pairing suboptimal and increase the risk of negative transfer. To address this issue, we propose Cross-Resolution Semantic Learning (CReSL), a GDA method that learns soft sourceto-target resolution correspondence from cross-domain class structure. First, CReSL constructs a multi-resolution representation bank using a shared Graph Neural Network and learnable resolution embeddings, with a resolution-indexed expert for each source resolution. Second, CReSL introduces Cross-Resolution Prototype Transport, which constructs class-resolution prototypes from source labels and soft target posteriors and converts cross-domain prototype discrepancies into expert-specific routing over target resolutions. Third, CReSL introduces Cross-Resolution Target Grafting, which constructs posterior-weighted target-to-source prototype displacements and enforces correspondence-weighted prediction consistency for instance-level adaptation under class uncertainty. Extensive experiments on graph benchmarks under diverse domain shifts show that CReSL outperforms strong representative baselines across most settings.

## Metadata
- **Published**: 2026-07-31T12:52:10Z
- **Authors**: Yingxu Wang, Haoze Huang, Zhongkai Zheng, Shangsong Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29365v1)