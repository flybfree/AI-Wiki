---
title: VibeVoice-ASR-BitNet Technical Report
published: 2026-07-23T09:08:04Z
authors: Songchen Xu, Ting Song, Shaohan Huang, Zhiliang Peng, Yan Xia, Yujie Tu, Xin Huang, Jianwei Yu, Li Dong, Furu Wei
url: http://arxiv.org/abs/2607.21075v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VibeVoice-ASR-BitNet Technical Report

## Abstract
We present VibeVoice-ASR-BitNet, a compressed variant of VibeVoice-ASR optimized for real-time inference on edge CPUs. We apply heterogeneous quantization tailored to the computational characteristics of each stage: the VAE acoustic tokenizer uses full-pipeline INT8 quantization (I8_S) with kernel fusion and SIMD optimization, while the autoregressive language model adopts BitNet-style ternary weights (I2_S). To preserve accuracy under aggressive compression, we employ a progressive quantization-aware training strategy. For inference, we implement custom SIMD kernels and fused operators within the ggml framework targeting both ARM and x86 platforms, achieving real-time recognition with RTF < 1 using as few as 3 CPU threads. VibeVoice-ASR-BitNet is 1.6-2.3x faster than Whisper.cpp at comparable model sizes (~1.6 GB), with only modest accuracy degradation compared to the FP16 baseline.

## Metadata
- **Published**: 2026-07-23T09:08:04Z
- **Authors**: Songchen Xu, Ting Song, Shaohan Huang, Zhiliang Peng, Yan Xia, Yujie Tu, Xin Huang, Jianwei Yu, Li Dong, Furu Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21075v1)