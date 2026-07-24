---
title: MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference
published: 2026-07-20T09:23:10Z
authors: Simla Burcu Harma, Danila Mishin, Zhengyuan Su, Ayan Chakraborty, Elizaveta Kostenok, Dongho Ha, Babak Falsafi, Martin Jaggi, Yunho Oh, Amir Yazdanbakhsh
url: http://arxiv.org/abs/2607.17733v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference

## Abstract
4-bit quantization enables efficient LLM inference, but suffers from significant accuracy degradation due to outliers. Prior work addresses this problem via data rotation or mixed-precision integer quantization, but often relies on software-managed scaling and frequent dequantization, incurring substantial overhead. Microscaling formats, such as MXINT, eliminate these inefficiencies by encoding scales in hardware, yet remain incompatible with rotation-based methods. Our analysis reveals that outliers vary in severity, from rare extremes to frequent mild deviations, and that quantization sensitivity is unevenly distributed across layers and columns. These insights motivate a fine-grained, sensitivity-guided approach. We introduce MXSens, a training-free method that assigns mixed mantissa bitwidths (4/6/8) based on column- and layer-wise sensitivity, naturally leveraging the block-wise structure of MXINT. MXSens outperforms state-of-the-art quantization methods across a range of models and tasks. Under the W4A4KV4 setting, MXSens achieves perplexities of 3.77 and 7.63 on LLaMA-2-70B and LLaMA-3-8B, respectively, substantially improving over existing baselines on WikiText-2. Our work establishes a new balance between accuracy and resource efficiency for LLM quantization.

## Metadata
- **Published**: 2026-07-20T09:23:10Z
- **Authors**: Simla Burcu Harma, Danila Mishin, Zhengyuan Su, Ayan Chakraborty, Elizaveta Kostenok, Dongho Ha, Babak Falsafi, Martin Jaggi, Yunho Oh, Amir Yazdanbakhsh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17733v1)