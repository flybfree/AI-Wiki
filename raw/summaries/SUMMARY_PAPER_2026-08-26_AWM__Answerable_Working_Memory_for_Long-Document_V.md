---
title: AWM: Answerable Working Memory for Long-Document VQA Agents
url: http://arxiv.org/abs/2608.25618v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_10-35-25Z_AWM_AnswerableWorkingMemoryforLong_DocumentVQAAgen.md
generated_at: 2026-08-26 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a diagnostic called memory‑only answerability to evaluate whether an agent’s working memory can support answering a question when only the terminal evidence is available, and it proposes AWM‑GRPO, a reinforcement‑learning method that rewards trajectories where this memory remains answerable. On benchmark long‑document VQA tasks, AWM‑GRPO boosts final‑answer accuracy by 8.1–11.9 points compared with RAG baselines while cutting the rate of correct answers that cannot be derived from working memory alone.

## Key Takeaways
- The paper shows that even when gold evidence pages are supplied, about 42.5 % of correctly answered questions still lack sufficient information in the terminal working memory to answer independently.
- AWM‑GRPO integrates a signal about answerability directly into the GRPO reward function, giving higher advantages to trajectories whose working memory remains answerable while keeping final‑answer correctness as the primary goal.
- The approach reduces the “memory‑missing‑correct” rate by 2.7 points relative to an answer‑only GRPO baseline on both MMLongBench‑Doc and LongDocURL.

## Context
Long‑document visual question answering depends heavily on agents that retrieve, inspect, and store evidence in working memory before synthesizing answers. Current evaluation focuses mainly on final‑answer correctness and whether the agent accessed the correct pages, ignoring how well stored evidence can be used when page context is removed, which creates a blind spot for memory quality.

## Implications
For practitioners developing long‑document VQA systems, this work highlights the need to monitor not only answer accuracy but also the completeness of working memory. In industry applications where document retrieval and summarization are critical, ensuring that stored evidence can independently support queries could lead to more robust and reliable AI agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25618v1)
