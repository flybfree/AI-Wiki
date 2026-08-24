---
title: Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents
published: 2026-08-21T00:14:38Z
authors: Quang Dao, Purvi Kathalkar, Kenneth Eaton
url: http://arxiv.org/abs/2608.20631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents

## Abstract
Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and expose reasoning to outdated, irrelevant, or misleading information, potentially degrading reasoning quality. Existing memory approaches organize or compress execution histories but provide limited mechanisms for deciding which memories remain active. We introduce the, a hierarchical memory system that organizes execution into tasks, subtasks, and actions while assigning each memory a dynamic retention score. Event-based updates and selection-based decay revise these scores, allowing WMT to preserve useful information, fold completed trajectories, suppress low-utility content, and retain access to folded context. We evaluate WMT on GAIA-Text using Qwen3-8B, Gemma 4 E4B, and Llama-3.1-8B, with ablations and memory-poisoning experiments. Relative to linear memory, WMT improves accuracy by an average of 9.97 percentage points while reducing prompt-token usage by 32.8%. Memory-poisoning experiments show that WMT limits the persistence and propagation of unreliable information. Our results suggest that effective long-horizon agent memory depends less on storing more information than on deciding which information should remain active.

## Metadata
- **Published**: 2026-08-21T00:14:38Z
- **Authors**: Quang Dao, Purvi Kathalkar, Kenneth Eaton
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20631v1)