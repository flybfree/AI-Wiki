---
title: When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized LLMs
published: 2026-08-26T16:32:50Z
authors: Yao Fu, Lijia Huang, Xiaomin Li, Runchao Li, Yu Yin, Kenneth A. Loparo
url: http://arxiv.org/abs/2608.25977v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized LLMs

## Abstract
Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences. While the Myers--Briggs Type Indicator (MBTI) has emerged as a common framework for assessing LLMs' personality, existing studies focus primarily on full-precision models and evaluate only final outputs. They overlook the widespread deployment of quantized LLMs requiring low memory footprints, whose personality traits remain underexplored. In this work, we present a systematic MBTI analysis of open-source LLMs across multiple precisions, including mainstream 4-bit methods (GPTQ, AWQ) and extreme 2-bit settings (AQLM variants). Beyond output-level evaluation, we examine how personality emerges across layers through option-level entropy and confidence-gap dynamics, and introduce Uncertainty-Amplified Layer Decoding (UALD) to study decoding-induced personality drift at inference time. Our results reveal a key insight: LLMs' personality is not a static property, but an emergent, layer-dependent decision process sensitive to quantization, prompting, and decoding. Specifically, we find that (1) ENFJ remains dominant across model families and precisions; (2) 4-bit quantization largely preserves coarse personality structure, while 2-bit quantization disrupts fine-grained prompt consistency and cross-precision agreement; (3) personality decisions emerges in upper layers, following substantial ambiguity in early layers; and (4) inference decoding can shift personality, while personality-aligned conditioning improves robustness. These findings provide a new perspective on the behavioral reliability of quantized LLMs and highlight the importance of considering internal dynamics and inference strategies in personality-sensitive chatbot applications.

## Metadata
- **Published**: 2026-08-26T16:32:50Z
- **Authors**: Yao Fu, Lijia Huang, Xiaomin Li, Runchao Li, Yu Yin, Kenneth A. Loparo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25977v1)