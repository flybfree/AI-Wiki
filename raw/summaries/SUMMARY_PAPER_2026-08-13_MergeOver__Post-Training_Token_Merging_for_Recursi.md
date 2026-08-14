---
title: MergeOver: Post-Training Token Merging for Recursive Vision Transformers
url: http://arxiv.org/abs/2608.13141v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_12-15-10Z_MergeOver_Post_TrainingTokenMergingforRecursiveVis.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MergeOver, a post‑training method that combines token merging with recursive weight sharing in SReT Vision Transformers. It achieves a modest drop in ImageNet accuracy while cutting memory usage by over 35 % on GPUs and latency improvements on edge devices without retraining.

## Key Takeaways
- The Unmerge tracking stack enables constraint‑safe merge rates that preserve spatial relationships during token reduction.
- A single‑shot schedule reduces tokens at the first block of each stage while keeping sequence length fixed across recursive layers.
- Benchmarks show 37.3 % and 38.4 % lower peak activation memory on GPUs, with latency reductions of up to 17.6 % on a Raspberry Pi 5.

## Context
Vision Transformers dominate computer vision but are limited by high parameter counts and quadratic compute costs, especially for edge deployment. Recent work on recursive weight sharing shows promise yet often requires retraining, hindering practical integration with token merging techniques.

## Implications
MergeOver provides a baseline for combining hierarchical recursive transformers with post‑training token reduction, offering a path to more efficient vision models that can run on constrained hardware without costly re‑training pipelines. These results suggest that future models can achieve both high accuracy and low resource consumption, encouraging broader adoption of efficient vision architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13141v1)
