---
title: Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation
published: 2026-08-31T18:17:49Z
authors: Ruotong Wang, Zihao Zhu, Siwei Lyu, Xin Tao, Baoyuan Wu
url: http://arxiv.org/abs/2609.00206v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation

## Abstract
Despite their growing use in video moderation, multimodal large language models (MLLMs) exhibit a compositional safety blind spot: videos composed of seemingly benign components can convey harmful meaning when interpreted as a whole. We refer to this phenomenon as Distributed Implicit Harm (DIH), where harm arises from relations among components distributed along a decomposition axis of the video, rather than from any single explicit cue. Among many possible axes, we study two representative cases: temporally distributed harm across visual segments (DIH-T) and cross-modal harm between audio and visual streams (DIH-M). Studying and mitigating DIH at scale requires data that is difficult to collect: such videos lack compositional harm annotations, evade retrieval based on local visual cues, keywords, or single-modality signals, and are consequently absent from existing safety datasets. To bridge this gap, we develop a multi-agent synthesis framework that composes individually benign components into harmful scenarios and generates diverse DIH videos with explicit reasoning annotations, yielding a dataset of over 9,000 videos spanning visual-only and audio-visual settings. Benchmarking over 30 MLLMs spanning frontier proprietary models and leading open-source systems reveals substantial and consistent deficits in detecting both DIH-T and DIH-M. Notably, this failure persists even among the strongest frontier models: they often correctly assess individual components in isolation but fail to recognize the harmful meaning that emerges from their composition. We further evaluate these models on a manually collected set of real-world DIH videos from social media and observe the same failure mode, highlighting DIH as a practical and underexplored challenge for video moderation.

## Metadata
- **Published**: 2026-08-31T18:17:49Z
- **Authors**: Ruotong Wang, Zihao Zhu, Siwei Lyu, Xin Tao, Baoyuan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00206v1)