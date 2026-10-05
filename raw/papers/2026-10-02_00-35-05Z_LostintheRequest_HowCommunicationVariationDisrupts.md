---
title: Lost in the Request: How Communication Variation Disrupts Retrieval and Action in Email Agents
published: 2026-10-02T00:35:05Z
authors: Feng Chen, Ritam Dutt, Atnaz Taheri, Alex Williams
url: http://arxiv.org/abs/2610.02627v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lost in the Request: How Communication Variation Disrupts Retrieval and Action in Email Agents

## Abstract
An email assistant should not complete less work simply because a user phrases the same request differently. Yet most benchmarks test each task with only one canonical request, leaving this form of robustness largely unmeasured. We test whether email assistants remain reliable when the requested information, available evidence, and expected outcome stay fixed, but the communication style or English variety changes. We construct validated variants along five communication-style axes and four rule-based dialect conditions, and evaluate them on three benchmarks: a retrieval-augmented generation (RAG) pipeline and two tool-using agents. Indirect requests reduce performance on all three benchmarks, while formal requests reduce performance on both agentic benchmarks. Examining the systems more closely shows that these failures have different causes. Verbose requests mainly hurt a lexical retriever by making the relevant email harder to find. By contrast, indirect and dialect variants remain harmful even when the relevant email is retrieved. In the agentic setting, indirect and formal requests mainly cause the agents to omit required actions, not to take more unsupported actions. These results show that a successful response is not enough to establish robustness: evaluations should vary how requests are expressed and separately measure whether agents complete the requested work.

## Metadata
- **Published**: 2026-10-02T00:35:05Z
- **Authors**: Feng Chen, Ritam Dutt, Atnaz Taheri, Alex Williams
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02627v1)