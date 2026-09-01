---
title: Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering
published: 2026-08-29T05:50:54Z
authors: Zimo Shi, Xander Tifft, Wen Xing
url: http://arxiv.org/abs/2608.29070v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering

## Abstract
Chain-of-thought (CoT) reasoning traces are increasingly proposed as a mechanism for AI oversight: a monitor inspecting a model's reasoning can, in principle, detect misbehavior invisible from outputs alone. This assumes CoT surfaces what a model is instructed to do regardless of the instructions given. We test this assumption along two axes. First, we introduce the Instruction-Compliance Gap (ICG): the difference in probability that a model's CoT explicitly references a hidden system prompt directive when that directive is malign versus benign. Across 100 task pairs and 8 frontier reasoning models from 5 families, we find consistent asymmetric disclosure, a higher probability of leaking malign hidden instructions than benign ones, in Qwen3-14B (Wilcoxon $p=0.0001$, $+13.9$pp), Qwen3-32B ($p=0.0011$, $+13.0$pp), Qwen3-235B ($p=0.035$, $+5.8$pp), and similar results with MiniMax-M2.5 and DeepSeek-R1. The detector has 100% precision against two independent blinded labelling passes, and an LLM monitor reading only the reasoning trace reproduces the asymmetry in all 8 models against directive-free controls, identifying the specific directive in 82% of malign traces which the detector classifies as clean. Second, steering vectors extracted in MiniMax-M2.5 via Contrastive Activation Addition causally induce hiding from bare prompts and suppress it from prompts that would otherwise produce it, replicating in Qwen3-14B under a pre-registered design. Benign and malign-derived hiding vectors are highly similar (cosine $0.804$ in MiniMax-M2.5; $0.970$ in Qwen3-14B), implying that in these models the disclosure asymmetry arises from differential activation of a shared hiding direction rather than separate mechanisms.

## Metadata
- **Published**: 2026-08-29T05:50:54Z
- **Authors**: Zimo Shi, Xander Tifft, Wen Xing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29070v1)