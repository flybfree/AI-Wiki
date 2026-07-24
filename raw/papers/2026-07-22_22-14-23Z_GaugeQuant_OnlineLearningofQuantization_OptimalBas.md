---
title: GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries
published: 2026-07-22T22:14:23Z
authors: Miguel P. Bento, João Seabra
url: http://arxiv.org/abs/2607.20757v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries

## Abstract
Transformers are known to have internal continuous symmetries that leave outputs invariant, while modifying quantization. GaugeQuant leverages this in-training by introducing a LogSumExp term to the loss that breaks the symmetries, thus selecting a basis that minimizes activation outliers. A stop-gradient operator ensures that only rotation matrices are updated, yielding the language modeling objective completely unaltered. Our requires no specific calibration data, no quantization simulation, and adds negligible training overhead. With the LLaMA-2 7B model under W4A4 quantization with group size 128, perplexity drops from 8.22 to 6.73, competing with post-training methods that require frozen models and calibration datasets. Under W4A16, perplexity drops from 11.16 to 5.45. Code is available at https://github.com/MPedraBento/gauge-quant.

## Metadata
- **Published**: 2026-07-22T22:14:23Z
- **Authors**: Miguel P. Bento, João Seabra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20757v1)