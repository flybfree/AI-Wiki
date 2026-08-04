---
title: On the Limits of Machine-Learned Ranking for Modern Microarchitectural Policies
published: 2026-08-02T06:55:43Z
authors: Yanxin Zhang, Shayne Wadle, Yuxuan Xiong, Zheyu Fu, Trivikram Krishnamurthy, Karu Sankaralingam
url: http://arxiv.org/abs/2608.01041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Limits of Machine-Learned Ranking for Modern Microarchitectural Policies

## Abstract
Machine-learning predictors estimate processor performance far faster than cycle-level simulation. For design-space exploration, however, the valuable test is not merely reproducing the usual hardware ordering, but identifying how different hardware configurations rank on individual program phases. We evaluate four ML-predictors in two design regimes: \emph{Structural Parameters} (SP), varying hardware resources such as issue width, ROB size, and cache capacity; and \emph{Behavioral Policies} (BP), varying prefetching and replacement algorithms. In the SP regime, aggregate ranking is strong, yet counter-intuitive windows(CIW)---where the configuration expected to be slower is faster---constitute $22.4\%$ of non-tied windows across five pairs with a clear architectural prior. CIW match across these pairs is only $23.3$--$39.9\%$; every point estimate is below the $50\%$ random strict-ordering reference. The BP regime presents a different failure: ground-truth ties cover $37.8\%$ of pair-windows, most strict pairs have margins of only a few cycles, and no model family reliably beats a feature-free majority baseline. NeuroScalar and SimNet fall below that baseline, Concorde is statistically tied with it, and the best selected OneDSE head improves by only $2.1$ percentage points. Accuracy rises mainly at large margins. We further show that this failure is not a matter of model capacity: an information-theoretic analysis reveals that when ranking outcomes depend on hidden microarchitectural state absent from the instruction stream, no trace-based predictor can exceed the Bayes accuracy determined by observable inputs alone. Thus high cycle or aggregate ranking accuracy can reflect mastery of easy, high-margin cases while missing the local reversals that carry the most architectural insight and for which cycle-level simulation remains indispensable.

## Metadata
- **Published**: 2026-08-02T06:55:43Z
- **Authors**: Yanxin Zhang, Shayne Wadle, Yuxuan Xiong, Zheyu Fu, Trivikram Krishnamurthy, Karu Sankaralingam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01041v1)