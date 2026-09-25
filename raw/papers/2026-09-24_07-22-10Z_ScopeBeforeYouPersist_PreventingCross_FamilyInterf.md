---
title: Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory
published: 2026-09-24T07:22:10Z
authors: Yezhou Cheng, Runjia Du, Zeming Liu, Qibai Chen, Hang Lyu, Yankai Zeng, Yilan Wei, Bojun Lin
url: http://arxiv.org/abs/2609.29144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory

## Abstract
Persistent memory lets language-model agents improve prompts and skills without updating model weights. We show that matching retrieval scope to certification scope enables these edits to support reliable repeated adaptation across recurring task families. We study frozen-model agents on ProcStream-RSI, a 12-round code-repair stream, using Orthogonal Regression Control (ORC), an execution-grounded gate for persistent skill edits. In an intervention that holds proposals and gate decisions fixed, retrieving each accepted skill only for its originating family raises mean hidden trajectory utility from 0.713 under global memory to 0.816 and changes harmful deployments from six of eight to none. In 27 paired randomized-order streams, Scoped-ORC improves mean trajectory utility by 0.063 [0.037, 0.094] over Global-ORC, accepts 63 rather than 12 updates, and produces multiple accepted updates in 19/27 streams, with 0/63 harmful acceptances. The global control reaches 0.713, below the static agent's 0.775, because locally valid edits can interfere with unrelated families. These results establish scope matching as a complementary control for persistent agent memory: certification determines whether an edit is supported, while retrieval scope determines where that evidence authorizes its use.

## Metadata
- **Published**: 2026-09-24T07:22:10Z
- **Authors**: Yezhou Cheng, Runjia Du, Zeming Liu, Qibai Chen, Hang Lyu, Yankai Zeng, Yilan Wei, Bojun Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29144v1)