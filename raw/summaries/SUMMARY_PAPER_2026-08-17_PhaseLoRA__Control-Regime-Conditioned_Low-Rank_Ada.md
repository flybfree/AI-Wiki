---
title: PhaseLoRA: Control-Regime-Conditioned Low-Rank Adaptation for Continuous-Action Vision-Language-Action Policies
url: http://arxiv.org/abs/2608.15285v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_15-32-08Z_PhaseLoRA_Control_Regime_ConditionedLow_RankAdapta.md
generated_at: 2026-08-17 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes PhaseLoRA, a lightweight low-rank adaptation technique for continuous-action vision-language-action policies that conditions updates on the phase of the trajectory. By using two descriptors—fine-control tendency and event/boundary intensity—the method adjusts the LoRA left factor at each prediction step while keeping the backbone frozen. On LIBERO the approach raises average success rate by 12.2 points compared with a matched high-rank LoRA baseline.

## Key Takeaways
- PhaseLoRA introduces two weakly supervised descriptors that capture fine-control tendency and event/boundary intensity to guide adaptation at each action-chunk prediction step.
- The method modulates only the LoRA left factor, allowing the effective low‑rank update direction to vary over time without altering the frozen backbone.
- Ablations show that random temporal modulation or scalar gating cannot achieve the performance gains of PhaseLoRA.

## Context
Continuous-action VLA policies face challenges because adaptation must be phase‑dependent and most parameter‑efficient fine‑tuning methods treat updates as static. This limitation hampers performance across complex manipulation regimes such as approach, contact transition, grasping, transport, and placement.

## Implications
PhaseLoRA demonstrates that within‑trajectory conditioning can serve as an effective lightweight PEFT axis for VLA systems. Practitioners can adopt this technique to fine‑tune models quickly without large compute costs, opening new possibilities for real‑time embodied AI agents in robotics and assistive technologies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15285v1)
