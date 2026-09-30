---
title: When Tools Silently Lie: Evaluating and Mitigating Blind Compliance in Tool-Augmented Data Agents
published: 2026-09-29T09:45:17Z
authors: Zifu Tao, Changqing Yin
url: http://arxiv.org/abs/2609.37153v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Tools Silently Lie: Evaluating and Mitigating Blind Compliance in Tool-Augmented Data Agents

## Abstract
Tool-augmented data agents rely on tool outputs for analytical decisions. Yet successful execution can return plausible but incorrect evidence, requiring agents to decide whether to trust or verify it. Understanding this failure requires examining both the evidence obtained through checking and the answer ultimately adopted. We introduce ToxicBench to measure checking and adoption under numerical, label, schema, and retrieval errors, pairing clean and poisoned observations over fixed source data. In the 118-task GPT evaluation across three adapters, poisoning lowers task success by 26 to 39 percentage points. Ordinary retries help under one-shot poisoning, whereas repeated poisoning reveals wrong-answer adoption after checking. Controls on three public tables isolate how supplied evidence affects recovery. After freezing the scorer, we compare its judgments with human annotations on 200 trajectories, finding 96% task-success agreement. Human judgments support retry gains over Base and confirm adoption after checking on audited tasks. We release trajectories, versioned scoring, and reference and delivery audits. These findings highlight evidence availability and answer selection as complementary dimensions of agent reliability.

## Metadata
- **Published**: 2026-09-29T09:45:17Z
- **Authors**: Zifu Tao, Changqing Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37153v1)