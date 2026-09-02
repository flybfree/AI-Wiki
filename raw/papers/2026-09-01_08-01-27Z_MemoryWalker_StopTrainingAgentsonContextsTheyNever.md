---
title: MemoryWalker: Stop Training Agents on Contexts They Never Saw
published: 2026-09-01T08:01:27Z
authors: Zinco J, Xunjie Zhu, Shen Huang, Zhenyi Wang, Pengjun Xie, Jieping Ye
url: http://arxiv.org/abs/2609.00865v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemoryWalker: Stop Training Agents on Contexts They Never Saw

## Abstract
Production agent harnesses such as Claude Code and Qwen-Agent compress context during rollout, but training under compression creates a conditioning problem: every eviction branches the effective history, so the learning object is a tree rather than a sequence. Existing linearizations either retain the rightmost path, causing time-travel leakage, or replay a depth-first traversal, causing train-inference mismatch. We introduce two exact, gradient-equivalent corrections: LogitTree, a segmented K-forward traversal, and a packed 4D attention mask. LogitTree requires K+1 backward passes; the 4D mask requires a custom kernel and white-box eviction records. We also propose SDCC (Self-Distillation for Conditioning Consistency), a single-backward-pass variational relaxation. At each eviction, it minimizes forward KL between the compressed student and a stop-gradient teacher on the reconstructed pre-eviction prefix. A residual per-junction KL of epsilon_KL gives an O(sqrt(epsilon_KL)) bound on the train-deployment total-variation gap. SDCC also applies to black-box harnesses. On seven web-search benchmarks with TC-RAG, AgentFold, MemexRL, Claude Code, and OpenCode, naive training inflates the train-rollout log-probability gap, especially on eviction-heavy batches. The exact methods stay at the no-compression floor, and SDCC substantially closes the gap, with lower logit drift and higher rollout rewards.

## Metadata
- **Published**: 2026-09-01T08:01:27Z
- **Authors**: Zinco J, Xunjie Zhu, Shen Huang, Zhenyi Wang, Pengjun Xie, Jieping Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00865v1)