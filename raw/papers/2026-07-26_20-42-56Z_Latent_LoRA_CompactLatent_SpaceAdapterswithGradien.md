---
title: Latent-LoRA: Compact Latent-Space Adapters with Gradient-Free Routing for Continual Learning
published: 2026-07-26T20:42:56Z
authors: Reza Rahimi Azghan, Gautham Krishna Gudur, Giulia Pedrielli, Pavan Turaga, Hassan Ghasemzadeh
url: http://arxiv.org/abs/2607.23837v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent-LoRA: Compact Latent-Space Adapters with Gradient-Free Routing for Continual Learning

## Abstract
Large language models generalize well to individual tasks but lack an inherent mechanism for learning them sequentially, leading to catastrophic forgetting. To mitigate this, LoRA-based continual learning methods allocate a separate low-rank adapter per task, yet existing approaches either require task identity at inference or sum all adapters indiscriminately, letting irrelevant branches distort the output. Recent gating-based solutions route inputs to the correct adapter but introduce trainable parameters that themselves need protection against forgetting. In this work, we observe that pooled token embeddings from a frozen LLM embedding layer already separate task distributions throughout the learning sequence. A Gaussian mixture model fitted on these embeddings, without any gradient-based training, is sufficient for task-agnostic adapter selection at test time. This eliminates the need for a learned gating module. On the adapter side, constraining each task's parameters to the principal subspace of the pretrained weights via SVD yields a compact latent-space parameterization. Within this subspace, orthogonal regularization directly controls inter-task interference. The resulting system, Latent-LoRA, is replay-free, requires no trainable routing component, and uses substantially fewer parameters per task. Experiments across five model scales and two established continual learning benchmarks show state-of-the-art performance with near-zero forgetting.

## Metadata
- **Published**: 2026-07-26T20:42:56Z
- **Authors**: Reza Rahimi Azghan, Gautham Krishna Gudur, Giulia Pedrielli, Pavan Turaga, Hassan Ghasemzadeh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23837v1)