---
title: Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification
published: 2026-08-16T08:59:22Z
authors: Chunyu Qi, Zhuoran Song, Jian Weng, Haozhe Jiang, Xueyuan Liu, Naifeng Jing, Guanghui He, Xiaoyao Liang, Haibing Guan
url: http://arxiv.org/abs/2608.15636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification

## Abstract
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in the field of embodied AI, but their high computational cost and limited predicted action length hinder real-time deployment. Although Dadu-Corki, a dedicated accelerator for efficient embodied AI, has been introduced, it does not exploit the inherent interaction patterns between the robot and its environment, which results in a relatively short predicted action length. We observe that robotic environments naturally alternate between active states-where precise actions are crucial-and inactive states-where actions have limited impact on task success. This insight enables a new scheduling opportunity: long-action-length speculative prediction in inactive states, paired with selective verification in active states.   We propose SpecVLA, an algorithm-system co-design framework that adaptively balances action length, inference latency, and task reliability. On the algorithm side, SpecVLA introduces a state-aware VLA inference execution paradigm and a hardware-friendly construction of a smaller verification model (sVLA) using differential residuals and block-wise mixed-precision quantization. On the system side, we develop a heterogeneous architecture consisting of a GPU and a robotic-specific hardware module, along with a speculative dataflow that decouples VLA and sVLA through parallel execution. Comprehensive evaluations on OpenVLA and RDT across LIBERO and ManiSkill benchmarks show that SpecVLA reduces end-to-end latency significantly while preserving task success rate. By enabling long-action-length speculative prediction with timely verification, SpecVLA achieves real-time robotic manipulation with both high efficiency and reliability.

## Metadata
- **Published**: 2026-08-16T08:59:22Z
- **Authors**: Chunyu Qi, Zhuoran Song, Jian Weng, Haozhe Jiang, Xueyuan Liu, Naifeng Jing, Guanghui He, Xiaoyao Liang, Haibing Guan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15636v1)