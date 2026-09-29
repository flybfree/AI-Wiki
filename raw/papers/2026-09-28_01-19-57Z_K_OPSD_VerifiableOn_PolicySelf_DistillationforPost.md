---
title: K-OPSD: Verifiable On-Policy Self-Distillation for Post-Training Vision-Language Models on AEC Drawings
published: 2026-09-28T01:19:57Z
authors: Yunfei Bai, Enrico Chionna, Akash Amol, Kawaljit Singh KC, Joern Tinnemeyer
url: http://arxiv.org/abs/2609.34082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# K-OPSD: Verifiable On-Policy Self-Distillation for Post-Training Vision-Language Models on AEC Drawings

## Abstract
Interpreting architecture, engineering, and construction (AEC) drawings is hard for general Multimodal Large Language Models (MLLMs) and vision-language models (VLMs). We introduce K-OPSD, a VLM post-training methodology for improving AEC drawing understanding. Building on On-Policy Self-Distillation (OPSD) with verifiable supervision, we construct a teacher from the model's own best-of-N generations, certified by a process-level verifier, and rescue failed prompts by resampling under a hint that exposes the verified answer. We then perform an on-policy model update by training on verified completions with a cross-entropy inner-loss, outperforming the bounded token-wise generalized Jensen-Shannon divergence (JSD) used by on-policy distillation. Using K-OPSD, we fine-tune Qwen3-VL models on the AECV-Bench dataset. The resulting models attain the top average judge score (0.819) and combined accuracy (0.738), achieving competitive results against open-source baseline models. The recipe transfers to the out-of-domain ArchCAD dataset, where the 8B model gains most. We present the verifier suite and the continual learning and self-improving pipeline, our results provide preliminary evidence that verifier-guided self-distillation is a promising route toward more reliable machine reading of architecture drawings.

## Metadata
- **Published**: 2026-09-28T01:19:57Z
- **Authors**: Yunfei Bai, Enrico Chionna, Akash Amol, Kawaljit Singh KC, Joern Tinnemeyer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34082v1)