---
title: On-Device Multi-Species Malaria Detection with Uncertainty-Calibrated Slide-Level Aggregation
published: 2026-08-09T08:09:25Z
authors: Idaya Seidu, Ahmed Tahiru Issah, Charles B. Delahunt, Carine Mukamakuza
url: http://arxiv.org/abs/2608.08566v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On-Device Multi-Species Malaria Detection with Uncertainty-Calibrated Slide-Level Aggregation

## Abstract
Malaria remains a leading cause of mortality in resource-limited settings, where expert microscopists are scarce. Automated diagnosis based on microscopy images thus has strong potential to improve care delivery. But for an algorithm to deploy, a necessary requirement is that it meet a suite of non-obvious (from a machine learning (ML) perspective) clinical constraints. Therefore, in close consultation with a national health center we developed a malaria diagnosis pipeline which addresses key requirements listed by the health care center but typically ignored in the ML malaria literature. In particular, it includes: (i) stopping criteria (to reduce image acquisition and time-to-result); (ii) human-in-the-loop functionality (for review and accountability); (iii) multi-species discrimination (since treatment varies by species); (iv) thick film detection (standard for microscopy); (v) computationally-efficient uncertainty calculations (to aid clinician review); and (vi) an edge device platform (since internet can be spotty in this catchment area). The mobile system performs all inference on-device using YOLOv13n deployed via TensorFlow Lite. It detects four species and white blood cells from Giemsa-stained thick blood smear images, aggregating per-image detections into slide-level parasitemia with World Health Organization (WHO)-standard quantification. This paper highlights these various clinical constraints and offers methods to address them. Evaluated on 2,739 annotated images across all four species, the system achieves mAP@0.5 of 0.863, per-image parasite count correlation of r = 0.812, slide-level r = 0.951 (soft counting, 10 images/slide), and runs entirely offline with a pipeline time of 10.27 +- 1.65 s per image.

## Metadata
- **Published**: 2026-08-09T08:09:25Z
- **Authors**: Idaya Seidu, Ahmed Tahiru Issah, Charles B. Delahunt, Carine Mukamakuza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08566v1)