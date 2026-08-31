---
title: HyQuant: Hybrid-Precision Quantization for LLM Attention
published: 2026-08-28T03:30:28Z
authors: Jiatong Ding, Bingxin Xing, Yu Zhang, Dian Ding, Xiaodong Yi, Xianbin Ouyang, Feihu Zhou, Kun Zhang, Zhenyu Guo, Hao Pan, Guangtao Xue, Yiming Zhang
url: http://arxiv.org/abs/2608.27875v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyQuant: Hybrid-Precision Quantization for LLM Attention

## Abstract
Quantization has been widely adopted in LLM training and inference to reduce cost and improve efficiency. However, low-bit quantization of the \emph{attention} module often introduces large errors at very low bit-widths, causing performance degradation. Existing methods mainly rely on smoothing techniques to handle outliers, while we propose a hybrid quantization design to better balance accuracy and efficiency. Specifically, we propose \textbf{HyQuant}, an efficient hybrid quantization framework for LLM attention. HyQuant quantizes most attention states into low-bit formats while retaining a small set of vertical-line tokens and local-window states in high precision. These accuracy-critical regions are selected using lightweight vertical-line-aware attention-pattern signals, reducing quantization error with limited overhead. In the Prefill stage, HyQuant uses a hybrid-precision quantized attention operator that preserves vertical-line tokens and a local sliding window in full precision while quantizing the remaining context. In the Decode stage, HyQuant applies the same principle to KV-cache compression and fuses KV dequantization with attention computation to improve memory and hardware efficiency. Across diverse tasks, models, and datasets, HyQuant maintains nearly lossless accuracy with an extremely simple design, demonstrating the efficiency and practical feasibility of hybrid quantization for LLM attention. Code is available at: https://github.com/jerrysfls/HyQuant .

## Metadata
- **Published**: 2026-08-28T03:30:28Z
- **Authors**: Jiatong Ding, Bingxin Xing, Yu Zhang, Dian Ding, Xiaodong Yi, Xianbin Ouyang, Feihu Zhou, Kun Zhang, Zhenyu Guo, Hao Pan, Guangtao Xue, Yiming Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27875v1)