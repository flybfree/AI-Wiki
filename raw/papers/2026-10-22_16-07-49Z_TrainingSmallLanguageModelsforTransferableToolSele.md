---
title: Training Small Language Models for Transferable Tool Selection
published: 2026-10-22T16:07:49Z
authors: Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon, Artem Kuriksha, Daniel Jiang, Andrea Zanette, Ayush Jain
url: http://arxiv.org/abs/2610.31483v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Small Language Models for Transferable Tool Selection

## Abstract
As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which are actually needed. Recent work instead leverages proprietary commercial LLMs like Claude or ChatGPT to drive a retriever, decomposing the instruction and selecting over retrieved candidates. We show that a small, open model can be trained via reinforcement learning to perform the same functionality. On ToolBench, a Qwen3-8B model post-trained with our recipe outperforms Llama-4-Maverick (402B). In addition, the trained model transfers directly to different retrievers and generalizes to new tool corpora in different domains.

## Metadata
- **Published**: 2026-10-22T16:07:49Z
- **Authors**: Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon, Artem Kuriksha, Daniel Jiang, Andrea Zanette, Ayush Jain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31483v1)