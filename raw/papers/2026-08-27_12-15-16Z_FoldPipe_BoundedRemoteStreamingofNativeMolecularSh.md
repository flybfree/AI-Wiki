---
title: FoldPipe: Bounded Remote Streaming of Native Molecular Shards with Asynchronous Prefetch
published: 2026-08-27T12:15:16Z
authors: Dhiren Mukesh Khatri
url: http://arxiv.org/abs/2608.27029v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FoldPipe: Bounded Remote Streaming of Native Molecular Shards with Asynchronous Prefetch

## Abstract
Training molecular machine-learning models on ephemeral or memory-constrained accelerator instances can require repeatedly retrieving preprocessed molecular graphs from remote storage. FoldPipe is a lightweight Python orchestration layer for already-sharded PyTorch and PyTorch Geometric data. It retrieves one shard ahead in a background thread while the consumer trains on the current shard, keeping the number of live shard payloads bounded with respect to total dataset size.   Asynchronous prefetch and bounded buffering are established systems techniques rather than novel scheduling algorithms. FoldPipe's contribution is a small integration targeted at native .pt molecular shards together with a source-pinned empirical characterization of its operating regime.   We evaluate a SchNet energy-and-force workload on MD17 aspirin using 20 paired, order-alternating benchmark passes on a Tesla T4. Each pass processes five pinned shards containing 25,000 structures. FoldPipe records 16.33 s mean I/O-compute overlap, compared with zero by construction for the sequential bounded baseline. Mean pass time is 76.78 s for FoldPipe and 83.37 s for the baseline. However, the geometric mean paired speedup is $1.059\times$ with a 95% bootstrap interval from $0.878\times$ to $1.288\times$. The experiment therefore verifies the overlap mechanism but is inconclusive about a reliable wall-clock speed advantage under the observed public-network variability.

## Metadata
- **Published**: 2026-08-27T12:15:16Z
- **Authors**: Dhiren Mukesh Khatri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27029v1)