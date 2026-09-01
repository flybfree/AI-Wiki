---
title: SpanCalib-VLM: Calibrated Hallucination Span Detection in Vision-Language Models
published: 2026-08-30T19:00:31Z
authors: Amanuel Gizachew Abebe, Yasmin Moslem
url: http://arxiv.org/abs/2608.29974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpanCalib-VLM: Calibrated Hallucination Span Detection in Vision-Language Models

## Abstract
Detecting hallucinations in Large Vision-Language Models (LVLMs) requires both accurate span localization and well-calibrated confidence scores. Fine-tuned generative VLMs excel at identifying hallucinated text spans but suffer from overconfidence and high inference latency. Discriminative sequence taggers offer deterministic speed and superior calibration but exhibit conservative span recall. We present SpanCalib-VLM, a hybrid dual-system for the SHROOM-Visions Shared Task that combines a multimodal sequence tagger, consisting of XLM-RoBERTa-Large fused with a SigLIP vision encoder via cross-attention, with our fine-tuned generative VLM (Qwen3.5-4B-SHROOM-SFT). Through a Union-Calibrated Fusion strategy, candidate spans from the generative model are re-scored with calibrated probabilities from the sequence tagger. On the SHROOM-Visions English evaluation split, our ensemble achieves a Pearson calibration correlation of 0.41 and an overall IoU of 0.39, with a clean-response IoU of 0.91} and overall detection accuracy of 70.7%. We make our model weights and code publicly available.

## Metadata
- **Published**: 2026-08-30T19:00:31Z
- **Authors**: Amanuel Gizachew Abebe, Yasmin Moslem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29974v1)