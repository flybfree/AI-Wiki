---
title: AutoEncoder-Compressed Parallel Split Learning for Pre-trained Model Fine-Tuning
published: 2026-07-20T13:08:41Z
authors: Bas Meuwissen, Vasileios Tsouvalas, Nirvana Meratnia
url: http://arxiv.org/abs/2607.17913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoEncoder-Compressed Parallel Split Learning for Pre-trained Model Fine-Tuning

## Abstract
Distributed Fine-Tuning (DFT) of large-scale Foundation Models (FMs) on resource-constrained edge devices is limited by local compute constraints and communication overhead. Parallel Split Learning (PSL) reduces client-side computation by keeping few model layers on each client and offloading the remaining computation to the server; however, clients must exchange intermediate activations and gradients with the server at every training step. Existing SL communication-compression methods mainly rely on task-agnostic heuristics, such as sparsification and quantization. While learnable SL compressors can better adapt to intermediate representations, they require co-training with the target model. Therefore, directly inserting them into off-the-shelf FMs introduces feature-distribution misalignment and degrades DFT performance. To address this, we propose AE-PSL, a communication-efficient PSL framework that compresses intermediate activations and gradients using a lightweight AutoEncoder (AE) placed at the split layer. To ensure compatibility of AE compression with pre-trained FMs, AE-PSL introduces a novel two-stage alignment mechanism, which adapts the AE to the pre-trained model's feature manifold and client-specific feature distributions before DFT.

## Metadata
- **Published**: 2026-07-20T13:08:41Z
- **Authors**: Bas Meuwissen, Vasileios Tsouvalas, Nirvana Meratnia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17913v1)