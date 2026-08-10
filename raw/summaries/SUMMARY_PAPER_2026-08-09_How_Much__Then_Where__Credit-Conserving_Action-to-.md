---
title: How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning
url: http://arxiv.org/abs/2608.07118v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_11-22-09Z_HowMuch_ThenWhere_Credit_ConservingAction_to_Token.md
generated_at: 2026-08-09 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FACTOR, a method that separates credit assignment in multi‑turn agent reinforcement learning into two distinct steps: first assigning trajectory‑level credits to actions using checkpoint‑calibrated TD residuals, then allocating each action’s credit across its tokens with feedback‑conditioned likelihood gaps. The approach yields per‑action normalization that preserves the average coefficient and avoids token‑level sign flips, improving performance over baselines on ALFWorld, WebShop, and ScienceWorld.

## Key Takeaways
- FACTOR uses checkpoint‑calibrated TD residuals to compute per‑action credits that telescope to the trajectory advantage.  
- Feedback‑conditioned teacher‑student likelihood gaps allocate each credit across realized action tokens while preserving the action‑average coefficient.  
- Ablations show that TD action credit is the primary driver of improvement, with hindsight token allocation providing complementary gains.

## Context
Credit assignment remains a challenge in multi‑turn RL because actions span multiple tokens and their contribution to overall reward is non‑trivial. Existing methods often couple trajectory and token credit, leading to unstable or biased allocations that hinder scalability across diverse environments and model families.

## Implications
FACTOR’s decoupled design simplifies hyperparameter tuning, allowing seamless transfer to larger backbones and different model families without retuning. Practitioners can leverage this framework to achieve more stable reward signals and better policy convergence in complex multi‑turn settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07118v1)
