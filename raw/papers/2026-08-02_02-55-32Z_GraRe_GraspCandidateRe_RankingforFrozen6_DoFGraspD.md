---
title: GraRe: Grasp Candidate Re-Ranking for Frozen 6-DoF Grasp Detectors
published: 2026-08-02T02:55:32Z
authors: Jibao Yuan, Yuhui Zhao, Yinzhen Lv, Chao Xu, Shun Li, Chenxi Deng, Shaofei Chen
url: http://arxiv.org/abs/2608.00946v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraRe: Grasp Candidate Re-Ranking for Frozen 6-DoF Grasp Detectors

## Abstract
Existing 6-DoF grasp detectors typically rank grasp candidates by detector confidence. However, our analysis on GraspNet-1Billion shows that detector confidence is often poorly aligned with grasp quality, causing successful grasp candidates to be ranked too low during execution. Motivated by this observation, we formulate grasp candidate re-ranking as a separate task for frozen detectors, aiming to improve candidate ordering without changing the detector or its grasp candidates. We propose GraRe, which estimates grasp quality from candidate attributes, shell-stratified local geometry, and object context. Candidate attributes condition the local geometric and object-context representations, and a Transformer fuses all three feature types. The predicted quality is combined with detector confidence to produce the final ranking. Experiments on GraspNet-1Billion with three frozen detectors show consistent improvements, with gains of up to 13.60 points in Average AP. Real-robot experiments further demonstrate robust grasping in cluttered scenes. These results show that improving candidate ranking provides a practical way to enhance frozen 6-DoF grasp detectors.

## Metadata
- **Published**: 2026-08-02T02:55:32Z
- **Authors**: Jibao Yuan, Yuhui Zhao, Yinzhen Lv, Chao Xu, Shun Li, Chenxi Deng, Shaofei Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00946v1)