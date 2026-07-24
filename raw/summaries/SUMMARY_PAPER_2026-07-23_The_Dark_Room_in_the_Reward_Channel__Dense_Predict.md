---
title: The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works
url: http://arxiv.org/abs/2607.21273v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_12-50-18Z_TheDarkRoomintheRewardChannel_DensePredictionRewar.md
generated_at: 2026-07-23 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why dense per‑step prediction rewards cause catastrophic failure when used with GRPO‑trained language models on long‑horizon tasks such as ALFWorld, describing the resulting “dark room” where agents predict perfectly but never succeed. It identifies that removing only the standard deviation normalization of GRPO’s advantage estimate restores baseline performance and explains this via a variance‑profile mechanism that amplifies within‑group reward variability.

## Key Takeaways
- Dense prediction rewards under group‑normalized RL produce an absorbing state where prediction accuracy reaches 1.0 while task success remains 0, indicating a systematic collapse of the policy.
- Ablating GRPO’s std normalization alone eliminates the collapse, showing that bounded shaping coefficients become unbounded pressure when variance does not decay with mastery.
- A variance‑profile criterion predicts collapses and can forecast outcomes for arms that have not yet run, offering a diagnostic tool for reward design.

## Context
This research addresses a growing concern in reinforcement learning: how to provide rich supervision without destabilizing learned policies. The “dark room” phenomenon illustrates the risk of overly dense signals when combined with normalization schemes that amplify variance, a problem relevant to scaling language models and long‑horizon RL.

## Implications
For practitioners, the findings warn against using dense prediction rewards in GRPO without careful variance control, suggesting alternative loss channels or signal‑delivery mechanisms. The insight may guide safer reward engineering as LLMs are deployed for complex, multi‑step tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21273v1)
