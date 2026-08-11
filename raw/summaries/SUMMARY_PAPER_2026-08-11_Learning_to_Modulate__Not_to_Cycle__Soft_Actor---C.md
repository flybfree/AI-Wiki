---
title: Learning to Modulate, Not to Cycle: Soft Actor---Critic Recovers Inverter-Style Heat-Pump Control
url: http://arxiv.org/abs/2608.09453v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_11-24-29Z_LearningtoModulate_NottoCycle_SoftActor___CriticRe.md
generated_at: 2026-08-11 12:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a reinforcement learning controller that explicitly penalizes compressor cycling in heat‑pump operation, aiming to recover the inverter‑style continuous modulation used in commercial systems. The Soft Actor‑Critic (SAC) algorithm is shown to learn a smooth policy with no daily start‑ups, while PPO reverts to frequent on/off cycles. On the BOPTEST hydronic case the SAC solution reduces thermal discomfort by up to 90.7 % at only an 11.5 % cost rise.

## Key Takeaways
- The reward function adds a levelised compressor‑wear term, making cycling directly penalized in the learning objective.  
- SAC discovers a continuous modulation policy that keeps the compressor engaged all day, eliminating start‑ups and achieving zero cycles per day.  
- PPO, despite similar training conditions, collapses to bang‑bang control, producing many daily start‑ups compared with the baseline.

## Context
Reinforcement learning is increasingly used for building energy management but often overlooks hardware wear caused by on/off cycling. This work bridges that gap by integrating mechanical durability into the RL reward, highlighting how algorithmic choices affect real‑world operational behavior.

## Implications
For HVAC engineers, the findings suggest that selecting SAC over PPO can lead to longer equipment life and smoother service intervals. Practitioners should consider wear‑aware rewards when deploying RL controllers in residential heat pumps to balance comfort and cost without unnecessary cycling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09453v1)
