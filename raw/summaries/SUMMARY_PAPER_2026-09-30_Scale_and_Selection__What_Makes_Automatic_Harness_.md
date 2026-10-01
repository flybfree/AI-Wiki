---
title: Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents
url: http://arxiv.org/abs/2609.39304v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_08-46-38Z_ScaleandSelection_WhatMakesAutomaticHarnessEvoluti.md
generated_at: 2026-09-30 22:01
model: qwen3.6-35b-a3b
---

## Summary
This paper explores the automatic evolution of harnesses for visual-interface robot agents by leveraging off-the-shelf coding agents as optimizers to refine prompts, tools, and control rules. The authors demonstrate that while automated optimization is feasible, its success relies heavily on two critical mechanisms: ensuring sufficient rollout volume per round to maintain a high signal-to-noise ratio and implementing a Champion-Challenger selection process to prevent performance drift caused by ill-judged edits.

## Key Takeaways
- Rollout scale directly dictates generalization and trustworthiness; expanding the training set from 5 to 100 rollouts per round increases held-out success from 47% to 67%, whereas small batches lead to severe overfitting where models achieve high scores on training tasks but fail on unseen data due to noisy binary outcomes.
- Unconditional acceptance of optimizer revisions results in rapid performance degradation within ten rounds as errors accumulate, but introducing a Champion-Challenger safeguard that promotes changes only when they strictly outperform the

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39304v1)
