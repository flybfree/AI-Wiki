---
title: MemDuet: Learning Dual-Process Memory for Long-Context Reasoning
published: 2026-10-14T10:16:13Z
authors: Jiangcheng Song, Haodong Jing, Yulin Mu, Lesong Tao, Jixin Wang, Jin Cui, Tianjing Ren, Runxuan Xie, Yongqiang Ma, Nanning Zheng
url: http://arxiv.org/abs/2610.19928v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemDuet: Learning Dual-Process Memory for Long-Context Reasoning

## Abstract
Reasoning over infinitely long documents is becoming a reality with recurrent memory agents. However, increasing context length exacerbates the trade-off between reasoning performance and inference efficiency. Inspired by Kahneman's account of fast and slow thinking, we propose MemDuet, a dual-process memory framework that learns to coordinate a small language model for fast, parallel evidence selection from raw context chunks (System 1) with a large language model for memory-update verification and memory updates in document order (System 2). We train MemDuet in three stages: supervised fine-tuning of System 1 for evidence selection, Group Relative Policy Optimization (GRPO) of System 2 for verification and memory rewriting, and joint optimization of both policies to coordinate selection and updating for long-context reasoning. Experiments on diverse long-context reasoning benchmarks (RULER-HQA, LongBench v2, and 2WikiMultiHopQA) demonstrate a favorable accuracy-efficiency trade-off as context length grows. Averaged across evaluation settings on the three datasets, MemDuet achieves an end-to-end inference speedup of 9.74x and an output-token reduction of 73.91% relative to RL-MemAgent.

## Metadata
- **Published**: 2026-10-14T10:16:13Z
- **Authors**: Jiangcheng Song, Haodong Jing, Yulin Mu, Lesong Tao, Jixin Wang, Jin Cui, Tianjing Ren, Runxuan Xie, Yongqiang Ma, Nanning Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19928v1)