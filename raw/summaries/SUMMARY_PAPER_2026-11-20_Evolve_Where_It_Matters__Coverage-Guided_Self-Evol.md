---
title: Evolve Where It Matters: Coverage-Guided Self-Evolution of Agent Skills
url: http://arxiv.org/abs/2611.25429v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-19_03-11-24Z_EvolveWhereItMatters_Coverage_GuidedSelf_Evolution.md
generated_at: 2026-11-20 21:50
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SkillPlumber, a framework that enables self-evolving agents to revise their own procedural skill instructions by leveraging instruction-level coverage analysis to pinpoint exactly where skills fall short. Rather than judging a task run as a whole, SkillPlumber labels each individual instruction as followed, not-followed, or not covered, allowing the agent to distinguish between incorrect instructions and instructions the agent simply failed to execute. Across three benchmarks and three executor models, SkillPlumber achieves 64.7% to 70.5% task-solving rates, outperforming the initial skill by 25.6 to 30.4 percentage points and the strongest baseline by 8.7 to 14.0 percentage points.

## Key Takeaways
- Instruction-level coverage is the critical innovation: by labeling every instruction in a run as follow, not-follow, or not covered, the framework separates two fundamentally different failure modes—wrong instructions versus instructions the agent did not follow—something prior self-evolution methods could not do because they judged runs only by overall outcome or coarse error location.
- SkillPlumber's architecture combines a persistent root cause analysis agent that converts each coverage label into a targeted revision question and validates each revision against the next run, with a maintainer component that distills investigation findings across multiple tasks into a shared strategy library, enabling transferable improvements rather than task-specific patches.
- Ablation evidence confirms coverage is essential: removing the coverage-guided mechanism reduces recovered failures by 20.8% on SkillsBench when using GPT-5.5, demonstrating that the performance gains are not merely from iterative self-correction but specifically from the diagnostic precision that coverage labels provide.

## Context
Self-evolving agents that modify their own prompts, tools, or skill packages represent a growing research direction aimed at reducing human engineering overhead in deploying LLM-based agents. Prior approaches typically treat a failed task run as a monolithic signal, prompting the agent to rewrite its skill instructions wholesale without understanding which specific instruction caused the failure. This paper builds on the recently introduced concept of instruction-level coverage as a diagnostic tool and repurposes it from a testing mechanism into an active evolution signal, bridging the gap between skill evaluation and skill improvement in a principled, fine-grained manner.

## Implications
For practitioners deploying agent systems in production, SkillPlumber offers a concrete path toward agents that can autonomously debug and improve their own procedural knowledge without human intervention, potentially reducing maintenance costs and improving reliability across diverse task domains. The finding that coverage-guided revision outperforms outcome-only self-correction by a wide margin suggests that future agent self-improvement pipelines should incorporate fine-grained execution tracing as a core component rather than relying on coarse pass/fail signals, which could reshape how agent frameworks are designed and evaluated in both research and industry settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.25429v1)
