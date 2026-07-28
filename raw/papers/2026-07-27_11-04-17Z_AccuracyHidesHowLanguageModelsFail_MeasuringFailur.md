---
title: Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets
published: 2026-07-27T11:04:17Z
authors: Zongyou Yang, Yinghan Hou
url: http://arxiv.org/abs/2607.24268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets

## Abstract
Language-model benchmarks collapse two distinct measurement questions into a single accuracy score: whether a response reached an evaluable state, and whether its answer was judged correct. We introduce a two-layer evaluation framework that separates scorer-independent execution evidence, including termination, answer exposure, parseability, and completion length, from scorer-dependent correctness. Across 2,550 outputs from five fixed Qwen and DeepSeek configurations on MATH and ARC-Challenge, matched 2,048-token limits produce sharply different execution mixtures: 49 of 450 Qwen MATH outputs terminate without a final answer, compared with 5 of 300 DeepSeek MATH outputs and none of the 750 ARC outputs. Among the same 300 DeepSeek MATH question-model pairs, no missing-final length termination is observed at 8,192 tokens. A coverage-audited targeted verification study further shows that candidate-selection and aggregation policies can substantially alter comparative accuracy estimates. These results demonstrate that accuracy conflates execution case mix with verification policy. Evaluations of test-time methods should therefore report pre-intervention execution states, verification coverage, and scorer provenance alongside accuracy.

## Metadata
- **Published**: 2026-07-27T11:04:17Z
- **Authors**: Zongyou Yang, Yinghan Hou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24268v1)