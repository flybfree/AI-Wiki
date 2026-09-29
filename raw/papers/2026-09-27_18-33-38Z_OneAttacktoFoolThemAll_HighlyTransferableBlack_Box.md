---
title: One Attack to Fool Them All: Highly Transferable Black-Box Adversarial Attacks on Frontier MLLMs
published: 2026-09-27T18:33:38Z
authors: Sen Nie, Jie Zhang, Zhongqi Wang, Shiguang Shan, Xilin Chen
url: http://arxiv.org/abs/2609.33833v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Attack to Fool Them All: Highly Transferable Black-Box Adversarial Attacks on Frontier MLLMs

## Abstract
Adversarial attacks have long posed a fundamental threat to machine learning systems. As multimodal large language models (MLLMs) rapidly evolve and become widely deployed, assessing their vulnerability to such attacks is essential for their safe use. In this work, we investigate whether a single adversarial image can consistently mislead diverse frontier MLLMs in black-box settings. We propose O-Attack, a highly transferable black-box attack framework. This framework builds on our insight that surrogate models contain a broad, high-level, cross-modally aligned semantic space. This space extends beyond final-layer outputs and provides multiple semantically consistent representations that remain underexploited by existing attacks. Within this space, O-Attack anchors aligned representations, progressively broadens semantic conditions, and optimizes perturbations through semantic consensus to promote consistent target alignment. By fully exploiting this space with the same surrogate models as M-Attack, O-Attack raises attack success rates on GPT-5.4 (29.1% to 77.2%), Claude-4.6 (42.8% to 81.6%), and Gemini-3.1 (38.2% to 80.9%). Extensive experiments across 24 MLLMs show that O-Attack outperforms six state-of-the-art methods in black-box transferability, with consistent effectiveness across prompts and improved efficiency and imperceptibility. This work exposes the practical safety risks posed by black-box adversarial attacks against frontier MLLMs, underscoring the need for more rigorous robustness evaluation and more effective defenses.

## Metadata
- **Published**: 2026-09-27T18:33:38Z
- **Authors**: Sen Nie, Jie Zhang, Zhongqi Wang, Shiguang Shan, Xilin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33833v1)