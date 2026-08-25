---
title: Beyond Fresh Starts: Stateful Inference for Streaming ASR in Conversational Voice Agents
published: 2026-08-22T20:46:02Z
authors: Sameep Chattopadhyay, Alexander Erdmann, Mari Ostendorf
url: http://arxiv.org/abs/2608.22101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Fresh Starts: Stateful Inference for Streaming ASR in Conversational Voice Agents

## Abstract
Modern voice-agent systems rely on streaming speech recognition models that operate under stringent latency constraints. This study shows that, due to the limited memory constraints of real-time processing, these systems are adversely impacted by conversational phenomena such as long silences and backchannels. While many agentic pipelines mitigate this by resetting state at each turn, this approach discards vital context and impairs performance at turn onsets. We propose two state-management strategies that preserve cross-utterance context to reduce onset errors. In experiments with two state-of-the-art streaming models on two spoken dialogue benchmarks, our best method yields an average of 15-21% relative WER reduction at utterance onsets.

## Metadata
- **Published**: 2026-08-22T20:46:02Z
- **Authors**: Sameep Chattopadhyay, Alexander Erdmann, Mari Ostendorf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22101v1)