---
title: D-CLOT: Double Closed Loop Optimal Transport for Unsupervised Action Segmentation
published: 2026-08-06T10:59:28Z
authors: Elena Bueno-Benito, Mariella Dimiccoli
url: http://arxiv.org/abs/2608.05877v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D-CLOT: Double Closed Loop Optimal Transport for Unsupervised Action Segmentation

## Abstract
Optimal transport (OT) has emerged as an effective framework for unsupervised action segmentation. Yet, in existing OT-based methods, the latent action prototypes that define the OT costs are not re-estimated from the refined frame geometry. Instead, they evolve solely through gradients from the pseudo-label loss. We identify this \emph{representation--prototype inconsistency} as a central bottleneck, particularly around ambiguous transitions and for short or infrequent actions. To address this issue, we build on the recently introduced CLOT, which refines frame embeddings based on estimated segment embeddings, and further re-estimates the action prototypes from the refined frame embeddings. Specifically, we introduce a graph-constrained module that regularizes the OT-refined frame and segment representations by preserving the local neighborhood geometry of the encoder output. An action-embedding refinement step then periodically re-anchors the prototypes to this stabilized representation geometry. We study two instantiations that share the same backbone, graph module, and objective: D-CLOT updates the prototypes using $k$-means, whereas D-CLOT$_{B}$ updates them as OT barycenters weighted by the refined transport plan, yielding an assignment-aware prototype update consistent with the current transport geometry. Across five established benchmarks, both variants improve segment-level quality over CLOT, with per-video gains of up to $+12.7$ F1 and $+10.2$ mIoU (YTI) and activity-level gains of up to $+8.9$ F1 (FS-Eval). We further establish the first unsupervised action-segmentation baseline on Assembly101, a procedural and substantially more fine-grained benchmark than those commonly used in prior work. Extensive ablations and sensitivity analyses demonstrate that the two refinement mechanisms are complementary and robust.

## Metadata
- **Published**: 2026-08-06T10:59:28Z
- **Authors**: Elena Bueno-Benito, Mariella Dimiccoli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05877v1)