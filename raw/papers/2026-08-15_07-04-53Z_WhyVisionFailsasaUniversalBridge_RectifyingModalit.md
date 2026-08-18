---
title: Why Vision Fails as a Universal Bridge: Rectifying Modality Asynchrony in Multilingual MLLMs
published: 2026-08-15T07:04:53Z
authors: Yihang Du, Juhao Liang, Zhengzhao Lai, Siyu Li, Yan Hu
url: http://arxiv.org/abs/2608.15085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Vision Fails as a Universal Bridge: Rectifying Modality Asynchrony in Multilingual MLLMs

## Abstract
Multimodal large language models (MLLMs) exhibit substantial performance degradation in non-English visual reasoning, despite the strong multilingual competence of their text-only backbones. While mechanistic evidence from text-only models suggests that non-English inputs are routed through an English-centric latent space, the multimodal implications of this phenomenon remain unexplored. Through rigorous mechanistic analysis, we identify the \textbf{Ghost Anchor} phenomenon: a temporal modality asynchrony where linguistic translation to the English semantic manifold completes in early layers, while visual semanticization remains immature. Consequently, visual signals are physically present yet functionally invisible during the early alignment window. To rectify this, we propose \textbf{ANCHOR}, a training framework employing Proactive Visual Anchoring (PVA) to accelerate early visual semantic emergence, ensuring visual representations proactively guide linguistic translation. Mechanistic interventions confirm that ANCHOR successfully restores the causal influence of visual signals during early translation. Furthermore, extensive experiments on XMMMU, MaXM, and CVQA demonstrate that ANCHOR consistently outperforms standard baselines, achieving robust visual reasoning across both fine-tuned and zero-shot languages.

## Metadata
- **Published**: 2026-08-15T07:04:53Z
- **Authors**: Yihang Du, Juhao Liang, Zhengzhao Lai, Siyu Li, Yan Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15085v1)