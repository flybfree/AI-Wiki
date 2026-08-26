---
title: MC-CXR: A Multi-Context Chest X-ray Benchmark for Context-Induced Disruption in Vision-Language Models
published: 2026-08-25T06:28:17Z
authors: Junhyeok Lee, Songsoo Kim, Kyu Sung Choi
url: http://arxiv.org/abs/2608.24118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MC-CXR: A Multi-Context Chest X-ray Benchmark for Context-Induced Disruption in Vision-Language Models

## Abstract
Vision-language models (VLMs) are increasingly used in clinical pipelines where a chest X-ray is interpreted alongside retrieved reports, preliminary notes, or prior imaging. Existing benchmarks measure whether models answer correctly in isolation, but not whether they preserve a correct image-only decision when plausible context conflicts with the image. We introduce Multi-Context Chest X-ray (MC-CXR), a benchmark of 240 cases expanded into 2,522 instances that isolates context-induced disruption through paired perturbation. Each case fixes the current image and target finding while presenting matched reliable and misleading context across text and prior CXR, with visual overlays where available. MC-CXR defines three task families and two paired metrics, the switch-to-wrong rate and the context-aligned error rate. We evaluate ten VLMs spanning open-source general, medical-domain, and closed-source systems. Image-only accuracy is necessary but insufficient. Mean switch rates range from 45.6-78.1% across misleading textual sources and 35.7-61.7% across misleading visual sources. Among switched predictions, 74.6% align with the misleading label for text versus 17.6% for visual context, a 57.0-point gap (95% CI 50.9-62.8). This text-visual asymmetry is observed under the standardized direct-answer protocol. The dataset is available on PhysioNet.

## Metadata
- **Published**: 2026-08-25T06:28:17Z
- **Authors**: Junhyeok Lee, Songsoo Kim, Kyu Sung Choi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24118v1)