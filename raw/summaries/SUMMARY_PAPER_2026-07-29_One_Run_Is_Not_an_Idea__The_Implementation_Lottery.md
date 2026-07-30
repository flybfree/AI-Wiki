---
title: One Run Is Not an Idea: The Implementation Lottery in Automated Research
url: http://arxiv.org/abs/2607.26587v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_08-06-43Z_OneRunIsNotanIdea_TheImplementationLotteryinAutoma.md
generated_at: 2026-07-29 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper quantifies the impact of a single implementation score on idea‑level conclusions in automated research. By comparing variance across runs and reruns, it shows that one run can mislead which idea is retained by up to 43.6 % of decisions, far exceeding the reliability of repeated artifact reruns.

## Key Takeaways
- Implementation variance exceeds same‑artifact rerun variance by more than fivefold on tabular tasks, indicating a strong lottery effect.
- The winner from one implementation draw differs from the winner under other two implementations in 25.6 % and 43.6 % of decisions respectively.
- Idea reliability remains compromised even after card‑level filtering under two outcome‑blind review rules.

## Context
Automated research systems rely on experimental scores to decide which ideas to retain, transfer, or store in memory. However, these systems currently treat a single run’s score as definitive evidence about the underlying mechanism, ignoring the variability introduced by different plausible implementations.

## Implications
If idea reliability is low, decisions that guide future research may be based on flawed data, leading to wasted effort and misaligned priorities. Researchers should prioritize collecting multiple implementation scores before any idea‑level branching or memory update occurs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26587v1)
