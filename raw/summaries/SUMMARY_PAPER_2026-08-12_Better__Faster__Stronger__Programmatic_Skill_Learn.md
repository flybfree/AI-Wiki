---
title: Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost
url: http://arxiv.org/abs/2608.11338v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_18-42-23Z_Better_Faster_Stronger_ProgrammaticSkillLearningBe.md
generated_at: 2026-08-12 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how learning skills as programs can lower the cost of augmenting large language model agents, achieving better performance while reducing resource consumption. The authors demonstrate that a program‑augmented agent learns and refactors skill sequences from past trajectories, resulting in consistent frontier results across three embodied environments.

## Key Takeaways
- Skill learning is treated as deterministic program execution, which eliminates trial‑and‑error exploration and mitigates long‑horizon risk.
- The method leverages latent signal in historical trajectories to guide incremental discovery of reusable skill programs without requiring external replay or validation.
- SpeedRunner, the proposed coding agent that refactors skills for future tasks, consistently attains state‑of‑the‑art learning efficiency while remaining robust to distribution shifts and environmental randomness.

## Context
In AI research, augmenting language models with external tools is a key strategy for expanding capability. Traditional approaches prioritize performance gains but often overlook cost implications, leading to inefficient resource use. This work bridges that gap by focusing on economical skill acquisition methods.

## Implications
For practitioners, treating skills as programs offers a scalable pathway to reduce training and inference costs in agent systems. The findings suggest that future AI agents can be designed to reuse learned skill modules, fostering more efficient and adaptable autonomous agents across diverse domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11338v1)
