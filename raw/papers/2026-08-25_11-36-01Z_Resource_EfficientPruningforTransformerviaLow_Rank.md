---
title: Resource-Efficient Pruning for Transformer via Low-Rank Importance Estimation
published: 2026-08-25T11:36:01Z
authors: Peng Liu, Huibing Zeng, Yiqun Zhang, Yang Yi, Jigang Wu
url: http://arxiv.org/abs/2608.24973v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Resource-Efficient Pruning for Transformer via Low-Rank Importance Estimation

## Abstract
With the rapid development of large-scale pre-trained language models based on Transformer architectures, their high computational and memory costs have become a major obstacle to deployment, especially in resource-constrained environments. Traditional pruning methods typically depend on full gradient-based importance estimation, and they necessitate prior finetuning of the model to achieve satisfactory performance. This process often results in intolerable resource consumption. This paper proposes REP-LIE, a new approach to enable resource-efficient pruning during the process of finetuning. REP-LIE leverages the gradients of LoRA low-rank matrices to estimate the importance of weights without requiring full gradient computation. To address the inherent randomness in importance estimation, a stability score is introduced, serving as the basis for iterative pruning of unimportant model parameters. The pruned model is further finetuned through lightweight updates, eliminating the need for full-parameter optimization in the process of finetuning. Extensive experiments on both medium-scale encoder models and large-scale generative models (LLaMA-7B and Mistral-7B) demonstrate that REP-LIE still achieves competitive performance compared to existing approaches.

## Metadata
- **Published**: 2026-08-25T11:36:01Z
- **Authors**: Peng Liu, Huibing Zeng, Yiqun Zhang, Yang Yi, Jigang Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24973v1)