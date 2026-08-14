---
title: Beyond Simulated Benchmarks: Evaluating Motion Representations for Fall Detection Under Real-World Data Scarcity
published: 2026-08-13T13:02:31Z
authors: Timilehin B. Aderinola, Ilaria D'Ascanio, Luca Palmerini, Lorenzo Chiari, Jochen Klenk, Clemens Becker, Brian Caulfield, Georgiana Ifrim
url: http://arxiv.org/abs/2608.13197v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Simulated Benchmarks: Evaluating Motion Representations for Fall Detection Under Real-World Data Scarcity

## Abstract
Falls are a major health concern for older adults, and wearable sensors have been widely explored for detecting falls and enabling timely intervention. However, real-world falls are extremely rare: collecting 100 of them requires an estimated 100,000 days of monitoring, resulting in severely limited labelled data for training machine learning models. Consequently, many approaches rely on simulated datasets, often reporting high laboratory performance but limited real-world generalisation. We present a systematic evaluation of motion representations for wearable fall detection under real-world data scarcity. Using accelerometer signals, we compare interval-based, kernel-based, symbolic, and foundation model representations. As an interpretable baseline, we additionally investigate a lightweight symbolic representation that converts short motion segments into symbolic sentences augmented with physically-grounded impact descriptors. Experiments use FallAllD, a simulated falls dataset, and FARSEEING, a clinically verified real-world falls dataset. Through cross-validation, controlled data scarcity, and cross-dataset transfer, we examine how representation choices affect robustness under realistic deployment. Our results reveal that highly parameterised kernel and foundation models excel on simulated data but degrade severely under both data scarcity and domain shift. Although the interval-based representation achieves the strongest absolute real-world performance, augmenting a symbolic representation with physically-grounded impact descriptors yields the smallest degradation under domain shift and retains detection sensitivity under extreme scarcity, albeit at lower precision. These findings highlight the importance of evaluating beyond simulated benchmarks and show that representation choice is critical for deployable fall detection given the scarcity of real-world data.

## Metadata
- **Published**: 2026-08-13T13:02:31Z
- **Authors**: Timilehin B. Aderinola, Ilaria D'Ascanio, Luca Palmerini, Lorenzo Chiari, Jochen Klenk, Clemens Becker, Brian Caulfield, Georgiana Ifrim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13197v1)