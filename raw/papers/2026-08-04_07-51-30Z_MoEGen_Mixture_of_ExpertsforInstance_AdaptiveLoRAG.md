---
title: MoEGen: Mixture-of-Experts for Instance-Adaptive LoRA Generation
published: 2026-08-04T07:51:30Z
authors: Yiming Zeng, Lei Lu, Zexin Li, Zhuochun Li, Shuoqiu Li, Shuyi Liao, Xidong Wu, Zeyu Zhang, Minmei Wang, Yu Zhao, Tingting Yu, Shangqian Gao
url: http://arxiv.org/abs/2608.03275v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoEGen: Mixture-of-Experts for Instance-Adaptive LoRA Generation

## Abstract
Parameter-efficient fine-tuning (PEFT) enables efficient adaptation of large language models, but existing MoE-based PEFT methods typically improve capacity by storing multiple full LoRA experts, causing adapter storage to grow linearly with the number of experts and restricting adaptation to a fixed expert pool. We ask whether MoE-based PEFT can produce instance-specific adaptations without explicitly storing a separate LoRA module for each expert. To address this gap, we propose MoEGen, an adaptation framework that shifts MoE-based PEFT from expert selection to expert-conditioned parameter generation. Instead of storing each expert as a full LoRA adapter, MoEGen represents each expert as a small learnable vector, termed an expert code. It routes each input over these vectors and uses their weighted combination to condition a lightweight hypernetwork that generates input-specific low-rank updates. This design decouples expert capacity from adapter storage while enabling instance-conditioned adaptation. Experiments on eight commonsense reasoning benchmarks show consistent improvements over strong static and MoE-based PEFT baselines across three backbones. MoEGen also performs strongly in joint medical and legal-domain adaptation.

## Metadata
- **Published**: 2026-08-04T07:51:30Z
- **Authors**: Yiming Zeng, Lei Lu, Zexin Li, Zhuochun Li, Shuoqiu Li, Shuyi Liao, Xidong Wu, Zeyu Zhang, Minmei Wang, Yu Zhao, Tingting Yu, Shangqian Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03275v1)