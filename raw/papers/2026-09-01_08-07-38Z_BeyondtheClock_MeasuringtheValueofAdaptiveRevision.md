---
title: Beyond the Clock: Measuring the Value of Adaptive Revision
published: 2026-09-01T08:07:38Z
authors: Ayushi Chadha
url: http://arxiv.org/abs/2609.00874v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Clock: Measuring the Value of Adaptive Revision

## Abstract
As agentic systems become compound systems, increasingly important decisions move above task execution itself: when should a higher-level controller preserve the strategy guiding another process, and when should it revise it? We study this meta-level control problem in a hierarchical latent reasoner whose manager can retain or replace a commitment governing lower-level computation. Across three precommitted training seeds, learned revision timing produces qualitatively different policies, ranging from an almost deterministic early clock to substantially more state conditioned schedule distributions, yet none outperforms the best forced timing policy evaluated on the same frozen checkpoint. This separates state dependence from decision value: a controller can vary its actions with internal state without turning that variation into a reproducible task-performance benefit. A deeper intervention study on the original checkpoint shows that timing itself is consequential and order-sensitive, while exhaustive enumeration reveals that a strong fixed schedule captures most of the measurable value available from timing at this decision budget. Counterfactual PERSIST/REPLAN diagnostics further show why score-level evidence can be misleading when predictability is dominated by decision position rather than within-position discrimination. Together, these results argue that learned meta-level control should be evaluated along three separate axes: whether its score depends on state, whether that dependence changes realized behavior, and whether those changes capture outcome value beyond a strong non-adaptive policy.

## Metadata
- **Published**: 2026-09-01T08:07:38Z
- **Authors**: Ayushi Chadha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00874v1)