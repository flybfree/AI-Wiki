---
title: LILAC: An Idempotent Neural Speech Codec
url: http://arxiv.org/abs/2608.05727v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_08-09-48Z_LILAC_AnIdempotentNeuralSpeechCodec.md
generated_at: 2026-08-06 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LILAC, a fully convolutional neural audio codec that is idempotent by design, meaning re‑encoding decoded speech yields the exact same token stream. The authors demonstrate that LILAC maintains high quality with UTMOS scores of 4.14 and 4.24 on LibriSpeech and LibriTTS‑R, matching state‑of‑the‑art sub‑kilobit‑per‑second codecs.

## Key Takeaways
- LILAC is built to be idempotent, so a single decode‑re‑encode pass does not alter any token, unlike the twelve baseline systems that average 15% token rewrites.  
- The codec operates at 24 kHz sampling rate with a bitrate of 0.75 kbit/s and a frequency resolution of 9.375 Hz, delivering low‑bandwidth speech representation.  
- LILAC achieves competitive quality scores (UTMOS 4.14 on LibriSpeech, 4.24 on LibriTTS‑R) that are comparable to the best existing sub‑kbit/s neural audio codecs.

## Context
Neural audio codecs have become essential for efficient speech processing in generation and editing pipelines, yet their non‑idempotent nature limits integration as token interfaces where re‑encoding is common. This limitation hampers pipeline robustness and reproducibility, prompting a need for codec designs that preserve information across multiple encoding steps.

## Implications
For practitioners building real‑time or offline speech systems, LILAC offers a reliable low‑bandwidth alternative that can be safely reused without quality loss. Its idempotent property simplifies deployment in streaming services and reduces the risk of cumulative errors, encouraging broader adoption of neural audio codecs in production pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05727v1)
