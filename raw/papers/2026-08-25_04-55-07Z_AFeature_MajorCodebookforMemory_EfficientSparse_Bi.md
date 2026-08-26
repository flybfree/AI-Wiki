---
title: A Feature-Major Codebook for Memory-Efficient Sparse-Binary Self-Organizing Maps: Scaling a MEDLINE Atlas to 1.05 Million Neurons on a Single Consumer GPU
published: 2026-08-25T04:55:07Z
authors: Andrew James Amos
url: http://arxiv.org/abs/2608.24067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Feature-Major Codebook for Memory-Efficient Sparse-Binary Self-Organizing Maps: Scaling a MEDLINE Atlas to 1.05 Million Neurons on a Single Consumer GPU

## Abstract
A self-organising map turns a large corpus into a browsable two-dimensional atlas, but building one at MEDLINE scale has been impractical: the best-matching-unit (BMU) search that dominates training is bound by the bandwidth needed to read the codebook every epoch. I show that this bottleneck is largely an artefact of codebook layout. Storing it feature-major with each feature's weights contiguous, W[v.M+i], recasts the search as a tiled sparse-dense product in which every loaded weight column is reused across a tile of samples. Varying only the layout, with implementation, precision and update rule held fixed, accelerates the BMU search by 4.5-8.5x. Because an exact-argmin BMU is invariant to how the codebook is stored, this gain costs nothing: held-out quantisation error agrees with a cuSPARSE baseline to within 0.5% at every map size. Against that baseline the advantage is a crossover rather than a constant: cuSPARSE.SOM is faster at small maps, SparseBin.SOM is 1.5x faster at 128x128 and 2.6x at 256x256, and at 512x512 it is the only one that runs at all on 24 GB. Paired with a radius-independent box-blur update and a convergence-based stopping rule, it trains a converged map over 29.9 million MEDLINE articles in about 72 s at 64x64 on one 24 GB GPU, and accommodates 262,144 neurons (512x512 edges) where every alternative algorithm I tested exceeds memory constraints. On a 141 GB H200 it reaches 1,048,576 neurons (1024x1024 edges) - to my knowledge the largest self-organising map yet reported. Held-out error follows a smooth power law with no elbow across three decades of map size, so the limit on resolution is compute rather than any breakpoint in the data. At matched work the design is ~82x faster than MedSOM, the CUDA implementation behind our earlier MEDLINE atlases and, at 128x128, 621x faster than the best available multicore-CPU library.

## Metadata
- **Published**: 2026-08-25T04:55:07Z
- **Authors**: Andrew James Amos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24067v1)