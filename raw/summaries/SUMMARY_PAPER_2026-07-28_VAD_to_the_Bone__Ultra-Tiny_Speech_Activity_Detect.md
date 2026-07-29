---
title: VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment
url: http://arxiv.org/abs/2607.25870v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_15-37-44Z_VADtotheBone_Ultra_TinySpeechActivityDetectionforE.md
generated_at: 2026-07-28 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces kiloVAD, a voice activity detection model that runs on edge devices using standard Mel features and CNN layers without requiring unsupported components such as learnable filterbanks or recurrent networks. It achieves an AUC of 0.850 on AVA‑Speech with only 2.1 k parameters and a 200 ms causal context, setting a new state‑of‑the‑art for deployment‑ready VAD.

## Key Takeaways
- kiloVAD is built exclusively from CNN layers and standard Mel features, making it compatible with widely supported hardware and software stacks.  
- The model employs per‑layer structured pruning combined with self‑distillation and angle‑based quantization‑aware training (QAT), which improves QAT performance by 1–4 % compared to standard QAT.  
- Under causal inference, kiloVAD delivers a high AUC of 0.850 while maintaining a tiny parameter count and short context window.

## Context
Voice activity detection is essential for always‑on audio processing where memory, latency, and compute are tightly constrained. Recent compact models have shown strong accuracy but often rely on architectures that are not universally deployable, highlighting the need for lightweight, hardware‑friendly solutions.

## Implications
This work demonstrates that state‑of‑the‑art VAD performance can be achieved without sacrificing compatibility with standard edge platforms, encouraging developers to adopt such models in real‑time applications. The results suggest a shift toward inference‑centric design where model size and causal constraints are prioritized over complex component usage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25870v1)
