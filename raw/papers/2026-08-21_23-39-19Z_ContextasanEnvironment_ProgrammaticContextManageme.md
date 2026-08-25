---
title: Context as an Environment: Programmatic Context Management for Long-Horizon Agents
published: 2026-08-21T23:39:19Z
authors: Yin Lin, Elaine Ang, Erkang Zhu, Bolin Ding, Jingren Zhou
url: http://arxiv.org/abs/2608.21690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Context as an Environment: Programmatic Context Management for Long-Horizon Agents

## Abstract
LLM agents increasingly take on long-running tasks whose history grows far beyond a single model context window. Existing approaches compress earlier interactions or extract selected information into fixed memory representations, committing to what to preserve before future needs are known. We present Scroll, a context manager that treats each agent session as an executable Session Environment. The environment is backed by an append-only Event Log and a sandboxed, persistent Python kernel. The kernel maintains a typed namespace across model calls, allowing tool outputs, retrieved history, and derived state to be bound to variables rather than serialized into the prompt at each call. Model-written code searches, materializes, and transforms session state through exec; only explicitly printed projections enter the model's working view for the next call. Context management thus becomes a programming task that inherits the improving coding abilities of LLMs, while the Event Log preserves lossless historical ground truth. As the working view approaches its budget, stale spans are evicted but remain recoverable: an eviction index keeps compact landmarks tied to exact Event Log addresses, so that the agent navigates directly to evicted regions instead of searching the full log. With Qwen3.8-Max as the backbone, Scroll achieves 94.8% on LongMemEval_S; 73.1% on BEAM_10M, surpassing the best published memory system by 5.1 points; and 86.7% on LOCA_256K, exceeding the best published long-horizon agent by 37.4 points.

## Metadata
- **Published**: 2026-08-21T23:39:19Z
- **Authors**: Yin Lin, Elaine Ang, Erkang Zhu, Bolin Ding, Jingren Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21690v1)