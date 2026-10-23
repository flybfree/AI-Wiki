---
title: Behind Aggregate Scores: What Systematically Varying Arena-Hard's LLM Judge Reveals
url: http://arxiv.org/abs/2610.30512v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-21_22-46-14Z_BehindAggregateScores_WhatSystematicallyVaryingAre.md
generated_at: 2026-10-22 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the reliability and sensitivity of LLM-based judges used in Arena-Hard v2.0 evaluations by systematically varying the judge's instructions, output format, and task framing while holding model answers fixed. The author demonstrates that aggregate benchmark scores can remain nearly stable even when individual win/tie/loss verdicts shift dramatically across prompts, revealing a critical gap between what aggregate scores convey and what they actually measure. The findings show that both repeated runs of identical setups and modifications to judge instructions introduce substantial prompt-level instability that aggregate metrics fail to capture.

## Key Takeaways
- Repeating the exact same default judging setup at temperature zero with a pinned model version shifts the aggregate score by only about one point, yet changes the win/tie/loss outcome on 21.2% of the 500 prompts tested, demonstrating that even deterministic-seeming configurations produce non-repeatable individual verdicts.
- Modifying judge instructions introduces additional sensitivity: one setup that requests a verdict without reasoning and removes several other instructions changes outcomes on 28.2 percentage points more prompts than the average of two unchanged reruns, while simultaneously dropping the aggregate score by 4.09 points. Conversely, a setup prioritizing accuracy criteria changes outcomes on 6.7 percentage points more prompts than reruns while the aggregate score barely moves, showing that instruction sensitivity and aggregate score stability are decoupled.
- The paper argues that a stable aggregate score does not establish that individual verdicts are repeatable, and recommends that evaluations relying on individual verdicts should repeat each setup and report both aggregate scores and prompt-level agreement rates to provide a more honest picture of judge reliability.

## Context
LLM-as-a-judge methodologies have become a dominant evaluation paradigm for comparing model outputs, with benchmarks like Arena-Hard relying on judge verdicts to produce leaderboards and preference labels used in training pipelines. This paper addresses a foundational trust question in that ecosystem: whether the individual judgments underpinning these scores are stable and reproducible. By systematically varying eight combinations of criteria, output format, and task framing across 500 prompts, the study provides the kind of controlled sensitivity analysis that the field has largely lacked, moving beyond single-run aggregate reporting toward a more rigorous understanding of judge behavior.

## Implications
For practitioners building evaluation pipelines, preference datasets, or model comparison tools, this work signals that single-run aggregate scores are insufficient evidence of judge reliability and that prompt-level instability can silently corrupt downstream training signals or benchmark rankings. Model developers and benchmark maintainers should incorporate repeated-run protocols and report agreement metrics alongside headline scores, while researchers using Arena-Hard-style verdicts as preference labels for fine-tuning or RLHF should treat individual judgments as noisy signals requiring replication. The findings also suggest that seemingly minor instruction changes in judge prompts can have outsized effects on individual outcomes, making prompt engineering for judges a high-stakes design decision rather than a trivial configuration choice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30512v1)
