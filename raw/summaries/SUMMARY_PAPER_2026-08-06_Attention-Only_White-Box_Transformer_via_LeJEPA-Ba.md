---
title: Attention-Only White-Box Transformer via LeJEPA-Based Self-Supervised Pretraining
url: http://arxiv.org/abs/2608.04213v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-04_20-26-12Z_Attention_OnlyWhite_BoxTransformerviaLeJEPA_BasedS.md
generated_at: 2026-08-06 00:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an attention-only white-box Transformer derived from LeJEPA self-supervised pretraining, achieving classification accuracies comparable to the original CRATE model on CIFAR-10 and CIFAR-100 while reducing parameter count by roughly 31%. The approach jointly optimizes the expansion term R(Z) with the sparse rate reduction objective using ADMM. Knowledge distillation further replaces MLP blocks with ReLU activations, cutting parameters even more.

## Key Takeaways
- The LeJEPA framework assumes an isotropic Gaussian distribution for embeddings, which is conceptually equivalent to the expansion term R(Z) in the sparse rate reduction objective guiding white-box Transformer optimization.  
- Optimization of the white-box network and self-supervised learning are performed together via alternating direction method of multipliers (ADMM).  
- The resulting model reduces parameter count by about 31% while preserving classification accuracy, and knowledge distillation can replace MLP blocks with ReLU activations to cut parameters further.

## Context
This work bridges the gap between network optimization and self-supervised learning for white-box models, offering a unified paradigm that decouples design from pretraining. It highlights how embedding distribution assumptions directly influence model efficiency and performance in transformer architectures.

## Implications
The findings suggest MLP layers may be redundant in standard ViT designs, enabling lighter attention-only models without sacrificing accuracy. Practitioners can adopt this approach to reduce computational cost and memory usage while maintaining competitive results.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04213v1)
