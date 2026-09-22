---
title: FoldQuantVLA: Native Low-Bit Quantization of Vision-Language-Action Models via Consistent Folding
published: 2026-09-21T11:28:41Z
authors: Hung T. Ho, Khanh D. Nguyen, Quang D. Nguyen, Thanh Q. Duong, Ngan Le, Meng Guo, Vien A. Ngo, An T. Le
url: http://arxiv.org/abs/2609.24433v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FoldQuantVLA: Native Low-Bit Quantization of Vision-Language-Action Models via Consistent Folding

## Abstract
Low-bit vision-language-action inference must reduce observation-to-action latency while preserving robot behavior. We present FoldQuantVLA, a post-training quantization framework that carries a consistent activation representation through calibration, weight rounding, and native integer execution. It combines channel scaling and block Hadamard transforms with dynamic per-token quantization, without policy retraining. Custom TensorRT plugins execute projections in both the language backbone and iterative action expert with four-bit weights and activations (W4A4) on Ada GPUs and Jetson AGX Orin. Evaluation spans LIBERO, SimplerEnv, and two robot platforms. Across three GR00T checkpoints and $π_{0.5}$, W4A4 achieves $1.20$ to $1.33\times$ speedups over floating-point TensorRT on Orin and $1.25$ to $1.52\times$ on desktop. Retaining language attention-output and feed-forward down projections at eight bits (W8A8) improves held-out action fidelity on all four checkpoints. Across four real-robot tasks, this configuration raises observed GR00T N1.7 success from $80.0\%$ with uniform W4A4 to $92.5\%$ over 80 trials per configuration, with a measured additional Orin latency of 1 ms.

## Metadata
- **Published**: 2026-09-21T11:28:41Z
- **Authors**: Hung T. Ho, Khanh D. Nguyen, Quang D. Nguyen, Thanh Q. Duong, Ngan Le, Meng Guo, Vien A. Ngo, An T. Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24433v1)