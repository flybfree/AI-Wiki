---
title: CUE-Mem: Benchmarking Long-Term User Memory via Implicit Cues in Multimodal Conversations
published: 2026-09-26T12:49:02Z
authors: Yulin Hu, Yanyan Zhao, Zimo Long, Xing Fu, Mengtong Ji, Weixiang Zhao, Yutai Hou, Qianchao Wang, Dandan Tu
url: http://arxiv.org/abs/2609.32574v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CUE-Mem: Benchmarking Long-Term User Memory via Implicit Cues in Multimodal Conversations

## Abstract
Long-term memory is essential for multimodal agents that interact with users across sustained conversations. However, user memories are not always explicitly stated: they may also be implied by recurring background objects in images, ambient sounds in audio, or other peripheral multimodal cues. Existing benchmarks largely focus on text-only memory or explicit multimodal evidence, leaving implicit multimodal cues underexplored. We introduce CUE-Mem, a text-image-audio benchmark for evaluating long-term user memory from implicit cues. CUE-Mem contains 2,674 questions across explicit and implicit evidence settings and covers four tasks: Entity Recall, Long Pattern, Personalized Recommendation, and Answer Refusal. Across textualized memory systems, implicit performance remains far below oracle evidence, locating the main bottleneck in preserving and retrieving subtle cues rather than question answerability. Increasing caption detail recovers more of this evidence, but brings uneven gains and rapidly growing token costs, motivating native multimodal access. Yet native access does not uniformly resolve the bottleneck: evidence use depends strongly on the backbone, while multimodal indexing introduces substantial retrieval noise. CUE-Mem provides a testbed for memory systems that selectively retain, retrieve, and use subtle multimodal evidence.

## Metadata
- **Published**: 2026-09-26T12:49:02Z
- **Authors**: Yulin Hu, Yanyan Zhao, Zimo Long, Xing Fu, Mengtong Ji, Weixiang Zhao, Yutai Hou, Qianchao Wang, Dandan Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32574v1)