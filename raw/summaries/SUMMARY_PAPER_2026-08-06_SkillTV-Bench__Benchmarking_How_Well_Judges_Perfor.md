---
title: SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution
url: http://arxiv.org/abs/2608.05573v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_03-52-37Z_SkillTV_Bench_BenchmarkingHowWellJudgesPerformonSk.md
generated_at: 2026-08-06 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SkillTV-Bench, a benchmark of 681 real agent trajectories across 50 tasks in eleven domains to evaluate skill-aware verification for both LLM-as-a-Judge and Agent-as-a-Judge methods. It also proposes SkillTV-Evolve, which externalizes procedural knowledge as reusable JudgeSkill to guide targeted inspections. The refined skill boosts accuracy by 14.8 percentage points on the same judge.

## Key Takeaways
- SkillTV-Bench provides a large-scale dataset that couples task-time skills with directly inspectable artifacts and environments, enabling verification beyond static trajectories.
- The externalized JudgeSkill allows agents to plan specific evidence checks, leading to more accurate verdicts than relying solely on final responses.
- An automated evolution loop using misjudged cases improves the skill by 14.8 percentage points, raising rollout success from 22.9% to 45.5%.

## Context
Current AI evaluation focuses on final outputs or static logs, overlooking procedural knowledge embedded in task execution. This gap limits the ability of agents to verify complex multi-step processes correctly. SkillTV-Bench addresses this by integrating skill-aware verification into a realistic agentic workflow.

## Implications
Practitioners can leverage JudgeSkill to design smarter verification systems that improve both accuracy and efficiency. The methodology offers a template for future benchmarks that combine task dynamics with observable evidence, fostering more robust AI agents in real-world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05573v1)
