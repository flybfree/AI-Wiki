---
title: Masked Topology Modeling for Self-Supervised Learning on Parametric CAD
published: 2026-07-22T18:13:08Z
authors: Heinrich Jiang, Jennifer Jang
url: http://arxiv.org/abs/2607.20642v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Masked Topology Modeling for Self-Supervised Learning on Parametric CAD

## Abstract
Computer aided design (CAD) is ubiquitous: virtually any modern object was designed using editable CAD tools. However, with the shortage of available CAD datasets in its native editable and parametric format, boundary representation (B-Rep), it is ever more important to develop data-efficient methods for this domain.   We present a new self-supervised pretraining task, Masked Topology Modeling (MTM), that leverages the face-adjacency graph, an induced structure unique to B-reps that the encoder can be asked to reconstruct. MTM masks a fraction of edges and trains a small head to predict each masked edge's convexity and curve type from the encoder's post-message-passing face features.   We combine MTM with a MoCo-style momentum-queue contrastive learning over B-rep-aware augmentations, a BFS-connected face-region masked-reconstruction objective, and pretraining on the ABC dataset and our new procedurally generated dataset to show strong performance on a number of benchmarks.

## Metadata
- **Published**: 2026-07-22T18:13:08Z
- **Authors**: Heinrich Jiang, Jennifer Jang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20642v1)