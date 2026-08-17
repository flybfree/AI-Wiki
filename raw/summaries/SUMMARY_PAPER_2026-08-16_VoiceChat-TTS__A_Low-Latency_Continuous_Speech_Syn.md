---
title: VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents
url: http://arxiv.org/abs/2608.13831v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_23-37-07Z_VoiceChat_TTS_ALow_LatencyContinuousSpeechSynthesi.md
generated_at: 2026-08-16 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VoiceChat-TTS, a low-latency continuous text-to-speech model that enables interactive agents to generate speech in real time while handling user interruptions gracefully. It streams LLM token streams directly into synthesis and produces silence when no input is present, avoiding the need for resetting attention caches.

## Key Takeaways
- VoiceChat-TTS processes LLM text-token streams continuously, allowing seamless speech generation without pausing or resetting the KV cache, which reduces latency.
- The model supports explicit interruption via control tokens and outputs silence when no input is available, preserving modularity and high fidelity.
- By integrating ASR, interruption handling, and synthesis in a single pipeline, VoiceChat-TTS maintains speech quality while enabling always-on responsiveness.

## Context
Current speech language models are often turn-based, limiting real-time interaction and requiring complex multi-stage pipelines that increase latency and degrade quality. This paper addresses those limitations by proposing a unified continuous model suitable for voice assistants and conversational agents.

## Implications
For industry practitioners, VoiceChat-TTS offers a practical solution for building responsive voice interfaces with minimal latency. The approach can be adopted in chatbots, smart speakers, and AR/VR systems where real-time speech is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13831v1)
