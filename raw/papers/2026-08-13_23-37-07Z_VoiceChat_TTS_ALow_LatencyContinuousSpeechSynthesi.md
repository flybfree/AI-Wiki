---
title: VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents
published: 2026-08-13T23:37:07Z
authors: Edresson Casanova, Jaehyeon Kim, Mariana Graterol Fuenmayor, Shehzeen Hussain, Viacheslav Klimkov, Valentin Mendelev, Mikyas Desta, Paarth Neekhara, Piotr Zelasko, Chen Chen, Elena Rastorgueva, Ke Hu, Ankita Pasad, Xuesong Yang, Aya Alja'fari, Rajarshi Roy, Rohan Badlani, Jason Roche, Jason Li, Zhehuai Chen
url: http://arxiv.org/abs/2608.13831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents

## Abstract
Spoken dialogue is a natural form of human--computer interaction, yet most speech language models remain limited to turn-based operation and lack real-time adaptability, such as user barge-in. Recent duplex speech-to-speech and speech-to-text models reduce latency by replacing multi-stage pipelines, but often compromise speech quality because accurate ASR, interruption handling, and high-fidelity synthesis must be optimized jointly. We propose VoiceChat-TTS, a low-latency, continuous, and streamable text-to-speech model for interactive agents. VoiceChat-TTS is driven directly by LLM text-token streams, supports explicit interruption via control tokens, and produces silence when no textual input is available. The model enables always-on, responsive speech generation while preserving modularity and high speech quality, and it supports mid-utterance interruptions without resetting the KV cache.

## Metadata
- **Published**: 2026-08-13T23:37:07Z
- **Authors**: Edresson Casanova, Jaehyeon Kim, Mariana Graterol Fuenmayor, Shehzeen Hussain, Viacheslav Klimkov, Valentin Mendelev, Mikyas Desta, Paarth Neekhara, Piotr Zelasko, Chen Chen, Elena Rastorgueva, Ke Hu, Ankita Pasad, Xuesong Yang, Aya Alja'fari, Rajarshi Roy, Rohan Badlani, Jason Roche, Jason Li, Zhehuai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13831v1)