---
title: Agent Self-Improvement with Frozen Weights: The Added Value and Limits of Failure Traces
published: 2026-11-08T12:39:45Z
authors: Arkid Mitra
url: http://arxiv.org/abs/2611.11342v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Self-Improvement with Frozen Weights: The Added Value and Limits of Failure Traces

## Abstract
We evaluate whether an AI agent's harness, the notes around its model, can learn from the agent's failure traces beyond a matched search that never sees them. It can, but less than it looks. We tested an open 9-billion-parameter model with fixed weights; a larger teacher model wrote its notes. On generated customer-service decisions, where both note writers were told the target rules, notes based on the agent's mistakes improved accuracy by 4.0 percentage points over notes from the same process with the mistakes withheld. That process alone, trying and keeping better-scoring notes, reached about 60% of the total improvement. In full customer-service conversations the same notes showed no demonstrated improvement. Separately, a strict screen of single lessons admitted two customer-service lessons, still awaiting tests on new data, and one tool-use lesson, written without seeing the agent's mistakes, which showed no demonstrated gain on new tool-use tasks. A neutral note with no procedure scored higher than the learned lessons (exploratory). A blind audit judged 146 of 240 tool-use test items defective.

## Metadata
- **Published**: 2026-11-08T12:39:45Z
- **Authors**: Arkid Mitra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.11342v1)