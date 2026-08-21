---
title: Learning how to Forget: Fine-tuning for Long-Context Sparse Attention
published: 2026-08-20T11:37:04Z
authors: Matthias Seeger, Zeyu Zhang, Vihang Patil, Konstantinos Benidis, Sebastian Schelter
url: http://arxiv.org/abs/2608.19920v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning how to Forget: Fine-tuning for Long-Context Sparse Attention

## Abstract
A lot of prior work addressed key-value (KV) cache selection and compression by sparse attention to enable long-context inference for transformer language models without excessive hardware budgets. We provide a new method for fine-tuning models with sparse attention. It works for any KV cache policy, runs on a moderate hardware budget (e.g., a single Nvidia A100 GPU with 40 GB RAM), and allows the model to co-adapt with the policy, often outperforming models trained with exact attention (sequence parallelism). We also provide an efficient implementation of H2O sparse attention (the leading policy in our experiments) with dedicated scaled dot product attention kernel support. KeysAndValues (https://github.com/awslabs/keys_values), a new open source library for long-context inference and fine-tuning, provides easy-to-use and performant code for all methods discussed here.

## Metadata
- **Published**: 2026-08-20T11:37:04Z
- **Authors**: Matthias Seeger, Zeyu Zhang, Vihang Patil, Konstantinos Benidis, Sebastian Schelter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19920v1)