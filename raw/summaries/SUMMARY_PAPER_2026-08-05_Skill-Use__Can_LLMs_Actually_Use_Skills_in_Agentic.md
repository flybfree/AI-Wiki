---
title: Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?
url: http://arxiv.org/abs/2608.04828v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_13-29-16Z_Skill_Use_CanLLMsActuallyUseSkillsinAgenticHarness.md
generated_at: 2026-08-05 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Skill-Use, a benchmark designed to evaluate whether large language model agents can recognize and apply skills independently. The authors find that reliable skill use remains limited across eight LLMs, with the strongest configuration scoring only 0.613 on the combined metric. Their results reveal that triggering and procedural compliance are major obstacles.

## Key Takeaways
- The benchmark measures whether an LLM agent can retrieve a skill’s full procedure from just its name and description, which was not previously evaluated.
- Reliable skill use remains low across tested models, with the best configuration achieving only 0.613 on the combined score.
- Triggering and procedural compliance are identified as independent bottlenecks that affect both scores and model rankings.

## Context
The rapid deployment of LLM agents in real‑world tasks depends on their ability to follow structured skill specifications without external prompting, yet existing evaluations focus solely on outcome quality rather than the underlying capability to locate and apply skills. This gap limits trustworthy assessment of agentic behavior.

## Implications
For practitioners, Skill-Use highlights that harness design heavily influences measurable performance, suggesting that improving agents requires both better model reasoning and more flexible skill interfaces. Industry adoption should prioritize evaluating agents under diverse harnesses to gauge true capability rather than harness‑specific scores.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04828v1)
