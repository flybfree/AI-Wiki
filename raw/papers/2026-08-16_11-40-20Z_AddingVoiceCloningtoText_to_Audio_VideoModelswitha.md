---
title: Adding Voice Cloning to Text-to-Audio-Video Models with a Single Zero-Initialised Layer
published: 2026-08-16T11:40:20Z
authors: Ivan Mikheev, Viacheslav Vasilev, Anna Dmitrienko, Alexey Letunovskiy, Ivan Kirillov, Kirill Chernyshev, Denis Dimitrov
url: http://arxiv.org/abs/2608.15690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adding Voice Cloning to Text-to-Audio-Video Models with a Single Zero-Initialised Layer

## Abstract
Text-to-audio-video (T2AV) generation models produce a video and its soundtrack from a textual description, but offer no control over whose voice speaks in the output. We show that a base T2AV model can be turned into a voice-cloning model by adding a single zero-initialized linear layer on top of its audio backbone, fine-tuning for a comparatively short training schedule, and conditioning on a short reference recording at inference time. The reference is injected through two complementary signals: its diffusion latents are prepended to the audio stream, and a global speaker embedding modulates token of the target audio. On a benchmark of 674 speaker-text pairs spanning 30 speakers we compare against five strong voice-cloning text-to-speech baselines: our enhanced 5B model attains the highest speaker-encoder cosine similarity (SECS) across three independent verification networks (ECAPA-TDNN, WavLM-SV, Resemblyzer), statistically significantly outperforming every baseline. A side product of the architecture is that the audio path can be evaluated without the video path at inference time, yielding a ~30x speed-up over the full audio-video diffusion loop while preserving the voice-cloning behaviour.

## Metadata
- **Published**: 2026-08-16T11:40:20Z
- **Authors**: Ivan Mikheev, Viacheslav Vasilev, Anna Dmitrienko, Alexey Letunovskiy, Ivan Kirillov, Kirill Chernyshev, Denis Dimitrov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15690v1)