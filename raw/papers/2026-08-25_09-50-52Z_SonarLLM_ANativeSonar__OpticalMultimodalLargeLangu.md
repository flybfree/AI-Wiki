---
title: SonarLLM: A Native Sonar--Optical Multimodal Large Language Model for Underwater Perception
published: 2026-08-25T09:50:52Z
authors: Cong Su, longxuan ma, Ling Dong, Guofeng Tang, Weijie Yin, Haohui Chen, Zhengtao Yu
url: http://arxiv.org/abs/2608.24325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SonarLLM: A Native Sonar--Optical Multimodal Large Language Model for Underwater Perception

## Abstract
Reliable underwater perception requires complementary sensing under variable visibility. Optical cameras capture appearance and semantics but degrade rapidly with turbidity, whereas imaging sonar preserves geometry while exhibiting distinct range-azimuth structure and acoustic artifacts. Existing MLLMs, built primarily on optical encoders, are therefore ill-suited to model sonar or adaptively exploit sonar-optical complementarity. We propose SonarLLM, a sonar-optical MLLM that treats sonar as a native perceptual modality. It combines a sonar-specific encoder, modality-specific physics-aware feature enhancement, and reliability-aware hierarchical fusion to align acoustic structure with optical semantics and dynamically adjust their contributions as sensing quality changes. We also introduce SonarBench, a paired benchmark that spans four tasks: recognition, counting, visual question answering, and captioning; and, across the benchmark, three input settings: sonar-only, optical-only, and fusion. By fixing the scene and sonar observation while varying optical degradation, SonarBench enables controlled measurement of cross-modal complementarity. SonarLLM achieves 72.0% macro accuracy across sonar-only recognition, counting, and VQA, outperforming the strongest baseline by 34.4 percentage points, and 68.7% under fusion, exceeding the best baseline by 25.1 points. For recognition and counting, the fusion-over-optical gain grows from 6.0 to 36.0 points as turbidity increases, indicating the increasing complementary value of sonar under controlled optical degradation. Together, these results show that robust heterogeneous perception depends not only on adding sonar, but on representing and weighting it according to its sensing characteristics.

## Metadata
- **Published**: 2026-08-25T09:50:52Z
- **Authors**: Cong Su, longxuan ma, Ling Dong, Guofeng Tang, Weijie Yin, Haohui Chen, Zhengtao Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24325v1)