---
title: Flash-CNNCap: Capacitance Extraction via Image Mapping
published: 2026-07-26T22:46:20Z
authors: Hector R. Rodriguez, Jiechen Huang, Wenjian Yu
url: http://arxiv.org/abs/2607.23877v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Flash-CNNCap: Capacitance Extraction via Image Mapping

## Abstract
We present Flash-CNNCap, a CNN-based capacitance extractor that reformulates full-matrix capacitance prediction as image-to-image regression over spatial contribution maps. Prior scalar CNN-based extractors require $O(n^2)$ forward passes to recover all pairwise capacitances in a window with $n$ conductors. Flash-CNNCap replaces the scalar target with dense contribution maps: a total-capacitance model and a master-conditioned coupling model each predict a spatial map that is reduced to conductor-level values through mask aggregation, cutting full-matrix reconstruction to $O(n)$ passes. The resulting totals and symmetrized pairwise couplings define the corresponding Maxwell-style capacitance matrix under the standard off-diagonal sign convention. The maps are learned from conductor-level labels without per-pixel supervision. An ablation study over 13 model configurations selects a U-Net that matches ResNet baselines on total capacitance (1.5-3.1% MARE) and achieves the strongest coupling accuracy (3.0-4.6% MARE) across all evaluated CapBench subsets, with a $17.5\times$ full-matrix speedup on windows containing 134 conductors on average. A deployed pipeline reads Design Exchange Format (DEF) geometry and writes Standard Parasitic Exchange Format (SPEF) output, processing 1,024 windows in 51.23 seconds with a $4.4\times$ speedup over OpenRCX on the same benchmark. Code and trained models are available at https://github.com/THU-numbda/flash-cnncap.

## Metadata
- **Published**: 2026-07-26T22:46:20Z
- **Authors**: Hector R. Rodriguez, Jiechen Huang, Wenjian Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23877v1)