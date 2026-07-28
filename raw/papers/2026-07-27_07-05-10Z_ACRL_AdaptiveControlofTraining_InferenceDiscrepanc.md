---
title: ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning
published: 2026-07-27T07:05:10Z
authors: Wenwu Fan, Qihong Lin, Zhijie Xia, Zhuo Zheng, Sihao Wang, Qiang Chen, Liangsheng Zhu
url: http://arxiv.org/abs/2607.24062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning

## Abstract
Reinforcement Learning (RL) training for Large Language Models (LLMs) often suffers from instability due to the discrepancy between training and inference. This training-inference discrepancy stems from two primary factors: an architectural separation between training and inference engines, and the use of low-precision quantization in inference versus higher-precision computation in training. To address training instability issues caused by high training-inference discrepancy, we present the principles and methods for its adaptive control. We propose Adaptive Control Reinforcement Learning (ACRL), which adaptively maintains the training-inference discrepancy within a reasonable range to ensure stable RL training. Beyond stabilization, ACRL inherently increases policy entropy, thereby enhancing exploration and improving accuracy. The experimental results show that when the inference engine utilizes FP8 quantization, ACRL consistently maintains the training-inference discrepancy within a reasonable range and stabilizes RL training. Furthermore, ACRL not only matches the accuracy of the BF16 baseline but also outperforms importance sampling (IS) fixes.

## Metadata
- **Published**: 2026-07-27T07:05:10Z
- **Authors**: Wenwu Fan, Qihong Lin, Zhijie Xia, Zhuo Zheng, Sihao Wang, Qiang Chen, Liangsheng Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24062v1)