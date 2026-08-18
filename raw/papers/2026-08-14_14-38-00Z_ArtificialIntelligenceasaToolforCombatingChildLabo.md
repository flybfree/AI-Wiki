---
title: Artificial Intelligence as a Tool for Combating Child Labour: A Real-Time Edge Vision Pipeline for Child Detection and Age Estimation
published: 2026-08-14T14:38:00Z
authors: Mark Nowak
url: http://arxiv.org/abs/2608.14770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Artificial Intelligence as a Tool for Combating Child Labour: A Real-Time Edge Vision Pipeline for Child Detection and Age Estimation

## Abstract
An estimated 138 million children remain in child labour worldwide, and the monitoring systems used by affected sectors, built on periodic household visits and interviews, systematically under-detect them. We present a real-time computer-vision pipeline, built and operated solely as a research prototype, that studies the feasibility of giving Child Labour Monitoring and Remediation Systems (CLMRS) a continuous, presence-based evidence channel. The pipeline combines a multi-task person and face detector (YOLO26x backbone in the CerberusDet framework), cascaded age estimation pairing MiVOLO v2 with a child-specialist model for ages 0-12, ByteTrack tracking, ArcFace and DINOv2 re-identification, and track-level fusion producing reviewable per-person records. The detector raises person mAP@0.5 from 0.390 to 0.683 over the previous-generation baseline; the child specialist reaches 1.944 years MAE on children-only validation, where widely used open-source stacks err by 18-23 years. FP8 TensorRT compilation yields a 1.77x speedup at +0.002 years MAE, bringing the pipeline above twice real-time on embedded hardware. On 26.8 hours of proxy video the system finds 634 unique child candidates versus 285 for its predecessor. We further report a seventeen-day unattended field pilot on a farm in Zimbabwe (38.7 million frames, six cameras) evaluated against a daily attendance register: software tuning improved detection yield 36-fold, and identity consolidation under a simultaneity veto cut over-reporting from 9.1x to 1.8-3.9x with zero proven-false merges. We document training and quantisation failures alongside successes, and the data-protection and human-in-the-loop safeguards such a system requires.

## Metadata
- **Published**: 2026-08-14T14:38:00Z
- **Authors**: Mark Nowak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14770v1)