---
title: SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding
published: 2026-10-12T21:53:20Z
authors: Boyuan Yang, Wei Gao
url: http://arxiv.org/abs/2610.17436v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding

## Abstract
Large language models (LLMs) on mobile devices can act as agents that call external software tools to complete complex tasks, but the major challenge of supporting on-device mobile agentic AI with LLMs is the long latency of LLM tool calling on mobile devices. In particular, the decode phase is the main contributor of such long latency, but is hard to speed up on mobile processors as it is bound by memory bandwidth rather than compute power. To address this limitation, in this paper we present SchemaWeaver, a new on-device mobile agentic AI technique that enforces schema-guided parallel decoding in the decode phase of LLM tool calling, to reduce its latency by producing multiple tokens in each decode pass. SchemaWeaver can be generically applied to the LLM inference engine on mobile devices without involving any training efforts or changes on LLMs, and our experiment results on major mobile SoCs and LLM families show that SchemaWeaver can reduce the LLM tool calling latency by up to 3.9 times, compared to the competitive baselines.

## Metadata
- **Published**: 2026-10-12T21:53:20Z
- **Authors**: Boyuan Yang, Wei Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17436v1)