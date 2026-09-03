---
title: SpeakPay: Domain-Adaptive LoRA Fine-Tuning of Whisper for Low-Resource Nepali Financial Speech Recognition
url: http://arxiv.org/abs/2609.01737v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_18-07-24Z_SpeakPay_Domain_AdaptiveLoRAFine_TuningofWhisperfo.md
generated_at: 2026-09-02 20:57
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SpeakPay, a voice‑first digital wallet designed for visually impaired users in Nepal, and presents domain‑adaptive LoRA fine‑tuning of Whisper large‑v2 to boost speech recognition on low‑resource Nepali financial commands. The adapted model cuts Word Error Rate from 129.95% (zero‑shot) to 42.58%, a 67.2 % relative reduction, and lifts Devanagari numeral accuracy from 0.0 % to 73.9 %.

## Key Takeaways
- The domain adaptation reduces Word Error Rate from 129.95 % (zero‑shot baseline) to 42.58%, a 67.2 % relative reduction.  
- Devanagari numeral recognition accuracy improves from 0.0 % to 73.9 %.  
- Transaction Success Rate jumps from 1.67 % to 33.33%, roughly a 20‑fold gain.

## Context
Low‑resource speech recognition often relies on large models that need extensive domain‑specific data, which is costly and impractical for niche languages like Nepali financial commands. This work shows that fine‑tuning with few labeled examples can yield substantial performance gains without massive datasets.

## Implications
The approach provides a scalable template for adapting state‑of‑the‑art speech models to underserved language communities, enabling inclusive digital services with minimal data investment; practitioners can apply LoRA techniques to other low‑resource domains efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01737v1)
