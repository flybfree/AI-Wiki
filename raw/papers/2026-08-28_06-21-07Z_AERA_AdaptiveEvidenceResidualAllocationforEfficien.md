---
title: AERA: Adaptive Evidence Residual Allocation for Efficient Test-Time Reasoning
published: 2026-08-28T06:21:07Z
authors: Ziming Wang, Ivor Tsang, Hangwei Qian
url: http://arxiv.org/abs/2608.27964v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AERA: Adaptive Evidence Residual Allocation for Efficient Test-Time Reasoning

## Abstract
Test-time scaling improves language-model reasoning by generating additional candidate solutions, but allocating the same inference budget to every problem is computationally wasteful. Existing adaptive stopping methods commonly rely on confidence, agreement, or answer stability, implicitly assuming that stronger current evidence indicates that further computation is unnecessary. We show that this assumption can fail: checkpoint-level correctness evolves non-monotonically, and observable evidence may strengthen before an answer collapses or weaken before it recovers. Motivated by this mismatch, we introduce Adaptive Evidence Residual Allocation (AERA), a sequential controller that learns whether additional computation is likely to recover a better answer from checkpoint-observable evidence. AERA characterizes cumulative response prefixes using answer-distribution, temporal, re-solving, semantic, and compute features, and repeatedly decides whether to stop or allocate the next response block. Future checkpoint correctness is used only to construct offline supervision and is never available to the controller at inference time. Across GSM8K and GPQA Diamond, AERA identifies question-specific residual opportunities while substantially reducing inference computation. In a frozen-threshold incremental-generation evaluation on 300 untouched GSM8K questions, AERA achieves 92.61% accuracy versus 93.01% with 128 responses while reducing completion tokens by 95.99%. These results suggest that adaptive reasoning should estimate the future value of computation rather than equating present confidence with correctness.

## Metadata
- **Published**: 2026-08-28T06:21:07Z
- **Authors**: Ziming Wang, Ivor Tsang, Hangwei Qian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27964v1)