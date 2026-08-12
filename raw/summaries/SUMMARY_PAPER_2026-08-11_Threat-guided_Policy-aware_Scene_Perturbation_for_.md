---
title: Threat-guided Policy-aware Scene Perturbation for Safe Autonomous Driving with Online Reinforcement Learning
url: http://arxiv.org/abs/2608.10403v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_02-49-50Z_Threat_guidedPolicy_awareScenePerturbationforSafeA.md
generated_at: 2026-08-11 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Threat-guided Policy-aware Scene Perturbation (TPSP) to enhance safety learning in online reinforcement learning for autonomous driving. By generating scene perturbations that align with the current policy’s weaknesses, TPSP improves training efficiency and achieves strong safety performance on NAVSIM v2 using about 4 million kilometers of simulated data.

## Key Takeaways
- The method uses a policy‑aware scene encoder to capture how the agent interacts with its environment, allowing perturbations that target critical objects rather than applying uniform changes.  
- Threat‑guided optimization evaluates safety by comparing rollout outcomes on original versus perturbed scenes, directing the generation of high‑value safety‑critical experiences.  
- Ablation results show that policy‑aware targeted perturbations provide more informative learning than random or policy‑unaware strategies, especially under limited interaction budgets.

## Context
Online reinforcement learning in autonomous driving faces a long‑tailed distribution of rare, dangerous scenarios that are hard to encounter naturally. Traditional scene synthesis often ignores the evolving behavior of the learned policy, leading to inefficient safety training. This work bridges that gap by making perturbations responsive to the current policy’s state and risk profile.

## Implications
For practitioners developing safe autonomous systems, TPSP offers a practical framework to enrich training data with contextually relevant challenges without excessive simulation cost. The approach can be adapted across domains where online learning meets real‑world safety constraints, fostering more robust and reliable agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10403v1)
