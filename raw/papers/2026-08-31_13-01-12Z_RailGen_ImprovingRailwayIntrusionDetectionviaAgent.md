---
title: RailGen: Improving Railway Intrusion Detection via Agent-Guided Small-Scale Foreign Object Generation
published: 2026-08-31T13:01:12Z
authors: Quan Hao, Ziyang Tao, Chenxi Zhang, Yudong Wang, Rui Shi, Liguo Zhang
url: http://arxiv.org/abs/2608.30727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RailGen: Improving Railway Intrusion Detection via Agent-Guided Small-Scale Foreign Object Generation

## Abstract
Small-object detection under long-tailed data distributions is a fundamental yet challenging problem in multimedia. Railway Foreign Object Detection (RFOD) epitomizes this challenge with easily confused small intrusions and scarce samples. To address these issues, we propose a generative-augmented detection paradigm that leverages multimodal image generation to enrich the feature space of rare and small objects. We first construct RailGen, a multimodal image generation agent based on large models. Under semantic constraints, RailGen automatically invokes tools to generate railway scenes, calibrate intrusion positions, extract foreign objects, and fuse them into realistic intrusion effects. This process produces high-quality synthetic samples that effectively densify the feature representations of tail classes and complete the small-object feature space. Within this paradigm, we further propose FocalDEIM, a detection framework designed to enhance training with generated data. FocalDEIM improves dense matching with Focal Modulation for better small-object discrimination and adopts Focal Loss to emphasize hard samples, thereby alleviating blurred inter-class boundaries in complex railway scenes. Experimental results demonstrate that RailGen can generate high-quality small-scale foreign objects, reducing the object pixel area by up to 58x and 13.85x on average. Equipped with these challenging samples, our paradigm surpasses the baseline DEIM by 5.6% and 7.5% in mAP@50 and mAP@(50-95), respectively, and outperforms existing state-of-the-art methods. Ablation studies verify RailGen's feature-space enrichment and FocalDEIM's boundary discrimination. The paradigm provides an effective multimodal generative solution for long-tailed small-object detection in safety-critical applications.

## Metadata
- **Published**: 2026-08-31T13:01:12Z
- **Authors**: Quan Hao, Ziyang Tao, Chenxi Zhang, Yudong Wang, Rui Shi, Liguo Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30727v1)