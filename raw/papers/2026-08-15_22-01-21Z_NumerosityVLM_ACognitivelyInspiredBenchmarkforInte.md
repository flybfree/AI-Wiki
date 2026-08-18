---
title: NumerosityVLM: A Cognitively Inspired Benchmark for Interpreting Numerosity Representations in Vision-Language Models
published: 2026-08-15T22:01:21Z
authors: Yiming Fu, Fangjun Li, Xiujin Liu, Ruidong Ma, Hang Yu, Zhichen Lu, Kanwei He, Alessandro Di Nuovo, Angelo Cangelosi, Zhegong Shangguan
url: http://arxiv.org/abs/2608.15425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NumerosityVLM: A Cognitively Inspired Benchmark for Interpreting Numerosity Representations in Vision-Language Models

## Abstract
Vision-language models (VLMs) achieve strong performance on high-level multimodal tasks, yet numerosity perception, a cognitive ability that emerges in human infants before language acquisition, remains poorly understood in current models, as existing counting benchmarks entangle numerosity with correlated visual factors. We introduce a cognitively inspired diagnostic benchmark, NumerosityVLM, comprising 10,800 synthetic images across six controlled conditions. The benchmark orthogonally manipulates object size, spatial arrangement, and numerosity, while progressively ablating texture, shape, and color. Evaluating seven VLMs in a zero-shot setting, multi-factor analysis reveals that model architecture explains the largest proportion of performance variance (partial $ω^{2}=0.325$), far exceeding visual conditions. Layer-wise probing further shows that linearly separable numerosity signals consistently emerge at early stages of the vision encoder, while performance differences across evaluated models are primarily associated with the language model component. Code and data are publicly available at https://github.com/fuy3/NumerosityVLM-Benchmark, and https://huggingface.co/datasets/fuy3/NumerosityVLM.

## Metadata
- **Published**: 2026-08-15T22:01:21Z
- **Authors**: Yiming Fu, Fangjun Li, Xiujin Liu, Ruidong Ma, Hang Yu, Zhichen Lu, Kanwei He, Alessandro Di Nuovo, Angelo Cangelosi, Zhegong Shangguan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15425v1)