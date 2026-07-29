---
title: CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization
url: http://arxiv.org/abs/2607.25659v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_12-45-19Z_CoRT_CounterfactualReplayforToken_LevelRubric_Guid.md
generated_at: 2026-07-28 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoRT, a token‑level credit weighting method for rubric‑conditioned GRPO that allocates reward across individual tokens within a response. By using counterfactual replay to rescore the same sampled answer under both the original rubric‑guided prompt and an equivalent criteria‑free prompt, CoRT derives tokenwise log‑likelihood contrasts that serve as a proxy for rubric dependence. The method shows an average improvement of 4.4 percentage points over matched response‑level GRPO across several tasks.

## Key Takeaways
- Rubric‑based reinforcement learning typically collapses explicit criteria into a single scalar reward, leaving no mechanism to credit different spans or formatting decisions within the same response.
- CoRT replaces this collapse with counterfactual replay that computes tokenwise log‑likelihood contrasts between rubric‑conditioned and criteria‑free prompts, providing a direct signal of how each token depends on the rubric context.
- Experiments across instruction‑tuned models demonstrate that CoRT yields a consistent advantage over matched response‑level GRPO, averaging 4.4 percentage points higher performance while avoiding an auxiliary scorer.

## Context
Current reinforcement learning pipelines for language generation treat rubric criteria as coarse‑grained rewards, which limits the ability to reward nuanced aspects of outputs such as specific spans or formatting choices. This paper addresses that limitation by proposing a token‑level approach that preserves fine‑grained credit allocation without introducing additional complex models.

## Implications
For practitioners, CoRT offers a straightforward way to refine rubric‑driven training while keeping the simplicity and stability of GRPO. In industry settings where instruction tuning relies on precise reward shaping, this method can lead to more accurate model behavior with minimal engineering overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25659v1)
