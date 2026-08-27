---
title: VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction
published: 2026-08-26T16:50:05Z
authors: Zhifei Xie, Jiaqi Lang, Ze An, Yifan Zhao, Dongchao Yang, Kai Li, Ziyang Ma, Mingbao Lin, Chunyan Miao, Shuicheng Yan
url: http://arxiv.org/abs/2608.26005v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction

## Abstract
Conversational systems, such as duplex speech language models (SLMs), still lack a streaming, accurate, and empathetic memory system as their soul. We introduce VoiceMem, a simple memory architecture with a parallel informational left brain, an emotional right brain, and streaming memory I/O mechanisms. We further build a complete pipeline for memory-aware SLM training, long-horizon evaluation, and decoupled deployment with interchangeable memory backends. Experiments and real-world deployment show three advantages: i) Accuracy: under top-5 retrieval, the left brain outperforms classical systems such as Mem0 at top-200 by nearly 30 points; ii) Emotional & Personal: the right brain, with short- and long-horizon affective attribution and dual-node persona modeling, achieves state-of-the-art performance across three persona benchmarks and improves the aggregate score by 4.29 points over the previous best system; and iii) Real-Time & Cheap: VoiceMem completes retrieval in 134 ms, well within standard VAD latency, adding no extra conversational delay while maintaining high accuracy and low cost. These results show that VoiceMem provides a practical memory foundation for real-time, personalized, and emotionally aware speech interaction.

## Metadata
- **Published**: 2026-08-26T16:50:05Z
- **Authors**: Zhifei Xie, Jiaqi Lang, Ze An, Yifan Zhao, Dongchao Yang, Kai Li, Ziyang Ma, Mingbao Lin, Chunyan Miao, Shuicheng Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26005v1)