---
title: A Probe Direction Is a Property of Its Prompt
url: http://arxiv.org/abs/2608.13329v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_14-57-37Z_AProbeDirectionIsaPropertyofItsPrompt.md
generated_at: 2026-08-13 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that a probe direction used to measure model sensitivity to evaluation prompts is not an intrinsic property of the model but depends on the choice of prompt. Experiments show that reported scores and trends with model size follow the prompt rather than the model, indicating measurement design flaws.

## Key Takeaways
- The instrument’s score varies with which “evaluation‑announcing” prompt is used, so the reported trend is driven by prompt selection not model architecture.
- Two studies disagree on the sign of a size trend because they chose different prompts; both can be reproduced from a single design choice.
- Most variance in scores comes from how models respond to each prompt, not from differences between models.

## Context
AI evaluation methods often rely on probe directions that compare activations under “evaluation” vs. non‑evaluation prompts. These probes aim to quantify model behavior but frequently ignore the arbitrary nature of the prompting design.

## Implications
If a probe’s score is influenced by prompt choice, it cannot be used for fair cross‑model comparison. Researchers must treat prompt selection as part of measurement design and avoid conflating it with model performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13329v1)
