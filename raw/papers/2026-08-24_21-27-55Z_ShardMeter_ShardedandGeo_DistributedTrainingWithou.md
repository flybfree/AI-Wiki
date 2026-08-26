---
title: ShardMeter: Sharded and Geo-Distributed Training Without the Guesswork
published: 2026-08-24T21:27:55Z
authors: Tim Beringer, Patrick Diem, Felix Wolf, Arya Mazaheri
url: http://arxiv.org/abs/2608.23840v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ShardMeter: Sharded and Geo-Distributed Training Without the Guesswork

## Abstract
Training large-scale AI models often outgrows a single data center, demanding sharded, multi-cluster, and decentralized training. However, the huge space of resource allocations makes exhaustive benchmarking and manual tuning impractical, while performance depends on tightly coupled factors like model size, GPU memory, batch size, bandwidth, and sharding strategy. We introduce ShardMeter, a lightweight analytical performance model that predicts the end-to-end runtime of transformer-based workloads across arbitrary sharded, distributed, and even decentralized training. Given a model's characteristics and a target hardware topology, ShardMeter estimates per-GPU and per-island throughput, training cost, total wall-clock time, and identifies performance bottlenecks. Our analysis reveals diminishing-return regimes as island size increases, quantifies transitions between compute- and communication-bound scaling, evaluates hyperparameter trade-offs, and models cost-throughput for large-scale decentralized training. ShardMeter exposes these insights to quickly explore the configuration space, choose near-optimal deployment plans, and avoid costly trial and error.

## Metadata
- **Published**: 2026-08-24T21:27:55Z
- **Authors**: Tim Beringer, Patrick Diem, Felix Wolf, Arya Mazaheri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23840v1)