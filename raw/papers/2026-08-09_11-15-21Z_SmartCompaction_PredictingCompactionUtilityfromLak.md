---
title: Smart Compaction: Predicting Compaction Utility from Lakehouse Table Metadata
published: 2026-08-09T11:15:21Z
authors: Jannic Cutura, Subash Prakash
url: http://arxiv.org/abs/2608.08639v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Smart Compaction: Predicting Compaction Utility from Lakehouse Table Metadata

## Abstract
Open lakehouse table formats accumulate small data files over time, which degrades query performance. Deciding when compaction is worthwhile remains threshold-driven, but which metadata features actually determine compaction utility is not well understood. We present an open simulation framework that generates 2,376 Apache Iceberg tables spanning three orders of magnitude in file size, extracts 17 metadata features from manifest files without reading data, and trains XGBoost to predict the continuous file-reduction ratio (R2 = 0.998, RMSE= 0.013). The binary compaction decision turns out to be trivially separable by a single partition-level threshold max_files_per_partition> 4, requiring no learned model. Cross-schema validation on 96 TPC-H tables confirms generalisation without retraining (R2 = 0.976). A query benchmark reveals that compaction benefits metadata-heavy queries but can slow full-scan aggregations by reducing task parallelism. All code and data are publicly available.

## Metadata
- **Published**: 2026-08-09T11:15:21Z
- **Authors**: Jannic Cutura, Subash Prakash
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08639v1)