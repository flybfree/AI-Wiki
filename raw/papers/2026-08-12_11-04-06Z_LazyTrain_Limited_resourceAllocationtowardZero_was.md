---
title: LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization in Large Language Model Training
published: 2026-08-12T11:04:06Z
authors: Xiaojun Wu, Cehao Yang, Honghao Liu, Xueyuan Lin, Xuhui Jiang, Chengjin Xu, Jia Li, Jian Guo
url: http://arxiv.org/abs/2608.11919v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization in Large Language Model Training

## Abstract
Training large language models on limited hardware is increasingly a scheduling problem across GPU compute, host memory, PCIe transfer, and storage bandwidth. Existing offloading systems reduce GPU residency, and MegaTrain shows that a CPU-master layer-streaming executor can train large models on a single GPU, but fixed checkpointing and placement heuristics still leave communication exposed on the critical path. We propose LazyTrain, an optimization layer over a layer-streaming executor. LazyTrain formulates checkpoint selection, activation placement, recomputation, and CPU-GPU-NVMe communication overlap as a mixed-integer scheduling problem, then executes the solved policy during training. It further couples 8-bit optimizer states with fast gradient clipping as a single Hybrid 8-bit operator: state compression reduces optimizer-state memory, while fast clipping counteracts the additional CPU-side update overhead. Across H800 experiments from Qwen2.5-3B to Qwen3.6-27B, LazyTrain improves sustained TFLOPS over matched baselines runs by approximately 1.24$\times$; RTX 3090 experiments likewise increase the maximum feasible batch size by one at each model scale. In the primary Qwen3.6-27B H800 MetaMathQA run, LazyTrain reaches 219.95 TFLOPS and 1361 tokens/s at batch size 72, peaks at 68.84\,GB of GPU memory, and obtains 95.42\% exact-match accuracy on the full evaluation split. The source code is available at https://github.com/DataArcTech/LazyTrain.

## Metadata
- **Published**: 2026-08-12T11:04:06Z
- **Authors**: Xiaojun Wu, Cehao Yang, Honghao Liu, Xueyuan Lin, Xuhui Jiang, Chengjin Xu, Jia Li, Jian Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11919v1)