---
title: Beat the Counter First: A Baseline for Temporal-Graph Anomaly Detectors
published: 2026-08-16T23:39:42Z
authors: Omair Shafi Ahmed, Zohair Shafi
url: http://arxiv.org/abs/2608.15965v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beat the Counter First: A Baseline for Temporal-Graph Anomaly Detectors

## Abstract
Progress in streaming, edge-level graph anomaly detection (GAD) has been marked by increasingly elaborate architectures, from count-min-sketch chi square tests to memory-augmented attention networks. Yet the empirical gains attributable to this added complexity have not been systematically evaluated. We propose SimpleCount, a reference with no parameter fitting that selects one scalar feature per dataset from a fixed pool of counts, recencies, first-occurrence indicators, and count-derived transforms. We compare SimpleCount with two temporal-graph detector models and an IsoForest control fitted to the complete feature vector across five public datasets and one synthetic dataset. SimpleCount matches or exceeds SLADE on three of six datasets and exceeds IsoForest on all six. We report paired statistical tests and five-seed SLADE evaluations. SLADE requires 23 to 133x more wall-clock time than SimpleCount. On Synth-Triangle and an additional Synth-Quad probe, pre-event structural scores recover the planted signal at AUC up to 0.955, while all evaluated detector models remain near random. The benefit of complexity is dataset-dependent, and every claimed gain should be reported against a strong one-feature reference together with its compute cost.

## Metadata
- **Published**: 2026-08-16T23:39:42Z
- **Authors**: Omair Shafi Ahmed, Zohair Shafi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15965v1)