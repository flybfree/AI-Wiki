---
title: Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating with MemGLU
published: 2026-08-07T15:20:24Z
authors: Yuting Ge, Pengju Yang, Mingkai Nie
url: http://arxiv.org/abs/2608.07323v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating with MemGLU

## Abstract
We test whether decoder-only language-model FFNs require SwiGLU's open positive tail. We introduce MemGLU as a closed-tail comparator derived from a memristive branch geometry. Across paired 9M and 30M pretraining runs with three seeds, MemGLU remains within about 0.1% of SwiGLU in validation NLL. Trained SwiGLU checkpoints are sensitive to positive-tail suppression, while mechanism diagnostics show that the two models use their gates differently despite similar losses. These results suggest that models adapt to the gate geometry available during pretraining. At the tested scales, SwiGLU's open positive tail is not necessary for decoder-only language-model FFNs.

## Metadata
- **Published**: 2026-08-07T15:20:24Z
- **Authors**: Yuting Ge, Pengju Yang, Mingkai Nie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07323v1)