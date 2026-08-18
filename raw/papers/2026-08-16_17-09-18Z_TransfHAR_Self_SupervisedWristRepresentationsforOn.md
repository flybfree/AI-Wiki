---
title: TransfHAR: Self-Supervised Wrist Representations for On-Demand Activity Recognition
published: 2026-08-16T17:09:18Z
authors: Aidan Bradshaw, Riku Arakawa, Xin Liu, Karan Ahuja
url: http://arxiv.org/abs/2608.15861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TransfHAR: Self-Supervised Wrist Representations for On-Demand Activity Recognition

## Abstract
Fine-grained wrist activity recognition can support applications such as procedural step guidance and context-aware assistance, yet acquiring labeled data for every new task, user, and activity granularity remains a bottleneck. We present TransfHAR, a self-supervised wrist IMU framework for on-demand, fine-grained activity recognition by learning transferable motion priors from global, unlabeled activities. We show that self-supervised pretraining on coarse wrist IMU activities (e.g., sitting, walking, exercise) learns motion structure rich enough to transfer to fine-grained manipulative, gestural, and procedural activities (e.g., snapping, stirring, waving) that are absent from pretraining. We implement TransfHAR as a real-time smartwatch application that lets users define and expand their own activity set for personalized recognition from only a few demonstrations. Across three offline cross-dataset evaluations, TransfHAR matches or exceeds fully supervised baselines that use complete label sets with equal or additional sensor channels, by 6.2 balanced-accuracy points on average. In an in-lab study with 10 participants each performing seven novel wrist activities, TransfHAR reaches 86.7% balanced accuracy across participants with five examples per class and 90.4% when updated from a single one-minute recording per class. These results indicate that broad self-supervised wrist pretraining provides an effective foundation for on-demand fine-grained activity recognition.

## Metadata
- **Published**: 2026-08-16T17:09:18Z
- **Authors**: Aidan Bradshaw, Riku Arakawa, Xin Liu, Karan Ahuja
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15861v1)