---
title: Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking
published: 2026-08-09T11:41:57Z
authors: Zhifeng Chu, Bin Wang
url: http://arxiv.org/abs/2608.08646v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking

## Abstract
Trajectory-User Linking (TUL) aims to identify the owner of an anonymous trajectory from a set of candidate users, providing a basis for user mobility analysis and personalized location-aware services. Existing methods often learn Point of Interest (POI), temporal, and semantic features independently, make limited use of structural knowledge shared across trajectories, and compress structural and sequential information before classification. To address these issues, we propose Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking (MakeTUL), which, to the best of our knowledge, is the first attempt to introduce knowledge graph representation learning into TUL. MakeTUL organizes visit-time, POI-category, and transfer-speed information as typed relations in a multi-relational mobility knowledge graph, allowing heterogeneous mobility semantics to jointly constrain the learned embeddings. The resulting POI representations are further enriched with high-order co-occurrence patterns extracted from the trajectory collection, providing structural prior knowledge for sparse and overlapping trajectories. By integrating these prior-enhanced representations with temporal, category, and transfer information, the trajectory sequence learning module captures ordered mobility patterns, while a dual-branch classification layer preserves and combines global structural evidence and sequential evidence at the decision level.

## Metadata
- **Published**: 2026-08-09T11:41:57Z
- **Authors**: Zhifeng Chu, Bin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08646v1)