---
title: Persistent Context Graphs for Efficient Memory Compaction in LLM Agents
published: 2026-09-30T16:43:28Z
authors: Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Zhaoxuan Tan, Pei Zhou, Mengting Wan, Yaar Harari, Evgeniy Gabrilovich, Shiyu Chang
url: http://arxiv.org/abs/2609.40118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Persistent Context Graphs for Efficient Memory Compaction in LLM Agents

## Abstract
As LLM capabilities advance, agents are tackling increasingly complex tasks over longer horizons. Their growing interaction histories make memory compaction essential for staying within context windows and reducing prefill cost. Existing methods summarize the history or compress its KV cache, often adding model computation to preserve information for future requests. A new user request can change which history matters, but reassessing that history with the model requires re-encoding it if the KV cache has expired. Past attention provides signals of historical importance and dependencies between messages, while relevance to the current task must be assessed using the new user request. We introduce ReCAP, a memory compaction method that stores attention-derived importance scores and dependency links in a lightweight, persistent context graph. For each new request, ReCAP combines stored importance with relevance cues from the request and follows dependency links to select messages and their supporting context, without additional model calls for selection. Compared with Codex's default summarization-based compaction, ReCAP reduces estimated latency for compaction and cold restoration by approximately 95% on both Qwen3-Coder and gpt-oss. It also roughly halves the historical context per call on SWE-Together at comparable task quality and improves accuracy on the code tasks of Lost-in-Conversation over full history by 19.8 and 41.2 points.

## Metadata
- **Published**: 2026-09-30T16:43:28Z
- **Authors**: Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Zhaoxuan Tan, Pei Zhou, Mengting Wan, Yaar Harari, Evgeniy Gabrilovich, Shiyu Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.40118v1)