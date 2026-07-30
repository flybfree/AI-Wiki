---
title: WikiLoop: Jointly Learning to Build and Navigate Agent-Native Wikis with Downstream Feedback
published: 2026-07-29T08:28:30Z
authors: Haoliang Ming, Feifei Li, Wenhui Que
url: http://arxiv.org/abs/2607.26604v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WikiLoop: Jointly Learning to Build and Navigate Agent-Native Wikis with Downstream Feedback

## Abstract
Knowledge-base construction and querying are typically optimized in isolation: retrieval-augmented agents operate over a fixed, externally maintained index, whereas construction receives no signal from downstream use. We present WikiLoop, a feedback-coupled framework that jointly learns to build and navigate an agent-native Wiki, a persistent linked-page knowledge base designed for machine navigation. A role-conditioned shared policy supports two interfaces: a Navigator retrieves evidence from the Wiki to answer queries, and a Builder proposes structured edits evaluated through downstream navigation. The Navigator follows a sufficiency-before-efficiency objective that applies retrieval-cost penalties only after full evidence has been collected. The Builder learns from utility differences: a frozen Navigator scores each candidate edit by its change in downstream performance, while a guard penalty discourages regressions on unrelated queries. Training combines sequential role-specific optimization with a final joint stage over role-homogeneous batches. With Qwen3.5-9B as the common backbone, WikiLoop reaches 62.6 aggregate Answer Correctness on AuthTrace, 6.3 points above LLM-Wiki, base, with the largest gains on multi-document queries. Controlled comparisons support the intended effects of both objectives, and the learned edits remain useful to a held-out Navigator. Paired comparisons indicate that the final shared policy largely retains both role-specific capabilities, improves Navigator and end-to-end Answer Correctness by 0.4 points relative to the corresponding specialist references, and consolidates both interfaces into one model. Without dataset-specific training, WikiLoop also improves over the same-backbone LLM-Wiki, base on HotpotQA and MuSiQue.

## Metadata
- **Published**: 2026-07-29T08:28:30Z
- **Authors**: Haoliang Ming, Feifei Li, Wenhui Que
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26604v1)