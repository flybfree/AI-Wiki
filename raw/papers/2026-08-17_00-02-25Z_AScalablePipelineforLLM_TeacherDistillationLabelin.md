---
title: A Scalable Pipeline for LLM-Teacher Distillation Labeling: Work-Stealing Job Scheduling and Memory-Aware GPU Concurrency
published: 2026-08-17T00:02:25Z
authors: Ravi Satya Durga Prasad Yenugula
url: http://arxiv.org/abs/2608.15975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Scalable Pipeline for LLM-Teacher Distillation Labeling: Work-Stealing Job Scheduling and Memory-Aware GPU Concurrency

## Abstract
Labeling large text corpora with LLM teachers has become a practical route to training data at scale. At millions of items, hand-labeling every batch is not feasible, and two questions dominate: what label quality a teacher buys per dollar, and how to keep a fleet of GPU workers busy under skewed, failure-prone workloads. We present a simple, reproducible pipeline that addresses both. First, a work-stealing ring pool: each worker owns a queue, drains it first, and then steals from ring successors, with exactly-once task claims via atomic conditional writes and crash tolerance via stale-claim sweeping. The claim protocol requires only a compare-and-set primitive from its storage layer; we implement it on a single SQLite file, which makes the reference implementation dependency-free and the experiments reproducible on one machine. Second, a memory-aware concurrency rule that sizes per-node parallelism by how many model copies fit on the GPU, so the same code runs safely across device sizes. Third, a relabeling benchmark methodology in which the teacher relabels a public dataset that already has gold labels, so quality reduces to an agreement measurement and cost follows from measured throughput. Under skewed load the pool sustains up to 3.4 times the throughput of static sharding while matching it at zero skew, loses 0 of 2,000 tasks when half the workers are killed mid-run (static sharding loses 953), and yields measured quality and cost points for an instruction-tuned teacher on irony and sentiment tasks. All experiments run on public data and commodity hardware; code, tests, and run logs are released.

## Metadata
- **Published**: 2026-08-17T00:02:25Z
- **Authors**: Ravi Satya Durga Prasad Yenugula
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15975v1)