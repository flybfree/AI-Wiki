---
title: PG-SFT: Balancing Capability Acquisition and Retention in Offline Agent Fine-Tuning
url: http://arxiv.org/abs/2610.00949v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_02-32-20Z_PG_SFT_BalancingCapabilityAcquisitionandRetentioni.md
generated_at: 2026-10-01 21:14
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the trade-off between acquiring new tool-use capabilities and preserving existing general reasoning skills during supervised fine-tuning on offline agent trajectories, identifying that standard approaches often cause significant regression in non-target benchmarks. The authors introduce Privilege-Guided SFT (PG-SFT), which employs turn-level information gain to dynamically modulate supervision strength based on the divergence from base model behavior. PG-SFT achieves a superior balance by substantially reducing distributional drift and capability degradation with only a marginal decrease in target-task performance compared to baselines like KL penalties or update magnitude constraints.

## Key Takeaways
- Standard supervised fine-tuning for agent trajectories frequently harms foundational capabilities such as general reasoning, tool calling, and code generation; moreover, conventional mitigation strategies including KL divergence penalties and limiting parameter update magnitudes are ineffective at preventing this distributional drift and performance regression.
- The proposed PG-SFT method leverages turn-level information gain from agent trajectories to adjust supervision strength adaptively, allowing the model to depart more aggressively from base behavior only in specific turns where new information is gained, thereby preserving knowledge in other areas.
-

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00949v1)
