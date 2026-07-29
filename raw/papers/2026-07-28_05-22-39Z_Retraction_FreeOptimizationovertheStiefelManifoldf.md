---
title: Retraction-Free Optimization over the Stiefel Manifold for the LoRA Fine-Tuning
published: 2026-07-28T05:22:39Z
authors: Yuan Zhang, Jiang Hu, Zhijian Lai, Lin Lin, Zaiwen Wen
url: http://arxiv.org/abs/2607.25299v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retraction-Free Optimization over the Stiefel Manifold for the LoRA Fine-Tuning

## Abstract
Optimization over the Stiefel manifold plays a significant role in various machine learning tasks. Existing methods either use the retraction operators, requiring costly orthonormalization for large-scale matrices, or employ landing methods that rely on careful step size selection and penalty parameter tuning. To address these challenges, we propose a retraction-free and penalty parameter-free algorithm that directly lands on the manifold. By leveraging the strongly-convex-like property of the quadratic penalty function and the proximal smoothness of the Stiefel manifold, we establish global convergence guarantees with the best-known iteration complexities under both constant and diminishing step sizes. Then, we reformulate the low-rank adaptation (LoRA) fine-tuning problem for large language models as a manifold optimization problem, introducing Manifold-LoRA for geometry-accelerated adaptation. This approach employs the proposed landing technique and a carefully designed step size strategy to accelerate the training process. Numerical experiments on benchmark datasets demonstrate the efficiency and strong downstream performance of the proposed method.

## Metadata
- **Published**: 2026-07-28T05:22:39Z
- **Authors**: Yuan Zhang, Jiang Hu, Zhijian Lai, Lin Lin, Zaiwen Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25299v1)