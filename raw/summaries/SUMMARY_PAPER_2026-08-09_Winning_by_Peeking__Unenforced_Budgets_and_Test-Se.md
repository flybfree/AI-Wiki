---
title: Winning by Peeking: Unenforced Budgets and Test-Set Selection Inflate Short-Budget AutoML Comparisons
url: http://arxiv.org/abs/2608.07303v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_15-00-10Z_WinningbyPeeking_UnenforcedBudgetsandTest_SetSelec.md
generated_at: 2026-08-09 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why AutoML system comparisons at very short time budgets (tens of seconds) can be misleadingly favorable. It demonstrates that Orcetra appeared to outperform FLAML and AutoGluon on 513 OpenML datasets, but these gains stem from protocol defects rather than genuine superiority.

## Key Takeaways
- The search loop scores every candidate on the test split, creating a headline metric that is a maximum over dozens of noisy estimates while baselines select on training data and touch the test set only once.  
- A 60‑second budget was checked before launching a candidate but never enforced during execution, leading to a median run time of 120 seconds—2.24 times longer than AutoGluon’s actual usage.  
- When the selection rule is moved to a validation split and the deadline is externally enforced, Orcetra’s win rate drops from 59.4 % to 34.3 %, eliminating all pairwise differences.

## Context
AutoML tools are frequently benchmarked under tight time constraints, with results presented in READMEs and workshop papers. These short‑budget comparisons often ignore how the search protocol and budget enforcement affect performance, leading to inflated conclusions that do not reflect real‑world efficiency.

## Implications
For researchers and practitioners, this work underscores the need for a checklist that enforces strict budget limits and uses validation splits for selection. Without such safeguards, AutoML rankings can mislead both academic discourse and industry adoption decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07303v1)
