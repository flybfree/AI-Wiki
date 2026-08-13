---
title: Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS with a Learnable Speaker Encoder
url: http://arxiv.org/abs/2608.11650v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_04-48-29Z_Confucius4_TTS_Transcript_FreeCross_LingualZero_Sh.md
generated_at: 2026-08-12 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Confucius4-TTS, a multilingual zero-shot TTS system that generates speech without requiring transcriptions of audio prompts. It supports 14 languages and can perform both intra-lingual and cross-lingual voice cloning. The model achieves high intelligibility and speaker similarity on benchmark evaluations.

## Key Takeaways
- Confucius4-TTS eliminates the need for prompt transcripts by using a learnable speaker encoder to extract timbre from self-supervised speech representations, enabling zero-shot generation across languages.
- The system employs a two-stage architecture with text-to-semantic and semantic-to-acoustic modules, allowing continuation cloning when reference audio is available.
- On CV3-Eval it reaches an average WER of 3.73% across six directions, outperforming prior methods in human evaluation.

## Context
Zero-shot TTS aims to produce speech from text without any pre‑trained voice data, yet most approaches still rely on transcripts which hinder cross‑lingual applications. This work demonstrates that a speaker encoder can capture voice identity purely from self‑supervised audio, opening the door to truly transcript‑free cloning.

## Implications
For industry, Confucius4-TTS reduces development costs by removing transcription pipelines and supporting rapid multilingual deployment. Practitioners can now clone voices across languages with minimal resources, accelerating personalized communication solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11650v1)
