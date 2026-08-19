---
title: Q-Learning With World Models
url: http://arxiv.org/abs/2608.17163v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_22-00-42Z_Q_LearningWithWorldModels.md
generated_at: 2026-08-18 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces QWM, a framework that combines standard Q‑learning with world models to perform test‑time search over imagined trajectories while the policy and value function are trained only on real online transitions. The approach avoids compounding bias inherent in model‑based RL that optimizes directly on imagined rollouts, enabling sample‑efficient learning for high‑dimensional tasks such as robot manipulation.

## Key Takeaways
- Off‑policy reinforcement learning can achieve sample efficiency but many model‑based methods suffer from bias because they optimize policy or value functions on simulated trajectories rather than real data.  
- QWM leverages world models to conduct test‑time search over imagined paths, yet the training remains grounded in actual transitions, thus preventing the accumulation of model error during learning.  
- On benchmark manipulation tasks Robomimic and LIBERO, QWM demonstrates superior performance compared with state‑of‑the‑art methods in both sample efficiency and final policy quality.

## Context
The rapid advancement of off‑policy RL has opened doors to more reliable policies for vision‑language‑action systems, yet the scalability of model‑based approaches remains limited by high computational cost and bias accumulation. This work addresses those challenges by integrating predictive world models into a conventional Q‑learning loop, preserving real‑world grounding while harnessing the efficiency gains of rollout search.

## Implications
For researchers, QWM offers a practical pathway to deploy sample‑efficient RL in complex robotic environments where data collection is costly and task horizons are long. Practitioners can expect faster convergence and higher performance without sacrificing reliability, making it a valuable tool for industry applications ranging from autonomous manipulation to service robotics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17163v1)
