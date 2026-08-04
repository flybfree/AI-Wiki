---
title: Geometry-Guided Layerwise FFN Width Allocation in Transformers
published: 2026-08-03T11:08:58Z
authors: Timur Mudarisov, Mikhail Burtsev, Radu State
url: http://arxiv.org/abs/2608.02064v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Geometry-Guided Layerwise FFN Width Allocation in Transformers

## Abstract
Feed-forward networks (FFNs) account for a large fraction of Transformer parameters, yet their hidden width is usually constant across depth. We ask whether this capacity can instead be allocated from a forward-pass measurement of layer behavior. We view each FFN as transporting a cloud of token representations and quantify the induced geometric change using correspondence-preserving shift, Gromov-Wasserstein distortion, and degree-one persistent homology under raw and scale-normalized metrics. A layerwise approximation surrogate yields an exact fixed-budget optimizer. Across seven pretrained language models, raw Euclidean work largely tracks residual-norm growth, whereas normalized work is predominantly front-loaded. Gromov-Wasserstein work is more consistently associated with perturbation-based layer sensitivity than the finite-sample topological estimate. In paired 128M and 256M training runs, several normalized-work schedules reduce mean validation loss relative to both uniform width and a hand-designed cosine taper. With the amplified paired differences at 440M, the best geometry-based allocations improve over uniform substantially larger than the cosine taper, while the anti-topological raw control is worse than uniform.

## Metadata
- **Published**: 2026-08-03T11:08:58Z
- **Authors**: Timur Mudarisov, Mikhail Burtsev, Radu State
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02064v1)