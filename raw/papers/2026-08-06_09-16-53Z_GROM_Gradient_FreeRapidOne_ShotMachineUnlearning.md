---
title: GROM: Gradient-Free Rapid One-Shot Machine Unlearning
published: 2026-08-06T09:16:53Z
authors: Paweł Batorski, Przemysław Spurek, Paul Swoboda
url: http://arxiv.org/abs/2608.05783v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GROM: Gradient-Free Rapid One-Shot Machine Unlearning

## Abstract
Machine unlearning has become a critical capability for safely removing specific, sensitive knowledge from large language models (LLMs). Current state-of-the-art approaches primarily rely on iterative, training-time unlearning via fine-tuning. However, even when utilizing parameter-efficient dimensionality reduction techniques like LoRA, gradient-based optimization remains computationally expensive and lacks explicit analytical formulations. It can also leave the targeted knowledge merely hidden rather than removed, to the point that simply quantizing the unlearned model restores much of what it was supposed to have erased. To resolve this, we propose a novel one-shot unlearning approach, abandoning iterative optimization in favor of a direct, exact analytical solution. We frame the unlearning process as a ridge-regularized least-squares optimization problem, deriving a closed-form additive update for targeted weight matrices. This update forces the selected layer to suppress unwanted content while strictly preserving its behavior on retained data. Computed from gradient-free forward passes alone, with no backpropagation and no iteration to convergence, GROM applies the weight edit in mere seconds, which makes it orders of magnitude faster than traditional fine-tuning. Extensive evaluations demonstrate that GROM achieves state-of-the-art forgetting-utility trade-offs on TOFU-5%, TOFU-10%, MUSE-Books, MUSE-News and WMDP, significantly reducing computational overhead without sacrificing overall model performance. Because the update removes the targeted content from the weights instead of masking it, GROM also withstands the low-bit quantization attack that recovers much of the content a gradient-based baseline had appeared to forget. Our code is publicly available at https://github.com/Batorskq/GROM.

## Metadata
- **Published**: 2026-08-06T09:16:53Z
- **Authors**: Paweł Batorski, Przemysław Spurek, Paul Swoboda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05783v1)