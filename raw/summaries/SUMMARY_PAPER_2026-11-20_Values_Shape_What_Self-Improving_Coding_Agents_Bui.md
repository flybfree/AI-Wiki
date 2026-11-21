---
title: Values Shape What Self-Improving Coding Agents Build
url: http://arxiv.org/abs/2611.23067v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-17_16-56-46Z_ValuesShapeWhatSelf_ImprovingCodingAgentsBuild.md
generated_at: 2026-11-20 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether embedding short value statements drawn from Schwartz's theory of basic human values into a self-improving coding agent's persistent instruction file alters both its performance and the nature of the solutions it produces. Across diverse coding tasks evaluated over multiple self-improvement iterations, the authors find that values such as openness to change measurably improve held-out performance, while opposing values like conservation degrade performance below a no-values baseline, and that values fundamentally reshape the size, complexity, and approach of the algorithms agents build.

## Key Takeaways
- Values have a measurable impact on agent performance across a diverse set of coding tasks. Specifically, openness-to-change values increase performance on held-out data, whereas conservation values produce scores that fall below those achieved by an agent given no values at all. This demonstrates that the content of an agent's persistent instruction file is not merely cosmetic but functionally consequential for downstream task outcomes.
- Values change what agents build, not just how well they perform. The solution algorithms produced under different value regimes differ in size, complexity, and overall approach, meaning that value statements steer the agent's design philosophy and creative direction in open-ended tasks. This finding highlights that self-improving agents are not value-neutral optimizers; their internalized principles shape the artifacts they generate.
- Human oversight remains necessary for designing effective values. When agents are allowed to revise their own values across iterations, the differences between value sets narrow, reducing the intended effect. Furthermore, values distilled from the AI literature provide no detectable performance gain over having no values at all, indicating that carefully curated, human-designed value statements are still required to meaningfully guide agent behavior.

## Context
Self-improving agents and autonomous coding systems are rapidly becoming central to AI research and software engineering practice, yet most optimization work focuses narrowly on output quality while neglecting the process and principles that guide how agents work. This paper fills that gap by borrowing from Schwartz's well-established psychological framework of basic human values and applying it to agent instruction design, bridging human values theory with machine learning agent architecture. It matters because as agents gain more autonomy over their own improvement loops, the question of what values they internalize becomes a design decision with real consequences for the software ecosystems they help construct.

## Implications
For practitioners building self-improving coding agents, this work suggests that carefully chosen value statements in persistent instruction files can serve as a lightweight steering mechanism that influences both performance and the architectural character of generated solutions, offering a design lever beyond traditional prompt engineering or reward shaping. For the broader field, it underscores that human oversight in value design cannot be delegated to agents themselves or to AI-generated value lists, as self-revision erodes intended distinctions and literature-derived values fail to outperform a null baseline. Industry teams deploying autonomous coding agents should therefore treat value specification as a deliberate, human-in-the-loop design task rather than an afterthought.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.23067v1)
