---
title: Content Based Video Narration of Gameplay with Vision Language Models
published: 2026-08-14T07:03:30Z
authors: Mathew Varghese
url: http://arxiv.org/abs/2608.14016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Content Based Video Narration of Gameplay with Vision Language Models

## Abstract
Live game commentary is scarce: it exists for professional esports broadcasts and almost nowhere else. We present a content-based video narration system that produces spoken, esports-style commentary for arbitrary gameplay recordings using a general-purpose vision-language model (VLM) and a text-to-speech back end, with no game-specific instrumentation, no engine telemetry, and no task-specific training. Three mechanisms carry the system. Temporal mosaic packing arranges nine uniformly sampled frames into a single 3x3 image, letting an image-native VLM reason about motion while consuming one image payload per segment instead of nine. Context-conditioned prompting replays the K most recent narrations as assistant-role history, suppressing the repetition that dominates per-segment captioning of static scenes. Duration-conditioned generation and elastic alignment constrain narration length in the prompt, then time-scale or symmetrically pad the synthesized audio so each utterance fills its segment slot exactly, giving frame-accurate muxing without a forced aligner. The implementation supports either cloud TTS or a 6-bit quantized 4B-parameter on-device TTS model on Apple silicon, making the speech stage fully local. We report a qualitative case study on real-time strategy footage, a cost model showing the mosaic reduces per-minute image payloads by 9x, and a candid account of observed failure modes - hallucinated game state, resolution loss from mosaicking, and prosody artifacts from time-scaling. We release the system as a reproducible baseline, with an evaluation protocol for the quantitative study a full version will report.

## Metadata
- **Published**: 2026-08-14T07:03:30Z
- **Authors**: Mathew Varghese
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14016v1)