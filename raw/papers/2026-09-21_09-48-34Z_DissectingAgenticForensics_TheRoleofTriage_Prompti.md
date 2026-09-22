---
title: Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection
published: 2026-09-21T09:48:34Z
authors: Xianlong Li, Pietro Bongini, Niccoló Pancino, Marco Blanchini, Benedetta Tondi, Mauro Barni
url: http://arxiv.org/abs/2609.24359v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection

## Abstract
Image forensics is increasingly an open-world problem: manipulations range from fully synthetic images to localized edits, splicing and swapping, while most forensic detectors remain specialized to a single manipulation family. Agentic AI has recently emerged as a promising solution. In principle, such systems can assess the reliability of individual detectors, identify out-of-scope evidence, and arbitrate conflicting reports. However, it remains unclear which components actually drive performance and whether their benefits persist under distribution shift. To answer these questions, we study a training-free agentic framework built around specialist detectors, per-detector triage, and conflict-aware evidence arbitration. Using six configurations and three multimodal large language model backbones, we dissect the role of triage, prompting, and reasoning quality on both in-distribution and out-of-distribution data. Our results show that naive detector fusion suffers from severe false-positive rates on authentic images. Triage and prompting consistently improve performance by filtering unreliable evidence and exposing detector limitations. However, the dominant factor is represented by reasoning itself: A stronger judge substantially outperforms a weaker one, particularly under distribution shift. Most notably, manipulation recall is nearly saturated across all configurations, indicating that the main challenge of open-world image forensics is not detecting manipulations, but calibrating trust in specialized forensic tools and arbitrating conflicting evidence.

## Metadata
- **Published**: 2026-09-21T09:48:34Z
- **Authors**: Xianlong Li, Pietro Bongini, Niccoló Pancino, Marco Blanchini, Benedetta Tondi, Mauro Barni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24359v1)