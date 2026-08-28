---
title: Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs
published: 2026-08-27T03:47:58Z
authors: Tanzila Rahman, Mehran Taghian Jazi, Yunke Peng, Zhuang Ma, Anandharaju Durai Raju, Yao Wang, Xing Huang, Hei Yi Mak, Shadan Golestan, Hoang Le, Yonghan Dong, Wei Guo, Yaoyuan Wang
url: http://arxiv.org/abs/2608.26581v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs

## Abstract
Low-bit quantization offers a promising avenue for reducing the computational and memory demands of Multimodal Large Language Models (MLLMs). Recent hardware support for low-precision formats, ranging from MXFP8 to ultra-low-bit formats such as MXFP4 and HiF4, has accelerated research into efficient MLLM training and deployment. In this work, we present a systematic study of these quantization schemes in representative MLLMs that span both video generation and reasoning tasks. Our analysis shows that MXFP8 achieves near-lossless performance, whereas aggressive 4-bit quantization leads to significant degradation. Through extensive ablations, we identify activation quantization as the primary source of this performance loss, contributing substantially more than weight quantization. Motivated by this observation, we propose Residual Fallback Quantization (RFQ), a lightweight activation reconstruction framework that supplements the primary ulta-low-bit activation representation with an auxiliary quantized residual pathway. By explicitly modeling and compensating for quantization errors, RFQ improves activation fidelity while preserving the efficiency advantages of ultra-low-bit computation. RFQ requires no architectural modifications and incurs negligible computational overhead. Extensive experiments on Wan2.2 and Qwen3-VL demonstrate that RFQ consistently recovers a substantial portion of the performance lost under the quantization of MXFP4 and HiF4, significantly narrowing the gap to BF16 baselines across both generation and 4 reasoning benchmarks. Our findings establish activation quantization as the dominant bottleneck in ultra-low-bit MLLMs and highlight residual-based activation reconstruction as an effective and practical strategy for robust 4-bit deployment.

## Metadata
- **Published**: 2026-08-27T03:47:58Z
- **Authors**: Tanzila Rahman, Mehran Taghian Jazi, Yunke Peng, Zhuang Ma, Anandharaju Durai Raju, Yao Wang, Xing Huang, Hei Yi Mak, Shadan Golestan, Hoang Le, Yonghan Dong, Wei Guo, Yaoyuan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26581v1)