---
title: Simple-OPD: Demystifying Warm-up for On-policy Distillation
published: 2026-08-07T04:47:38Z
authors: Tao Liu, Taiqiang Wu, Mao Zheng, Xuan Luo, Runming Yang, Xuewei Yang, Junjie Wang, Yujiu Yang
url: http://arxiv.org/abs/2608.06802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simple-OPD: Demystifying Warm-up for On-policy Distillation

## Abstract
On-policy distillation (OPD) trains a student on its own rollouts with token-level supervision from teacher models, but its effectiveness can depend strongly on the warm-up stage before OPD. In this paper, we demystify warm-up for OPD from both data and training perspectives. For data, we find that effective warm-up relies on teacher-compatible chain-of-thought supervision, and that even incorrect teacher rollouts can provide comparable benefits to correct ones. This suggests that warm-up primarily transfers a teacher-compatible thinking pattern rather than merely correct answers. For training, we show that low-rank adaptation (LoRA) with a near-saturation training duration better balances in-domain adaptation and out-of-distribution generalization than full-parameter SFT. Based on these findings, we propose Simple-OPD, a plug-and-play initialization method that warms up the student on teacher-generated CoT with LoRA before OPD. Experiments across diverse settings demonstrate the effectiveness and robustness of Simple-OPD.

## Metadata
- **Published**: 2026-08-07T04:47:38Z
- **Authors**: Tao Liu, Taiqiang Wu, Mao Zheng, Xuan Luo, Runming Yang, Xuewei Yang, Junjie Wang, Yujiu Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06802v1)