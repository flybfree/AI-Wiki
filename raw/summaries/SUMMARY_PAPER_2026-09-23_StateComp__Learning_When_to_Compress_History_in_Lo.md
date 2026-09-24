---
title: StateComp: Learning When to Compress History in Long Horizon Agents
url: http://arxiv.org/abs/2609.27298v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_03-34-08Z_StateComp_LearningWhentoCompressHistoryinLongHoriz.md
generated_at: 2026-09-23 22:19
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces StateComp, a framework designed to optimize context management for long-horizon agents by determining the optimal moment to compress historical interactions based on the current agent state. By moving beyond fixed windowing or simple relevance metrics, the authors demonstrate that they can significantly reduce token overhead and increase inference speed without sacrificing task performance.

## Key Takeaways
- The core innovation lies in identifying "safe" compression points; the authors argue that premature compression risks losing critical information needed for future steps, while excessive retention leads to high computational costs and context window limitations.
- StateComp utilizes a two-stage annotation procedure to create KEEP and READY supervision data, combined with an imbalance-aware router trained on the hidden representations of a frozen language model to make real-time decisions about which history to compress.
- The framework employs a bounded state representation to minimize the cost of evaluating long histories and groups adjacent "ready" interactions into continuous spans for compact summarization; these methods achieved a 52.27% reduction in tokens and a 12.67x speedup in representation extraction on the WorkBuddyBench dataset.

## Context
As Large Language Models (LLMs) are increasingly deployed as agents to handle complex, multi-step tasks, the growing length of interaction history poses a significant barrier to scalability and efficiency. Current methods for managing this context often rely on arbitrary truncation or fixed windows, which lack the nuance required to preserve critical historical information while minimizing costs.

## Implications
This research provides a scalable pathway for deploying long-horizon agents in production environments where token costs and latency are primary constraints. By providing a mechanism that intelligently manages memory based on state transitions rather than arbitrary rules, it allows for the deployment of more complex, persistent AI assistants that can operate over much longer durations with significantly lower overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.27298v1)
