---
title: SurgLAT: Surgical Latent Attention Tracking for Depth-Aware Robotic Laparoscope Control
published: 2026-08-08T03:04:01Z
authors: Rulin Zhou, Qiujie Song, Yujie Ma, An Wang, Wanhao Liu, Guoheng Ma, Yidu Wang, Guankun Wang, Xingrong Diao, Jiankun Wang, Chaowei Zhu, Xianming Liu, Hongliang Ren
url: http://arxiv.org/abs/2608.07876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SurgLAT: Surgical Latent Attention Tracking for Depth-Aware Robotic Laparoscope Control

## Abstract
Autonomous laparoscopic camera control requires continuous understanding of the surgeon's operative intent in dynamic surgical scenes, where the target operative region is not a stable physical object but a latent and temporally evolving attention state. In this work, we present Surgical Latent Attention Tracking (SurgLAT), a causal online framework for latent surgical attention modeling and autonomous laparoscopic view control. SurgLAT uses a frozen DINOv3 encoder and a state-conditioned spatial token mixer to extract operative evidence under a memory-guided spatial prior, while a selective causal latent memory module jointly models short-term motion continuity and long-horizon surgical intent evolution through dynamic retrieval of current, recent, and historical latent states. The learned latent surgical attention state is decoded into a probabilistic attention heatmap and operative region for downstream endoscope guidance. Beyond perception, we further introduce a robotic deployment framework with explicit laparoscopic Remote Center of Motion (RCM) constrained control based on virtual-axis formulation, together with redundancy-aware null-space initialization for stable and smooth manipulator motion. We validate the full system on real laparoscopic surgical videos and a physical robotic laparoscope platform. Experimental results demonstrate robust online operative-region tracking and stable autonomous endoscopy adjustment under occlusion, rapid motion, and target transitions, highlighting the effectiveness of latent surgical intent modeling for surgical autonomy.

## Metadata
- **Published**: 2026-08-08T03:04:01Z
- **Authors**: Rulin Zhou, Qiujie Song, Yujie Ma, An Wang, Wanhao Liu, Guoheng Ma, Yidu Wang, Guankun Wang, Xingrong Diao, Jiankun Wang, Chaowei Zhu, Xianming Liu, Hongliang Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07876v1)