---
title: Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents
url: http://arxiv.org/abs/2609.01245v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_13-44-40Z_ExploreMore_DriftLess_Outcome_OnlyReinforcementLea.md
generated_at: 2026-09-01 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CANOPY, a reinforcement‑learning protocol that trains LLM agents using only outcome‑only rewards and on‑policy updates. On the AppWorld coding benchmark, a Qwen3‑14B policy reaches top performance without task‑specific supervision or extra scaffolding, demonstrating that long‑horizon interactive learning can be achieved with minimal data.

## Key Takeaways
- Signal starvation occurs when sparse outcome‑only rewards produce gradients only in mixed rollout groups, silencing the hardest tasks.  
- Policy drift arises because compressing many updates into a small task pool collapses the sampling distribution, reducing informative signals.  
- CANOPY rescues both by scaling same‑task exploration until natural signals reappear, keeping updates on‑policy and KL‑anchored to the agent’s own action tokens.

## Context
Current research often relies on dense rewards, skill libraries, or multi‑agent orchestration to compensate for limited data in small open models. This paper argues that these workarounds mask deeper issues in outcome‑only RL, which limits model performance despite abundant interaction budgets.

## Implications
The findings suggest that outcome‑only reinforcement learning can be a viable path for deploying long‑horizon interactive agents on modest compute resources. Practitioners may adopt CANOPY to reduce reliance on external supervision and accelerate agent training cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01245v1)
