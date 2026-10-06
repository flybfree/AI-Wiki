---
title: Anosognosia in LLMs: Probing Self-Awareness of Quantized Computational Substrate
published: 2026-10-05T11:55:01Z
authors: Yoshihiro Izawa, Gouki Minegishi, Yoko Yamakata
url: http://arxiv.org/abs/2610.06174v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Anosognosia in LLMs: Probing Self-Awareness of Quantized Computational Substrate

## Abstract
Can LLMs recognize degradation in their own computational substrate? Inspired by anosognosia, a neurological condition in which patients fail to recognize impairments in their own abilities, we investigate whether LLMs can recognize degradation in their computational substrate induced by quantization. We first show that existing models fail to self-report their quantization state, even when provided with their own generated text as an external cue. Linear probing reveals that, while generated text carries almost no trace of quantization, internal representations contain clear, method-specific fingerprints. Through training, models learn to identify severely degraded outputs such as those of 4-bit models by comparison, yet still fail to do so from a single output. A shared LoRA trained jointly across quantization levels succeeded in reading out internal fingerprints, but fails on unseen quantization methods, merely mapping method-specific fingerprints to labels. Whereas external self-observation can restore awareness in some cases of human anosognosia, our results suggest that the more promising route to enabling such awareness in LLMs may lie in their internal representations. Our results highlight fundamental limits of generalizability to LLM self-monitoring.

## Metadata
- **Published**: 2026-10-05T11:55:01Z
- **Authors**: Yoshihiro Izawa, Gouki Minegishi, Yoko Yamakata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06174v1)