---
title: DiD It in 87 Minutes: A Label-Free Softmax-to-Linear Adaptation of Vision Transformers for Object Detection
published: 2026-08-23T11:21:16Z
authors: Huaiyuan Qin, Gabriel James Goenawan, Zihang Lin, Muli Yang, Hongyuan Zhu
url: http://arxiv.org/abs/2608.22368v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DiD It in 87 Minutes: A Label-Free Softmax-to-Linear Adaptation of Vision Transformers for Object Detection

## Abstract
While linear attention is a compelling mechanism for high-resolution object detection due to its reduced cost for global token mixing, converting the Softmax-attention ViT backbone of a trained detector into a linear-attention one is not a trivial drop-in replacement. Directly swapping the attention operator leads to severe performance degradation, and generic label-free distillation, though effective for classification, often fails on detection tasks. We argue that the central challenge is \textit{detector-interface preservation}: the converted backbone must reproduce the exact feature tensors expected by the fixed downstream detector, rather than merely imitating internal Softmax hidden states. To address this, we introduce Detector-Interface Distillation (DiD), a label-free conversion method that exclusively trains the linear-attention backbone by aligning detector-facing interface tensors with those of a frozen Softmax teacher. On DOTA-v1.5, DiD substantially outperforms established baselines and matches supervised, fully trained linear models. Adaptation completes in roughly 87 minutes on 4 GPUs, and the linearized backbone cuts inference latency by ~62% and peak memory by ~49%. We hope our findings offer the community a simple, label-free route to reusing trained Softmax detectors as efficient linear ones, and encourage interface-aware objectives in future architecture-conversion work.

## Metadata
- **Published**: 2026-08-23T11:21:16Z
- **Authors**: Huaiyuan Qin, Gabriel James Goenawan, Zihang Lin, Muli Yang, Hongyuan Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22368v1)