---
title: Voice Memory for Agentic Speech Recognition
url: http://arxiv.org/abs/2607.26410v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_02-42-56Z_VoiceMemoryforAgenticSpeechRecognition.md
generated_at: 2026-07-29 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Voice Memory, an inference‑only correction mechanism for agentic speech recognition that separates a frozen corrector from an asynchronous score‑gated optimizer. By limiting the optimizer to edits that strictly improve held‑out scores, Voice Memory reduces over‑correction errors and improves weighted word error rates across diverse domains without adding parameters or changing any model weights.

## Key Takeaways
- The fixed memory file enables a per‑utterance decision between acting on a hypothesis or abstaining, preserving the 1‑best baseline while allowing occasional corrections.  
- Bounded edits driven by a score gate cut over‑correction from up to 64% to 35%, especially in noisy financial news scenarios.  
- Weighted word error rates drop from 8.36% to 7.52% across ten HyPoradise domains, with the largest gains seen for air‑travel commands and far‑field speech.

## Context
Voice Memory extends the ASR‑LM framework by introducing a listener‑thinker split that keeps the learned skill auditable and portable. It demonstrates how controlled generative error correction can be integrated into real‑time inference pipelines without computational overhead, aligning with trends toward efficient, modular AI systems.

## Implications
For industry practitioners, Voice Memory offers a practical way to enhance ASR accuracy while maintaining low latency and zero additional parameters, supporting deployment in resource‑constrained environments. The method’s portability across corrector families could inspire future research into auditable, self‑correcting speech recognition architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26410v1)
