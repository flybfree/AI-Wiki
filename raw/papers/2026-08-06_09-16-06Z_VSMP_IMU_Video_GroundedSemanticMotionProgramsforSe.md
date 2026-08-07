---
title: VSMP-IMU: Video-Grounded Semantic Motion Programs for Sensor-Aware Synthetic IMU Generation
published: 2026-08-06T09:16:06Z
authors: Lala Shakti Swarup Ray, Vitor Fortes Rey, Mengxi Liu, Paul Lukowicz, Bo Zhou
url: http://arxiv.org/abs/2608.05782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VSMP-IMU: Video-Grounded Semantic Motion Programs for Sensor-Aware Synthetic IMU Generation

## Abstract
Wearable human activity recognition (HAR) is often limited by the scarcity of labeled sensor data, especially in low-resource, class-imbalanced, and subject-generalization settings. Synthetic IMU generation can reduce this dependency and enhance HAR machine learning model's performance, but existing approaches face a trade-off without addressing all factors: video-driven methods are visually grounded but sensitive to pose-estimation errors, while text-driven methods are controllable but often weakly grounded in how activities are actually performed. We present VSMP-IMU, a video-grounded framework for controllable synthetic IMU generation based on a structured Semantic Motion Program (SMP), which separates activity-defining semantics from label-preserving variation. Given an input video, VSMP-IMU extracts and augments an SMP, uses it to synthesize motion, converts the motion into virtual IMU signals, and grounds the resulting signals to the target wearable domain. We evaluate VSMP-IMU against state-of-the-art synthetic data generation methods on five public IMU-HAR datasets under leave-one-person-out evaluation. VSMP-IMU achieves an average Macro-F1 of 78.33%, improving over real-only training by 9.77% and over the strongest prior synthetic baseline by 4.04%. In low-resource settings with reduced training data-samples, it improves over real-only training by 18.54% and over the strongest prior synthetic baselines by more than 6% on average. Under long-tail evaluation in imbalanced datasets, it improves tail-class Macro-F1 by 19.86% over Real-only training and by 4.76% over SOTA. These results show that structured video-grounded semantics provide a practical foundation for controllable, wearable-relevant synthetic sensor data generation.

## Metadata
- **Published**: 2026-08-06T09:16:06Z
- **Authors**: Lala Shakti Swarup Ray, Vitor Fortes Rey, Mengxi Liu, Paul Lukowicz, Bo Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05782v1)