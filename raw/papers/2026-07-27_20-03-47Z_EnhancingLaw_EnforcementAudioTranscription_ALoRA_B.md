---
title: Enhancing Law-Enforcement Audio Transcription: A LoRA-Based Adaptation of Whisper for BWC Footage
published: 2026-07-27T20:03:47Z
authors: Vivek Senthil, Zhiqiang Tao, Ernest Fokoué
url: http://arxiv.org/abs/2607.27245v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Law-Enforcement Audio Transcription: A LoRA-Based Adaptation of Whisper for BWC Footage

## Abstract
Modern policing faces a "visibility paradox" where law enforcement agencies possess petabytes of Body-Worn Camera (BWC) footage that remains largely unutilized for accountability or systemic review due to the prohibitive labor costs of manual transcription. This research presents a framework for adapting the OpenAI Whisper architecture to the unique acoustic and linguistic challenges of the policing environment. By employing Parameter-Efficient Fine-Tuning (PEFT) through Low-Rank Adaptation (LoRA), we address the significant performance degradation observed in zero-shot models when confronted with high-stress scenarios, sirens, and radio interference. Crucially, we demonstrate that this adaptation is feasible on consumer-grade hardware (Acer Nitro local machine with NVIDIA 4GB GTX GPU) using 8-bit quantization and gradient checkpointing. We further integrate these transcriptions into a symbolic reasoning pipeline using a domain-specific ontology to transform raw audio into evidence-linked incident graphs, achieving a 93.7% lexicon mapping rate for the advancement of procedural justice and transparency.

## Metadata
- **Published**: 2026-07-27T20:03:47Z
- **Authors**: Vivek Senthil, Zhiqiang Tao, Ernest Fokoué
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27245v1)