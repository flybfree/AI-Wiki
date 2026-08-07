---
title: A Unified Framework for Trajectory Prediction with Explicit Planning and Reaction Decomposition
published: 2026-08-06T07:13:26Z
authors: Jiaheng Chen, Jiaxing Li, Tinghe Zhang, Chaopeng Guo
url: http://arxiv.org/abs/2608.05673v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Unified Framework for Trajectory Prediction with Explicit Planning and Reaction Decomposition

## Abstract
Trajectory prediction has shifted toward structured formulations with explicit social modeling. However, existing methods inadequately distinguish the functional roles of social influence in trajectory planning. Observing that agents typically form motion plans by anticipating others' future behaviors before making local reactive adjustments, we identify social interactions as playing staged roles, namely planning precedes reaction. We propose INTraJ, a unified framework that decomposes social influence into two stages: a planning stage constructs reference trajectories using future social information, and a reaction stage recovers local adjustments from the residual between full-context prediction and the reference. INTraJ supports both multi-target and single-target paradigms. Extensive experiments on four standard benchmarks, including Argoverse 2, Argoverse 2-ped, ETH/UCY, and SDD, demonstrate consistent improvements, particularly in FDE and long-horizon consistency, with state-of-the-art performance achieved in several settings. INTraJ reframes trajectory prediction as a planning-driven two-stage process, validating that staged social modeling is critical for stable predictions. The code is publicly available at https://github.com/11isnotavailable/INTraJ.

## Metadata
- **Published**: 2026-08-06T07:13:26Z
- **Authors**: Jiaheng Chen, Jiaxing Li, Tinghe Zhang, Chaopeng Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05673v1)