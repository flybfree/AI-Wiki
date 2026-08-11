---
title: LUCID: Latent-Skill Unified Control via Imagined Dynamics for Long-Horizon Humanoid Loco-Manipulation
url: http://arxiv.org/abs/2608.07746v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-07_20-26-34Z_LUCID_Latent_SkillUnifiedControlviaImaginedDynamic.md
generated_at: 2026-08-11 13:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LUCID, a hierarchical model‑based reinforcement learning framework for long‑horizon humanoid loco‑manipulation. By training a low‑level latent‑conditioned policy through adversarial imitation and freezing it while jointly optimizing a high‑level planner and a macro‑dynamics world model, LUCID enables reliable composition of whole‑body skills across complex task sequences. Experiments on simulated multi‑object rearrangement show higher full‑task success and partial‑completion rates than prior baselines.

## Key Takeaways
- The framework separates low‑level skill execution from high‑level planning using imagined rollouts of a learned dynamics model, allowing the planner to reason about future states without real execution.  
- A structured latent‑conditioned low‑level policy is trained via adversarial imitation and then frozen, providing stable behavior for downstream optimization.  
- The macro‑dynamics world model predicts temporally extended state transitions induced by latent decisions, facilitating high‑level policy improvement.

## Context
The need for humanoid robots to perform intricate, multi‑step manipulation tasks drives research into scalable skill composition methods. Traditional approaches rely on fixed planners or task‑specific policies that limit flexibility and adaptability in real‑world scenarios. LUCID addresses these limitations by integrating model‑based planning with learned dynamics, offering a more robust alternative.

## Implications
LUCID’s architecture can be applied to any domain requiring sequential skill execution, from robotics to autonomous vehicles, improving task success rates and operational efficiency. Practitioners may leverage the framework to design modular robotic agents capable of handling complex, long‑horizon challenges without extensive retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07746v1)
