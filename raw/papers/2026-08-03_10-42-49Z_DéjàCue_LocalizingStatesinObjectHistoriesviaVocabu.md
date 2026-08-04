---
title: Déjà Cue: Localizing States in Object Histories via Vocabulary-Relative Coordinates
published: 2026-08-03T10:42:49Z
authors: Haofan Cao, Zhichao You, Yunkai Yang, Liang Guo, Jie Wang, Chongshou Li
url: http://arxiv.org/abs/2608.02044v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Déjà Cue: Localizing States in Object Histories via Vocabulary-Relative Coordinates

## Abstract
Tracking links observations of the same object through visual change, yet cannot by itself determine when the object is empty or filled, intact or cut. We formulate identity-conditioned state-moment retrieval: given a tracked-object history and alternative state descriptions, localize an interval in which each described state holds. Absolute image-text similarity scores descriptions independently; because every visible frame depicts the same target, shared object compatibility can obscure the state evidence needed to identify the target interval. The alternatives provide the missing reference: evidence for one state should be measured against the others. We introduce Déjà Cue, a training-free framework that turns these alternatives into a vocabulary-relative coordinate system. It subtracts their state-balanced centroid from each description, calibrates frame scores, and scans multiple durations within contiguous visible runs using a frozen encoder. On 78 VOST histories, holding the temporal scan fixed and changing only the query reference nearly doubles R@1 at tIoU 0.5 from 10.3\% to 20.5\% and raises Top-1 tIoU from 16.0\% to 21.5\%. Candidate-rank analyses show that vocabulary-relative queries rank useful intervals higher within the same candidate set. Related state descriptions can therefore serve as an object-specific, query-time coordinate system for reading frozen visual representations.

## Metadata
- **Published**: 2026-08-03T10:42:49Z
- **Authors**: Haofan Cao, Zhichao You, Yunkai Yang, Liang Guo, Jie Wang, Chongshou Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02044v1)