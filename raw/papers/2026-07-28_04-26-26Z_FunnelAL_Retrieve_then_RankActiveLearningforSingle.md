---
title: FunnelAL: Retrieve-then-Rank Active Learning for Single-Class Discovery
published: 2026-07-28T04:26:26Z
authors: Reihaneh Rostami, Brian Goodwin
url: http://arxiv.org/abs/2607.25276v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FunnelAL: Retrieve-then-Rank Active Learning for Single-Class Discovery

## Abstract
We present FunnelAL, a retrieve-then-rank active learning system for single-class discovery, which adapts the multi-stage funnel architecture of industrial recommender systems to data annotation. Large-scale supervised learning faces two challenges: efficiently finding relevant samples in a massive corpus, and distinguishing true positives from visually confusable negatives when embeddings do not cleanly separate classes. Conventional active learning offers a principled framework for reducing annotation cost, yet it treats sample selection as a single-stage process that addresses neither challenge efficiently. FunnelAL decomposes the problem into cascaded stages. Starting from a single positive and negative example, the system iterates through: (1) embedding-based retrieval scoring that narrows the corpus to a manageable candidate set; (2) a precision-triggered ranking stage that exploits a learned ranker (RankNet) while batch precision remains high, then automatically blends in committee-based exploration (QBC) once returns diminish; and (3) feedback from the annotator's labels that refines both stages in subsequent iterations. We evaluate on three diverse image classification benchmarks. With a perfect annotator, FunnelAL attains the best final F1 on all three benchmarks, the best annotation efficiency (first in AULC), and the fewest annotation rounds. The most recent single-class discovery methods (GAL, PF-MA) at best match its final quality, and only at consistently higher labeling cost. Under annotator labeling errors at realistic rates, FunnelAL remains first or statistically tied for first while classical uncertainty-based methods degrade two to three times faster. Our work provides a concrete bridge between multi-stage recommender systems and active learning.

## Metadata
- **Published**: 2026-07-28T04:26:26Z
- **Authors**: Reihaneh Rostami, Brian Goodwin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25276v1)