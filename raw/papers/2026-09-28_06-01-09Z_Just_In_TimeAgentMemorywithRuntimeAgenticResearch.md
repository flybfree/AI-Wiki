---
title: Just-In-Time Agent Memory with Runtime Agentic Research
published: 2026-09-28T06:01:09Z
authors: Bingyu Yan, Chaofan Li, Hongjin Qian, Shuqi Lu, Chaozhuo Li, Zheng Liu
url: http://arxiv.org/abs/2609.34385v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Just-In-Time Agent Memory with Runtime Agentic Research

## Abstract
Memory is critical for AI agents. Many existing agent-memory systems follow an Ahead-of-Time (AOT) design, constructing memory before a specific request arrives. While this reduces online serving cost, such request-agnostic memory construction can discard fine-grained information that later becomes important. To address this limitation, we propose Just-In-Time Agent Memory (JAM), a trainable framework for query-conditioned context construction at runtime. A Memorizer preserves complete raw histories in a hierarchical page-store with compact navigational summaries, while a Researcher iteratively retrieves, inspects, and integrates evidence for each request. To train these memory-use behaviors, we introduce Memory-Gym, an evidence-grounded data synthesis pipeline covering nine task types across six domains, and optimize the Researcher through verified-trajectory supervised fine-tuning followed by Hint-guided Group Relative Policy Optimization. We demonstrate the effectiveness of JAM across a variety of benchmarks on agent memory and long-context processing, where it achieves stronger task performance than AOT-style memory systems while remaining substantially more efficient than prior trained agentic memory approaches. To support reproducibility and future research, we release our anonymized source code at https://github.com/VectorSpaceLab/general-agentic-memory.

## Metadata
- **Published**: 2026-09-28T06:01:09Z
- **Authors**: Bingyu Yan, Chaofan Li, Hongjin Qian, Shuqi Lu, Chaozhuo Li, Zheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34385v1)