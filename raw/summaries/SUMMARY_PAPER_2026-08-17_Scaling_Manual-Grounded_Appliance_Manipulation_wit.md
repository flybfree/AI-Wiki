---
title: Scaling Manual-Grounded Appliance Manipulation with Data Synthesis and Unified Planning
url: http://arxiv.org/abs/2608.15863v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_17-15-54Z_ScalingManual_GroundedApplianceManipulationwithDat.md
generated_at: 2026-08-17 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MAGE, a scalable data synthesis pipeline that automatically generates part grounding, long-horizon planning, and closed-loop recovery from appliance manuals, and builds UseAppliance, the first large-scale dataset for manual-grounded appliance manipulation planning. AppliancePlan demonstrates over 10x improvement on open-loop tasks and consistent SOTA performance across all tasks.

## Key Takeaways
- MAGE introduces a Hierarchical Appliance Graph that automates part grounding, long-horizon planning, and closed-loop recovery from manuals.
- UseAppliance provides 22 appliance categories with over 89K part annotations, 53K manipulation tasks, and 33K closed-loop adjustment steps.
- AppliancePlan achieves a 7B parameter model that outperforms baselines by more than tenfold on open-loop planning while beating state-of-the-art models across all tasks.

## Context
This work tackles the scarcity of diverse task-oriented datasets for long-horizon manipulation, which limits large language models' ability to plan reliably. By synthesizing data from manuals, it creates a realistic bridge between simulation and real-world robotics.

## Implications
The approach enables general-purpose household robots that can understand and execute appliance instructions without extensive fine-tuning, accelerating industry adoption of smart home automation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15863v1)
