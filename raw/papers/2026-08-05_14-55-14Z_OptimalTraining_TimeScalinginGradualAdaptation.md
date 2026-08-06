---
title: Optimal Training-Time Scaling in Gradual Adaptation
published: 2026-08-05T14:55:14Z
authors: Zonghuan Xu, Krishna Harish
url: http://arxiv.org/abs/2608.04927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimal Training-Time Scaling in Gradual Adaptation

## Abstract
In gradual adaptation, how should the training time on each task change as the number of intermediate tasks increases? We study this question for overparameterized linear regression tasks that change smoothly and share a zero-loss solution. With $N$ tasks and training time $s_N$ on each, the final learning progress converges to a continuum curve when $Ns_N\toτ$. The limiting progress is $Θ(τ)$ for small $τ$ and $Θ(τ^{-1})$ for large $τ$, so both very short and very long training produce little progress. It follows that optimal per-task training times scale as $s_N^\star=Θ(N^{-1})$, equivalently $Ns_N^\star=Θ(1)$. Experiments on gradually rotated MNIST and a natural Yearbook time shift are consistent with less per-task training as the path is divided more finely.

## Metadata
- **Published**: 2026-08-05T14:55:14Z
- **Authors**: Zonghuan Xu, Krishna Harish
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04927v1)