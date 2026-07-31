---
title: SemPIC: Learning Semantic Position-Independent KV Caches
published: 2026-07-30T11:45:24Z
authors: Hui Xie, Peng Xiao, Yutong Deng\textsuperscript, Shuoran Dou, Jian Yang, Jinyang Guo
url: http://arxiv.org/abs/2607.28069v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SemPIC: Learning Semantic Position-Independent KV Caches

## Abstract
Long-context retrieval and agentic workloads repeatedly reuse the same documents under changing instructions, histories, and document orders. Prefix caching cannot exploit this reuse, while position-independent caching (PIC) remains unreliable because independently compiled KV states lack the future context in which they will be consumed. Our diagnostics show that a learned boundary-conditioned baseline sharply reduces attention deviation near reusable-block boundaries but leaves interior and task-level residuals, motivating adaptation of the document representation itself. We present \emph{SemPIC}, which trains a LoRA-enabled Writer to compile native per-layer document KVs through behavioral distillation while retaining the pretrained decoder as an unchanged Reader. Adaptation is confined to offline cache construction, preserving the standard KV interface and cache-hit decoding path. We further introduce KV Gradient Checkpointing, which reduces peak training memory without severing gradients through cached KVs. Across three models and four tasks, SemPIC raises mean micro-F1 over KV Packet from 0.53 to 0.60, approaching Full Recompute at 0.62.

## Metadata
- **Published**: 2026-07-30T11:45:24Z
- **Authors**: Hui Xie, Peng Xiao, Yutong Deng\textsuperscript, Shuoran Dou, Jian Yang, Jinyang Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28069v1)