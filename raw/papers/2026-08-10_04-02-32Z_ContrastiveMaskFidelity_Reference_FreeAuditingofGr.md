---
title: Contrastive Mask Fidelity: Reference-Free Auditing of Ground-Truth Masks in Remote Sensing Semantic Segmentation
published: 2026-08-10T04:02:32Z
authors: Shuaishuai Cao, Shuwei Peng, Meng Tang, Min Huang, Youjin Wang, Jie Chen, Jing Ouyang, Zhiwei Zhai
url: http://arxiv.org/abs/2608.09101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contrastive Mask Fidelity: Reference-Free Auditing of Ground-Truth Masks in Remote Sensing Semantic Segmentation

## Abstract
Semantic segmentation models are trained and evaluated against human-drawn masks, yet remote-sensing annotations are often coarse, incomplete, or misaligned; high overlap scores may then reflect agreement with imperfect labels rather than faithfulness to the image, creating an evaluation paradox. We introduce Contrastive Mask Fidelity (CMF), a training-free, reference-free metric that scores competing class masks directly against image evidence. CMF composites keep and erase counterfactual views of each mask and asks a frozen vision-language judge whether class evidence is concentrated inside the mask and absent outside. We validate CMF on controlled mask corruptions, then audit 10,731 image-class pairs across ten remote-sensing benchmarks using candidate masks from Seg-Probe, a training-free open-vocabulary probe built on SegEarth-OV3 that outperforms prior baselines on nine of ten datasets. The audit reveals systematic, class-dependent annotation distortion: man-made classes such as buildings, roads, and cars favor the candidate mask on 62-85% of pairs, whereas ambiguous land cover more often favors human annotations. On a blinded three-annotator consensus, CMF matches expert judgment on 81% of pairs, exceeding keep-only scoring, model confidence, and a trained label-quality baseline. Finally, conservative class-wise arbitration yields supervision that improves cross-domain transfer over raw annotations and matched replacement controls, positioning CMF as a scalable tool for auditing ground truth rather than presuming it infallible.

## Metadata
- **Published**: 2026-08-10T04:02:32Z
- **Authors**: Shuaishuai Cao, Shuwei Peng, Meng Tang, Min Huang, Youjin Wang, Jie Chen, Jing Ouyang, Zhiwei Zhai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09101v1)