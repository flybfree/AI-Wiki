---
title: Learning Situation-Conditioned Thinking Policies for Long-Term LLM Agents
published: 2026-10-07T07:34:08Z
authors: Hong Su
url: http://arxiv.org/abs/2610.09590v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Situation-Conditioned Thinking Policies for Long-Term LLM Agents

## Abstract
Long-running autonomous agents must reuse accumulated reasoning experience without allowing explicit historical memory and LLM context to grow indefinitely. However, existing memory mechanisms mainly retrieve, summarize, or compress past content and do not directly learn when particular kinds of thinking should be activated or discover new thinking knowledge from temporally dispersed experiences. This paper proposes a situation-conditioned thinking memory framework that transforms historical reasoning experience into a lightweight policy for predicting what should be thought about in the current situation, while leaving detailed reasoning to a large language model. Situations may represent temporal or spatiotemporal evolution rather than only current states. Temporary experiences are also periodically analyzed across multiple independent episodes to identify repeated long-range regularities, which are consolidated into new thinking knowledge and further internalized by the lightweight policy. Experiments show that the learned policy achieves 1.000 F1 on temporal-rule generalization, improves DeepSeek reasoning F1 from 0.789 to 0.868, reduces online processing time from 0.3636 ms to 0.0382 ms per query at 30,000 historical situations, and reaches 1.000 relation-discovery F1 and future-thinking accuracy after sufficient repeated cross-experience evidence.

## Metadata
- **Published**: 2026-10-07T07:34:08Z
- **Authors**: Hong Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09590v1)