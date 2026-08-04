---
title: SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation
url: http://arxiv.org/abs/2608.02287v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_14-18-00Z_SKT_Skill_UseTrainingatScaleviaVerifiedSyntheticDa.md
generated_at: 2026-08-03 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SKT, a pipeline that creates skill-grounded tasks and verifies them using large public skills to generate executable trajectories for language-model agents. By synthesizing 4,000 task packages from 2,000 skills and producing 27,164 verified trajectories, the study shows supervised fine‑tuning on these trajectories boosts skill use across diverse models. The results establish a scalable method for training agents to identify, apply, and coordinate skills.

## Key Takeaways
- SKT selects single‑skill and multi‑skill configurations, synthesizes tasks with rule‑based and agent‑based verification, and retains only trajectories that substantially use every required skill.
- Using 2,000 public skills the pipeline generates 4,000 task packages and 27,164 verified trajectories, demonstrating high coverage and reliability.
- Supervised fine‑tuning on SKT‑generated trajectories consistently improves skill‑use performance across models, benchmarks, and agent harnesses.

## Context
Agent skills aim to embed procedural knowledge into language models, but current approaches often fail to ensure agents can correctly retrieve and apply them. Verified data synthesis addresses this gap by providing high‑quality, task‑specific examples that align with the skill set, enabling more reliable training than random or manually curated datasets.

## Implications
This work offers practitioners a scalable framework for building domain‑specific skill sets without extensive manual labeling, reducing development time and cost. As skills become central to agent capabilities, verified synthetic data pipelines like SKT can accelerate research and deployment of intelligent agents across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02287v1)
