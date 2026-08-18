---
title: NPU Offloading of a Frozen Visual Encoder for Robot Policy Training
published: 2026-08-15T03:19:09Z
authors: Hyojun Yun, Seungjae Won, Hyungpil Moon
url: http://arxiv.org/abs/2608.15002v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NPU Offloading of a Frozen Visual Encoder for Robot Policy Training

## Abstract
When a robot policy is trained for a new task or dataset, its visual encoder can be frozen and only its action generation module trained, reducing training cost. Freezing removes the encoder's backward pass, but its forward pass must still run at every training step because the input images change, so it keeps consuming GPU compute. We therefore ask whether moving this computation to a low power AI accelerator such as an NPU can reduce total energy despite the added data transfer and longer training time, and how it affects policy performance. We built an asynchronous training pipeline that uses both a GPU and an NPU for the AR-Actor specialist. The frozen visual encoder runs in A8W8 INT8 on a Mobilint Aries2 NPU, while the FP32 action expert is trained on an NVIDIA GeForce RTX 5060 Ti GPU. We compared a GPU-only baseline with four conditions, L1 to L4, which gradually extend NPU offloading from one to four Transformer encoder layers. Each condition was trained for 30,000 steps with three random seeds. We measured GPU board power for the GPU-only condition and combined GPU and NPU board power for the NPU conditions. Energy per sample decreased by 17.1% in L1, which offloaded ResNet18 and the first encoder layer, and by 27.9% in L4, which offloaded ResNet18 and all four encoder layers. In contrast, training time per sample increased by 15.2% in L1 and 37.7% in L4, and peak allocated GPU memory decreased by 19.8 to 20.7%. The 15 resulting policies were each evaluated with the same 300 environment seeds, for a total of 4,500 simulator rollouts. The combined success rate was 93.33% for GPU-only and 91.44 to 92.89% for the NPU conditions. These results show that NPU offloading of a frozen visual encoder can reduce training energy, but it increases training time and lowers policy success rate by 0.44 to 1.89 percentage points compared with GPU-only training.

## Metadata
- **Published**: 2026-08-15T03:19:09Z
- **Authors**: Hyojun Yun, Seungjae Won, Hyungpil Moon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15002v1)