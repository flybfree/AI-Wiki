---
title: Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model
url: http://arxiv.org/abs/2607.13013v1
type: paper-summary
date: 2026-07-15
source_paper: 2026-07-14_17-53-22Z_Audio_NativeSpeechRecognitionwithaFrozenDiscrete_D.md
generated_at: 2026-07-15 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an audio‑native speech recognition system that uses a frozen discrete‑diffusion language model to generate whole transcripts in parallel, instead of autoregressive token‑by‑token decoding. The model integrates a Whisper encoder and lightweight adapters while training only 42 million parameters, achieving a 6.6% word error rate on LibriSpeech test‑clean. The frozen diffusion model avoids the need for large‑scale fine‑tuning of the backbone, keeping training efficient.

## Key Takeaways
- The diffusion approach refines the entire transcript across eight parallel steps, enabling faster processing regardless of utterance length.
- A connectionist temporal classification loss applied through a frozen output head resolves the deadlock where acoustic features are ignored by attention layers.
- The model uses a single adapter trained on six languages and reaches 6.6% word error rate on English, Hindi, and Mandarin.

## Context
Autoregressive decoders dominate speech recognition but suffer from sequential latency and limited parallelism. Diffusion models have shown promise in image generation but are rarely applied to audio without heavy adaptation. This work demonstrates that diffusion can be made audio‑native with minimal parameter overhead. Current systems often require separate acoustic and language models, increasing complexity.

## Implications
The approach could enable real‑time transcription services by leveraging parallel generation, reducing hardware costs. It also opens doors for multilingual deployment using a single adapter, supporting diverse language markets efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.13013v1)
