---
title: SESSE: Sketch, Expand, Sort, Summarize, Evaluate -- LLM-as-Judge Evaluation via Structured Decomposition
published: 2026-08-18T20:27:56Z
authors: Dae Lee, Mihai Delgeanu, Adel Youssef
url: http://arxiv.org/abs/2608.18303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SESSE: Sketch, Expand, Sort, Summarize, Evaluate -- LLM-as-Judge Evaluation via Structured Decomposition

## Abstract
LLM-as-judge evaluation reduces response quality assessment to a single holistic A/B preference choice, providing no mechanism to isolate which quality dimensions drove the preference or distinguish model errors from genuine label ambiguity. We propose SESSE (Sketch, Expand, Sort, Summarize, Evaluate), a training-free framework that decomposes holistic judgment into structured sub-questions mined directly from the judge's own error cases; requiring no oracle responses, task-specific rubrics, or fine-tuning. On RewardBench (n=1,000), SESSE achieves near-parity with the chain-of-thought baseline and is competitive with RISE-Judge-32B (92.7%), a fine-tuned specialist, while remaining fully training-free. Per-criterion vote evidence provides an interpretable audit trail for diagnosing label ambiguity and judge failure modes unavailable from a single holistic output token.

## Metadata
- **Published**: 2026-08-18T20:27:56Z
- **Authors**: Dae Lee, Mihai Delgeanu, Adel Youssef
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18303v1)