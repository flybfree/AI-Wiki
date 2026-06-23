---
title: The Unreasonable Effectiveness of VLMs for Zero-shot Procedural Mistake Detection
published: 2026-06-19T16:31:44Z
authors: Serdar Ozsoy, Lars Doorenbos, Federico Spurio, Gianpiero Francesca, Juergen Gall
url: http://arxiv.org/abs/2606.21579v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Unreasonable Effectiveness of VLMs for Zero-shot Procedural Mistake Detection

## Abstract
Procedural mistake detection is important for quality control and user assistance across many disciplines. Recent work in this field has achieved significant gains by using the reasoning capabilities of Video-Language Models (VLMs) as components within multi-stage pipelines, which consist of separate modules for supervised temporal action segmentation, error detection, and explainability. Consequently, they remain dependent on tailored training datasets and require task-specific training, limiting their wider applicability. To remedy this, we introduce zero-shot procedural mistake detection and propose a unified Zero-shot Procedural Mistake detection (ZeProM) framework that jointly solves procedural mistake detection and temporal action segmentation with a single pre-trained VLM. By evaluating our framework on two canonical mistake detection benchmarks, EgoPER and CaptainCook4D, we find that ZeProM can perform these tasks successfully, while approaching, or even outperforming, the performance of fully supervised methods. For instance, we achieve a 4.4 point improvement in EDA and a 2.0 point improvement in F1@.5 on average over all five EgoPER tasks compared to the strongest supervised methods. Overall, our results show the potential of unified methods for procedural mistake detection, and we hope this will steer the field away from highly complex pipelines and toward more generally applicable solutions.

## Metadata
- **Published**: 2026-06-19T16:31:44Z
- **Authors**: Serdar Ozsoy, Lars Doorenbos, Federico Spurio, Gianpiero Francesca, Juergen Gall
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.21579v1)