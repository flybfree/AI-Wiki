---
title: STCAD: Scalable Trajectory Clustering and Anomaly Detection on Terabyte-Scale AIS Data
published: 2026-08-10T21:32:42Z
authors: Bertram Hage, Alexander Schiøtz, Felix Thomsen, Christian Rand, Peder Heiselberg
url: http://arxiv.org/abs/2608.10249v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STCAD: Scalable Trajectory Clustering and Anomaly Detection on Terabyte-Scale AIS Data

## Abstract
We present a scalable framework for unsupervised clustering of maritime trajectories derived from terabyte-scale Automatic Identification System (AIS) archives. Variable-length trajectories are encoded with a custom BERT-based model trained via masked token modeling and clustered using CURE hierarchical clustering, producing physically interpretable trajectory groups without requiring a predefined number of clusters. An intrinsic unsupervised anomaly detection method based on reconstruction loss and clustering noise assignment identifies irregular navigation patterns. The framework is demonstrated on a national-scale AIS dataset comprising billions of messages spanning one year, yielding stable trajectory clusters and a clear separation between nominal and anomalous vessel behavior.

## Metadata
- **Published**: 2026-08-10T21:32:42Z
- **Authors**: Bertram Hage, Alexander Schiøtz, Felix Thomsen, Christian Rand, Peder Heiselberg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10249v1)