---
title: Scalable Frequency- and Length-Aware Subdocument Deduplication for Large Language Model Pretraining
published: 2026-08-04T04:02:28Z
authors: Hai Wang, Chenhao Wang, Qifeng Cai, Yixiu Liu, Miao Peng, Nuo Chen, Yuanlin Tu, Chengcheng Xu, Feng Zhang
url: http://arxiv.org/abs/2608.03089v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scalable Frequency- and Length-Aware Subdocument Deduplication for Large Language Model Pretraining

## Abstract
Large-scale pretraining corpora contain substantial duplicate content. Although document-level deduplication is widely used, removing subdocument-level redundancy remains challenging. At corpus scale, suffix-array-based methods are commonly applied independently within shards, leaving cross-shard duplicates undetected and making the resulting retention behavior sensitive to the sharding configuration. Hash-based methods enable global exact duplicate counting, but often rely on fixed copy-retention policies that cannot accommodate heterogeneous repetition patterns. We propose a scalable subdocument deduplication framework that decouples duplicate detection from copy retention. It identifies duplicate groups through natural-boundary segmentation, normalized exact hashing, and distributed aggregation, and then applies an explicit frequency- and length-aware retention policy that allocates an adaptive copy budget to each group, retaining more copies of low-frequency or short repetitions while more aggressively deleting high-frequency or long ones. Experiments on FineWeb-Edu and a code-containing web corpus show that models trained on data processed by our method achieve the best overall performance among the evaluated settings. These results underscore the importance of explicit copy-retention control.

## Metadata
- **Published**: 2026-08-04T04:02:28Z
- **Authors**: Hai Wang, Chenhao Wang, Qifeng Cai, Yixiu Liu, Miao Peng, Nuo Chen, Yuanlin Tu, Chengcheng Xu, Feng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03089v1)