---
title: PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents
published: 2026-08-02T03:20:54Z
authors: Jingyu Sun, Yan Lin, Yuyang Xue, Yifan Wang, Zhengtao Yao, Rui Qian, Zefeng Xu, Jiachen Li, Xianyang Liu, Jiancheng Pan, Jingyuan Sun, Syed Murtuza Baker, Hongpeng Zhou
url: http://arxiv.org/abs/2608.00962v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PMMC: Prospective Multimodal Memory Compilation for Long-Term LVLM Agents

## Abstract
Long-term memory is essential for LVLM agents to maintain consistency and integrate information across extended multimodal interactions. Existing agent memory systems, however, often reduce visual experiences into textual summaries or rely on static retrieve-then-reason pipelines, which are inefficient at query time and brittle when questions require image-text binding, temporal updates, or visual details. We propose Prospective Multimodal Memory Compilation, a framework that shifts part of the memory reasoning process from query time to memory consolidation time. Given accumulated multimodal interactions, a Questioner predicts future question candidates, a Planner compiles question-conditioned multimodal memory programs, and a Doubter verifies whether the planned evidence path can support the predicted answer. The verified question-program pairs form a structured question bank for efficient query-time routing and evidence retrieval. Experiments on multimodal long-term memory benchmarks show that our method improves answer quality and visual evidence recall while reducing query-time token and latency costs. Extensive ablations analyze the effects of self-feedback, dynamic planning, raw-image access, and question bank coverage.

## Metadata
- **Published**: 2026-08-02T03:20:54Z
- **Authors**: Jingyu Sun, Yan Lin, Yuyang Xue, Yifan Wang, Zhengtao Yao, Rui Qian, Zefeng Xu, Jiachen Li, Xianyang Liu, Jiancheng Pan, Jingyuan Sun, Syed Murtuza Baker, Hongpeng Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00962v1)