---
title: PoLoRA: A Preconditioned Orthogonalized LoRA Optimizer
published: 2026-07-20T07:16:31Z
authors: Nikhil Ghosh, Tetiana Parshakova, Robert M. Gower
url: http://arxiv.org/abs/2607.17620v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PoLoRA: A Preconditioned Orthogonalized LoRA Optimizer

## Abstract
Low-rank adaptation (LoRA) makes finetuning large language models cheaper by adding to each weight matrix a trainable low-rank update parameterized as the product of two matrices. These matrices are usually trained with Adam, which treats them as a single flat vector of parameters and ignores both the matrix and product structure of LoRA. Applying a matrix-aware optimizer such as Muon to each factor does not consistently improve over Adam, and neither do the product-aware Muon variants proposed in concurrent works. To realize consistent gains, we introduce PoLoRA, a Preconditioned Orthogonalized LoRA optimizer built from three ingredients: a product-aware spectral update direction, curvature preconditioning derived from controlling the per-sample loss change, and a magnitude rule that controls the sizes of both the factor and merged updates. We evaluate PoLoRA on instruction-tuning datasets for code and math across models from 1B to 8B parameters, and find that it reaches the final held-out loss achieved by tuned Adam in 1.2-1.7 times fewer steps, while adding at most 3% per-step overhead. Compared to Adam, PoLoRA is also less sensitive to the learning rate, and its optimal learning rate is stable across ranks.

## Metadata
- **Published**: 2026-07-20T07:16:31Z
- **Authors**: Nikhil Ghosh, Tetiana Parshakova, Robert M. Gower
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17620v1)