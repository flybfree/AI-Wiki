---
title: When More References Hurt: Contamination-Aware DINOv2 Memory Banks for Few-Shot Steel Defect Detection
published: 2026-08-22T19:02:40Z
authors: Hannaneh Kalantari, Javad Khoramdel
url: http://arxiv.org/abs/2608.22082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When More References Hurt: Contamination-Aware DINOv2 Memory Banks for Few-Shot Steel Defect Detection

## Abstract
Patch-memory anomaly detectors assume that their reference bank is normal, an assumption that is difficult to guarantee when additional industrial images are unverified. We study whether a few trusted normal images can safely recover useful normal patches from such references without defect masks. Starting from the DINOv2 patch-memory formulation used by AnomalyDINO, we score candidate patches by distance to a clean seed bank, discard the most suspicious 20%, merge the retained patches with the seed, and enforce a fixed budget by greedy coreset selection. On Severstal, naive additional references contain 9.46% anomalous patches; the proposed trim rejects 78.1\% of them and reduces residual contamination to 2.59%. At an equal 51,200-patch development budget, the proposed bank reaches 0.1084 AUPRC versus 0.0950 for naive expansion, 0.0952 for random removal, and 0.1030 for eight clean images. Injecting only 0.5\% anomalous patches into a clean bank reduces AUPRC from 0.1030 to 0.0759. On all five completed held-out pairs, the proposed bank improves over naive expansion, with a mean gain of 0.0142 AUPRC. Reference purity is therefore a first-order design variable, and unverified images are useful only when their contribution is filtered explicitly.

## Metadata
- **Published**: 2026-08-22T19:02:40Z
- **Authors**: Hannaneh Kalantari, Javad Khoramdel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22082v1)