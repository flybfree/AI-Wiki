---
title: LatCom: Cross-Agent Latent Compression for Efficient Multi-Agent Collaboration
published: 2026-09-29T08:36:55Z
authors: Shinan Zhang, Tao Zhang, Qihui Zhu, Mengjie Zhang, Dong Jin, Yunpeng Hou, Shuangwu Chen, Xiaobin Tan, Quan Zheng, Jian Yang
url: http://arxiv.org/abs/2609.37017v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LatCom: Cross-Agent Latent Compression for Efficient Multi-Agent Collaboration

## Abstract
LLM-based multi-agent systems (MAS) increasingly use latent collaboration to avoid the information loss and repeated encoding-decoding overhead of natural-language communication. However, directly forwarding all sender latents makes the receiver-side context scale with both the number of agents and the reasoning length, increasing computation, memory usage, and collaboration latency. A natural solution is latent compression. But we find that cross-agent redundancy remains unresolved in existing latent compression approaches, which typically compress each sender independently and then concatenate the results. We propose LatCom, a cross-agent latent compression framework for efficient multi-agent latent collaboration. LatCom maps multiple sender latents into a fixed number of receiver-readable and task-relevant slots. Rather than reconstructing all sender hidden states, it optimizes the compressed latents for receiver-side task utility. LatCom trains the compressor in two stages: single-sender readability learning first establishes a latent interface interpretable by the frozen receiver, and multi-sender fusion learning then trains the compressor to fuse complementary evidence and remove redundancy across agents. Experiments on multiple benchmarks with Qwen3-4B show that LatCom achieves an average 2.46x inference speed-up over LatentMAS and reduces output token usage by 70.3% while maintaining comparable average accuracy.

## Metadata
- **Published**: 2026-09-29T08:36:55Z
- **Authors**: Shinan Zhang, Tao Zhang, Qihui Zhu, Mengjie Zhang, Dong Jin, Yunpeng Hou, Shuangwu Chen, Xiaobin Tan, Quan Zheng, Jian Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37017v1)