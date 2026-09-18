---
title: From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation
url: http://arxiv.org/abs/2609.19413v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-16_20-52-17Z_FromRollouttoReset_AGraph_BasedHarnessforAutonomou.md
generated_at: 2026-09-17 21:20
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces HALTER, a framework designed to automate the evaluation of long-horizon robot manipulation tasks by autonomously resetting scenes between rollouts. Unlike previous systems that struggle with the vast variety of terminal states in complex tasks, HALTER uses a library of learned atomic reset skills and an LLM-driven reasoning engine to restore environments efficiently.

## Key Takeaways
- HALTER addresses the scalability limitations of existing automated evaluation systems by planning over a library of learned atomic reset skills. This approach allows the system to handle a combinatorial number of terminal configurations, which previously required human intervention or failed when using single-policy reset methods.
- The architecture utilizes a spatial scene graph constructed from point clouds and vision foundation models. An LLM then reasons over this graph to perform three critical functions: scoring the robot's performance, planning the necessary sequence of reset actions, and verifying whether the reset was successful—all without requiring any task-specific labeled success images.
- Empirical evaluations on a Franka arm demonstrate that HALTER achieves a 76% success rate in scene restoration, significantly outperforming both AutoEval (52%) and motion-planning methods (65%). Furthermore, it reduces the manual operator time required for evaluation campaigns by 72% while maintaining high accuracy in identifying completed skills and verifying reset success.

## Context
As robot manipulation policies become more sophisticated, a major bottleneck in research is the inability to perform large-scale, reproducible evaluations due to the need for human intervention to reset environments between trials. This paper addresses this infrastructure gap by providing a scalable way to evaluate long-horizon tasks, which is essential for moving toward general-purpose robotics and reliable benchmarking.

## Implications
HALTER significantly lowers the barrier for researchers to conduct large-scale evaluation campaigns by automating the most labor-intensive part of the process: manual environment resetting. By enabling more frequent and diverse testing, this framework will likely accelerate the development of complex robot manipulation skills and provide a more objective standard for measuring progress in the field.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19413v1)
