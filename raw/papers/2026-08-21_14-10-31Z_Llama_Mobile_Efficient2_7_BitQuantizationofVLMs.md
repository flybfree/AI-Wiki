---
title: Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs
published: 2026-08-21T14:10:31Z
authors: Luka Ribar, Jeevan Bhoot, Douglas Orr
url: http://arxiv.org/abs/2608.21134v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs

## Abstract
Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements. We present a framework for quantizing VLMs for efficient inference on resource-constrained hardware. Our approach combines a quantization pipeline that uses the model itself to generate training data and does not require access to the training setup, with a novel 2.7-bit-per-parameter format supporting efficient execution on Arm CPUs. We validate our approach by compressing the Llama 3.2 11B Vision Instruct model to 3.7 GB with 8-bit activations, preserving strong performance on a set of standard visual question answering tasks.

## Metadata
- **Published**: 2026-08-21T14:10:31Z
- **Authors**: Luka Ribar, Jeevan Bhoot, Douglas Orr
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21134v1)