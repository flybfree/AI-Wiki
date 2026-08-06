---
title: ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment
url: http://arxiv.org/abs/2608.05102v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-41-31Z_ABSeeker_TrainingLong_HorizonSearchAgentsviaAnswer.md
generated_at: 2026-08-05 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Answer-Backtracked Credit Assignment (ABC) to train long‑horizon search agents by converting sparse trajectory outcomes into step‑level supervision. It demonstrates that ABSeeker, trained on Qwen3.5-4B with 8.5k examples, reaches 37.3% on BrowseComp and 39.1% on BrowseComp‑ZH, improving to 55.3% and 52.9% with context management.

## Key Takeaways
- ABC transforms a single binary answer into dense step‑level rewards by tracing clues back from the final answer.
- The framework reweights each turn’s loss in SFT and uses step scores as rewards in GRPO, enabling fine‑grained credit assignment.
- ABSeeker achieves state‑of‑the‑art performance on BrowseComp despite using only a small dataset.

## Context
Long‑horizon search agents face the challenge of distinguishing useful actions from errors across many steps. Existing training treats all steps uniformly, limiting learning efficiency and performance.

## Implications
This fine‑grained credit assignment can be applied to any long‑horizon retrieval task, reducing reliance on large labeled datasets. Practitioners may integrate ABC into existing SFT or RL pipelines to boost accuracy with minimal data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05102v1)
