---
title: Reproducible Evaluation as the Substrate for Safe Prompt Compression in Production Agents
published: 2026-10-22T22:24:35Z
authors: Prabal Vashisht, Zheng Hu, Ying Yang
url: http://arxiv.org/abs/2610.31972v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reproducible Evaluation as the Substrate for Safe Prompt Compression in Production Agents

## Abstract
Evaluating conversational agents that act on live, mutable enterprise data is hard: replayed sessions drift as backend state changes, and a benchmark built today can silently go stale as the data it describes moves on. We present an offline evaluation harness for a production conversational agent that stays reproducible despite the live data it operates on changing, and that can be regenerated on demand once it goes stale. We then use this harness as the fitness function for GEPA-based prompt optimization under a correctness gate that guards against reward hacking. Applied to a production merchant-facing agent, correctness-gated compression shrinks the agent's full prompt surface by 3.5-7.6% without regressing held-out task correctness, consistently across three independent subject-model families, and for one, correctness measurably improves.

## Metadata
- **Published**: 2026-10-22T22:24:35Z
- **Authors**: Prabal Vashisht, Zheng Hu, Ying Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31972v1)