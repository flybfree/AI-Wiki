---
title: Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents
published: 2026-09-01T14:04:27Z
authors: Jinqing Zhao, Chengcan Wu
url: http://arxiv.org/abs/2609.01272v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents

## Abstract
Prospective memory means carrying out a deferred intention at the right future cue while other work continues. Benchmarks now isolate it as an agent skill, yet frontier LLMs still struggle: the best published PM-Bench scaffold reaches only 65.1% Set-F1. We argue that this loop is schema-constrained state tracking rather than open-ended reasoning, and that small models can execute it when the action space is typed. We propose the Prospective Intention Store (PIS) that puts lifecycle logic in code and scoped language work on the model. The scaffold is agentic and training-free: no selector fine-tuning and no trajectory distillation. On PM-Bench, DeepSeek-Chat with PIS reaches 82.9% Set-F1. On Gemma-E2B, Set-F1 is only 4.2% without a store and at most 6.6% under seven retrospective memories, while PIS reaches 66.2%. PIS further reaches 70.1% Set-F1, where retrospective memory methods stay at most 54.4%. PIS sets a new state of the art on this benchmark and enables small models to surpass the published large-model scaffold.

## Metadata
- **Published**: 2026-09-01T14:04:27Z
- **Authors**: Jinqing Zhao, Chengcan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01272v1)