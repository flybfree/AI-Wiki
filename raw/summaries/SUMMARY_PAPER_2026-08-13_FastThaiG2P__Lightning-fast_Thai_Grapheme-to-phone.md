---
title: FastThaiG2P: Lightning-fast Thai Grapheme-to-phoneme Conversion for Voice Agent Pipelines
url: http://arxiv.org/abs/2608.12814v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_04-46-01Z_FastThaiG2P_Lightning_fastThaiGrapheme_to_phonemeC.md
generated_at: 2026-08-13 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
FastThaiG2P introduces a sub‑millisecond grapheme‑to‑phoneme conversion system for Thai that integrates with Text‑to‑Speech pipelines using International Phonetic Alphabet and Kokoro‑TTS conventions. The method relies on a PyThaiNLP tokenized dictionary, normalization rules, and out‑of‑vocabulary fallbacks to achieve an average latency of 0.15 ms per utterance while keeping the OOV rate low at 0.5 %. Evaluation on the Som‑TTS dataset shows that the system can drive an 82M‑parameter StyleTTS 2 model at a real‑time factor of 0.25 with ONNX CPU inference.

## Key Takeaways
- The pipeline processes Thai text to phonemes in under half a millisecond, with tokenization consuming 30 % and normalization 12 % of the total time.  
- Out‑of‑vocabulary handling accounts for only 58 % of the latency, resulting in an OOV rate as low as 0.5 %.  
- The system enables real‑time Text‑to‑Speech at a factor of 0.25 using an 82M‑parameter StyleTTS 2 model on CPU via ONNX.

## Context
Thai speech synthesis remains challenging due to its tonal nature and complex orthography, limiting the speed of existing G2P models. FastThaiG2P addresses these issues by combining a lightweight dictionary with efficient normalization, demonstrating that real‑time performance is achievable without sacrificing intelligibility in voice agents.

## Implications
For developers building Thai voice assistants or TTS services, FastThaiG2P offers a ready‑to‑use solution that reduces latency and improves user experience. The method’s modular design allows integration into existing pipelines, making it valuable for both research prototyping and commercial deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12814v1)
