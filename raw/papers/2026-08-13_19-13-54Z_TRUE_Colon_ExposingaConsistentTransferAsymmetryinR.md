---
title: TRUE-Colon: Exposing a Consistent Transfer Asymmetry in Real-Time Polyp Detection
published: 2026-08-13T19:13:54Z
authors: Sebastian Doerrich, Andreas Franz Schwab, Francesco Di Salvo, Shyam Nandan Rai, Hanh Huyen My Nguyen, Christian Ledig
url: http://arxiv.org/abs/2608.13711v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRUE-Colon: Exposing a Consistent Transfer Asymmetry in Real-Time Polyp Detection

## Abstract
Computer-aided detection (CADe) systems for colonoscopy promise to reduce clinical miss rates, yet reliable real-world deployment remains elusive. This translational gap stems in part from a structural flaw in model development: the reliance on curated datasets that under-represent the long negative stretches and procedure-related artifacts characteristic of routine examinations. Training and evaluating architectures strictly on these lesion-centric benchmarks creates an illusion of success, since such benchmarks cannot capture clinically crucial metrics. To expose this gap, we establish TRUE-Colon, a standardized benchmarking protocol that measures key deployment characteristics alongside localization accuracy, and evaluate four real-time architectures (Faster R-CNN, YOLOv8, YOLOv11, RT-DETR) across curated benchmarks (SUN, PICCOLO) and 60 unedited, full-length procedures (REAL-Colon). We observe a consistent transfer asymmetry: models trained strictly on curated clips suffer a severe performance collapse when evaluated on full procedures, whereas procedure-trained models substantially improve rejection of non-polyp content on REAL-Colon, and largely retain their accuracy on curated benchmarks. Beyond transferability, we find that the Transformer detector attains the strongest sensitivity and the earliest, most persistent detections, while the convolutional detectors stay competitive at a higher throughput. Together, these results indicate that both training and benchmarking for deployable CADe should shift from curated, lesion-centric clips toward full-procedure data and deployment-relevant operating points. Source code is available at https://github.com/sdoerrich97/true-colon.

## Metadata
- **Published**: 2026-08-13T19:13:54Z
- **Authors**: Sebastian Doerrich, Andreas Franz Schwab, Francesco Di Salvo, Shyam Nandan Rai, Hanh Huyen My Nguyen, Christian Ledig
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13711v1)