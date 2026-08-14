---
title: FastThaiG2P: Lightning-fast Thai Grapheme-to-phoneme Conversion for Voice Agent Pipelines
published: 2026-08-13T04:46:01Z
authors: Charin Polpanumas
url: http://arxiv.org/abs/2608.12814v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FastThaiG2P: Lightning-fast Thai Grapheme-to-phoneme Conversion for Voice Agent Pipelines

## Abstract
FastThaiG2P provides sub-millisecond Thai grapheme-to-phoneme conversion for text-to-speech pipelines (International Phonetic Alphabet and Kokoro-TTS conventions) using a PyThaiNLP-tokenized, extensible dictionary and normalization rules for common Central Thai speech. The approach achieves an average latency of 0.15 ms per utterance on a benchmark of 27,242 synthetically generated utterances, of which 30\% is spent on tokenization, 12\% on normalization, and 58\% on out-of-vocabulary fallbacks (0.5\% OOV rate). To demonstrate its effectiveness, we used FastThaiG2P to phonemize Som-TTS, an open dataset containing 20 hours of grapheme-and-audio pairs, then trained an 82M-parameter StyleTTS 2 model based on a Kokoro-TTS recipe. The resulting model vocalizes intelligible Thai speech suitable for prototyping and development at 0.25 real-time factor (4x real-time) with ONNX inference on CPU.

## Metadata
- **Published**: 2026-08-13T04:46:01Z
- **Authors**: Charin Polpanumas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12814v1)