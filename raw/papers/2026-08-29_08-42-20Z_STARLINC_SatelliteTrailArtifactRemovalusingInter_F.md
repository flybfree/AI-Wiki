---
title: STARLINC: Satellite Trail Artifact Removal using Inter-Frame Correlation
published: 2026-08-29T08:42:20Z
authors: Shingeon Kim, Hyeyoon Lee, Dain Kwon, Kanghyun Choi, Sunjong Park, Mi-Ryang Kim, Jeong-Eun Lee, Jinho Lee
url: http://arxiv.org/abs/2608.29145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STARLINC: Satellite Trail Artifact Removal using Inter-Frame Correlation

## Abstract
The rapid expansion of low Earth orbit satellites such as Starlink is increasingly contaminating astronomical surveys. In practice, contaminated images are often identified through inspection. However, modern surveys generate terabytes of data each night, making manual screening infeasible and necessitating reliable automated methods for satellite trail removal. Unfortunately, existing general-domain line detection methods fail to generalize to astronomical images due to domain mismatch, which are mostly grayscale with sparse bright stars and have a low signal-to-noise ratio. Moreover, training new models from scratch is impractical due to the lack of large-scale annotated astronomical datasets. To address these challenges, we introduce STARLINC, the first ML-based framework for satellite trail removal without requiring tedious pixel-level annotation of astronomical images. STARLINC combines synthetic satellite trail generation for training, inter-frame differential maps from temporally adjacent exposures to highlight transient trails, and heatmaps to provide additional localization cues for pixel-level segmentation. Extensive experiments on real-world data demonstrate substantial improvements over baselines, establishing STARLINC as a scalable solution for next-generation astronomical surveys. Code is available at https://github.com/starioKim/STARLINC.

## Metadata
- **Published**: 2026-08-29T08:42:20Z
- **Authors**: Shingeon Kim, Hyeyoon Lee, Dain Kwon, Kanghyun Choi, Sunjong Park, Mi-Ryang Kim, Jeong-Eun Lee, Jinho Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29145v1)