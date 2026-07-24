---
title: From a Multilingual Streaming ASR Backbone to Kenyan-Language Systems: Data-Centric Adaptation of Nemotron 3.5 for Kikuyu, Dholuo, and Kalenjin
published: 2026-07-21T09:52:57Z
authors: Mark Gatere
url: http://arxiv.org/abs/2607.18912v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From a Multilingual Streaming ASR Backbone to Kenyan-Language Systems: Data-Centric Adaptation of Nemotron 3.5 for Kikuyu, Dholuo, and Kalenjin

## Abstract
Automatic speech recognition (ASR) for African languages is constrained by orthographic inconsistency, annotation artifacts, missing audio, speaker and domain imbalance, and evaluation procedures that differ from deployment. We present an end-to-end engineering study adapting NVIDIA Nemotron 3.5 ASR Streaming 0.6B to Kikuyu, Dholuo, and Kalenjin. Starting from a Kenyan Swahili-adapted checkpoint, we retain its cache-aware FastConformer RNN-T, prompt conditioning, and streaming decoder during full-parameter fine-tuning. The study covers corpus auditing, Unicode normalization, split checks, duration filtering, low-rate continuation, validation-based checkpoint selection, true-streaming evaluation, artifact preservation, and isolated serving.   On internal, adaptively consulted evaluation sets excluded from gradient updates at context [56,13], selected Kikuyu and Dholuo models achieve 42.97% and 33.98% WER, respectively. Dholuo records 9.59% CER and 8.13% no-space CER under its frozen historical label policy; Kikuyu records 7.79% no-space CER. Kalenjin remains a work in progress: v1-v reaches 68.74% WER on a 2,411-row clean-v3 diagnostic subset excluding long-pause annotations, digit-bearing references, and targets shorter than three tokens. Its checkpoint selection used a mixed-source validation manifest containing test-origin rows, so the score is not an independent generalization estimate. We also report negative findings involving non-speech labels, short-utterance over-generation, boundary-sensitive WER, and cloud job-lifecycle failures. We make no state-of-the-art claim because the internal sets, repeated consultation, and normalization differ from public benchmarks. This work provides an auditable account of adapting a multilingual streaming model into language-specific systems without discarding streaming constraints.

## Metadata
- **Published**: 2026-07-21T09:52:57Z
- **Authors**: Mark Gatere
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18912v1)