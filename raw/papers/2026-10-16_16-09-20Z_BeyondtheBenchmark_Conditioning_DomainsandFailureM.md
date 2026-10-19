---
title: Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS
published: 2026-10-16T16:09:20Z
authors: Séverin Baroudi, Yanis Labrak, Petr Motlicek, Hervé Bredin, Ricard Marxer
url: http://arxiv.org/abs/2610.23678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS

## Abstract
Qwen3-TTS reports state-of-the-art zero-shot voice cloning, but its technical report leaves open how the model should be conditioned, how it behaves outside read speech, and how it fails. We characterise its two cloning interfaces, in-context learning (ICL) and X-Vector, against Chatterbox, XTTS-v2 and F5-TTS on read, meeting, emotional and air-traffic-control (ATC) speech, using eighteen objective measures, an LLM judge, a spoofing countermeasure and a listening test. Neither interface dominates: ICL clones timbre more closely from correctly transcribed references, X-Vector clones timing, and ICL degrades sharply when a short reference transcript is wrong. Domain explains four times more variance than system choice. Qwen3-TTS leads on intelligibility and pitch register but trails on prosody, and the objective measures rank systems differently from listeners. An off-the-shelf countermeasure flags its clones no more often than genuine recordings, and on ATC radio it fails for every system. Code and audio are released.

## Metadata
- **Published**: 2026-10-16T16:09:20Z
- **Authors**: Séverin Baroudi, Yanis Labrak, Petr Motlicek, Hervé Bredin, Ricard Marxer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23678v1)