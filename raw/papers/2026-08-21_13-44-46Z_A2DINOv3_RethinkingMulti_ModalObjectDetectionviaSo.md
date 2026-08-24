---
title: A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration
published: 2026-08-21T13:44:46Z
authors: Jiekang Feng, Zhihe Fan, Yunqi Zhu, Xinjie Yao, Yueying Zhang, Yike Gao, Ranxin Li, Guanzuo Chen
url: http://arxiv.org/abs/2608.21099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration

## Abstract
Multi-modal object detection is essential for robust scene understanding in challenging conditions, including low-light and adverse environments. Recent vision foundation models (e.g., DINOv3) have exhibited strong representation capabilities, yet adapting them to multi-modal scenarios remains challenging. Existing dense cross-modal fusion strategies often force heterogeneous modalities to interact indiscriminately, which may introduce redundant information and disrupt the valuable pre-trained representations. To address this issue, we revisit multi-modal fusion from the perspective of socialized learning and propose adapter to DINOv3 (A2DINOv3), a multi-expert collaboration framework with a Socialized Collaboration Protocol (SCP). Specifically, RGB and infrared branches are modeled as heterogeneous experts that independently preserve their specialized knowledge while exchanging complementary information through selective and constrained interactions. This design mitigates harmful cross-modal interference and prevents degradation of pre-trained priors during adaptation. Furthermore, a zero-initialization strategy is introduced to gradually activate cross-modal collaboration, enabling a smooth transition from modality-specific learning to cooperative representation learning. Extensive experiments on four multi-modal benchmarks, including aerial detection (GAIIC), autonomous driving (FLIR), low-light surveillance (LLVIP), and diverse real-world scenarios (M3FD), demonstrate that A2DINOv3 consistently achieves state-of-the-art performance in multi-modal object detection.

## Metadata
- **Published**: 2026-08-21T13:44:46Z
- **Authors**: Jiekang Feng, Zhihe Fan, Yunqi Zhu, Xinjie Yao, Yueying Zhang, Yike Gao, Ranxin Li, Guanzuo Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21099v1)