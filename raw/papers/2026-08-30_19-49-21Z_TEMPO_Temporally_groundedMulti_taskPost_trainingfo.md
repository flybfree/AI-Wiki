---
title: TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models
published: 2026-08-30T19:49:21Z
authors: Apoorva Kulkarni, Kaousheik Jayakumar, Sreyan Ghosh, Utathya Aich, Ramani Duraiswami, Dinesh Manocha
url: http://arxiv.org/abs/2608.29999v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models

## Abstract
Large audio-language models (LALMs) describe audio at the clip level but cannot assign timestamps to the events, speakers, or sounds they identify. Despite being essential for downstream tasks like speech recognition and dense audio captioning, timestamping remains a key limitation of most LALMs. We present TEMPO (Temporally-grounded Multi-task Post-training), the first unified model to handle audio, speech, and music timestamping tasks. Our core contribution is a supervised fine-tuning (SFT) stage built on three innovations: atomic timestamp tokens, a time-aware projector that injects sinusoidal wall-clock encodings into audio frame embeddings, and a distance-aware Gaussian loss. Our training is based on a synthetic-to-real curriculum. We further introduce, to our knowledge, the first application of reinforcement learning to unified audio timestamping, using GRPO with verifiable temporal rewards that directly optimize the evaluation objectives. Rather than serving as the primary source of performance gains, GRPO acts as a refinement stage on top of the SFT checkpoint, providing modest additional improvements. To support this work, we build a training dataset containing 119K samples and an evaluation benchmark containing 10K samples, drawn from established corpora across five tasks. On this benchmark, TEMPO outperforms Audio Flamingo Next and Qwen3-Omni, two state-of-the-art LALMs explicitly trained on timestamped data. Experiments confirm that SFT delivers most of these gains, with GRPO providing consistent but moderate refinements.

## Metadata
- **Published**: 2026-08-30T19:49:21Z
- **Authors**: Apoorva Kulkarni, Kaousheik Jayakumar, Sreyan Ghosh, Utathya Aich, Ramani Duraiswami, Dinesh Manocha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29999v1)