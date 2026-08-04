---
title: Abstention as an Action Can Kill Both the Reward Gradient and the KL Anchor: Collapse Law and Repair for Error-Penalized Reinforcement Learning
url: http://arxiv.org/abs/2608.00301v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_21-31-07Z_AbstentionasanActionCanKillBoththeRewardGradientan.md
generated_at: 2026-08-03 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how error‑penalized reinforcement learning can mislead agents to abstain even when they could answer correctly, showing that the reward gradient and KL anchor both vanish under certain conditions. It demonstrates a “collapse law” where abstention kills performance, then offers a repair by separating confidence reporting from decision making.

## Key Takeaways
- The reward gradient and the KL‑anchor are throttled by the same gate‑saturation factor when abstaining is treated as an action, causing both to die together. 
- In sparse‑answer regimes group normalization effectively replaces penalties with a unit penalty, shifting the learned threshold from λ/(1+λ) to ½. 
- A mandatory confidence report that is always emitted prevents gate saturation, preserving gradient flow and keeping the calibrated optimum attractive.

## Context
Error‑penalized scoring rules are common in RL for preventing hallucinations, but they assume agents can express uncertainty without hurting performance. This work reveals a hidden instability when abstention is modeled as an action, highlighting the need to keep reporting mechanisms decoupled from decision logic.

## Implications
For practitioners, the collapse law warns against treating abstention as a learnable policy that shares gradients with reward signals. The proposed repair suggests embedding confidence scores separately, which can improve coverage and calibration without sacrificing learning stability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00301v1)
