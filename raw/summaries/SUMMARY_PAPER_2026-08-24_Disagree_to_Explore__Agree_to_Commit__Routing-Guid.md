---
title: Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents
url: http://arxiv.org/abs/2608.22191v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_03-07-03Z_DisagreetoExplore_AgreetoCommit_Routing_GuidedTest.md
generated_at: 2026-08-24 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Risa, a routing‑guided test‑time scaling method that uses native MoE router traces to steer and arbitrate actions within software‑engineering agents without external judges or selection‑time tests. Experiments on SWE‑bench Verified show that Risa’s arbitration raises the macro‑average resolved rate from 44.9 % under uniform sampling to 48.2 % for the gpt‑oss family, matching text consensus while avoiding answer‑string matching.

## Key Takeaways
- Routing provides a robust behavioral role signal that can be read token‑granularly and compared decision‑matched across trajectories.  
- Risa’s arbitration encourages diverse exploration within each trajectory while promoting controlled convergence toward a final patch commitment.  
- Across independently sampled trajectories, agreement at informative patch positions selects the best candidate without needing an external judge.

## Context
The difficulty of test‑time scaling arises from non‑canonical answer forms and correlated sibling actions in long tool‑use trajectories. Native MoE routers capture these dynamics directly, offering a lightweight alternative to human‑written selectors. This work demonstrates that such internal signals can be leveraged for more reliable agent performance.

## Implications
For practitioners, Risa reduces the need for costly external evaluation loops, enabling faster iteration cycles and lower resource consumption. In industry, it offers a scalable framework for deploying MoE agents across diverse codebases while maintaining high resolution rates on benchmark tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22191v1)
