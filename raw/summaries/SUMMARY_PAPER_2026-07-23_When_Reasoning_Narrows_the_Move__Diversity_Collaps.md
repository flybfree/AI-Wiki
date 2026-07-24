---
title: When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play
url: http://arxiv.org/abs/2607.19523v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_19-10-38Z_WhenReasoningNarrowstheMove_DiversityCollapseinLLM.md
generated_at: 2026-07-23 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how supervised fine‑tuning (SFT) of large language models affects behavioral diversity in deterministic board games such as tic‑tac‑toe variants. Experiments across state evaluation, arena gameplay, and training trajectories reveal that reasoning‑mode generation often reduces action variety even when accuracy improves, indicating a collapse beyond the minimal trade‑off expected.

## Key Takeaways
- Reasoning‑mode generation suppresses action diversity without proportionally boosting accuracy, showing a divergence from the anticipated trade‑off.  
- Standard SFT improves accuracy but triggers premature diversity collapse that exceeds what is minimally required by the accuracy‑diversity relationship.  
- Training on all optimal actions per state (action augmentation) partially mitigates this effect, highlighting narrow‑support imitation as a cause of policy collapse.

## Context
Understanding how model training influences exploratory behavior is crucial for developing agents that remain adaptable in sequential decision tasks. This work addresses a gap where SFT, commonly used to align models with human preferences, may unintentionally lock the system into a narrow strategy space.

## Implications
For practitioners, preserving action support during fine‑tuning can help maintain useful exploration and prevent overfitting to a single optimal policy. In industry applications, this insight could improve robustness of AI agents in games and other environments where diverse strategies are valuable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19523v1)
