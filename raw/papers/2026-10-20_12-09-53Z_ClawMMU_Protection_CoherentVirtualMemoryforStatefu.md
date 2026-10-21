---
title: ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents
published: 2026-10-20T12:09:53Z
authors: Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique, Lars Henning Klein, Akhil Arora, Ashvin Goel, Laurent Bindschaedler
url: http://arxiv.org/abs/2610.28093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents

## Abstract
AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose ClawMMU, a protection layer that labels every piece of memory with its owner, scope, origins, and authority. ClawMMU checks these labels whenever content enters the model's context, is written to storage, returns from storage, or drives a tool call. Its central rule is that information may rise in authority, but authority never lifts itself. Because the checks depend on where content came from, not on what it says, memory attacks become classical protection faults that the harness stops even when the model is fooled.

## Metadata
- **Published**: 2026-10-20T12:09:53Z
- **Authors**: Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique, Lars Henning Klein, Akhil Arora, Ashvin Goel, Laurent Bindschaedler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28093v1)