---
title: SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models
url: http://arxiv.org/abs/2608.10538v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_06-22-02Z_SKILLER_Language_LevelReinforcementLearningforReus.md
generated_at: 2026-08-11 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SKILLER, a natural‑language driven reinforcement learning framework that automatically creates executor‑specific skills for small language models. By treating the small model system as an environment and using a strong model as both actor and critic, SKILLER propagates all reinforcement signals through natural language instructions. The experiments show absolute gains of 4.3 to 20.4 percentage points on Qwen3.5‑9B and 1.8 to 13.3 points on Qwen3.5‑4B compared with other skill generation methods.

## Key Takeaways
- SKILLER leverages reinforcement learning where all signals are encoded in natural language, allowing skill generation without direct model interaction.
- The framework outperforms three open‑source and one closed‑source skill generation or evolution methods across five benchmarks.
- The results match the performance of strong closed‑source models on single‑skill tasks in SkillsBench.

## Context
The rapid improvement of open‑source language models that run efficiently on consumer‑grade GPUs creates a demand for cost‑effective ways to constrain model behavior. Traditional skill extraction relies on expensive closed‑source systems, limiting real‑world deployment. This work bridges the gap by applying reinforcement learning directly to small models, offering a scalable alternative.

## Implications
For industry practitioners, SKILLER reduces inference costs and enables seamless integration of skills into agent harnesses without relying on proprietary APIs. It encourages open‑source skill generation, fostering interoperability across different model sizes and hardware constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10538v1)
