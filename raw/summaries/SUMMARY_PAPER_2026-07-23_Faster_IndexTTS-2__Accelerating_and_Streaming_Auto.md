---
title: Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs
url: http://arxiv.org/abs/2607.21042v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_08-24-21Z_FasterIndexTTS_2_AcceleratingandStreamingAutoregre.md
generated_at: 2026-07-23 22:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Faster IndexTTS‑2, a GPU‑accelerated version of the state‑of‑the‑art autoregressive TTS system that combines GPT, a flow‑matching diffusion transformer, and a vocoder. The authors achieve up to fivefold speedup for the GPT component and three‑and‑a‑half times faster end‑to‑end inference while keeping quality metrics such as word error rate, speaker similarity, and naturalness unchanged.

## Key Takeaways
- Faster IndexTTS‑2 leverages NVIDIA TensorRT and TensorRT‑LLM to compress each neural network layer, delivering a 5.0× speedup for the autoregressive GPT stage on GPU hardware.  
- The end‑to‑end synthesis time drops to 3.6× faster than the original model, enabling real‑time streaming output suitable for interactive applications.  
- All quality assessments remain within acceptable limits, showing that acceleration does not compromise word error rate, speaker similarity, or naturalness.

## Context
Autoregressive text‑to‑speech models are prized for high‑quality synthesis but are limited by sequential token generation, which hampers real‑time deployment. This work addresses the latency bottleneck by applying model compression techniques to major components, illustrating how GPU‑centric acceleration can preserve performance in production pipelines.

## Implications
For researchers, Faster IndexTTS‑2 provides a practical benchmark for accelerating autoregressive TTS systems on GPUs without sacrificing quality. Industry practitioners can adopt these TensorRT optimizations to integrate low‑latency speech synthesis into voice assistants and streaming services, driving faster user interaction and broader accessibility of AI‑generated audio.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21042v1)
