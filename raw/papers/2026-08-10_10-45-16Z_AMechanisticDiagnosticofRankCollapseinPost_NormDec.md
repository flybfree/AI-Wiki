---
title: A Mechanistic Diagnostic of Rank Collapse in Post-Norm Decoder Transformers
published: 2026-08-10T10:45:16Z
authors: Xingjian Wang, Qingyu Han, Xiaodong Luo, Yin Zhang
url: http://arxiv.org/abs/2608.09417v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Mechanistic Diagnostic of Rank Collapse in Post-Norm Decoder Transformers

## Abstract
Deep decoder-only Transformers often replace the original Post-Norm architecture with Pre-Norm variants because Post-Norm training is highly sensitive to warmup and learning rate under conventional initialization schemes. Although prior work has identified rank collapse and gradient vanishing as related symptoms, it remains poorly understood how causal attention creates high-similarity representations and why training dynamics fail to repair them. We give a two-stage analysis of Post-Norm rank collapse using token similarity as a scalar state variable. First, at initialization, causal attention acts approximately as a prefix-averaging operator that increases token similarity across depth, while the SwiGLU branch contributes only a smaller damping effect. Second, once training enters a high-similarity regime, growth of pre-normalization residual norms makes the RMSNorm backward factor contractive; under mild conditions, gradients to earlier layers decay geometrically. As a complementary result, we characterize the properties of a collapsed network: its best predictor is frequency distribution with relatively high loss floor, and gradients in collapsed layers vanish at frequency distribution. Experiments on 48-layer decoder-only Transformers trained on C4 dataset match the predicted initialization-time similarity growth and collapse-time gradient contraction, and show that collapsed runs stay near the predicted frequency loss. Together, these results distinguish the forward similarity amplification and backward repair incapacity in Post-Norm collapse, while also characterizing the behavior of collapsed networks.

## Metadata
- **Published**: 2026-08-10T10:45:16Z
- **Authors**: Xingjian Wang, Qingyu Han, Xiaodong Luo, Yin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09417v1)