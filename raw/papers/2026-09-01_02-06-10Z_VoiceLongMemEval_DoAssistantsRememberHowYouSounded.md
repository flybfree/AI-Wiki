---
title: VoiceLongMemEval: Do Assistants Remember How You Sounded?
published: 2026-09-01T02:06:10Z
authors: Ramit Pahwa, Parivesh Priye, Apoorva Beedu
url: http://arxiv.org/abs/2609.00570v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VoiceLongMemEval: Do Assistants Remember How You Sounded?

## Abstract
With the growing scale of multi-agent architectures and large language models, deployed AI assistants are increasingly tasked with reasoning over long, continuous, multi-session conversation histories. Current benchmarks evaluate this dialogue history as information retrieval over long horizon, temporal reasoning, or knowledge updates, while crucially ignoring the fundamental dynamics of human-agent interaction, i.e. how they said it. To address this gap, we present VoiceLongMemEval (VLME) benchmark, where every answer depends on paralinguistic metadata (emotion labels, prosody descriptors, and voice events) attached to conversational turns, which is otherwise unrecoverable from the words alone. Every item passes a three-stage adversarial gate, ensuring that a strong language model fails when given only the transcript. Evaluating leading frontier and open-weight models reveals a pervasive affect gap; providing text-track paralinguistic metadata yields a 0.09 to 0.38 accuracy boost (0.61 to 0.69 when prompted with evidence hints), while standard ASR pipelines systematically discard this signal. Additionally, audio-native models successfully extract these cues directly from speech (0.354 to 0.412 vs. 0.325 blind). Code and dataset will be made available upon acceptance.

## Metadata
- **Published**: 2026-09-01T02:06:10Z
- **Authors**: Ramit Pahwa, Parivesh Priye, Apoorva Beedu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00570v1)