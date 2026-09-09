---
title: Miles v0.1: Production-Level Post-Training
published: 2026-09-08T07:35:47Z
authors:  RadixArk,  :, Tom Chen, Mao Cheng, Shi Dong, Kangrui Du, Yanbin Jiang, Jiajun Li, Yiming Li, Tao Lin, Yusheng Su, Andy Ye, Yueming Yuan, Zhichen Zeng
url: http://arxiv.org/abs/2609.08368v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Miles v0.1: Production-Level Post-Training

## Abstract
We present Miles v0.1, a full-stack, production-ready system for frontier post-training. Building upon the clean design of slime, Miles designs each stage of the reinforcement-learning (RL) training loop around a single principle: components should be verified, clean, and customizable. With accuracy, efficiency, reliability, and scalability as first-class goals, Miles aims to make frontier-scale RL accessible to researchers and enterprises alike. This report walks through the system end to end: rollout engines built on SGLang, a trainer with a choice of two backends (NVIDIA Megatron-LM and PyTorch FSDP), and three weight-synchronization transports for different deployment topologies. Beyond full-parameter RL, Miles also supports LoRA RL, on-policy distillation, supervised fine-tuning, and true-on-policy rollout-training alignment, and extends the same architecture to diffusion models. We close with an end-to-end case study: fully asynchronous agentic RL on a GLM-5.2 744B-A40B model over terminal-use coding tasks, running on 64 NVIDIA GB300 GPUs with a median step time of 263 seconds over the first 30 measured steps. Miles is open-sourced at https://github.com/radixark/miles, with the project website at https://miles.radixark.com.

## Metadata
- **Published**: 2026-09-08T07:35:47Z
- **Authors**:  RadixArk,  :, Tom Chen, Mao Cheng, Shi Dong, Kangrui Du, Yanbin Jiang, Jiajun Li, Yiming Li, Tao Lin, Yusheng Su, Andy Ye, Yueming Yuan, Zhichen Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08368v1)