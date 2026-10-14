---
title: A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented Software Evolution
url: http://arxiv.org/abs/2610.15765v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_16-43-43Z_ADecadeinaDay_SynthesizingAgent_NativeInterfacesfr.md
generated_at: 2026-10-13 21:51
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how desktop software interfaces affect the performance of large language model agents, treating software evolution as a natural source of interface variation. The authors introduce DeskIF-Bench, a benchmark of 255 tasks across six desktop applications, and find that newer software releases consistently outperform older ones for agent use. They identify three critical interface properties—discoverability, granularity, and observability—and propose ANIS, a framework that synthesizes agent-native interfaces, achieving measurable improvements in task success and significant reductions in token usage.

## Key Takeaways
- The authors constructed DeskIF-Bench, a benchmark of 255 artifact-verified tasks spanning six desktop applications, where the task, agent, and verifier are held constant while the software release is varied. This experimental design isolates the effect of interface changes on agent performance, revealing that the newest release consistently outperforms the oldest across two models and six applications, demonstrating that interface design directly and measurably impacts agent capability.
- Trajectory analysis across agent interactions identified three interface properties that determine agent usability: discoverability (how easily agents can find available operations), granularity (the level at which operations are exposed), and observability (how clearly agents can perceive the effects of their actions). These properties explain why some software versions are easier for agents to navigate than others, providing a principled framework for evaluating interface suitability for autonomous agents.
- The ANIS framework synthesizes agent-native interfaces from installed application capabilities, producing atomic interfaces that improve task success by 3.8 and 3.5 percentage points over native SDK use with DeepSeek V4 Flash and Claude Haiku 4.5 respectively, while reducing online token usage by approximately 73%. Goal-level commands further raise success rates to 74.5% and 67.4%, showing that higher-level abstractions compound the benefits of interface redesign.

## Context
As large language model agents increasingly interact with desktop applications, the fundamental assumption that software interfaces are designed for human perception and motor control becomes a bottleneck. This paper addresses a gap in the AI research community by providing the first systematic, controlled study of how interface evolution affects agent performance, moving beyond anecdotal observations to quantifiable evidence. It bridges software engineering and AI agent research by treating decades of human-oriented software evolution as a natural experiment, offering a methodological template for studying agent-software interaction at scale.

## Implications
For practitioners building agent systems, this work demonstrates that interface design is not a secondary concern but a primary determinant of agent success, with measurable gains achievable through interface synthesis rather than model scaling alone. The 73% reduction in token usage alongside improved success rates suggests that agent-native interface layers can dramatically lower operational costs while improving reliability. For software developers and product teams, the identified properties of discoverability, granularity, and observability provide actionable design guidelines for making existing applications accessible to autonomous agents, potentially reshaping how desktop software is architected in an agent-driven computing era.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15765v1)
