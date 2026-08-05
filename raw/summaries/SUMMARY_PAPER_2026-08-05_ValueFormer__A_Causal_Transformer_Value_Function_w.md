---
title: ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies
url: http://arxiv.org/abs/2608.02958v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_23-46-39Z_ValueFormer_ACausalTransformerValueFunctionwithSta.md
generated_at: 2026-08-05 01:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ValueFormer, a compact causal transformer that generates per‑frame value signals for Vision‑Language‑Action policies trained by behavior cloning. By providing both a smooth Monte Carlo value and a sharp binary mistake detector in a single forward pass, the model learns dense labels that guide training without costly reinforcement learning. On a real‑robot sandwich‑assembly task, the method lifts completion rates from 70 % to 85 % within statistical noise.

## Key Takeaways
- ValueFormer emits two per‑frame signals: a continuous Monte Carlo value V_mc for advantage estimation and a binary error flag that pulls in opposite directions, enabling dense supervision.  
- Failed episodes are labeled with a stage‑aware return that preserves the success curve before failure, so recovery attempts also generate useful training data.  
- The batched bf16 encoder reduces live serving cost 3–5 times, allowing the critic to run at 2 Hz alongside the policy on a single GPU.

## Context
Current VLA policies rely on sparse reinforcement signals that are impractical for real‑robot experiments, where simulation is limited by deformable objects. Dense per‑frame labels are theoretically feasible but rarely implemented due to computational and architectural constraints. ValueFormer demonstrates that a lightweight causal transformer can replace these bottlenecks.

## Implications
The approach lowers the cost of training VLA agents, making high‑fidelity robotics more accessible. Practitioners can adopt value‑based supervision without heavy reinforcement infrastructure, accelerating progress toward autonomous manipulation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02958v1)
