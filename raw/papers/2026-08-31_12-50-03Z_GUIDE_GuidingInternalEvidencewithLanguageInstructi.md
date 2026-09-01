---
title: GUIDE: Guiding Internal Evidence with Language Instructions
published: 2026-08-31T12:50:03Z
authors: Soyeon Caren Han, Hyunsuk Chung, Jinwoo Kim, Seungyeon Ji, Kyungreem Han
url: http://arxiv.org/abs/2608.30712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GUIDE: Guiding Internal Evidence with Language Instructions

## Abstract
Large multimodal models follow instructions about what to generate, but not necessarily about what evidence to rely on. Hence, models may continue to depend on shortcut-associated cues even when instructions suggest otherwise. We introduce GUIDE, a framework for controlling internal evidence usage through language instructions. GUIDE combines grouped parameter-efficient adaptation with instruction-conditioned gating to modulate multimodal evidence pathways during reasoning and generation. We further introduce a pathway-level evaluation framework that characterizes instruction-conditioned evidence modulation through reliance sensitivity, controlled perturbation analysis, pathway modulation, and autoregressive decoding dynamics. Across multimodal reasoning, classification, and generation, GUIDE induces structured and instruction-aligned redistribution of evidence reliance while largely preserving task behavior. Experiments on GQA, TextVQA, MM-IMDb, CREMA-D, RAVDESS, and Flickr30K show that GUIDE improves robustness under targeted evidence perturbations and enables controllable modulation across diverse multimodal settings. This suggests that multimodal instruction following can extend beyond output control toward regulating how different evidence sources contribute to model predictions.

## Metadata
- **Published**: 2026-08-31T12:50:03Z
- **Authors**: Soyeon Caren Han, Hyunsuk Chung, Jinwoo Kim, Seungyeon Ji, Kyungreem Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30712v1)