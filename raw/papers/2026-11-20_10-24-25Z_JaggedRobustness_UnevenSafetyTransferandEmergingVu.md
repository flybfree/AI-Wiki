---
title: Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization
published: 2026-11-20T10:24:25Z
authors: Ramneek Agnihotri, Yingte Xu, Hans Vath
url: http://arxiv.org/abs/2611.27424v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization

## Abstract
Quantization enables efficient inference in language models through model parameter compression. This work audits the impact of quantization on capability and safety domains including model safeguards, instruction-following, ethics and bias. Through benchmarks, we find that model safeguards and bias can degrade under quantization, while other capabilities such as truthfulness remain more stable in Qwen3-4B. We define this uneven transfer of LLM capabilities under quantization as Jagged Robustness. We find multiple factors driving Jagged Robustness: task complexity, evaluation method and generation coherence. Moreover, we verify the degradation of model safeguards by observing increased compliance with unsafe requests under quantization, and demonstrate universal adversarial suffix attacks that are benign for the full model but jailbreak quantized models. The findings indicate that it is risky to assume that the performance and robustness can transfer evenly across different capability domains from full models to quantized models.

## Metadata
- **Published**: 2026-11-20T10:24:25Z
- **Authors**: Ramneek Agnihotri, Yingte Xu, Hans Vath
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.27424v1)