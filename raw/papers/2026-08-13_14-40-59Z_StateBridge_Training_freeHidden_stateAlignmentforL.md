---
title: StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems
published: 2026-08-13T14:40:59Z
authors: Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
url: http://arxiv.org/abs/2608.13317v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems

## Abstract
Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability. We propose StateBridge, a training-free latent communication approach that aligns the sender's final-layer hidden states to the receiver's input space via a closed-form orthogonal transformation. Lightweight norm calibration and vocabulary anchoring ensure compatibility with the pretrained input distribution. The aligned states are prepended to the input of the receiver agent as a continuous prefix. We evaluate StateBridge on math reasoning, code generation, and question answering with four models from two families. StateBridge achieves the best or tied-best score on 22 out of 26 model-task pairs, consistently outperforming the strongest baseline.

## Metadata
- **Published**: 2026-08-13T14:40:59Z
- **Authors**: Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13317v1)