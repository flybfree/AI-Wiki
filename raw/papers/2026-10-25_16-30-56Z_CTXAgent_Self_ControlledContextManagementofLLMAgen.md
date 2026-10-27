---
title: CTXAgent - Self-Controlled Context Management of LLM Agents
published: 2026-10-25T16:30:56Z
authors: Matthias Busch, Marius Tacke, Roland C. Aydin, Christian Feiler, Christian J. Cyron
url: http://arxiv.org/abs/2610.34425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CTXAgent - Self-Controlled Context Management of LLM Agents

## Abstract
Agent harnesses keep long sessions inside the context window by compacting the history when a token threshold is crossed. We study an alternative in which the model manages its own context: it decides when to compact, what to keep and what to write as the hand-off, given two tools and one paragraph of guidance. Since earlier work found that open-weight models cannot manage their own context without scaffolding, we compare seven frontier models under identical conditions, with and without the context tools, on token cost and benchmark score, and we compare our harness with three widely used harnesses on two of these models. The benchmark is assembled from existing ones: coding exercises, multi-step SciCode problems and SWE-bench Pro and Terminal-Bench 4.0 tasks are interleaved with planted facts, ephemeral observations and standing instructions, all checked deterministically, in sessions of 35-212 turns that resemble a user working through different tasks in one chat. Most of the strongest models manage their context: they compact and curate regularly, the live context of the mixed sessions stays mostly below 100k tokens, and their benchmark scores mostly do not drop significantly. For the models that manage their context well, the cost reduction is substantial but varies between models, because some models compact so often that other costs increase. With Claude Opus 5.5, the self-managed harness matches Claude Code on task success at 34% lower cost than its explicit 200k-window configuration and 49% lower than its default, with no context window to choose. We release the agent, the benchmark and all result rows.

## Metadata
- **Published**: 2026-10-25T16:30:56Z
- **Authors**: Matthias Busch, Marius Tacke, Roland C. Aydin, Christian Feiler, Christian J. Cyron
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34425v1)