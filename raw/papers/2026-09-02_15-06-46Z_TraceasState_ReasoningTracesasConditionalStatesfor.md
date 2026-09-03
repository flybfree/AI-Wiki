---
title: Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers
published: 2026-09-02T15:06:46Z
authors: Xu Zou, Jie Tang
url: http://arxiv.org/abs/2609.02702v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers

## Abstract
Transformers process information causally, but long-context reasoning may depend on task state discovered only later. We formalize this mismatch through conditional state update tasks. For causal state update processors, providing the condition first can require exponentially less memory in the worst case than providing it last.   Motivated by this principle, we introduce Trace as State. We use collected reasoning traces as a textual proxy for task state and place it before the long-context block on a fresh pass, allowing information derived previously to guide rereading.   We conduct extensive experiments on Trace as State and Trace Append, a matched control that uses the same task state proxy but put it after the context. Across three models and three long-context datasets, Trace as State outperforms Trace Append in 26 of 27 reported combinations of model, task, and metric. On GraphWalks Parents, exact match lifts DeepSeek V4 Pro Preview from 29.2% on the initial pass and 43.0% with Trace Appendto 81.8% with Trace as State, and from 66.4% and 83.2% to 100.0% for GLM-5.2. These results show that placing traces before the context can improve long-context reasoning while retaining the causal transformer structure.

## Metadata
- **Published**: 2026-09-02T15:06:46Z
- **Authors**: Xu Zou, Jie Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02702v1)