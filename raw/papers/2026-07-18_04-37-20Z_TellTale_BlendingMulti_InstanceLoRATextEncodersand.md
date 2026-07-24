---
title: TellTale: Blending Multi-Instance LoRA Text Encoders and a Zero-Shot LLM Judge for Ambivalence/Hesitancy Recognition in Videos
published: 2026-07-18T04:37:20Z
authors: Abdel-Karim Al-Tamimi, Ali Rodan
url: http://arxiv.org/abs/2607.16635v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TellTale: Blending Multi-Instance LoRA Text Encoders and a Zero-Shot LLM Judge for Ambivalence/Hesitancy Recognition in Videos

## Abstract
We present TellTale, a text-only approach to ambivalence/hesitancy (A/H) recognition in interview videos, evaluated on the BAH dataset as part of the 3rd A/H Video Recognition Challenge (11th ABAW Workshop, ECCV 2026). Although the dataset provides video, audio, facial crops, and transcripts, TellTale relies on the transcript alone and combines three probability streams. Two text encoders, multilingual-e5-large and mDeBERTa-v3-base, are fine-tuned with parameter-efficient LoRA adapters under a multiple-instance learning (MIL) objective, in which transcript chunks are scored individually and pooled with a smooth maximum so that only the video-level label is needed for supervision. The third stream requires no training: a quantized 14B instruction LLM is prompted, zero-shot, to rate each transcript for A/H. The three probabilities are combined by a weighted average and a single decision threshold, both selected on participant-grouped cross-validated predictions. On the organizer-scored private test set of 152 videos from unseen participants, TellTale achieves a Macro-F1 of 0.7364 and an average precision of 0.7940, compared with 0.2827 Macro-F1 for the official vision-based baseline.

## Metadata
- **Published**: 2026-07-18T04:37:20Z
- **Authors**: Abdel-Karim Al-Tamimi, Ali Rodan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16635v1)