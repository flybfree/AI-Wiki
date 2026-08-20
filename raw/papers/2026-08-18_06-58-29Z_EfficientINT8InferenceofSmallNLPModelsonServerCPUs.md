---
title: Efficient INT8 Inference of Small NLP Models on Server CPUs with PyTorch Native Stack
published: 2026-08-18T06:58:29Z
authors: Weiwen Xia, Yuxin Cui, E Cao
url: http://arxiv.org/abs/2608.18182v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient INT8 Inference of Small NLP Models on Server CPUs with PyTorch Native Stack

## Abstract
Small NLP models, especially BERT-family encoders, remain important in industrial workloads such as classification, ranking, and retrieval even in the era of large language models. On server CPUs, INT8 quantization offers an attractive latency-throughput-cost trade-off, but users increasingly expect such acceleration to be available directly in the native PyTorch stack. We integrate SmoothQuant into TorchAO and optimize the resulting inference path for Intel Xeon CPUs through graph-level fusion in TorchInductor and efficient INT8 GEMM kernel selection across oneDNN-, AVX512_VNNI-, and AMX-based implementations. Across BERT, DistilBERT, and XLM-RoBERTa benchmarks, the approach delivers up to 5.8x end-to-end throughput speedup with negligible---and in some cases no measurable---accuracy loss relative to the FP32 baseline. We also validated our work by detailed performance analysis with roofline models. The implementation has been upstreamed to PyTorch and TorchAO, enabling out-of-the-box deployment with native PyTorch tooling

## Metadata
- **Published**: 2026-08-18T06:58:29Z
- **Authors**: Weiwen Xia, Yuxin Cui, E Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18182v1)