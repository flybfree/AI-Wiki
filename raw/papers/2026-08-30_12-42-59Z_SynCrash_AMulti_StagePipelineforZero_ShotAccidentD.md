---
title: SynCrash: A Multi-Stage Pipeline for Zero-Shot Accident Detection and Localization in Traffic Surveillance Video
published: 2026-08-30T12:42:59Z
authors: Arkya Jyoti Bagchi, Ritul Jangir, Varun Raskar
url: http://arxiv.org/abs/2608.29759v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SynCrash: A Multi-Stage Pipeline for Zero-Shot Accident Detection and Localization in Traffic Surveillance Video

## Abstract
We present SynCrash, a multi-stage pipeline for zero-shot accident detection, spatial localization, and collision-type classification in fixed-view CCTV surveillance video. Our approach addresses the ACCIDENT at CVPR 2026 Challenge, which requires predicting when an accident occurs, where in the frame the impact happens, and what type of collision it is, all without access to labeled real-world training data. The pipeline operates in three decoupled stages: (1) Temporal localization via a VideoMAEv2-giant backbone fine-tuned on CARLA-based synthetic clips with metadata-aware embeddings and dense sliding-window inference; (2) Spatial localization using YOLO for object detection combined with a physics-informed hybrid heuristic that leverages bounding-box overlap and trajectory-based reasoning to predict the impact point; and (3) Collision-type classification using a lightweight rule-based strategy derived from the number and configuration of detected vehicles. The key insight is that temporal understanding benefits from supervised fine-tuning on synthetic data, whereas spatial understanding is better served by pretrained object detectors and physics priors that transfer naturally across domains.

## Metadata
- **Published**: 2026-08-30T12:42:59Z
- **Authors**: Arkya Jyoti Bagchi, Ritul Jangir, Varun Raskar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29759v1)