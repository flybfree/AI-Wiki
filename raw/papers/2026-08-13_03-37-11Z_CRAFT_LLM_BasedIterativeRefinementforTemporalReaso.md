---
title: CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives
published: 2026-08-13T03:37:11Z
authors: Chengyang He, Tahreem Arif, Marko Zivkovic, Lijing Wang, Yue Ning, Ping Wang
url: http://arxiv.org/abs/2608.12779v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives

## Abstract
Understanding the temporal progression of symptoms in clinical narratives is critical for disease monitoring, safety surveillance, and causality assessment. Clinical narratives, however, rarely provide explicit temporal anchors. Current approaches to temporal information reasoning focus predominantly on pairwise relation classification across multi-visit and timestamp-rich records, leaving the reconstruction of structured symptom trajectories from individual anchor-sparse reports largely unaddressed. We propose CRAFT, an LLM framework that pairs a generator with a constraint-based verifier to iteratively produce and refine stage-wise symptom timelines through targeted feedback. We conduct evaluation on MedTempo, a new benchmark of 5,347 vaccine adverse-event narratives spanning three COVID-19 vaccine types, with expert-validated temporal stage annotations for 3,166 reports. Experiments across four LLM backbones demonstrate that CRAFT consistently improves temporal ordering accuracy, with ablation analysis isolating the contribution of generator and verifier components across model capability levels.

## Metadata
- **Published**: 2026-08-13T03:37:11Z
- **Authors**: Chengyang He, Tahreem Arif, Marko Zivkovic, Lijing Wang, Yue Ning, Ping Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12779v1)