---
title: NeuRoute: Logit-Guided Neural Routing for Billion-Scale Vector Search with Sub-Hour Index Construction
published: 2026-08-15T22:44:10Z
authors: Xingqiao Wang, Zi Wang, Xiaowei Xu
url: http://arxiv.org/abs/2608.15438v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeuRoute: Logit-Guided Neural Routing for Billion-Scale Vector Search with Sub-Hour Index Construction

## Abstract
Building approximate nearest neighbor (ANN) indexes at billion scale is often dominated by expensive global clustering or graph construction, making time-to-index a first-order systems concern. We present NeuRoute, a learned hashing index that turns short binary codes into an effective routing primitive for large-scale vector search. NeuRoute trains a lightweight neural network encoder with a selective similarity-preserving objective to produce well-balanced binary addresses. During construction, NeuRoute organizes vectors into buckets by their codes and performs bucket-local clustering in the encoder's low-dimensional space to form centroids. At query time, NeuRoute exploits the encoder logits as an uncertainty signal: it uses deviation-to-threshold scores to prioritize uncertain-bit perturbations for query-adaptive multi-bucket probing, scores bucket-local centroids by their distances to the query to form a compact candidate cluster set, and applies centroid-stage gating with heap-quality-driven early stopping to prune low-value clusters before exact refinement. On billion-scale benchmarks, NeuRoute achieves strong accuracy-throughput trade-offs with fast index construction: on BigANN-1B it reaches $90.3\%$ Recall@10 at 2,414 QPS and is $1.7\times$ faster than OPQ+IVF-PQ (refine) at comparable accuracy, while completing end-to-end training+construction in under an hour on both BigANN-1B and Deep1B-1B. These results show that logit-guided neural routing can make hashing competitive as a lightweight ANN indexing framework at billion scale. Source code and artifacts are available at https://github.com/XingqiaoWang/NeuRoute.

## Metadata
- **Published**: 2026-08-15T22:44:10Z
- **Authors**: Xingqiao Wang, Zi Wang, Xiaowei Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15438v1)