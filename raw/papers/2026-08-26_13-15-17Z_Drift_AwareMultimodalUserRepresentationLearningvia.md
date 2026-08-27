---
title: Drift-Aware Multimodal User Representation Learning via Multi-Scale Temporal Modeling and Sparse Mixture-of-Experts
published: 2026-08-26T13:15:17Z
authors: Ziqing Qian, Haohang Chen, Shengqi Dang, Yuhan Xiong, Canyu Shen, Jiaying Lei, Nan Cao
url: http://arxiv.org/abs/2608.25773v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Drift-Aware Multimodal User Representation Learning via Multi-Scale Temporal Modeling and Sparse Mixture-of-Experts

## Abstract
Understanding user preferences from noisy and temporally evolving social media behaviors is fundamentally challenging due to interest drift, where user preferences shift across time and exhibit both multi-scale temporal patterns and diverse co-existing interests. To address this, we propose DUMoE, a unified framework for drift-aware multimodal user representation learning. Our model consists of (i) a temporal dynamics-aware backbone that captures and integrates static profiles, short-term behavioral signals, and long-term dependencies into a coherent representation, and (ii) a sparse mixture-of-experts (MoE) interest adapter that disentangles multiple latent interests via expert specialization and adaptive routing. Each expert models a distinct interest subspace, while a gating network dynamically selects and aggregates a sparse subset of relevant experts for each user. To enable stable and effective optimization, we further introduce a three-stage training strategy that decouples backbone learning, expert specialization, and gating optimization. Extensive experiments on real-world social media datasets show that DUMoE consistently outperforms state-of-the-art methods on both user interest prediction and interaction prediction tasks.

## Metadata
- **Published**: 2026-08-26T13:15:17Z
- **Authors**: Ziqing Qian, Haohang Chen, Shengqi Dang, Yuhan Xiong, Canyu Shen, Jiaying Lei, Nan Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25773v1)