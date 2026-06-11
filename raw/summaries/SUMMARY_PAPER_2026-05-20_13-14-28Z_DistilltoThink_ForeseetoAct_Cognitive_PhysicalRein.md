---
title: Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving
url: http://arxiv.org/abs/2605.21139v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-20_13-14-28Z_DistilltoThink_ForeseetoAct_Cognitive_PhysicalRein.md
generated_at: 2026-06-11 10:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoPhy, a CognitivePhysical reinforcement learning framework that overcomes the imitation‑learning ceiling in autonomous driving by integrating cognitive semantics and foresighted physical modeling. Experiments show state‑of‑the‑art performance on NAVSIM v1/v2 while enabling safer, intent‑aware behavior through a dual‑reward optimization scheme.

## Key Takeaways
- The VLM knowledge is distilled into the BEV encoder at zero inference cost, discarding the VLM entirely to retain cognitive ability without extra computation.  
- An auto‑regressive BEV world model predicts future semantic maps conditioned on candidate actions, providing an interpretable sandbox for safety metric extraction.  
- Policy optimization uses GRPO with a dual reward: a physical reward from BEV rollouts enforces hard constraints and a cognitive reward from a language‑aligned scorer ensures intent compliance.

## Context
Current end‑to‑end autonomous driving systems rely on behavioral cloning, which cannot learn beyond observed trajectories. The field urgently needs methods that combine semantic understanding with predictive physics to achieve safer, more flexible behavior without costly real‑world data.

## Implications
CoPhy offers a cost‑effective way to embed human language commands into vehicle cognition while guaranteeing safety through interpretable rollout predictions. Practitioners can leverage this framework to build autonomous systems that are both compliant and adaptable to novel scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.21139v1)
