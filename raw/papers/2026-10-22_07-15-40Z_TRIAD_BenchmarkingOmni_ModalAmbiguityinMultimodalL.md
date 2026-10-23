---
title: TRIAD: Benchmarking Omni-Modal Ambiguity in Multimodal Large Language Models
published: 2026-10-22T07:15:40Z
authors: Zhaolu Kang, Yidi Wang, Yile Li, Siqi Zeng, Yingjie He, Richeng Xuan, Zhichao hu
url: http://arxiv.org/abs/2610.30841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRIAD: Benchmarking Omni-Modal Ambiguity in Multimodal Large Language Models

## Abstract
Ambiguity is a central feature of natural communication: a sentence, image, or sound may remain underspecified until evidence from the other channels is considered. Yet current multimodal benchmarks mostly test perception, recognition, or reasoning over already determinate inputs, leaving unclear whether omni-modal large language models can resolve ambiguity distributed across text, vision, and audio. We introduce TRIAD, a benchmark for omni-modal ambiguity resolution. Each item is a text--image--audio triplet paired with a question and a set of answer options, and is constructed so that the full triplet determines a unique answer while removing any one modality makes the set of consistent options non-unique. TRIAD contains $327$ hand-written queries in $86$ scene groups and covers $18$ ambiguity categories across the three modalities. Evaluating $14$ omni-modal systems reveals that strong item-level performance does not translate into robust scene-level disambiguation: the best model still trails humans by over $20$ points in group accuracy. Removing answer options widens the gap further, driving model group accuracy to the single digits while humans remain robust. Leave-one-out and transcript/description counterfactuals further show that current systems often underuse audio cues when text and image are present. TRIAD reframes omni-modal evaluation around disambiguation rather than recognition, and provides a taxonomy, benchmark, and diagnostic protocol for measuring this capability.

## Metadata
- **Published**: 2026-10-22T07:15:40Z
- **Authors**: Zhaolu Kang, Yidi Wang, Yile Li, Siqi Zeng, Yingjie He, Richeng Xuan, Zhichao hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30841v1)