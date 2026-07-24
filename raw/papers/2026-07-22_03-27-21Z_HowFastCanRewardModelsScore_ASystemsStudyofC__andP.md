---
title: How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF
published: 2026-07-22T03:27:21Z
authors: Venkata Naga Sai Vishnu Rohit Pulipaka, Anish Katta, Deva Rohit Reddy Peddireddy
url: http://arxiv.org/abs/2607.19712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF

## Abstract
In RLHF pipelines, reward scoring blocks policy updates. Slow scoring bottlenecks the entire loop, since no update runs until every rollout gets a score. And yet most setups just default to PyTorch eager mode or torch.compile, no one checks if that's actually fastest. Scoring itself is small. Rollout generation eats far more of a typical RLHF step. But scoring and generation fight over the same CPU and GPU resources, so a faster scoring engine doesn't shrink step time on its own. It mainly frees up capacity generation can use instead. We built a native C++ inference engine on ONNX Runtime. First step: confirm correctness. Output matched the PyTorch reference to 5.7 x 10^-6 on CPU and 4.2 x 10^-3 on GPU, close enough to trust. Then we tested it against PyTorch eager mode, torch.compile, and FastAPI, on both CPU and GPU. CPU was decisive. Our engine beat every baseline, confidence intervals didn't even overlap. GPU gave a different view: we beat PyTorch and FastAPI, but torch.compile came out ahead. Further testing traced the speedup to ONNX Runtime itself, not C++ as a language. And batching strategy mattered more than either the language or the runtime choice, more than we expected. The results are from repeated, independent runs, since single runs just aren't reliable enough to trust.

## Metadata
- **Published**: 2026-07-22T03:27:21Z
- **Authors**: Venkata Naga Sai Vishnu Rohit Pulipaka, Anish Katta, Deva Rohit Reddy Peddireddy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19712v1)