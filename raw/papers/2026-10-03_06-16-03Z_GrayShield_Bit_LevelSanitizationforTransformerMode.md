---
title: GrayShield: Bit-Level Sanitization for Transformer Model Supply-Chain Security
published: 2026-10-03T06:16:03Z
authors: Armstrong Foundjem, Tsung-Hsien Chuang, Foutse Khomh, Mohamed Amine Merzouk
url: http://arxiv.org/abs/2610.04319v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GrayShield: Bit-Level Sanitization for Transformer Model Supply-Chain Security

## Abstract
Transformer models such as BERT and Vision Transformer~(ViT) achieve strong performance via densely parameterized attention backbones. However, the least significant bits~(LSBs) of their 32-bit floating-point weights can be abused as covert channels to conceal malicious payloads, posing a serious threat to the AI model supply chain. We propose \GS (\GSabbr), a lightweight, post-training, zero-data sanitization method that completely replaces the declared mantissa-LSB channel with a Gray-code-guided low-transition sequence. Complete payload-independent overwrite, whether keyed or public, makes the sanitized target bits independent of the embedded payload and gives that declared channel zero capacity. Gray coding supplies overwrite structure, while a keyed per-tensor phase supplies pattern diversity. Benchmarked against seven post-training defenses on four Transformer model presets and two real-world malware payloads, \GSabbr maintains sub-$1\%$ accuracy impact and achieves $49.96\pm0.66$ percentage-point Recovery Reduction (RR) under five implemented attacker variants. Because pre-defense recovery is effectively $100\%$, RR near 50 percentage points corresponds to post-sanitization bit accuracy at binary chance. Its main empirical advantage is stable near-chance sanitization with substantially smaller weight-distribution shift than the evaluated near-chance baselines PatternMask (PM) and Post-Training Quantization (PTQ).

## Metadata
- **Published**: 2026-10-03T06:16:03Z
- **Authors**: Armstrong Foundjem, Tsung-Hsien Chuang, Foutse Khomh, Mohamed Amine Merzouk
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04319v1)