---
title: Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control
url: http://arxiv.org/abs/2607.27914v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_09-28-37Z_ExactActionValuesAreNotEnough_Rollout_VerifiedRein.md
generated_at: 2026-07-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a method to improve multi-zone VAV control using rollout‑verified reinforcement fine‑tuning of a reasoning model, showing that exact action values alone are insufficient and that a learned critic can mislead despite high correlation. On a physics‑based four‑zone emulator the approach reduced HVAC electricity by 4.5% compared with a baseline but failed to sustain gains after training.

## Key Takeaways
- The rollout verifier exposed that within‑state ranking was unreliable, as the critic selected the best candidate in only five of ten states despite near‑perfect across‑time correlation.
- Deterministic rollouts restored saved states and applied one candidate before TD3 scoring, yet 200 steps produced no sustained improvement in sampled‑action returns.
- GPT‑5 achieved larger electricity reduction (6.2%) but lowered ventilation margin, indicating that exact rollout scores do not reveal next‑state effects or direction of improvement.

## Context
This work addresses the gap between theoretical RL performance and real‑world deployment where building models are costly and training data scarce. By leveraging large language model reasoning capabilities, it demonstrates a path toward scalable HVAC control without physics‑specific calibration.

## Implications
Practitioners can adopt rollout verification to audit learned critics before fine‑tuning, avoiding hidden biases that degrade energy efficiency. The findings suggest that transition‑focused supervised fine‑tuning should precede value‑based RL in complex multi‑agent environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27914v1)
