---
title: ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization
published: 2026-07-28T10:07:18Z
authors: Haochen Jiang, Jialei Pan, Yuzhe Sun, Zhe Dong, Lecheng Ren, Yanfeng Gu, Tianzhu Liu
url: http://arxiv.org/abs/2607.25524v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization

## Abstract
Unmanned aerial vehicle (UAV)-satellite cross-view geo-localization matches UAV images against satellite imagery and has achieved impressive accuracy on clean (non-degraded) image benchmarks. In real-world flights, however, UAV observations are frequently affected by adverse weather, illumination changes, platform motion, sensor noise, and compression, while the robustness of existing methods under such degradations remains largely unexamined. In this paper, we present UAVSat-Deg, a large-scale robustness benchmark for degraded UAV-satellite geo-localization, comprising University-1652-Deg and SUES-200-Deg. UAVSat-Deg covers 27 corruption types, including 19 core and 8 compound corruptions, at three severity levels, supports bidirectional drone-to-satellite and satellite-to-drone retrieval as well as multi-height UAV acquisition, and contains more than 11.7 million pre-generated corrupted test images. Benchmarking representative methods under this protocol reveals substantial robustness gaps, particularly under severe and compound corruptions. To address this problem, we propose ReLATE, a Reliable Evidence Learning framework with Adaptive Token Evidence Regulation, which realizes reliability-adaptive feature fusion during descriptor construction. ReLATE estimates a structure-smoothed reliability field over visual tokens, aggregates trustworthy local evidence, and adaptively integrates it into query-derived representations; the regulated query representations are then combined with the CLS-token and GeM-pooled branches to form the final cross-view descriptor. Across both test sets and retrieval directions, ReLATE achieves the best average corrupted-test performance among the compared methods while maintaining competitive accuracy on clean images. The code and dataset will be available at https://github.com/JHC626/ReLATE.

## Metadata
- **Published**: 2026-07-28T10:07:18Z
- **Authors**: Haochen Jiang, Jialei Pan, Yuzhe Sun, Zhe Dong, Lecheng Ren, Yanfeng Gu, Tianzhu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25524v1)