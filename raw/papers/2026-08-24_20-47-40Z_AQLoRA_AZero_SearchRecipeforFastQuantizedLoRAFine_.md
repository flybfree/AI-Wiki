---
title: AQLoRA: A Zero-Search Recipe for Fast Quantized LoRA Fine-Tuning
published: 2026-08-24T20:47:40Z
authors: Md Romyull Islam
url: http://arxiv.org/abs/2608.23816v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AQLoRA: A Zero-Search Recipe for Fast Quantized LoRA Fine-Tuning

## Abstract
Quantized fine-tuning (QLoRA) saves memory but not time. It dequantizes every 4-bit weight on the fly, so it trains more slowly than fp16 LoRA. We present AQLoRA (Adaptive-Quantization LoRA), a recipe that buys part of that time back. One CPU pass over the weights sets everything, with no search and no calibration data. The pass ranks layers by NF4 reconstruction error and keeps the top-K in fp16 under a memory budget. Those layers skip dequantization, which is where the speed comes from. A quality setting adapts every layer. A speed setting adapts only the top blocks, so the backward pass stops early. The rule reproduces Unsloth's hand-curated dynamic-4bit selection exactly, in seconds, where search-based allocation needs repeated calibration passes.   We evaluate on Commonsense-170K across six models and four architecture families, from 1.4B to 14B. The speed setting trains 11.1 +/- 2.7% faster than well-tuned QLoRA and gives up about one accuracy point. It was faster in all nine independent timing sessions, at worst by 7%. The quality setting trains 4.8 +/- 2.4% faster. Its accuracy is level with QLoRA on every model and within a point of fp16 LoRA, for 0.2 GiB more memory. These error bars are measured between independent sessions, not within one. Earning them taught us three rules for timing on shared hardware. Fix the measurement duration, not the step count. Measure the noise floor from a duplicated arm, not a nearly identical method. Repeat whole sessions: a floor computed inside one sweep understates the real uncertainty several times over, and the random seed controls almost none of it.   We validate the recipe with controls and report the two that failed. Choosing adapter layers by weight density is no better than random. Choosing protected layers by quantization error is not either. The count of protected layers, not their identity, carries the speed effect.

## Metadata
- **Published**: 2026-08-24T20:47:40Z
- **Authors**: Md Romyull Islam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23816v1)