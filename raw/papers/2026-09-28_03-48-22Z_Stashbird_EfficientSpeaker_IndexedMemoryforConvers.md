---
title: Stashbird: Efficient Speaker-Indexed Memory for Conversational Agents
published: 2026-09-28T03:48:22Z
authors: Chidera Biringa, Lucas Yannul, Xiaowen Wang, Marco Ayala, Nicholas Yi, Alex Moyse, Nishant Manchanda, Vivek Gupta
url: http://arxiv.org/abs/2609.34242v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stashbird: Efficient Speaker-Indexed Memory for Conversational Agents

## Abstract
AI agents require memory that preserves information across user-agent exchanges, user-to-user conversations, and group conversations with or without agent participation, while supporting updates as evidence changes or is removed. We present Stashbird, an agent memory system that links source episodes to derived memory state through explicit provenance. Stashbird organizes memory into episodic records, semantic relations, community summaries, and persisted graph state, with lifecycle operations for incremental updates and episode-level deletion. We evaluate question-answering accuracy and model-facing workload across four long-term memory benchmarks. On LoCoMo, Stashbird uses 76.4x fewer ingestion prompt tokens than Graphiti. Compared with reproduced Hindsight on the same benchmark, it uses 8.1x fewer retrieval prompt tokens, with accuracy 1.6 percentage points lower. It achieves higher accuracy than Hindsight on LongMemEval-S and GroupMemBench and comparable accuracy on EverMemBench.

## Metadata
- **Published**: 2026-09-28T03:48:22Z
- **Authors**: Chidera Biringa, Lucas Yannul, Xiaowen Wang, Marco Ayala, Nicholas Yi, Alex Moyse, Nishant Manchanda, Vivek Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34242v1)