---
title: Fine-Tuning of Transformer models with Frames
published: 2026-08-26T22:13:45Z
authors: Harshavardhan Adepu, Li Zhang, Sanjiv Kumar, Vikas Singh
url: http://arxiv.org/abs/2608.26430v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-Tuning of Transformer models with Frames

## Abstract
Parameter-Efficient Fine-Tuning (PEFT) strategies such as Low-Rank Adaptation (LoRA) are effective solutions for fine-tuning large-scale pre-trained models; however, their memory requirements scale with the size of the model, $\mathcal{O}(dr)$, where $d$ is the model's hidden dimension and $r$ is the rank. Our proposal, FrameFT, models the parameter update $ΔW$ with a sparse coefficient matrix in a Fusion Frame basis. Fusion Frames can be generated algorithmically and shared across model layers, enabling very efficient updates. Only the sparse coefficients of the basis expansion are stored/optimized, reducing the memory footprint. The sparse structure of the coefficient matrix in FrameFT and the sparsity in the Fusion Frames give large compute benefits, and our analysis provides formal convergence results. We evaluate the idea across a suite of supervised fine-tuning benchmarks, focusing on language tasks, but also report application to vision models. Our experiments show that FrameFT achieves performance on par with/exceeding state-of-the-art PEFT techniques, but needs far fewer trainable parameters.

## Metadata
- **Published**: 2026-08-26T22:13:45Z
- **Authors**: Harshavardhan Adepu, Li Zhang, Sanjiv Kumar, Vikas Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26430v1)