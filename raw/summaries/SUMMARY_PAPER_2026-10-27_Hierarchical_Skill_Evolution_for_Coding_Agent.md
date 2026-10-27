---
title: Hierarchical Skill Evolution for Coding Agent
url: http://arxiv.org/abs/2610.35616v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_15-34-29Z_HierarchicalSkillEvolutionforCodingAgent.md
generated_at: 2026-10-27 00:11
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Hierarchical Skill Evolution (HSE), a method for distilling reusable procedural skills from coding agent trajectories through a three-tier evidence aggregation pipeline that moves from task-level extraction to repository-level consolidation to cross-repository generalization. The approach uses an external writer-evaluator loop to iteratively generate and assess skills without modifying the underlying coding model, and demonstrates that just 10 skills evolved from SWE-Gym trajectories improve coding performance across multiple benchmarks, models, and agent harnesses.

## Key Takeaways
- HSE employs a three-stage hierarchical distillation process: first extracting task-level evidence from individual coding trajectories, then aggregating recurring evidence within the same repository to form repository-specific skill candidates, and finally consolidating consistent patterns across repositories into transferable skills. This hierarchy progressively filters out task-specific and repository-specific noise while preserving procedural knowledge that generalizes across diverse coding environments.
- The skill evolution is driven by an external writer-evaluator loop that generates candidate skills and assesses their quality, while the underlying coding model remains completely frozen. The loop externally updates both the writer and evaluator policies over successive iterations to improve subsequent skill generation and assessment quality, creating a self-improving skill library without any model fine-tuning.
- Empirical evaluation on SWE-bench Verified and DeepSWE using GLM-5.2 across Pi and Claude Code harnesses, as well as GPT-5.5 and Opus 4.8 with Pi, shows that 10 skills evolved solely from SWE-Gym trajectories improve coding performance across all evaluated settings, demonstrating cross-benchmark, cross-model, and cross-harness transfer. Additionally, evolving skills from target-benchmark trajectories without verifier feedback, relying solely on the learned evaluator, yields further gains through benchmark-tailored skills.

## Context
This work sits at the intersection of LLM-based coding agents, procedural knowledge distillation, and continual learning without parameter updates. As coding agents like Claude Code and Pi become widely deployed for software engineering tasks, a critical bottleneck is that each agent must rediscover solutions from scratch for every new task or repository. HSE addresses this by treating agent trajectories as a learning substrate from which transferable procedural knowledge can be extracted, offering a model-agnostic mechanism for agent self-improvement that does not require expensive fine-tuning or access to training weights.

## Implications
For practitioners deploying coding agents at scale, HSE suggests that a small, carefully curated library of transferable skills can yield meaningful performance gains across heterogeneous models and tooling environments, reducing the need for per-task prompt engineering or model-specific tuning. For the broader AI research community, the writer-evaluator loop that operates entirely outside the frozen model opens a path toward agent self-improvement systems where knowledge is externalized and refined iteratively, potentially enabling agents to accumulate domain expertise over time without ever modifying their foundational architecture.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35616v1)
