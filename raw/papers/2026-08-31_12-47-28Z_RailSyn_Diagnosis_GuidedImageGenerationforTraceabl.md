---
title: RailSyn: Diagnosis-Guided Image Generation for Traceable Data Completion in Railway Foreign Object Detection
published: 2026-08-31T12:47:28Z
authors: Quan Hao, Chenxi Zhang, Ziyang Tao, Yuyuan Zhou, Yudong Wang, Rui Shi, Lechuan Xu, Changhao Liu, Liguo Zhang
url: http://arxiv.org/abs/2608.30709v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RailSyn: Diagnosis-Guided Image Generation for Traceable Data Completion in Railway Foreign Object Detection

## Abstract
Railway foreign object detection (RFOD) is critical to safe railway operation, yet scarce real positive samples incompletely represent task-relevant variations in object scale, intrusion relation, railway scene, illumination, and adverse weather. Existing synthetic augmentation can improve RFOD detection, but its gains lack an explicit account of the task-relevant deficiencies complemented by the generated data. We therefore introduce RailSyn, a diagnosis-guided framework comprising a real-referenced Inspector and a requirement-aligned Generator. The Inspector constructs a variable-radius empirical cover from finite real observations to localize candidate completion regions and profile synthetic pools. The resulting audit identifies railway-context, intrusion-semantic, and visual-consistency requirements; the Generator addresses them through domain adaptation, agent-planned placement and physical contact relations, and plan-consistent conditional refinement. Using the Inspector, we further trace representation-space changes across generation variants; the complete system attains a local-shell occupation of $C_{gap}$ to 13.64%, which measures generated coverage of real-derived completion regions. Extensive experiments show AP50--95 gains of up to 4.9 points and consistent improvements across nine mainstream detectors, demonstrating broad cross-architecture utility.

## Metadata
- **Published**: 2026-08-31T12:47:28Z
- **Authors**: Quan Hao, Chenxi Zhang, Ziyang Tao, Yuyuan Zhou, Yudong Wang, Rui Shi, Lechuan Xu, Changhao Liu, Liguo Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30709v1)