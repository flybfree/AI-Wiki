---
title: Manifold-Constrained Hyper-Connections for Parameter-Efficient Finetuning
published: 2026-07-20T16:24:17Z
authors: Valentijn Oldenburg, Floris de Kam, Bente Zuijdam, Lieve Eberson, Nicky van Zutphen, Stef de Wildt, Ivo Verhoeven
url: http://arxiv.org/abs/2607.18130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Manifold-Constrained Hyper-Connections for Parameter-Efficient Finetuning

## Abstract
Most parameter-efficient finetuning (PEFT) methods adapt weights or activations, thus leaving one of the key Transformer components unchanged: residual connections. This paper investigates Manifold-Constrained Hyper-Connections (mHC), a generalisation of residual connections, as a novel PEFT approach, wrapping frozen OLMo-2 backbones with learned residual routing modules. We find that mHC can finetune frozen Transformers, but that its role differs fundamentally from the original pre-training setting: in finetuning, fixing the residual mixing matrix to identity often improves performance. As a standalone PEFT method, mHC does not consistently outperform LoRA. However, at matched trainable parameter budgets, mHC+LoRA combinations improve language-modelling loss and show task-dependent benchmark gains at both 1B and 7B scale. Overall, our results identify residual routing as a distinct and promising novel PEFT axis.

## Metadata
- **Published**: 2026-07-20T16:24:17Z
- **Authors**: Valentijn Oldenburg, Floris de Kam, Bente Zuijdam, Lieve Eberson, Nicky van Zutphen, Stef de Wildt, Ivo Verhoeven
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18130v1)