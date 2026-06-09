---
title: Random-Set Graph Neural Networks
published: 2026-05-12T11:38:13Z
authors: Tommy Woodley, Shireen Kudukkil Manchingal, Matteo Tolloso, Davide Bacciu, Fabio Cuzzolin
url: http://arxiv.org/abs/2605.11987v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Random-Set Graph Neural Networks

## Abstract
Uncertainty quantification has become an important factor in understanding the data representations produced by Graph Neural Networks (GNNs). Despite their predictive capabilities being ever useful across industrial workspaces, the inherent uncertainty induced by the nature of the data is a huge mitigating factor to GNN performance. While aleatoric uncertainty is the result of noisy and incomplete stochastic data such as missing edges or over-smoothing, epistemic uncertainty arises from lack of knowledge about a system or model (e.g., a graph's topology or node feature representation), which can be reduced by gathering more data and information. In this paper, we propose an original new framework in which node-level epistemic uncertainty is modelled in a belief function (finite random set) formalism. The resulting Random-Set Graph Neural Networks have a belief-function head predicting a random set over the list of classes, from which both a precise probability prediction and a measure of epistemic uncertainty can be obtained. Extensive experiments on 9 different graph learning datasets, including real-world autonomous driving benchmarks as such Nuscene and ROAD, demonstrate RS-GNN's superior uncertainty quantification capabilities

## Metadata
- **Published**: 2026-05-12T11:38:13Z
- **Authors**: Tommy Woodley, Shireen Kudukkil Manchingal, Matteo Tolloso, Davide Bacciu, Fabio Cuzzolin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.11987v1)