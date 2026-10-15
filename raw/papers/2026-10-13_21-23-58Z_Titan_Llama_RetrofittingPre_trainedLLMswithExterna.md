---
title: Titan-Llama: Retrofitting Pre-trained LLMs with External Neural Memory Modules
published: 2026-10-13T21:23:58Z
authors: Sarah Pan, Ali Behrouz
url: http://arxiv.org/abs/2610.19210v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Titan-Llama: Retrofitting Pre-trained LLMs with External Neural Memory Modules

## Abstract
Transformers are efficient to pre-train at scale because attention permits parallel computation across sequence positions, but long-context inference requires increasingly large KV caches. Efficient recurrent alternatives reduce the asymptotic complexity of inference, but their sequential dependence limits token-wise parallelism during training, making them harder to scale. Further, the current paradigm of extending long context tasks creates competing notions of retaining information precisely and keeping long-context inference efficient. To address this gap, we introduce Titan-Llama, a post-training method for retrofitting attention-based language models with a hierarchical memory architecture that updates parameters at test-time. Titan-Llama applies a blockwise attention mask and preserves full-fidelity attention over recent tokens while compressing historical context into recurrent, fixed-size neural memory modules (NMMs). Our formulation allows pre-trained attention layers to be replaced without training a new language model from scratch. On Llama-3.2-1B-Instruct, Titan-Llama raises accuracy over segmented attention windows from 23.87\% to 40.51\% on QuALITY and from 14.50\% to 40.75\% on LongHealth. Inference benchmarks show more than 20\% faster prefill, 37\% faster decode at medium context lengths, and 24\% lower steady-state decode memory usage in the evaluated configurations. Together, these results demonstrate that incorporating memory architecture mechanisms that utilize test-time training effectively modulates long-context behavior of pre-trained models, offering a practical route to adapting pre-trained transformers for efficient long-context inference. Our code is released on Github \href{https://github.com/sarahpannn/titans-pytorch/tree/main}{GitHub}

## Metadata
- **Published**: 2026-10-13T21:23:58Z
- **Authors**: Sarah Pan, Ali Behrouz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19210v1)